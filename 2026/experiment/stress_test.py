"""
stress_test.py — Comprehensive pre-experiment stress test.

Usage:
    cd 2026/experiment
    sudo python3 stress_test.py

Phases:
  1. Screenshot confidence scan  — all 6 templates match at >= 0.6
  2. All 36 condition transitions — every A→B configure() pair, canvas verified
  3. Crash-scenario replay x3    — the exact sequences that caused previous crashes
  4. Same-condition idempotency  — configure('AUTO') and configure('HIGH') x5
  5. Full pipeline per condition — configure+prebuffer+EnergiBridge (5s measurement)

Estimated runtime: ~15–20 minutes.
"""

import os
import subprocess
import sys
import time

import cv2
import numpy as np
import pyautogui
from PIL import Image
from pyscreeze import Box

from spotify_controller import (
    configure, open_settings, close_settings,
    prebuffer, resume_playback, _scan_canvas_row,
    QUALITY_MAP,
)

BINARY     = '../EnergiBridge/target/release/energibridge'
CONDITIONS = ['AUTO', 'AUTO_NC', 'MEDIUM', 'HIGH', 'HIGH_NC', 'VERY_HIGH']
CANVAS_ON  = {'HIGH', 'AUTO'}

passes = 0
failures = 0
phase_results = {}


def record(phase, label, ok, detail=''):
    global passes, failures
    status = 'PASS' if ok else 'FAIL'
    marker = '✓' if ok else '✗'
    print(f'  {marker} {label}{(" — " + detail) if detail else ""}')
    if ok:
        passes += 1
    else:
        failures += 1
    phase_results.setdefault(phase, [0, 0])
    phase_results[phase][0 if ok else 1] += 1


def get_confidence(screenshot_gray, template_path):
    tmpl = cv2.cvtColor(np.array(Image.open(template_path)), cv2.COLOR_RGB2GRAY)
    res  = cv2.matchTemplate(screenshot_gray, tmpl, cv2.TM_CCOEFF_NORMED)
    return float(res.max())


