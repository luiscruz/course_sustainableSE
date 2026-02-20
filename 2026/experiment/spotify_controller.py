"""
spotify_controller.py — Configure Spotify settings via PyAutoGUI + AppleScript.

Settings are changed BEFORE EnergiBridge starts so the settings-change energy
is NOT included in the measurement window.

Prerequisites:
  - macOS: grant accessibility + screen recording permissions to Terminal/IDE
  - pip install pyautogui pillow
  - Reference screenshots in screenshots/ directory (see README)
"""

import os
import subprocess
import time
import pyautogui

# Map experiment condition labels to Spotify UI quality strings
QUALITY_MAP = {
    'LOW':    'low',
    'MEDIUM': 'normal',
    'HIGH':   'very_high',
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
    dropdown = pyautogui.locateOnScreen('screenshots/quality_dropdown.png', confidence=0.7)
    assert dropdown is not None, (
        'Could not locate quality dropdown button on screen.\n'
        'Make sure Spotify Settings > Audio Quality is visible and '
        'screenshots/quality_dropdown.png matches the dropdown arrow.'
    )
    pyautogui.click(dropdown)
    time.sleep(1.0)   # wait for dropdown list to appear

    # Step 2 — click the desired option
    quality_key = QUALITY_MAP[condition]
    option_path = f'screenshots/quality_{quality_key}.png'
    btn = pyautogui.locateOnScreen(option_path, confidence=0.7)
    assert btn is not None, (
        f'Could not locate quality option on screen: {option_path}\n'
        'Make sure the dropdown is open and the reference screenshot matches '
        'the option in its unselected state.'
    )
    pyautogui.click(btn)
    time.sleep(0.5)


def _find_canvas_toggle(dropdown):
    """
    Locate Canvas toggle via pixel-column scan (fallback when screenshots fail).

    Scans a 5px-wide strip starting from the dropdown's y position downwards.
    Toggle order from the quality dropdown: Auto adjust quality (0), compact
    library layout (1), show local files (2), show now-playing panel (3),
    Canvas (4).

    Handles Retina (2x) displays: PIL returns physical pixels, so cy values are
    divided by the detected scale factor before being used as click coordinates.

    Returns (toggle_x, canvas_y, is_on).
    """
    # Right-align with the dropdown control column; the toggle oval shares the
    # same right-hand column as the dropdown arrow.
    toggle_x = dropdown.left + dropdown.width - 13
    y_start  = dropdown.top                        # scan from the dropdown downwards
    screen_h = pyautogui.size().height
    scan_h   = min(800, screen_h - y_start - 1)   # logical pixels; stay on screen

    # One screenshot grab — fast batch access via PIL
    img    = pyautogui.screenshot(region=(toggle_x - 2, y_start, 5, scan_h))
    # On Retina (2×) displays PIL returns physical pixels; detect scale
    scale  = max(1, round(img.height / scan_h))    # 1 on normal, 2 on Retina
    cx     = img.width // 2                         # centre column in physical pixels
    pixels = img.load()

    regions, in_region, region_start = [], False, 0
    for y in range(img.height):
        r, g, b   = pixels[cx, y][:3]
        is_green  = g > 140 and r < 100                                    # Spotify ON (green)
        is_grey   = 70 < r < 180 and abs(r - g) < 25 and abs(g - b) < 25  # OFF (grey oval)
        is_toggle = is_green or is_grey

        if is_toggle and not in_region:
            in_region, region_start = True, y
        elif not is_toggle and in_region:
            in_region = False
            if y - region_start >= 6 * scale:                             # noise threshold
                cy        = region_start + (y - region_start) // 2
                rc, gc    = pixels[cx, cy][:2]
                canvas_y  = y_start + cy // scale                         # logical coordinate
                regions.append((canvas_y, gc > 140 and rc < 100))

    assert len(regions) >= 5, (
        f'Canvas toggle not found — found only {len(regions)} toggle region(s) in scan.\n'
        'Expected ≥5 toggles below the quality dropdown: auto-adjust, compact-lib,\n'
        'local-files, now-playing, Canvas.\n'
        'Run the calibration command to debug:\n'
        '  python3 -c "from spotify_controller import _debug_canvas_scan; _debug_canvas_scan()"'
    )
    canvas_y, is_on = regions[4]     # 5th toggle below the dropdown = Canvas
    return toggle_x, canvas_y, is_on


def _debug_canvas_scan():
    """One-shot diagnostic: open settings and print all toggle positions found."""
    open_settings()
    time.sleep(0.5)
    dropdown = pyautogui.locateOnScreen('screenshots/quality_dropdown.png', confidence=0.7)
    assert dropdown is not None, 'quality_dropdown not found'
    print(f'Dropdown at: {dropdown}')
    toggle_x = dropdown.left + dropdown.width - 13
    y_start  = dropdown.top
    screen_h = pyautogui.size().height
    scan_h   = min(800, screen_h - y_start - 1)
    img      = pyautogui.screenshot(region=(toggle_x - 2, y_start, 5, scan_h))
    scale    = max(1, round(img.height / scan_h))
    cx       = img.width // 2
    pixels   = img.load()
    print(f'Image size: {img.size}, scale: {scale}, scan_h (logical): {scan_h}')
    regions, in_region, region_start = [], False, 0
    for y in range(img.height):
        r, g, b = pixels[cx, y][:3]
        is_toggle = (g > 140 and r < 100) or (70 < r < 180 and abs(r-g) < 25 and abs(g-b) < 25)
        if is_toggle and not in_region:
            in_region, region_start = True, y
        elif not is_toggle and in_region:
            in_region = False
            if y - region_start >= 6 * scale:
                cy = region_start + (y - region_start) // 2
                rc, gc = pixels[cx, cy][:2]
                canvas_y = y_start + cy // scale
                regions.append((canvas_y, gc > 140 and rc < 100))
    print(f'Toggles found (logical_y, is_on): {regions}')
    print(f'Expected Canvas at regions[4]: {regions[4] if len(regions)>=5 else "NOT FOUND"}')


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
    Canvas is ON only for HIGH, OFF for LOW and MEDIUM.

    Strategy:
      1. Locate the Canvas row using its unique label (canvas_label.png).
      2. Scan the row's pixels for green (ON) or grey (OFF) toggle colours —
         pixel colour is unambiguous and avoids template-matching false positives.
      3. Click only if current state does not match desired state.

    Fallback: pixel-column scan anchored on the quality dropdown.
    """
    want_on    = (condition == 'HIGH')
    label_path = 'screenshots/canvas_label.png'

    # ── Label + pixel-colour detection (preferred) ────────────────────────────
    if os.path.exists(label_path):
        try:
            label = pyautogui.locateOnScreen(label_path, confidence=0.7)
        except pyautogui.ImageNotFoundException:
            label = None

        if label is not None:
            toggle_x, toggle_y, is_on = _scan_canvas_row(label)
            if is_on != want_on:
                pyautogui.click(toggle_x, toggle_y)
                time.sleep(0.5)
            return

    # ── Pixel-scan fallback ───────────────────────────────────────────────────
    dropdown = pyautogui.locateOnScreen('screenshots/quality_dropdown.png', confidence=0.7)
    assert dropdown is not None, (
        'Could not locate quality dropdown to anchor Canvas scan.\n'
        'Make sure Spotify Settings > Audio Quality is visible.'
    )
    toggle_x, canvas_y, is_on = _find_canvas_toggle(dropdown)
    if is_on != want_on:
        pyautogui.click(toggle_x, canvas_y)
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


SEEK_SCRIPT = 'tell application "Spotify" to set player position to 0'


def seek_to_start():
    """Seek Spotify playback position to 0:00 via AppleScript."""
    subprocess.run(['osascript', '-e', SEEK_SCRIPT], check=True)


def prebuffer(prebuffer_seconds=15, settle_seconds=5):
    """
    Warm the Spotify audio buffer at the CURRENTLY configured quality.
    Call AFTER configure() and BEFORE EnergiBridge starts.

    Sequence: seek → play 15s → seek → pause → settle 5s
    The opening seek is defensive: handles crashes that left playback mid-song.
    """
    bring_spotify_to_front()
    play_cmd  = ['osascript', '-e', 'tell application "Spotify" to play']
    pause_cmd = ['osascript', '-e', 'tell application "Spotify" to pause']

    seek_to_start()
    time.sleep(0.5)
    subprocess.run(play_cmd, check=True)
    time.sleep(prebuffer_seconds)   # buffer fills at correct bitrate
    seek_to_start()
    time.sleep(0.5)
    subprocess.run(pause_cmd, check=True)
    time.sleep(settle_seconds)      # CPU/network decay before measurement
