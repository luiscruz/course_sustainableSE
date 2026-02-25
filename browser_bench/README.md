# Browser Energy Benchmark

This tool automates energy consumption measurements for web browsers while running standard benchmarks (Speedometer 3.1, JetStream 2, MotionMark 1.3.1) and a control idle test. It uses Selenium for automation and `pyEnergiBridge` for energy readings.

## Setup

1. **Prerequisites**: Ensure you have Python and `uv` installed.
2. **Install Dependencies**:
   ```sh
   uv init
   uv sync
   ```
3. **Install Browser Drivers**:

   ***macOS***
   ```sh
   brew install --cask chromedriver
   # For Firefox: brew install --cask geckodriver
   ``` 
   ***Windows*** \
   Chrome:
   1. Download ChromeDriver: https://developer.chrome.com/docs/chromedriver/downloads
   2. Extract the .exe
   3. Add its folder to your PATH OR place it in your project directory
   
   Firefox:
   1. Download GeckoDriver: https://github.com/mozilla/geckodriver/releases
   2. Extract geckodriver.exe
   3. Add it to your PATH

   Verify:
   ```sh
   chromedriver --version
   geckodriver --version
   ``` 


4. **Configure EnergiBridge**:
   Update `pyenergibridge_config.json` with the absolute path to your `energibridge` binary.
   ```json
   {
       "binary_path": "/path/to/energibridge"
   }
   ```
   For more setup instructions, see [pyEnergiBridge on GitHub](https://github.com/luiscruz/pyEnergiBridge).

## Usage

Run the benchmark suite:

```sh
uv run main.py
```

## Configuration

Edit the `--- CONFIGURATION ---` section in `main.py` to adjust:

- `BROWSER`: Target browser (`"chrome"` or `"firefox"`).
- `ACTUAL_ROUNDS`: Number of measurement rounds per test (default: 30).
- `WARMUP_ROUNDS`: Number of warmup rounds before measurements (default: 5).
- `DURATION`: Duration in seconds for each test iteration (default: 15).
- `OUTPUT_CSV`: Filename for results.

> **⚠️ Warning:** A full run with default settings takes approximately **30 minutes per browser** to complete. Ensure your device is plugged to power and keep the machine idle during tests for accurate results.

## Output Data

Results are saved to `[BROWSER]_experiment_results.csv` containing:

- **Timestamp**: ISO 8601 time of test.
- **Round_Type**: `warmup` or `actual`.
- **Test_Name**: Benchmark name (e.g., `speedometer`, `control`).
- **Energy_Joules**: Total energy consumed during the test.
- **Duration_Sec**: Exact duration of the test.
- **Power_Avg_Watts**: Average power usage (Energy / Duration).
