"""
run_experiment.py — Full 90-run experiment orchestrator.

Usage:
    cd 2026/experiment
    sudo python3 run_experiment.py

Prerequisites:
  1. Open Spotify manually, search for the chosen song (≥45s long), pause at 0:00.
  2. Reference screenshots exist in screenshots/ directory.
  3. EnergiBridge binary built at ../EnergiBridge/target/release/energibridge.
  4. Keep this terminal alive for the entire ~2.9-hour run (sudo cache).

Run order:
  - 90 runs total: 30× LOW + 30× MEDIUM + 30× HIGH, shuffled with seed 42.
  - progress.json tracks completed runs for crash recovery.
  - On fresh start: 300s warmup. On resume: 60s warmup before next run.

Estimated runtime: ~2.9 hours (90 × ~115s per run).
"""

import json
import os
import random
import subprocess
import time

from spotify_controller import configure, prebuffer
from warmup import fibonacci_warmup

# ── Configuration ─────────────────────────────────────────────────────────────
RESULTS        = 'results'
BINARY         = '../EnergiBridge/target/release/energibridge'
PROGRESS_FILE  = 'progress.json'
COOLDOWN_S     = 60      # seconds between runs
WARMUP_S       = 300     # seconds for initial full warmup
RESUME_WARMUP_S = 60     # shorter warmup on crash-resume
PREBUFFER_S    = 15      # seconds of pre-buffering per run
SETTLE_S       = 5       # seconds of settle after prebuffer
SEED           = 42
CONDITIONS     = ['LOW', 'MEDIUM', 'HIGH']
REPS_PER_COND  = 30
# ─────────────────────────────────────────────────────────────────────────────


def build_run_order():
    """Return a deterministic 90-item list of condition labels."""
    order = CONDITIONS * REPS_PER_COND
    rng = random.Random(SEED)
    rng.shuffle(order)
    return order


def load_progress():
    """Return the set of already-completed run indices (0-based)."""
    if not os.path.exists(PROGRESS_FILE):
        return set()
    with open(PROGRESS_FILE) as f:
        data = json.load(f)
    return set(data.get('completed', []))


def save_progress(completed_indices):
    """Persist the set of completed run indices to progress.json."""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump({'completed': sorted(completed_indices)}, f)


def _validate_csv(path):
    """Warn if the output CSV looks wrong. Returns True if healthy."""
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print(f'  ERROR: {path} is missing or empty.')
        return False
    with open(path) as f:
        lines = f.readlines()
    header = lines[0].strip() if lines else ''
    row_count = len(lines) - 1
    has_power = 'SYSTEM_POWER' in header
    print(f'  Rows (excl. header): {row_count}')
    print(f'  SYSTEM_POWER present: {has_power}')
    if row_count < 100:
        print(f'  WARNING: fewer than 100 rows — expected ~150 at 200ms interval.')
    if not has_power:
        print(f'  WARNING: SYSTEM_POWER column missing — check EnergiBridge output.')
    return has_power and row_count >= 100


def run_single_iteration(run_index, condition, counter_label):
    """
    Execute one measurement run:
      configure → prebuffer → EnergiBridge → validate CSV

    Returns the output CSV path.
    """
    os.makedirs(RESULTS, exist_ok=True)
    output_csv = os.path.join(RESULTS, f'{condition.lower()}_run_{counter_label:02d}.csv')

    print(f'\n{"="*60}')
    print(f'Run {run_index + 1}/90  |  Condition: {condition}  |  File: {output_csv}')
    print(f'{"="*60}')

    # Configure Spotify quality + canvas
    screenshots_present = all(
        os.path.exists(f'screenshots/{f}')
        for f in ['quality_dropdown.png',
                  'quality_low.png', 'quality_normal.png', 'quality_very_high.png',
                  'canvas_label.png', 'canvas_toggle_on.png', 'canvas_toggle_off.png']
    )
    if screenshots_present:
        print(f'  Configuring Spotify → {condition}...')
        configure(condition)
        print('  Settings applied.')
    else:
        print(f'  SKIPPED auto-configure (no screenshots). Verify manually: {condition}')

    # Pre-buffer outside measurement window
    print(f'  Pre-buffering {PREBUFFER_S}s at {condition} quality...')
    prebuffer(prebuffer_seconds=PREBUFFER_S, settle_seconds=SETTLE_S)
    print('  Buffer warm. Spotify paused at 0:00.')

    # EnergiBridge measurement
    print(f'  Starting EnergiBridge → {output_csv}')
    subprocess.run(
        [
            'sudo', BINARY,
            '-o', output_csv,
            '--',
            'python3', 'play_session.py',
        ],
        check=True,
    )

    # Validate
    _validate_csv(output_csv)
    return output_csv


def main():
    os.makedirs(RESULTS, exist_ok=True)

    # Refresh sudo timestamp so it doesn't expire mid-run
    print('Refreshing sudo credentials (keep this terminal alive)...')
    subprocess.run(['sudo', '-v'], check=True)

    # Prevent display sleep during unattended run
    caffeinate = subprocess.Popen(['caffeinate', '-d'])
    print('caffeinate started (display sleep suppressed).')

    try:
        run_order   = build_run_order()
        completed   = load_progress()
        is_resume   = len(completed) > 0

        total_runs  = len(run_order)

        if is_resume:
            remaining = total_runs - len(completed)
            print(f'\nResuming experiment — {len(completed)}/{total_runs} runs already done.')
            print(f'Running short {RESUME_WARMUP_S}s warmup before next run...')
            fibonacci_warmup(seconds=RESUME_WARMUP_S)
            print('Warmup complete.')
        else:
            print(f'\nFresh start — {total_runs} runs planned.')
            print(f'Running {WARMUP_S}s CPU warmup...')
            fibonacci_warmup(seconds=WARMUP_S)
            print('Warmup complete.')

        # Per-condition counters for filename numbering
        cond_counter = {c: 0 for c in CONDITIONS}

        for run_index, condition in enumerate(run_order):
            if run_index in completed:
                cond_counter[condition] += 1
                print(f'  Skipping run {run_index + 1} ({condition}) — already done.')
                continue

            cond_counter[condition] += 1
            counter_label = cond_counter[condition]

            run_single_iteration(run_index, condition, counter_label)

            completed.add(run_index)
            save_progress(completed)

            # Cooldown between runs (skip after last run)
            if run_index < total_runs - 1:
                print(f'\n  Cooldown {COOLDOWN_S}s...')
                time.sleep(COOLDOWN_S)

        print('\n' + '='*60)
        print('Experiment complete. All 90 runs finished.')
        print(f'Results in: {os.path.abspath(RESULTS)}')

    finally:
        caffeinate.terminate()
        print('caffeinate stopped.')


if __name__ == '__main__':
    main()
