import time
import random
import csv
import os
import json
import subprocess
import platform
from tqdm import tqdm
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURATION ---
OUTPUT_CSV = "experiment_results.csv"
WARMUP_ROUNDS = 5
ACTUAL_ROUNDS = 30
DURATION = 15
BROWSER = "firefox"        # "chrome" or "firefox"
MAX_RETRIES = 2

CONFIG_PATH = "pyenergibridge_config.json"


def load_energibridge_path() -> str:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    path = cfg.get("binary_path")
    if not path:
        raise FileNotFoundError(f"`binary_path` missing in {CONFIG_PATH}")
    if not os.path.exists(path):
        raise FileNotFoundError(f"EnergiBridge binary not found at: {path}")
    return path


ENERGIBRIDGE_EXE = load_energibridge_path()


# --- SELENIUM SETUP ---
def get_driver():
    if BROWSER == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--incognito")
        opts.add_argument("--use-fake-ui-for-media-stream")
        # Avoid --no-sandbox on Windows/macOS; it's primarily for Linux containers.
        driver = webdriver.Chrome(options=opts)
    elif BROWSER == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("--private")
        opts.set_preference("media.navigator.permission.disabled", True)
        driver = webdriver.Firefox(options=opts)
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")
    return driver


def _build_anchor_command(seconds: int):
    system = platform.system()
    if system == "Windows":
        return ["cmd", "/c", f"timeout /t {seconds} >nul"]
    # Linux / macOS
    return ["sleep", str(seconds)]


def measure_window(seconds: int, temp_csv: str):
    """
    Measures system energy for `seconds` while the browser benchmark continues.
    Returns (energy_joules, exec_time_seconds).
    """
    anchor = _build_anchor_command(seconds)
    cmd = [ENERGIBRIDGE_EXE, "--summary", *anchor]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = (proc.stdout or "") + "\n" + (proc.stderr or "")

    # Parse EnergiBridge summary line:
    # "Energy consumption in joules: X for Y sec of execution."
    energy = None
    exec_time = None

    for line in out.splitlines():
        line = line.strip()
        if line.lower().startswith("energy consumption in joules:"):
            try:
                joules_str = line.split("joules:")[1].split("for")[0].strip()
                secs_str = line.split("for")[1].split("sec")[0].strip()
                energy = float(joules_str)
                exec_time = float(secs_str)
                break
            except Exception:
                pass

    if energy is None or exec_time is None:
        raise RuntimeError(
            "Failed to parse EnergiBridge summary output.\n"
            f"Exit code: {proc.returncode}\n"
            f"Output:\n{out}"
        )

    return energy, exec_time


# TESTS
def run_control(driver, duration):
    driver.get("about:blank")
    return measure_window(duration, "temp_control.csv")


def run_speedometer(driver, duration):
    driver.get("https://browserbench.org/Speedometer3.1/")
    wait = WebDriverWait(driver, 30)
    start_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "start-tests-button")))
    start_btn.click()
    return measure_window(duration, "temp_speedometer.csv")


def run_jetstream(driver, duration):
    driver.get("https://browserbench.org/JetStream/")
    wait = WebDriverWait(driver, 60)
    start_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button")))
    start_btn.click()
    return measure_window(duration, "temp_jetstream.csv")


def run_motionmark(driver, duration):
    driver.get("https://browserbench.org/MotionMark1.3.1/")
    wait = WebDriverWait(driver, 60)
    start_btn = wait.until(EC.element_to_be_clickable((By.ID, "start-button")))
    start_btn.click()
    return measure_window(duration, "temp_motionmark.csv")


def main():
    output_file = f"{BROWSER}_{OUTPUT_CSV}"
    if not os.path.exists(output_file):
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Round_Type", "Test_Name", "Energy_Joules", "Duration_Sec", "Power_Avg_Watts"])

    tests = ["control", "speedometer", "jetstream", "motionmark"]

    queue = []
    for _ in range(WARMUP_ROUNDS):
        queue.append(("warmup", random.choice(tests)))

    actual_tasks = []
    for t in tests:
        actual_tasks.extend([t] * ACTUAL_ROUNDS)
    random.shuffle(actual_tasks)

    for t in actual_tasks:
        queue.append(("actual", t))

    print(f"Total runs scheduled: {len(queue)}")

    for i, (round_type, test_name) in enumerate(tqdm(queue, desc="Benchmarks", unit="test")):
        tqdm.write(f"[{i + 1}/{len(queue)}] Running {round_type} -> {test_name}...")

        for attempt in range(1, MAX_RETRIES + 1):
            driver = None
            try:
                driver = get_driver()

                if test_name == "control":
                    energy, exec_time = run_control(driver, DURATION)
                elif test_name == "speedometer":
                    energy, exec_time = run_speedometer(driver, DURATION)
                elif test_name == "jetstream":
                    energy, exec_time = run_jetstream(driver, DURATION)
                elif test_name == "motionmark":
                    energy, exec_time = run_motionmark(driver, DURATION)
                else:
                    raise ValueError(f"Unknown test: {test_name}")

                avg_power = energy / exec_time if exec_time > 0 else 0.0

                with open(output_file, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.now().isoformat(), round_type, test_name, energy, exec_time, avg_power])

                tqdm.write(f"   -> {energy:.2f} J over {exec_time:.2f} s ({avg_power:.2f} W)")
                break

            except Exception as e:
                if attempt < MAX_RETRIES:
                    tqdm.write(f"   -> Attempt {attempt} failed, retrying: {e}")
                    time.sleep(3)
                else:
                    tqdm.write(f"   -> FAILED after {MAX_RETRIES} attempts: {e}")

            finally:
                if driver:
                    driver.quit()

        time.sleep(2)


if __name__ == "__main__":
    main()