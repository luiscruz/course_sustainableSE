"""
Experiment Runner — automates the full experiment matrix.

Runs Google Meet and Microsoft Teams experiments with varying bot counts,
repeated multiple times for statistical significance.
"""

import argparse
import csv
import json
import os
import sys
import time
import logging
import random
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from bot_manager import BotConfig
from energy_measure import measure_experiment

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("experiment_runner")


# ---------------------------------------------------------------------------
# Experiment matrix
# ---------------------------------------------------------------------------

DEFAULT_REPEATS = 30
DEFAULT_CALL_DURATION = 120  # seconds
COOLDOWN_BETWEEN_RUNS = 60  # seconds — let system settle between experiments


def run_full_experiment(
    meet_url: str | None = None,
    teams_url: str | None = None,
    repeats: int = DEFAULT_REPEATS,
    call_duration: int = DEFAULT_CALL_DURATION,
    output_dir: str = "data",
    headless: bool = True,
    join_min: int = 5,
    join_max: int = 15,
    shuffle: bool = True,
    random_seed: int | None = None,
):
    """
    Run experiment matrix (single bot per run):
      - For each platform (meet, teams)
      - Repeat `repeats` times
      - Randomized execution order
    """

    platforms = []
    if meet_url:
        platforms.append(("meet", meet_url))
    if teams_url:
        platforms.append(("teams", teams_url))

    if not platforms:
        log.error("No meeting URLs provided. Use --meet-url and/or --teams-url")
        sys.exit(1)

    # ---------------------------------------------------
    # 1️⃣ Build experiment queue
    # ---------------------------------------------------
    experiment_queue = []

    for platform_name, url in platforms:
        for repeat_i in range(repeats):
            experiment_queue.append({
                "platform": platform_name,
                "url": url,
                "repeat": repeat_i + 1,
            })

    total_runs = len(experiment_queue)

    log.info(
        f"Experiment matrix: "
        f"{len(platforms)} platforms × "
        f"{repeats} repeats = {total_runs} runs"
    )

    # ---------------------------------------------------
    # 2️⃣ Shuffle execution order
    # ---------------------------------------------------
    
    random.seed(random_seed)
    random.shuffle(experiment_queue)
    log.info("Experiment order randomized.")

    os.makedirs(output_dir, exist_ok=True)

    all_results = []

    # ---------------------------------------------------
    # 3️⃣ Execute
    # ---------------------------------------------------
    for run_number, exp in enumerate(experiment_queue, start=1):

        label = f"{exp['platform']}_1bot_r{exp['repeat']}"

        log.info(f"\n{'='*60}")
        log.info(f"Run {run_number}/{total_runs}: {label}")
        log.info(f"{'='*60}")

        config = BotConfig(
            platform=exp["platform"],
            meeting_url=exp["url"],
            num_bots=1,   # ← fixed to 1
            call_duration=call_duration,
            join_interval_min=join_min,
            join_interval_max=join_max,
            headless=headless,
        )

        try:
            result = measure_experiment(
                config,
                output_dir=output_dir,
                experiment_label=label,
            )

            result["repeat"] = exp["repeat"]
            result["run_number"] = run_number
            all_results.append(result)

            log.info(
                f"Run {run_number} done: "
                f"energy={result.get('energy_cpu_joules', 'N/A')}J, "
                f"avg_cpu={result.get('avg_cpu_percent', 'N/A')}%"
            )

        except Exception as e:
            log.error(f"Run {run_number} FAILED: {e}")
            all_results.append({
                "platform": exp["platform"],
                "repeat": exp["repeat"],
                "run_number": run_number,
                "error": str(e),
            })

        # Cooldown between runs
        if run_number < total_runs:
            log.info(f"Cooldown: waiting {COOLDOWN_BETWEEN_RUNS}s before next run...")
            time.sleep(COOLDOWN_BETWEEN_RUNS)

    _save_combined_results(all_results, output_dir)
    _print_summary(all_results)

    return all_results


def _save_combined_results(results: list[dict], output_dir: str):
    """Save all experiment results to a single CSV."""
    if not results:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(output_dir, f"experiment_combined_{timestamp}.csv")

    # Collect all possible keys
    all_keys = set()
    for r in results:
        all_keys.update(r.keys())
    all_keys = sorted(all_keys)

    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=all_keys, extrasaction="ignore")
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    log.info(f"Saved combined results to {filepath}")

    # Also save as JSON for easier programmatic access
    json_path = os.path.join(output_dir, f"experiment_combined_{timestamp}.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    log.info(f"Saved combined JSON to {json_path}")


def _print_summary(results: list[dict]):
    """Print a summary table of all experiments."""
    print("\n" + "=" * 80)
    print("EXPERIMENT SUMMARY")
    print("=" * 80)
    print(f"{'Run':<5} {'Platform':<8} {'Bots':<6} {'Rep':<5} "
          f"{'Energy (J)':<12} {'Avg CPU%':<10} {'Net Recv (MB)':<14} {'Status':<8}")
    print("-" * 80)

    for r in results:
        if "error" in r:
            status = "FAIL"
            energy = "N/A"
            cpu = "N/A"
            net = "N/A"
        else:
            status = "OK"
            energy = f"{r.get('energy_cpu_joules', 'N/A')}"
            cpu = f"{r.get('avg_cpu_percent', 'N/A')}"
            net = f"{r.get('total_net_recv_mb', 'N/A')}"

        print(f"{r.get('run_number', '?'):<5} {r.get('platform', '?'):<8} "
              f"{r.get('num_bots', '?'):<6} {r.get('repeat', '?'):<5} "
              f"{energy:<12} {cpu:<10} {net:<14} {status:<8}")

    print("=" * 80)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Run the full experiment matrix for energy measurement"
    )
    parser.add_argument("--meet-url", default=os.getenv("MEET_URL"),
                        help="Google Meet URL")
    parser.add_argument("--teams-url", default=os.getenv("TEAMS_URL"),
                        help="Microsoft Teams URL")
    parser.add_argument("--repeats", type=int, default=DEFAULT_REPEATS,
                        help="Repetitions per configuration (default: 3)")
    parser.add_argument("--duration", type=int, default=DEFAULT_CALL_DURATION,
                        help="Call duration in seconds (default: 120)")
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--visible", action="store_true",
                        help="Run browsers in visible mode")
    parser.add_argument("--join-min", type=int, default=5)
    parser.add_argument("--join-max", type=int, default=15)
    args = parser.parse_args()

    results = run_full_experiment(
        meet_url=args.meet_url,
        teams_url=args.teams_url,
        repeats=args.repeats,
        call_duration=args.duration,
        output_dir=args.output_dir,
        headless=not args.visible,
        join_min=args.join_min,
        join_max=args.join_max,
    )

    successful = sum(1 for r in results if "error" not in r)
    print(f"\nDone: {successful}/{len(results)} runs completed successfully")


if __name__ == "__main__":
    main()
