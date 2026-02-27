# Energy Consumption: Google Meet vs Microsoft Teams

Comparing client-side energy consumption of video calls on Google Meet and Microsoft Teams using automated browser bots and hardware-level energy measurement.

**Course:** Sustainable Software Engineering (SSE) — TU Delft 2026

---

## Prerequisites

You need these installed on your machine before starting:

| Tool | Version | Check command | Install |
|------|---------|---------------|---------|
| **Python** | 3.10+ | `python3 --version` | [python.org](https://www.python.org/downloads/) |
| **Google Chrome** | Latest | Check in Chrome menu → About | [google.com/chrome](https://www.google.com/chrome/) |
| **Rust** | Latest | `cargo --version` | [rustup.rs](https://rustup.rs/) |
| **pip** | Latest | `pip3 --version` | Comes with Python |

> **Note:** ChromeDriver is installed automatically by `webdriver-manager` — you don't need to install it manually.

---

## Setup (step by step)

### 1. Clone and enter the project

```bash
git clone <repo-url>
cd SSE-26
```

### 2. Create a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
# venv\Scripts\activate       # Windows (PowerShell)
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

This installs: `selenium`, `webdriver-manager`, `psutil`, `pandas`, `matplotlib`, `seaborn`, `numpy`, `python-dotenv`.

### 4. Build EnergiBridge (energy measurement tool)

[EnergiBridge](https://github.com/tdurieux/EnergiBridge) is a cross-platform tool that measures **real system power** (Watts) during experiments.

```bash
# Install Rust if you don't have it yet
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# Clone and build EnergiBridge
cd EnergiBridge
cargo build -r
cd ..
```

Verify it works:

```bash
EnergiBridge/target/release/energibridge --summary -m 2 sleep 2
# Should print: "Energy consumption in joules: XX.XX for 2.XX sec of execution."
```

### 5. Create meeting links and configure `.env`

**Create your meetings:**
- **Google Meet:** Go to [meet.google.com](https://meet.google.com), click "New meeting" → "Start an instant meeting". Copy the URL (looks like `https://meet.google.com/abc-defg-hij`).
- **Microsoft Teams:** Go to [teams.live.com](https://teams.live.com), click "Meet now" → "Get a link to share". Copy the URL (looks like `https://teams.live.com/meet/123456789?p=xxxxx`).

**Configure the `.env` file:**

```bash
cp .env.example .env
```

Open `.env` in any text editor and paste your meeting URLs:

```env
# Paste your meeting URLs here:
MEET_URL=https://meet.google.com/abc-defg-hij
TEAMS_URL=https://teams.live.com/meet/123456789?p=xxxxx

# Leave the rest as default:
TEAMS_GUEST_NAME=Bot
CHROME_BINARY=
CHROMEDRIVER_PATH=
ENERGY_TOOL=energibridge
DEFAULT_CALL_DURATION=120
BOT_JOIN_INTERVAL_MIN=5
BOT_JOIN_INTERVAL_MAX=15
```

### 6. Important: Stay in the meetings yourself!

The bots join as **guests**. You must:
1. **Be in the meeting yourself** (as the host) during the experiment
2. **Google Meet:** Turn off "Ask to join" in meeting settings so bots join instantly
3. **Microsoft Teams:** Admit bots from the lobby when they appear, or change lobby settings to let everyone in

---

## Running Experiments

### Quick test (verify everything works)

First run a short test with 2 bots to make sure the setup is correct:

```bash
cd src

# Test Google Meet (2 bots, 30 seconds)
python bot_manager.py --platform meet --url "YOUR_MEET_URL" --bots 2 --duration 30 --visible

# Test Microsoft Teams (2 bots, 30 seconds)
python bot_manager.py --platform teams --url "YOUR_TEAMS_URL" --bots 2 --duration 30 --visible
```

You should see Chrome windows open, bots join the meeting, wait 30 seconds, and leave. If something fails, check the error messages.

### Single energy measurement test

```bash
# Meet with energy measurement
python energy_measure.py --platform meet --url "YOUR_MEET_URL" --bots 2 --duration 60 --visible --output-dir ../data

# Teams with energy measurement
python energy_measure.py --platform teams --url "YOUR_TEAMS_URL" --bots 2 --duration 60 --visible --output-dir ../data
```

This creates three files per run in `data/`:
- `*_summary.csv` — one row with totals (energy in Joules, avg power in Watts, CPU, network)
- `*_timeseries.csv` — per-second CPU, memory, and network measurements
- `*_energibridge.csv` — high-frequency power readings from EnergiBridge (~5 samples/sec)

### Full experiment (30 runs per platform)

```bash
python run_experiment.py \
  --meet-url "YOUR_MEET_URL" \
  --teams-url "YOUR_TEAMS_URL" \
  --bot-counts 2 5 \
  --repeats 15 \
  --duration 120 \
  --visible
```

This runs: 2 platforms × 2 bot counts × 15 repeats = **60 experiments** with 30-second cooldown between each. Takes ~3-4 hours.

### Analyze results and generate charts

```bash
python analyze.py --data-dir ../data --output-dir ../figures
```

This generates in `figures/`:
- `energy_bar_comparison.png` — Energy consumption: Meet vs Teams
- `energy_scaling.png` — How energy scales with participant count
- `power_over_time_Xbots.png` — System power (Watts) over time per bot count
- `cpu_over_time_Xbots.png` — CPU usage over time per bot count
- `network_comparison.png` — Network traffic comparison
- `summary_statistics.csv` — Table with all statistics

---

## Project Structure

```
SSE-26/
├── .env.example              # Template — copy to .env and fill in URLs
├── .env                      # Your meeting URLs (not committed to git)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── EnergiBridge/             # Energy measurement tool (built from source)
│   └── target/release/energibridge
├── src/
│   ├── bot_manager.py        # Selenium bots that join Meet/Teams calls
│   ├── energy_measure.py     # Energy measurement wrapper (EnergiBridge)
│   ├── run_experiment.py     # Runs full experiment matrix automatically
│   └── analyze.py            # Generates charts and statistics from data
├── data/                     # Raw experiment results (CSV per run)
└── figures/                  # Generated charts (PNG)
```

---

## How It Works

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────┐
│ run_experiment   │────▶│ energy_measure    │────▶│ bot_manager │
│                  │     │                  │     │             │
│ For each:        │     │ Starts           │     │ Opens Chrome│
│ - platform       │     │   EnergiBridge   │     │ Joins call  │
│ - bot count      │     │ Starts network   │     │ Waits       │
│ - repeat         │     │   monitoring     │     │ Leaves call │
│                  │     │ Runs bots        │     │ Closes      │
│                  │     │ Stops            │     │             │
│                  │     │   EnergiBridge   │     │             │
│                  │     │ Saves CSVs       │     │             │
└─────────────────┘     └──────────────────┘     └─────────────┘
         │
         ▼
┌─────────────────┐
│ analyze.py      │
│                 │
│ Reads all CSVs  │
│ Generates charts│
│ Prints stats    │
└─────────────────┘
```

1. **bot_manager.py** opens real Chrome browsers (not headless — Meet blocks headless) with fake camera/mic streams. Each bot navigates to the meeting URL, enters a guest name, clicks "Join", waits for the configured duration, then clicks "Leave".

2. **energy_measure.py** wraps the bot manager. Before bots start, it launches EnergiBridge as a background process to measure system power in real-time. It also records network traffic every second via psutil. After bots finish, EnergiBridge is stopped and all data is saved to CSV.

3. **run_experiment.py** automates the full matrix: for each platform × bot count × repeat, it calls `energy_measure.py` with a 30-second cooldown between runs.

4. **analyze.py** reads all the CSV files and generates comparison charts with error bars.

---

## Energy Measurement

Energy is measured using [EnergiBridge](https://github.com/tdurieux/EnergiBridge), which reads hardware power sensors:

| Platform | Sensor | What it measures |
|----------|--------|------------------|
| **macOS (Apple Silicon)** | `powermetrics` | Total system power via SMC (System Management Controller) |
| **macOS (Intel)** | RAPL | CPU package power via Intel Running Average Power Limit |
| **Linux (Intel/AMD)** | RAPL | CPU package + DRAM power via MSR registers |
| **Windows** | LibreHardwareMonitor | CPU package power |

EnergiBridge outputs the `SYSTEM_POWER (Watts)` column at ~5 samples/second. Total energy (Joules) = integral of power over time.

**Fallback:** If EnergiBridge is not installed, the script falls back to a psutil-based estimate: `energy ≈ (CPU% / 100) × TDP × duration`. This is less accurate but works on any platform.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `chromedriver` not found | It's installed automatically. If it fails, check your Chrome version matches |
| `cargo` not found | Install Rust: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| EnergiBridge build fails | Make sure Rust is installed: `cargo --version`. Then `cd EnergiBridge && cargo build -r` |
| Bots don't join Google Meet | Make sure you're NOT in headless mode. Meet blocks headless Chrome |
| Bots stuck in Teams lobby | You need to admit them manually, or change lobby settings |
| `page load timeout` | Normal — Meet uses WebSockets. The code handles this with `page_load_strategy = "eager"` |
| `StaleElementReferenceException` | Normal — the code retries automatically. Meet/Teams update DOM frequently |

---

## Notes

- Bots use `--use-fake-device-for-media-stream` — no real camera/microphone needed
- Chrome runs in **visible mode** (not headless) because Google Meet blocks headless browsers
- On Linux servers without a display, use Xvfb: `Xvfb :99 -screen 0 1280x720x24 & export DISPLAY=:99`
- Each experiment creates timestamped CSV files — old data is never overwritten
- The `.env` file is gitignored — meeting URLs stay private
