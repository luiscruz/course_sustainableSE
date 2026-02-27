"""
spotify_controller.py — Configure Spotify settings via PyAutoGUI + AppleScript.

Settings are changed BEFORE EnergiBridge starts so the settings-change energy
is NOT included in the measurement window.

Prerequisites:
  - macOS: grant accessibility + screen recording permissions to Terminal/IDE
  - pip install pyautogui pillow
  - Reference screenshots in screenshots/ directory (see README)
"""

import subprocess
import time
import pyautogui

# Map experiment condition labels to Spotify UI quality strings
QUALITY_MAP = {
    'AUTO':      'automatic',
    'AUTO_NC':   'automatic',
    'MEDIUM':    'normal',
    'HIGH':      'high',
    'HIGH_NC':   'high',
    'VERY_HIGH': 'very_high',
}


def bring_spotify_to_front():
    """Activate Spotify via AppleScript and wait for it to become frontmost."""
    subprocess.run(
        ['osascript', '-e', 'tell application "Spotify" to activate'],
        check=True
    )
    time.sleep(1)


def open_settings():
    """Bring Spotify to front and open its Preferences window."""
    bring_spotify_to_front()
    pyautogui.hotkey('command', ',')
    time.sleep(2.0)                     # wait for settings window to fully render
    pyautogui.hotkey('command', 'up')   # normalize scroll → Audio Quality always visible
    time.sleep(0.5)


def set_audio_quality(condition):
    """
    Select the audio quality for the given condition via the dropdown.

    Two-step process:
      1. Click the dropdown button (screenshots/quality_dropdown.png) to open it.
      2. Click the desired option from the open list.

    Expects screenshot files at:
        screenshots/quality_dropdown.png   — the dropdown button (arrow area),
                                             consistent regardless of current value
        screenshots/quality_low.png        — "Low" option in the open dropdown
        screenshots/quality_normal.png     — "Normal" option in the open dropdown
        screenshots/quality_very_high.png  — "High" option in the open dropdown

    All option screenshots should be taken while the dropdown is open and the
    option is NOT currently selected (no checkmark on it).

    Raises AssertionError if any screenshot is not found on screen.
    """
    # Step 1 — open the dropdown
    dropdown = pyautogui.locateOnScreen('screenshots/quality_dropdown.png', confidence=0.6)
    assert dropdown is not None, (
        'Could not locate quality dropdown button on screen.\n'
        'Make sure Spotify Settings > Audio Quality is visible and '
        'screenshots/quality_dropdown.png matches the dropdown arrow.'
    )
    # The dropdown button ("Very high ▼") sits in the rightmost ~8% of the
    # matched row. Using a fraction avoids being thrown off by how wide the
    # matched region is (full-screen template vs narrow crop).
    click_x = int(dropdown.left + dropdown.width * 0.92)
    click_y = dropdown.top + dropdown.height // 2
    pyautogui.click(click_x, click_y)
    time.sleep(1.0)   # wait for dropdown list to appear

    # Step 2 — click the desired option (full-screen search + retry)
    quality_key = QUALITY_MAP[condition]
    option_path = f'screenshots/quality_{quality_key}.png'
    for attempt in range(3):
        btn = pyautogui.locateOnScreen(option_path, confidence=0.62)
        if btn is not None:
            print(f'    [quality] found {quality_key!r} at {pyautogui.center(btn)}, clicking')
            pyautogui.click(pyautogui.center(btn))
            time.sleep(0.5)
            return
        print(f'    [quality] attempt {attempt+1}: {quality_key!r} not found at confidence=0.62')
        if attempt < 2:
            # Dropdown may have closed; dismiss and re-open
            pyautogui.press('escape')
            time.sleep(0.3)
            pyautogui.click(click_x, click_y)
            time.sleep(1.0)
    raise AssertionError(
        f'Could not locate quality option after 3 attempts: {option_path}\n'
        'Make sure the dropdown is open and the reference screenshot matches '
        'the option in its unselected state.'
    )


