"""
run_single.py — Run a single measurement iteration for validation.

Usage:
    cd 2026/experiment
    python3 run_single.py

Before running:
  1. Open Spotify manually, search for the chosen song, pause at 0:00
  2. Ensure reference screenshots exist in screenshots/
     (canvas_on.png, canvas_off.png, quality_low.png,
      quality_normal.png, quality_very_high.png)
  3. Confirm EnergiBridge binary is built at ../EnergiBridge/target/release/energibridge

Change CONDITION below to 'LOW', 'MEDIUM', or 'HIGH' to test each condition.
"""

import subprocess
import os
import time

from spotify_controller import configure, prebuffer
from warmup import fibonacci_warmup

# ── Configuration ────────────────────────────────────────────────────────────
CONDITION = 'HIGH'    # 'LOW' | 'MEDIUM' | 'HIGH'
RUN_ID    = 1
RESULTS   = 'results'
BINARY    = '../EnergiBridge/target/release/energibridge'
WARMUP_SECONDS = 0    # warm-up already completed; set to 300 for fresh runs
# ─────────────────────────────────────────────────────────────────────────────

os.makedirs(RESULTS, exist_ok=True)

# Step 1 — Warm up CPU to stabilise energy baseline
if WARMUP_SECONDS > 0:
    print(f'[1/4] Warming up for {WARMUP_SECONDS}s...')
    fibonacci_warmup(seconds=WARMUP_SECONDS)
    print('      Warm-up complete.')
else:
    print('[1/4] Warm-up skipped.')

# Step 2 — Configure Spotify settings (outside measurement window)
screenshots_present = all(
    os.path.exists(f'screenshots/{f}')
    for f in ['quality_dropdown.png',
              'quality_automatic.png', 'quality_normal.png', 'quality_high.png',
              'quality_very_high.png',
              'canvas_label.png', 'canvas_toggle_on.png', 'canvas_toggle_off.png']
)
if screenshots_present:
    print(f'[2/4] Configuring Spotify for condition: {CONDITION}')
    configure(CONDITION)
    print('      Settings applied.')
else:
    print(f'[2/4] SKIPPED auto-configure (no screenshots found).')
    print(f'      *** Manually verify Spotify is set to: {CONDITION} ***')
    print(f'        HIGH   → Very High quality, Canvas ON')
    print(f'        MEDIUM → Normal quality,   Canvas OFF')
    print(f'        LOW    → Low quality,       Canvas OFF')
    print('      Proceeding in 30 seconds — configure Spotify now if needed...')
    for i in range(30, 0, -5):
        print(f'        {i}s remaining...')
        time.sleep(5)

# Step 3 — Pre-buffer (outside measurement window)
print(f'[3/4] Pre-buffering 15s at {CONDITION} quality...')
prebuffer(prebuffer_seconds=15, settle_seconds=5)
print('      Buffer warm. Spotify paused at 0:00.')

# Step 4 — Run EnergiBridge wrapping play_session.py
output_csv = f'{RESULTS}/{CONDITION.lower()}_run_{RUN_ID:02d}.csv'
print(f'[4/4] Starting measurement → {output_csv}')

result = subprocess.run(
    [
        'sudo', BINARY,
        '-o', output_csv,
        '--',
        'python3', 'play_session.py',
    ],
    check=True,
)

print(f'\nDone. CSV saved to {output_csv}')

# ── Quick sanity check ────────────────────────────────────────────────────────
if os.path.exists(output_csv) and os.path.getsize(output_csv) > 0:
    with open(output_csv) as f:
        lines = f.readlines()
    header = lines[0].strip() if lines else ''
    row_count = len(lines) - 1  # exclude header
    has_power = 'SYSTEM_POWER' in header
    print(f'  Rows (excl. header): {row_count}')
    print(f'  SYSTEM_POWER column present: {has_power}')
    if row_count < 100:
        print('  WARNING: fewer than 100 rows — expected ~150 at 200ms interval.')
    if not has_power:
        print('  WARNING: SYSTEM_POWER column missing — check EnergiBridge output.')
else:
    print(f'  ERROR: {output_csv} is missing or empty.')
