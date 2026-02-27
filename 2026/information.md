# Spotify Streaming Quality — Energy Experiment

Measures whole-system power draw (`SYSTEM_POWER`, Watts via Apple SMC) across
six Spotify streaming conditions on macOS / Apple Silicon using EnergiBridge.

## Conditions

| Label      | Audio quality | Canvas (video) |
|------------|---------------|----------------|
| AUTO       | Automatic     | ON             |
| AUTO_NC    | Automatic     | OFF            |
| HIGH       | Very High     | ON             |
| HIGH_NC    | Very High     | OFF            |
| MEDIUM     | Normal        | OFF            |
| VERY_HIGH  | Very High     | OFF            |

## Prerequisites

- macOS with Apple Silicon
- Spotify desktop app — open, a song ≥ 45 s queued, paused at 0:00
- EnergiBridge binary built at `../EnergiBridge/target/release/energibridge`
  (`cargo build -r` inside `../EnergiBridge/`)
- Python 3.10+
- `sudo` access (required by EnergiBridge to read SMC power counters)

## Setup

```bash
cd experiment
pip install -r requirements.txt
```

## Files

| File | Description |
|------|-------------|
| `run_experiment.py` | **Main orchestrator.** Runs 180 measurements (30 × 6 conditions) in a seeded-random order with crash recovery via `progress.json`. Per-run pipeline: (1) configure Spotify quality + Canvas, (2) seek to 0:00 and play 10 s to warm the audio decoder and fill the buffer, (3) pause and resume — then wait 18 s for the decoder startup power spike to fully clear, (4) start EnergiBridge and record 13 s of steady-state power, (5) pause Spotify. Total runtime ~2.5 h. |
| `play_session.py` | Measurement target invoked by EnergiBridge. Sleeps for 13 s (Spotify plays uninterrupted in the background) then issues a pause command. Not run directly. |
| `spotify_controller.py` | PyAutoGUI automation layer. Opens Spotify's settings panel and sets streaming quality and Canvas (background video) toggle via OpenCV screenshot template matching. Used by every run to switch conditions reliably. |
| `warmup.py` | Runs a 60 s Fibonacci computation before the experiment starts to bring the CPU to a stable thermal and power baseline, reducing run-to-run variance in early measurements. |
| `stress_test.py` | Pre-experiment health check across 5 phases: (1) screenshot template confidence scan, (2) all 36 condition-to-condition transitions, (3) crash-scenario replay, (4) idempotency check, (5) full pipeline per condition with a short EnergiBridge measurement. Run this before the main experiment to catch any setup issues. |
| `run_single.py` | Lightweight script for running and validating a single condition manually. Useful for spot-checking after setup changes. |
| `analysis.py` | Loads all result CSVs, trims the first 5 s transient, and computes per-run metrics (total energy J, average power W, peak power W, CPU usage, temperature). Runs Shapiro-Wilk normality tests and applies Welch t-test or Mann-Whitney U for pairwise condition comparisons. Outputs violin plots to `analysis_plots/`. |
| `screenshots/` | PNG templates used by `spotify_controller.py` for screen matching (quality dropdown, option labels, Canvas toggle label). |
| `results/` | One CSV per measurement run, written by `run_experiment.py` via EnergiBridge. |

## How to Run

### 1. Validate setup (recommended)

```bash
cd experiment
sudo python3 stress_test.py
```

### 2. Run the experiment

Open Spotify, search for a song ≥ 45 s, pause at 0:00.

```bash
cd experiment
sudo python3 run_experiment.py
# Automatically resumes from progress.json if interrupted
```

### 3. Analyse results

```bash
python3 analysis.py
# Violin plots → analysis_plots/   Statistics → stdout
```

## Why only 13 s of recording?

The song must be ≥ 45 s long, but only 13 s are actually recorded. The rest
of the song duration is consumed by the per-run pipeline:

```
Seek to 0:00
└─ Play 10 s      → warms audio decoder, fills network buffer
└─ Pause + 1 s    → power decays
└─ Resume + 18 s  → absorbs the ~15–16 s decoder startup spike
                    (spike caused by re-initialising the audio pipeline after resume)
└─ EnergiBridge records 13 s of steady-state power   ← only this goes in the CSV
└─ Pause
```

Song position at start of recording: 0 + 10 + 18 = **28 s into the song**.
Song position at end of recording: 28 + 13 = **41 s** — well within the 45 s minimum.

The 13 s window captures only steady-state streaming power, free of startup
transients. With 30 runs per condition the statistical power is sufficient.

## Results Format

Each CSV in `results/` is a 13 s EnergiBridge measurement window (~67 rows
at ~200 ms sampling). Key column: `SYSTEM_POWER (Watts)`.