def _scan_canvas_row(label):
    """
    Find the Canvas toggle by scanning the row's pixels horizontally.

    Locates the FIRST toggle-coloured pixel in the row then steps 21 physical
    pixels right (half the toggle's 42 px physical width) to land on its centre.
    Using only the first pixel avoids being dragged rightward by stray grey/green
    pixels from other UI elements further along the row.

    Returns (toggle_x, toggle_y, is_on) in logical screen coordinates.
    Raises AssertionError if no toggle-coloured pixels are found.
    """
    scan_x = label.left + label.width          # start right of the label text
    # Cap at 600 logical px — on 1920px displays the toggle can be ~490px past
    # the label right edge; 600 covers that while staying clear of album art
    # and other app windows that appear further right.
    scan_w = min(600, pyautogui.size().width - scan_x)
    img    = pyautogui.screenshot(region=(scan_x, label.top, scan_w, label.height))
    scale  = max(1, round(img.height / label.height))   # 2 on Retina, 1 otherwise
    cy     = img.height // 2
    pixels = img.load()

    # Find the first toggle-coloured pixel; colour at that pixel tells us state.
    # Toggle left edge is always coloured (green for ON, grey for OFF) at the
    # centre row, so the very first hit is the toggle's left edge.
    TOGGLE_HALF_PX = 21   # half of the 42 physical-pixel toggle width
    for lx in range(img.width):
        r, g, b = pixels[lx, cy][:3]
        is_green = g > 140 and r < 100
        is_grey  = 70 < r < 180 and abs(r - g) < 25 and abs(g - b) < 25
        if is_green or is_grey:
            center_phys = lx + TOGGLE_HALF_PX
            toggle_x    = scan_x + center_phys // scale
            toggle_y    = label.top + label.height // 2
            return toggle_x, toggle_y, is_green   # green=ON, grey/else=OFF

    raise AssertionError(
        'No toggle-coloured pixels found in Canvas row scan.\n'
        'Run: python3 -c "from spotify_controller import _debug_canvas_scan; _debug_canvas_scan()"'
    )


def set_canvas(condition):
    """
    Toggle the Canvas setting to the correct state.
    Canvas is ON only for HIGH and AUTO; OFF for all others.

    Locates the Canvas row via canvas_label.png, then reads the toggle
    colour (green=ON, grey=OFF) and clicks only if the state is wrong.
    Raises AssertionError if the label cannot be found — the retry loop
    in run_experiment.py will catch this and retry configure().
    """
    want_on    = condition in ('HIGH', 'AUTO')
    label_path = 'screenshots/canvas_label.png'

    try:
        label = pyautogui.locateOnScreen(label_path, confidence=0.6)
    except Exception:
        label = None

    assert label is not None, (
        'Could not locate canvas_label.png on screen.\n'
        'Make sure Spotify Settings is open and scrolled to show the Canvas row.'
    )

    toggle_x, toggle_y, is_on = _scan_canvas_row(label)
    if is_on != want_on:
        pyautogui.click(toggle_x, toggle_y)
        time.sleep(0.5)


def close_settings():
    """Close the Spotify Preferences window."""
    pyautogui.hotkey('command', 'w')
    time.sleep(0.5)


def configure(condition):
    """
    Full configuration sequence for a given experiment condition.

    Args:
        condition: One of 'LOW', 'MEDIUM', 'HIGH'
    """
    assert condition in QUALITY_MAP, f'Unknown condition: {condition!r}'
    open_settings()
    set_audio_quality(condition)
    # Let the dropdown animation finish and re-normalise scroll position so
    # canvas_label.png is in the same position as in the standalone test.
    time.sleep(1.0)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.8)
    set_canvas(condition)
    close_settings()


def seek_to_position(seconds):
    """Seek Spotify playback to an arbitrary position (seconds) via AppleScript."""
    script = f'tell application "Spotify" to set player position to {seconds}'
    subprocess.run(['osascript', '-e', script], check=True)


def seek_to_start():
    """Seek Spotify playback position to 0:00 via AppleScript."""
    seek_to_position(0)


def prebuffer(prebuffer_seconds=15, settle_seconds=5):
    """
    Warm the Spotify audio/video decoder at the CURRENTLY configured quality.
    Call AFTER configure() and BEFORE EnergiBridge starts.

    Sequence: seek to 0:00 → play prebuffer_seconds → pause (stay mid-song) → settle
    The final pause preserves decoder state so measurement resumes without a cold-start
    spike. Do NOT seek back to 0:00 here — that would reset the decoder.
    """
    bring_spotify_to_front()
    play_cmd  = ['osascript', '-e', 'tell application "Spotify" to play']
    pause_cmd = ['osascript', '-e', 'tell application "Spotify" to pause']

    seek_to_start()                         # defensive: reset to known position
    time.sleep(0.5)
    subprocess.run(play_cmd, check=True)
    time.sleep(prebuffer_seconds)           # decoder warms up, buffer fills
    subprocess.run(pause_cmd, check=True)   # pause mid-song, decoder state preserved
    time.sleep(settle_seconds)              # CPU/network decay before measurement


def resume_playback(settle_seconds=5):
    """
    Resume Spotify from its paused mid-song position and wait for the startup
    transient to clear before EnergiBridge begins recording.

    The audio decoder initialization causes a power spike for the first ~5 s
    after play() is called from a paused state.  By starting playback HERE
    (before energibridge launches) the spike is excluded from the CSV entirely,
    so no post-hoc trimming is needed.
    """
    play_cmd = ['osascript', '-e', 'tell application "Spotify" to play']
    subprocess.run(play_cmd, check=True)
    time.sleep(settle_seconds)              # wait for spike to fully decay
