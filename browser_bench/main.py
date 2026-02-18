import time
import random
import csv
import os
from tqdm import tqdm
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyEnergiBridge.api import EnergiBridgeRunner

# --- CONFIGURATION ---
OUTPUT_CSV = "experiment_results.csv"
WARMUP_ROUNDS = 5
ACTUAL_ROUNDS = 30
DURATION = 15  # Seconds to measure per test
BROWSER = "firefox"


# --- SELENIUM SETUP ---
def get_driver():
    if BROWSER == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--incognito")
        opts.add_argument("--use-fake-ui-for-media-stream")
        opts.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=opts)
    elif BROWSER == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("--private")
        opts.set_preference("media.navigator.permission.disabled", True)
        driver = webdriver.Firefox(options=opts)
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")
    return driver


def run_control(driver, runner, duration):
    """Idle test: Open browser to static page and wait."""
    driver.get("https://browserbench.org/")

    # Start Energy Measurement
    runner.start(results_file="temp_control.csv")
    try:
        time.sleep(duration)
    finally:
        return runner.stop()


def run_speedometer(driver, runner, duration):
    """Speedometer 3.1 Test"""
    driver.get("https://browserbench.org/Speedometer3.1/")
    wait = WebDriverWait(driver, 10)

    # Wait for the app to load and find start button
    start_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "start-tests-button")))

    runner.start(results_file="temp_speedometer.csv")
    try:
        start_btn.click()
        time.sleep(duration)
    finally:
        return runner.stop()


def run_jetstream(driver, runner, duration):
    """JetStream 2 Test"""
    driver.get("https://browserbench.org/JetStream/")
    wait = WebDriverWait(driver, 30)  # JetStream loads 325 tests before button appears

    start_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button")))

    runner.start(results_file="temp_jetstream.csv")
    try:
        start_btn.click()
        time.sleep(duration)
    finally:
        return runner.stop()


def run_motionmark(driver, runner, duration):
    """MotionMark 1.3.1 Test"""
    driver.get("https://browserbench.org/MotionMark1.3.1/")
    wait = WebDriverWait(driver, 30)

    # MotionMark requires clicking "Run Benchmark"
    start_btn = wait.until(EC.element_to_be_clickable((By.ID, "start-button")))

    runner.start(results_file="temp_motionmark.csv")
    try:
        start_btn.click()
        time.sleep(duration)
    finally:
        return runner.stop()


# --- MAIN ORCHESTRATOR ---

MAX_RETRIES = 2

def main():
    # 1. Initialize API
    runner = EnergiBridgeRunner()

    # 2. Setup Master CSV
    output_file = BROWSER + "_" + OUTPUT_CSV
    if not os.path.exists(output_file):
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["Timestamp", "Round_Type", "Test_Name", "Energy_Joules", "Duration_Sec", "Power_Avg_Watts"])

    # 3. generate execution queue
    tests = ["control", "speedometer", "jetstream", "motionmark"]

    # Create the list of actual runs
    queue = []

    # Add Warmups (Random selection)
    for _ in range(WARMUP_ROUNDS):
        queue.append(("warmup", random.choice(tests)))

    # Add Actual Rounds (Ensure exact count per type)
    actual_tasks = []
    for t in tests:
        actual_tasks.extend([t] * ACTUAL_ROUNDS)
    random.shuffle(actual_tasks)  # Randomize order

    for t in actual_tasks:
        queue.append(("actual", t))

    print(f"Total runs scheduled: {len(queue)}")

    # 4. execution loop
    for i, (round_type, test_name) in enumerate(tqdm(queue, desc="Benchmarks", unit="test")):
        tqdm.write(f"[{i + 1}/{len(queue)}] Running {round_type} -> {test_name}...")

        for attempt in range(1, MAX_RETRIES + 1):
            driver = None
            try:
                driver = get_driver()

                energy = 0.0
                exec_time = 0.0

                if test_name == "control":
                    energy, exec_time = run_control(driver, runner, DURATION)
                elif test_name == "speedometer":
                    energy, exec_time = run_speedometer(driver, runner, DURATION)
                elif test_name == "jetstream":
                    energy, exec_time = run_jetstream(driver, runner, DURATION)
                elif test_name == "motionmark":
                    energy, exec_time = run_motionmark(driver, runner, DURATION)

                # Calculate Average Power
                avg_power = energy / exec_time if exec_time > 0 else 0

                # Save to CSV
                with open(output_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        datetime.now().isoformat(),
                        round_type,
                        test_name,
                        energy,
                        exec_time,
                        avg_power
                    ])

                tqdm.write(f"   -> {energy:.2f} J over {exec_time:.2f} s ({avg_power:.2f} W)")
                break  # Success, move to next test

            except Exception as e:
                # Ensure EnergiBridge stops if it was left running
                try:
                    runner.stop()
                except:
                    pass

                if attempt < MAX_RETRIES:
                    tqdm.write(f"   -> Attempt {attempt} failed, retrying: {e}")
                    time.sleep(3)
                else:
                    tqdm.write(f"   -> FAILED after {MAX_RETRIES} attempts: {e}")

            finally:
                if driver:
                    driver.quit()

        # 5. Cooldown for Thermal Consistency
        time.sleep(2)


if __name__ == "__main__":
    main()
    