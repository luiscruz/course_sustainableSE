"""
play_session.py — EnergiBridge measurement target.

EnergiBridge wraps this script:
    sudo energibridge -o results/condition_run_XX.csv -- python3 play_session.py

By the time this script runs, Spotify is ALREADY playing in steady state.
resume_playback() in run_experiment.py called play() and waited SETTLE_SECONDS
for the startup transient to clear before energibridge was launched.

This script simply:
  1. Waits MEASUREMENT_SECONDS (Spotify plays uninterrupted)
  2. Pauses Spotify

No seek, no play call — the CSV contains only clean steady-state power data.
"""

import subprocess
import time

MEASUREMENT_SECONDS = 13


def _osascript(cmd):
    subprocess.run(['osascript', '-e', cmd], check=True)


def pause():
    _osascript('tell application "Spotify" to pause')


if __name__ == '__main__':
    time.sleep(MEASUREMENT_SECONDS)
    pause()
