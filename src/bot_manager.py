"""
Bot Manager — Selenium-based automation for joining Google Meet and Microsoft Teams calls.

Spins up multiple headless Chrome instances with fake media streams.
Each bot joins the meeting, stays for a configurable duration, then leaves.
"""

import argparse
import logging
import os
import random
import sys
import time
import threading
from dataclasses import dataclass, field
from typing import Optional

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    WebDriverException,
)

try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    ChromeDriverManager = None

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("bot_manager")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass
class BotConfig:
    platform: str  # "meet" or "teams"
    meeting_url: str
    num_bots: int = 1
    call_duration: int = 120  # seconds each bot stays in the call
    join_interval_min: int = 5  # min seconds between bot joins
    join_interval_max: int = 15  # max seconds between bot joins
    headless: bool = False  # Meet blocks headless Chrome — always visible
    guest_name: str = "Bot"
    chrome_binary: Optional[str] = None
    chromedriver_path: Optional[str] = None

    @classmethod
    def from_env_and_args(cls, args) -> "BotConfig":
        return cls(
            platform=args.platform,
            meeting_url=args.url,
            num_bots=args.bots,
            call_duration=args.duration,
            join_interval_min=args.join_min,
            join_interval_max=args.join_max,
            headless=not args.visible,
            guest_name=os.getenv("TEAMS_GUEST_NAME", "Bot"),
            chrome_binary=os.getenv("CHROME_BINARY") or None,
            chromedriver_path=os.getenv("CHROMEDRIVER_PATH") or None,
        )


# ---------------------------------------------------------------------------
# Chrome setup
# ---------------------------------------------------------------------------

def create_chrome_options(config: BotConfig, bot_id: int) -> Options:
    """Create Chrome options with fake media streams and appropriate flags.

    NOTE: Google Meet blocks headless Chrome ("You can't join this video call").
    We always run in visible (non-headless) mode. On Linux servers without a
    display, use Xvfb (virtual framebuffer) to create a virtual display:
        Xvfb :99 -screen 0 1280x720x24 &
        export DISPLAY=:99
    """
    opts = Options()

    # Fake media streams — no real camera/mic needed
    opts.add_argument("--use-fake-device-for-media-stream")
    opts.add_argument("--use-fake-ui-for-media-stream")

    # Disable notifications and infobars
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-infobars")
    opts.add_argument("--disable-extensions")

    # Auto-grant permissions (camera, mic)
    opts.add_argument("--auto-select-desktop-capture-source=Entire screen")
    opts.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.notifications": 2,

            # Prevent external Teams app from launching
            "protocol_handler.excluded_schemes": {
                "msteams": True
            }
        },
    )

    # Anti-bot-detection: Google Meet rejects headless Chrome, so we run
    # in visible mode and mask Selenium automation signals.
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--disable-external-intent-requests")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Meet never fires the "load" event (streaming WebSockets). Use "eager"
    # so driver.get() returns as soon as DOM is ready, not waiting for load.
    opts.page_load_strategy = "eager"

    # Do NOT use headless — Meet blocks it with "You can't join this video call"

    # Performance / stability
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1280,720")
    opts.add_argument(f"--user-data-dir=/tmp/chrome_bot_{bot_id}")
    opts.add_argument("--disable-background-timer-throttling")
    opts.add_argument("--disable-backgrounding-occluded-windows")
    opts.add_argument("--disable-renderer-backgrounding")

    if config.chrome_binary:
        opts.binary_location = config.chrome_binary

    return opts


def create_driver(config: BotConfig, bot_id: int) -> webdriver.Chrome:
    """Create a Chrome WebDriver instance with anti-detection."""
    opts = create_chrome_options(config, bot_id)

    if config.chromedriver_path:
        service = Service(executable_path=config.chromedriver_path)
    elif ChromeDriverManager:
        service = Service(ChromeDriverManager().install())
    else:
        service = Service()  # rely on chromedriver being in PATH

    driver = webdriver.Chrome(service=service, options=opts)
    driver.set_page_load_timeout(60)

    # Hide navigator.webdriver flag so Meet doesn't detect automation
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })

    return driver


