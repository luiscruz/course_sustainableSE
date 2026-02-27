import argparse
import logging
import os
import random
import time
from dataclasses import dataclass
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    ChromeDriverManager = None

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("bot_manager")


@dataclass
class BotConfig:
    platform: str
    meeting_url: str
    num_bots: int
    guest_name: str
    delay: float


def create_bot_driver() -> webdriver.Chrome:
    opts = Options()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--use-fake-ui-for-media-stream")
    opts.add_argument("--use-fake-device-for-media-stream")
    opts.add_argument("--mute-audio")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--incognito")

    opts.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.notifications": 2,
    })

    service = Service(ChromeDriverManager().install()) if ChromeDriverManager else Service()
    driver = webdriver.Chrome(service=service, options=opts)
    return driver


def prevent_inactivity(driver, bot_id):
    """Simulates a tiny mouse movement to trick the platform into thinking the user is active."""
    try:
        actions = ActionChains(driver)
        # Move mouse by 1 pixel and back
        actions.move_by_offset(1, 1).perform()
        actions.move_by_offset(-1, -1).perform()

        # Optional: Send a 'Shift' key press to the body (doesn't affect chat/UI)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SHIFT)

        log.debug(f"Keep-alive signal sent for Bot {bot_id}")
    except Exception:
        # If the window is closed or navigation failed, we skip
        pass


def handle_media_toggle(driver, platform):
    wait = WebDriverWait(driver, 15)
    try:
        if platform == "meet":
            mic_xpath = "//div[@role='button'][contains(@aria-label, 'microphone')]"
            cam_xpath = "//div[@role='button'][contains(@aria-label, 'camera')]"
            mic_btn = wait.until(EC.element_to_be_clickable((By.XPATH, mic_xpath)))
            driver.execute_script("arguments[0].click();", mic_btn)
            time.sleep(0.5)
            cam_btn = wait.until(EC.element_to_be_clickable((By.XPATH, cam_xpath)))
            driver.execute_script("arguments[0].click();", cam_btn)
        elif platform == "teams":
            mic_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-tid='prejoin-mic-toggle']")))
            driver.execute_script("arguments[0].click();", mic_btn)
            time.sleep(0.5)
            cam_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-tid='prejoin-video-toggle']")))
            driver.execute_script("arguments[0].click();", cam_btn)
    except Exception as e:
        log.warning(f"Media toggle UI fail, using shortcuts.")
        actions = ActionChains(driver)
        if platform == "meet":
            actions.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform()
            actions.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform()


def join_process(driver, config: BotConfig, bot_id: int):
    wait = WebDriverWait(driver, 30)
    driver.get(config.meeting_url)
    bot_display_name = f"{config.guest_name} {bot_id}"

    try:
        if config.platform == "meet":
            name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label*='name']")))
            handle_media_toggle(driver, "meet")
            time.sleep(1)
            name_field.send_keys(bot_display_name)
            join_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(), 'Ask to join')] | //span[contains(text(), 'Join now')]")))
            join_btn.click()
        elif config.platform == "teams":
            try:
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue on this browser')]"))).click()
            except:
                pass
            handle_media_toggle(driver, "teams")
            name_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Type your name']")))
            name_input.send_keys(bot_display_name)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Join now')]"))).click()
        log.info(f" Bot {bot_id} joined.")
    except Exception as e:
        log.error(f" Bot {bot_id} failed: {str(e)[:50]}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", choices=["meet", "teams"], required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--bots", type=int, default=1)
    parser.add_argument("--delay", type=float, default=5.0)
    args = parser.parse_args()

    config = BotConfig(
        platform=args.platform,
        meeting_url=args.url,
        num_bots=args.bots,
        guest_name=os.getenv("GUEST_NAME", "Meeting Bot"),
        delay=args.delay
    )

    active_drivers = []

    try:
        # Initial Deployment
        for i in range(config.num_bots):
            bot_num = i + 1
            log.info(f"🚀 Deploying Bot {bot_num}...")
            driver = create_bot_driver()
            active_drivers.append(driver)
            join_process(driver, config, bot_num)

            if bot_num < config.num_bots:
                time.sleep(random.uniform(config.delay, config.delay + 2))

        # --- THE BYPASS LOOP ---
        log.info("All bots deployed. Monitoring for inactivity...")
        while True:
            # Wait 60 seconds between pulses
            time.sleep(60)
            for idx, driver in enumerate(active_drivers):
                prevent_inactivity(driver, idx + 1)

    except KeyboardInterrupt:
        log.info("Shutting down...")
    finally:
        for d in active_drivers:
            d.quit()


if __name__ == "__main__":
    main()