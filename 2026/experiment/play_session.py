"""
play_session.py — EnergiBridge measurement target.

EnergiBridge wraps this script:
    sudo energibridge -o results/condition_run_XX.csv -- python3 play_session.py

The script:
  1. Starts Spotify playback via AppleScript
  2. Waits exactly 60 seconds (the measurement window)
  3. Pauses Spotify

Assumes Spotify is already open and a song is loaded/paused at 0:00.
"""

import subprocess
import time

MEASUREMENT_SECONDS = 45


def play():
    subprocess.run(
        ['osascript', '-e', 'tell application "Spotify" to play'],
        check=True
    )


def pause():
    subprocess.run(
        ['osascript', '-e', 'tell application "Spotify" to pause'],
        check=True
    )


if __name__ == '__main__':
    play()
    time.sleep(MEASUREMENT_SECONDS)
    pause()