# ---------------------------------------------------------------------------
# Google Meet join logic
# ---------------------------------------------------------------------------

def join_google_meet(driver: webdriver.Chrome, url: str, bot_id: int, guest_name: str):
    log.info(f"Bot {bot_id}: Opening Google Meet URL")
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    # 1. Handle the Name Input
    time.sleep(3)
    name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label*='name']")))
    name_input.send_keys(f"{guest_name} {bot_id}")
    log.info(f"Bot {bot_id}: Name entered")
    # 3. Click the Join Button
    # We use a combined XPATH to find "Join now" OR "Ask to join"
    join_xpath = "//button[span[contains(text(), 'Join')] or contains(., 'Join')]"
    join_btn = wait.until(EC.element_to_be_clickable((By.XPATH, join_xpath)))
    
    # A tiny sleep here prevents "ElementClickInterceptedException" 
    # as animations finish
    join_btn.click()
    log.info(f"Bot {bot_id}: Join button clicked")
    time.sleep(1)


def leave_google_meet(driver: webdriver.Chrome, bot_id: int):
    """Leave a Google Meet call."""
    # Direct lookup since we only have one primary selector
    btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Leave call']")
    
    # Use JS click to bypass potential overlays
    driver.execute_script("arguments[0].click();", btn)
    log.info(f"Bot {bot_id}: Left Google Meet")


# ---------------------------------------------------------------------------
# Microsoft Teams join logic
# ---------------------------------------------------------------------------

def join_microsoft_teams(driver: webdriver.Chrome, url: str, bot_id: int, guest_name: str):
  
    log.info(f"Bot {bot_id}: Opening Teams URL")
    driver.get(url)
    time.sleep(1)
    # Step 1: Launcher — click "Continue on this browser"
    _select_teams_browser_option(driver, bot_id)
    time.sleep(6)  # Teams takes a while to load the pre-join screen

    _set_teams_guest_name(driver, bot_id, guest_name)
    # Step 5: Click "Join now"
    _click_teams_join(driver, bot_id)
    log.info(f"Bot {bot_id}: In Teams lobby (or meeting)")
    time.sleep(3)  # Wait for lobby/meeting to stabilize


def _select_teams_browser_option(driver, bot_id):
    """Click 'Continue on this browser' on the Teams launcher page."""
    
    xpath = "//button[contains(., 'Continue on this browser')]"
    
    el = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", el)
    log.info(f"Bot {bot_id}: Selected 'Continue on this browser'")
    return

def _set_teams_guest_name(driver, bot_id, guest_name):
    """Enter guest display name in Teams pre-join screen."""
    selector = "input[placeholder='Type your name']"
    full_name = f"{guest_name} {bot_id}"

    name_input = driver.find_element(By.CSS_SELECTOR, selector)
    name_input.clear()
    name_input.send_keys(full_name)
    
    log.info(f"Bot {bot_id}: Set Teams guest name '{full_name}'")
    return 


def _click_teams_join(driver, bot_id):
    """Click the 'Join now' button in Teams pre-join screen using explicit waits."""
    xpath = "//button[contains(., 'Join now')]"
    

    # Wait up to 10 seconds for the button to be present and clickable
    # This replaces the manual 'range(3)' loop and 'sleep(3)'
    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    
    driver.execute_script("arguments[0].click();", btn)
    log.info(f"Bot {bot_id}: Clicked Teams 'Join now'")


def leave_microsoft_teams(driver, bot_id):
    driver.find_element("tag name", "body").click()
    time.sleep(2)

    ActionChains(driver) \
        .key_down(Keys.COMMAND) \
        .key_down(Keys.SHIFT) \
        .send_keys("h") \
        .key_up(Keys.SHIFT) \
        .key_up(Keys.COMMAND) \
        .perform()
    time.sleep(2)



# ---------------------------------------------------------------------------
# Bot lifecycle
# ---------------------------------------------------------------------------

@dataclass
class BotResult:
    bot_id: int
    join_time: float = 0.0
    leave_time: float = 0.0
    duration: float = 0.0
    success: bool = False
    error: Optional[str] = None


