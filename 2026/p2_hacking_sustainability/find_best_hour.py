#!/usr/bin/env python3
"""
find_best_hour.py
-----------------
Fetches a 24-hour CO2 intensity forecast from the WattTime v3 API for
CAISO_NORTH, identifies the lowest-carbon hour, prints a GitHub Actions
cron recommendation, and writes the result to the environment.

Environment updates
-------------------
* Inside GitHub Actions  → appends  GHA_BEST_HOUR=<HH>  to $GITHUB_ENV
                           (makes the variable available to subsequent steps)
* Locally                → writes/updates  GHA_BEST_HOUR=<HH>  in .env
                           (same directory as this script)

Credentials (loaded from .env or real environment):
  USERNAME    WattTime account username
  PASSWORD    WattTime account password
"""

import os
import sys
import re
import requests
from datetime import datetime, timezone
from collections import defaultdict
import statistics
from pathlib import Path
from dotenv import load_dotenv, set_key, dotenv_values

# ---------------------------------------------------------------------------
# 1. Load credentials
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
ENV_FILE = SCRIPT_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

# Support the typo present in the notebook ('USERNAMME') as fallback
USERNAME = os.getenv("USERNAME") or os.getenv("USERNAMME")
PASSWORD = os.getenv("PASSWORD")

if not USERNAME or not PASSWORD:
    print(
        "ERROR: Missing WattTime credentials.\n"
        "Set USERNAME and PASSWORD in your .env file or environment.",
        file=sys.stderr,
    )
    sys.exit(1)

# ---------------------------------------------------------------------------
# 2. Authenticate
# ---------------------------------------------------------------------------
print("Authenticating with WattTime …")
resp = requests.get("https://api.watttime.org/login", auth=(USERNAME, PASSWORD), timeout=15)
resp.raise_for_status()
TOKEN = resp.json()["token"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
print(f"  OK — token prefix: {TOKEN[:20]}…")

# ---------------------------------------------------------------------------
# 3. Fetch 24-hour forecast for CAISO_NORTH
# ---------------------------------------------------------------------------
REGION = "CAISO_NORTH"
SIGNAL = "co2_moer"
LBS_MWH_TO_G_KWH = 453.592 / 1000  # convert lbs/MWh → g CO₂/kWh

print(f"\nFetching 24-hour {SIGNAL} forecast for {REGION} …")
resp = requests.get(
    "https://api.watttime.org/v3/forecast",
    headers=HEADERS,
    params={"region": REGION, "signal_type": SIGNAL, "horizon_hours": 24},
    timeout=15,
)
resp.raise_for_status()

forecast_points = [
    (
        datetime.fromisoformat(pt["point_time"]).astimezone(timezone.utc),
        round(float(pt["value"]) * LBS_MWH_TO_G_KWH, 2),
    )
    for pt in resp.json()["data"]
]

print(f"  {len(forecast_points)} data points (5-min resolution)")
print(
    f"  Window: {forecast_points[0][0].strftime('%Y-%m-%d %H:%M UTC')} "
    f"→ {forecast_points[-1][0].strftime('%Y-%m-%d %H:%M UTC')}"
)

# ---------------------------------------------------------------------------
# 4. Compute hourly averages and rank them
# ---------------------------------------------------------------------------
hourly_buckets: dict = defaultdict(list)
for ts, g_co2 in forecast_points:
    hourly_buckets[ts.replace(minute=0, second=0, microsecond=0)].append(g_co2)

hourly = sorted(
    [
        {
            "hour": h,
            "avg": round(statistics.mean(v), 1),
            "min": round(min(v), 1),
        }
        for h, v in hourly_buckets.items()
    ],
    key=lambda x: x["hour"],
)
ranked = sorted(hourly, key=lambda x: x["avg"])
best_hour = ranked[0]
worst_hour = ranked[-1]

# ---------------------------------------------------------------------------
# 5. Print full ranking
# ---------------------------------------------------------------------------
print(f"\n{'Hour (UTC)':<22} {'Avg g CO₂/kWh':>14} {'Min g CO₂/kWh':>14}")
print("-" * 52)
for row in ranked:
    marker = "  ← BEST" if row["hour"] == best_hour["hour"] else ""
    print(
        f"{row['hour'].strftime('%m/%d %H:00 UTC'):<22}"
        f"{row['avg']:>14.1f}"
        f"{row['min']:>14.1f}"
        f"{marker}"
    )

# ---------------------------------------------------------------------------
# 6. Summary & cron recommendation
# ---------------------------------------------------------------------------
cron_hour = best_hour["hour"].hour
top5 = ranked[:5]
saving_pct = round((1 - best_hour["avg"] / worst_hour["avg"]) * 100, 1)

print()
print("=" * 60)
print(" BEST TIME TO RUN A GITHUB ACTION (next 24 h)")
print("=" * 60)
print(f" Region  : {REGION}  (≈ Azure westus / San Francisco)")
print(f" Signal  : WattTime {SIGNAL}  (Marginal Emissions Rate)")
print()
print(" Top 5 cleanest hours:")
for i, row in enumerate(top5, 1):
    print(f"   {i}. {row['hour'].strftime('%m/%d %H:00 UTC')}  →  {row['avg']:6.1f} g CO₂/kWh")
print()
print(f" ✓ Best hour : {best_hour['hour'].strftime('%m/%d %H:00 UTC')}")
print(f"   Average   : {best_hour['avg']} g CO₂/kWh")
print(f"   Minimum   : {best_hour['min']} g CO₂/kWh")
print()
print(" GitHub Actions cron schedule (UTC):")
print()
print("   on:")
print("     schedule:")
print(f"       - cron: '0 {cron_hour} * * *'")
print()
print(
    f" vs worst hour ({worst_hour['hour'].strftime('%H:00 UTC')}, "
    f"{worst_hour['avg']} g CO₂/kWh): "
    f"running at the best hour saves ~{saving_pct}% of carbon emissions."
)
print("=" * 60)

# ---------------------------------------------------------------------------
# 7. Update environment variable  GHA_BEST_HOUR
# ---------------------------------------------------------------------------
best_hour_str = str(cron_hour)

github_env = os.getenv("GITHUB_ENV")
if github_env:
    # Running inside GitHub Actions — persist variable for subsequent steps
    with open(github_env, "a") as f:
        f.write(f"GHA_BEST_HOUR={best_hour_str}\n")
        f.write(f"GHA_BEST_CRON=0 {cron_hour} * * *\n")
    print(f"\n[GH Actions] Written GHA_BEST_HOUR={best_hour_str} to $GITHUB_ENV")
else:
    # Running locally — update / create the .env file
    if not ENV_FILE.exists():
        ENV_FILE.touch()

    # Use python-dotenv's set_key to safely update or insert the value
    set_key(str(ENV_FILE), "GHA_BEST_HOUR", best_hour_str)
    set_key(str(ENV_FILE), "GHA_BEST_CRON", f"0 {cron_hour} * * *")
    print(f"\n[Local] Updated GHA_BEST_HOUR={best_hour_str} in {ENV_FILE}")
    print(f"[Local] Updated GHA_BEST_CRON='0 {cron_hour} * * *' in {ENV_FILE}")