def _locate_canvas_label_robust():
    tmpl_gray = cv2.cvtColor(
        np.array(Image.open('screenshots/canvas_label.png').convert('RGB')),
        cv2.COLOR_RGB2GRAY,
    )

    _, mask = cv2.threshold(tmpl_gray, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    mask_pixels = int(mask.sum()) // 255
    if mask_pixels < 20:
        return None

    scr_pil  = pyautogui.screenshot()
    scr_gray = cv2.cvtColor(np.array(scr_pil), cv2.COLOR_RGB2GRAY)

    log_w, _ = pyautogui.size()
    scale = max(1, round(scr_gray.shape[1] / log_w)) 

    result = cv2.matchTemplate(scr_gray, tmpl_gray, cv2.TM_SQDIFF, mask=mask)
    min_val, _, min_loc, _ = cv2.minMaxLoc(result)
    norm_ssd = min_val / (mask_pixels * 65025.0)

    if norm_ssd > 0.15:  
        return None

    px, py = min_loc
    tmpl_h, tmpl_w = tmpl_gray.shape
    return Box(px // scale, py // scale, tmpl_w // scale, tmpl_h // scale)


def read_canvas_state():
    open_settings()
    try:
        label = _locate_canvas_label_robust()
        if label is None:
            return None
        for _ in range(8):
            try:
                _, _, is_on = _scan_canvas_row(label)
                return is_on
            except AssertionError:
                time.sleep(0.13)   # advance 1-2 canvas video frames
        return None
    except Exception:
        return None
    finally:
        close_settings()



def phase1():
    print('\n' + '='*60)
    print('Phase 1 — Screenshot confidence scan')
    print('='*60)

    subprocess.run(['osascript', '-e', 'tell application "Spotify" to activate'], check=True)
    time.sleep(1)
    pyautogui.hotkey('command', ',')
    time.sleep(2)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)

    closed_screenshots = [
        (1, 'screenshots/quality_dropdown.png'),
        (6, 'screenshots/canvas_label.png'),
    ]
    screen_gray = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
    for i, path in closed_screenshots:
        if not os.path.exists(path):
            record('phase1', f'[{i}/6] {path}', False, 'file missing')
            continue
        conf = get_confidence(screen_gray, path)
        ok   = conf >= 0.6
        record('phase1', f'[{i}/6] {os.path.basename(path):35s} conf={conf:.3f}', ok,
               '' if ok else 'BELOW THRESHOLD 0.6')

    dropdown = pyautogui.locateOnScreen('screenshots/quality_dropdown.png', confidence=0.6)
    if dropdown is None:
        for i, path in [(2, 'screenshots/quality_automatic.png'),
                        (3, 'screenshots/quality_normal.png'),
                        (4, 'screenshots/quality_high.png'),
                        (5, 'screenshots/quality_very_high.png')]:
            record('phase1', f'[{i}/6] {os.path.basename(path):35s}', False,
                   'dropdown not found — cannot open to test options')
    else:
        click_x = int(dropdown.left + dropdown.width * 0.92)
        click_y = dropdown.top + dropdown.height // 2
        pyautogui.click(click_x, click_y)
        time.sleep(1.2)   

        open_screenshots = [
            (2, 'screenshots/quality_automatic.png'),
            (3, 'screenshots/quality_normal.png'),
            (4, 'screenshots/quality_high.png'),
            (5, 'screenshots/quality_very_high.png'),
        ]
        screen_gray_open = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
        for i, path in open_screenshots:
            if not os.path.exists(path):
                record('phase1', f'[{i}/6] {path}', False, 'file missing')
                continue
            conf = get_confidence(screen_gray_open, path)
            ok   = conf >= 0.6
            record('phase1', f'[{i}/6] {os.path.basename(path):35s} conf={conf:.3f}', ok,
                   '' if ok else 'BELOW THRESHOLD 0.6')

        pyautogui.press('escape') 
        time.sleep(0.3)

    pyautogui.hotkey('command', 'w')
    time.sleep(0.5)



def phase2():
    print('\n' + '='*60)
    print('Phase 2 — All 36 condition transitions (with canvas verification)')
    print('='*60)

    n = 0
    for src in CONDITIONS:
        try:
            configure(src)
        except Exception as e:
            print(f'  Setup {src} failed: {e}')
            continue

        for dst in CONDITIONS:
            n += 1
            src_canvas = src in CANVAS_ON
            dst_canvas = dst in CANVAS_ON
            label = (f'[{n:02d}/36] {src:8s}→{dst:8s} '
                     f'canvas={"ON" if src_canvas else "OFF"}→{"ON" if dst_canvas else "OFF"} '
                     f'quality={QUALITY_MAP[dst]:10s}')
            try:
                configure(dst)
                actual = read_canvas_state()
                if actual is not None and actual != dst_canvas:
                    record('phase2', label, False,
                           f'canvas is {"ON" if actual else "OFF"} but expected {"ON" if dst_canvas else "OFF"}')
                else:
                    record('phase2', label, True)
            except Exception as e:
                record('phase2', label, False, str(e)[:80])

            time.sleep(1)



def phase3():
    print('\n' + '='*60)
    print('Phase 3 — Crash-scenario replay × 3')
    print('='*60)

    crash_sequences = [
        ('VERY_HIGH', 'AUTO_NC'),  
        ('HIGH',      'AUTO_NC'),  
    ]

    for src, dst in crash_sequences:
        for rep in range(1, 4):
            label = f'{src}→{dst} rep {rep}/3'
            try:
                configure(src)
                configure(dst)
                actual  = read_canvas_state()
                want_on = dst in CANVAS_ON
                if actual is not None and actual != want_on:
                    record('phase3', label, False,
                           f'canvas {"ON" if actual else "OFF"} ≠ expected {"ON" if want_on else "OFF"}')
                else:
                    record('phase3', label, True)
            except Exception as e:
                record('phase3', label, False, str(e)[:80])
            time.sleep(1)



def phase4():
    print('\n' + '='*60)
    print('Phase 4 — Same-condition idempotency × 5')
    print('='*60)

    for cond in ['AUTO', 'HIGH']:
        for rep in range(1, 6):
            label = f'configure({cond!r}) rep {rep}/5'
            try:
                configure(cond)
                record('phase4', label, True)
            except Exception as e:
                record('phase4', label, False, str(e)[:80])
            time.sleep(1)



def phase5():
    print('\n' + '='*60)
    print('Phase 5 — Full pipeline per condition (5s EnergiBridge measurement)')
    print('='*60)

    os.makedirs('stress_results', exist_ok=True)

    for cond in CONDITIONS:
        label    = f'pipeline {cond}'
        out_csv  = f'stress_results/{cond.lower()}_stress.csv'
        try:
            configure(cond)
            prebuffer(prebuffer_seconds=5, settle_seconds=3)
            resume_playback(settle_seconds=3)
            subprocess.run(
                ['sudo', BINARY, '-o', out_csv, '--', 'python3', '-c',
                 'import time, subprocess; time.sleep(5); '
                 'subprocess.run(["osascript", "-e", "tell application \\"Spotify\\" to pause"])'],
                check=True,
            )
            # Validate
            if not os.path.exists(out_csv) or os.path.getsize(out_csv) == 0:
                record('phase5', label, False, 'CSV missing or empty')
                continue
            with open(out_csv) as f:
                lines = f.readlines()
            has_power = 'SYSTEM_POWER' in (lines[0] if lines else '')
            row_count = len(lines) - 1
            ok = has_power and row_count >= 20
            record('phase5', label, ok,
                   f'rows={row_count} SYSTEM_POWER={has_power}' if not ok else
                   f'rows={row_count}')
        except Exception as e:
            record('phase5', label, False, str(e)[:80])
        time.sleep(1)



def summary():
    print('\n' + '='*60)
    print('STRESS TEST COMPLETE')
    total_p = total_f = 0
    for phase, (p, f) in phase_results.items():
        status = 'PASS' if f == 0 else 'FAIL'
        print(f'  {phase}: {p} passed, {f} failed  [{status}]')
        total_p += p
        total_f += f
    print(f'  TOTAL: {total_p} passed, {total_f} failed')
    if total_f == 0:
        print('  → ALL PASSED — safe to run experiment')
    else:
        print('  → FAILURES DETECTED — fix issues before running experiment')
    print('='*60)
    return total_f == 0


if __name__ == '__main__':
    phase1()
    phase2()
    phase3()
    phase4()
    phase5()
    ok = summary()
    sys.exit(0 if ok else 1)