def run_single_bot(config: BotConfig, bot_id: int) -> BotResult:
    """Run a single bot: create browser, join call, wait, leave, close."""
    result = BotResult(bot_id=bot_id)
    driver = None

    try:
        driver = create_driver(config, bot_id)
        result.join_time = time.time()

        if config.platform == "meet":
            join_google_meet(driver, config.meeting_url, bot_id, config.guest_name)
        elif config.platform == "teams":
            join_microsoft_teams(driver, config.meeting_url, bot_id, config.guest_name)
        else:
            raise ValueError(f"Unknown platform: {config.platform}")

        # Stay in the call
        log.info(f"Bot {bot_id}: Staying in call for {config.call_duration}s")
        time.sleep(config.call_duration)

        # Leave (best-effort — don't fail the whole bot if leave button is tricky)
        try:
            if config.platform == "meet":
                leave_google_meet(driver, bot_id)
            else:
                leave_microsoft_teams(driver, bot_id)
        except Exception as e:
            log.warning(f"Bot {bot_id}: Leave error (non-fatal): {e}")

        result.leave_time = time.time()
        result.duration = result.leave_time - result.join_time
        result.success = True

    except Exception as e:
        result.error = str(e)
        log.error(f"Bot {bot_id}: Error — {e}")
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass
        # Clean up temp profile
        import shutil
        tmp_dir = f"/tmp/chrome_bot_{bot_id}"
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir, ignore_errors=True)

    return result

# ---------------------------------------------------------------------------
# Bot manager (orchestrator)
# ---------------------------------------------------------------------------

def run_bots(config: BotConfig) -> list[BotResult]:
    """
    Spin up multiple bots with random join intervals.
    Bots run in parallel threads; each bot joins, waits, then leaves.
    """
    log.info(f"Starting {config.num_bots} bots on {config.platform} — "
             f"duration={config.call_duration}s, "
             f"join interval={config.join_interval_min}-{config.join_interval_max}s")

    results: list[BotResult] = [None] * config.num_bots
    threads: list[threading.Thread] = []

    def _bot_worker(bot_id):
        results[bot_id] = run_single_bot(config, bot_id)

    for i in range(config.num_bots):
        if i > 0:
            delay = random.uniform(config.join_interval_min, config.join_interval_max)
            log.info(f"Waiting {delay:.1f}s before launching bot {i}")
            time.sleep(delay)

        t = threading.Thread(target=_bot_worker, args=(i,), name=f"bot-{i}")
        t.start()
        threads.append(t)

    # Wait for all bots to finish
    for t in threads:
        t.join()

    # Summary
    success = sum(1 for r in results if r and r.success)
    log.info(f"Done: {success}/{config.num_bots} bots completed successfully")

    return [r for r in results if r is not None]


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Bot Manager — join video calls with multiple browser bots"
    )
    parser.add_argument(
        "--platform",
        choices=["meet", "teams"],
        required=True,
        help="Video call platform (meet or teams)",
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Meeting URL to join",
    )
    parser.add_argument(
        "--bots",
        type=int,
        default=2,
        help="Number of bots to spawn (default: 2)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=int(os.getenv("DEFAULT_CALL_DURATION", "120")),
        help="Seconds each bot stays in the call (default: 120)",
    )
    parser.add_argument(
        "--join-min",
        type=int,
        default=int(os.getenv("BOT_JOIN_INTERVAL_MIN", "5")),
        help="Min seconds between bot joins (default: 5)",
    )
    parser.add_argument(
        "--join-max",
        type=int,
        default=int(os.getenv("BOT_JOIN_INTERVAL_MAX", "15")),
        help="Max seconds between bot joins (default: 15)",
    )
    parser.add_argument(
        "--visible",
        action="store_true",
        help="Run browsers in visible mode (not headless)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    config = BotConfig.from_env_and_args(args)
    results = run_bots(config)

    print("\n--- Bot Results ---")
    for r in results:
        status = "OK" if r.success else f"FAIL: {r.error}"
        print(f"  Bot {r.bot_id}: {status} (duration: {r.duration:.1f}s)")

    return results


if __name__ == "__main__":
    main()
