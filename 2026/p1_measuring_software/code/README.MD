# LLM Inference Energy Benchmark — Setup & Usage

This repository contains scripts to run LLM inference, measure energy consumption with **EnergiBridge**, and analyze the results.

The repository includes:

* `llma.ipynb` — Notebook with GPU runable code, outputs `GPU_runs.csv`
* `download.py` — A file that downloads the quantizations.
* `run.py` — runs a single CPU inference and outputs JSON metrics
* `inference.sh` — orchestrates repeated runs and energy measurement, outputs `CPU_runs.csv`
* `plot_stats.py` — analyzes results and generates plots
* `CPU_runs.csv` / `GPU_runs.csv` — example result files
* `requirements.txt` — A file that includes the requirements to run the energy measurements locally.

# 1. Install System Dependencies

Linux is recommended.

Install `jq` (required by the runner script):

```bash
sudo apt update
sudo apt install -y jq
```

Verify installation:

```bash
jq --version
```

---

# 2. Create Python Environment (Local Machine)

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

Install dependencies:

```bash
pip install -r requirements.txt
```

These dependencies are only needed for:

* parsing results
* statistics
* plotting

Inference dependencies are handled separately (for example in Colab).

---

# 3. Install EnergiBridge

Install Rust:

```bash
curl https://sh.rustup.rs -sSf | sh
```

Clone and build:

```bash
git clone https://github.com/tdurieux/EnergiBridge
cd EnergiBridge
cargo build --release
```

Binary will be located at:

```
target/release/energibridge
```

---

# 4. Download GGUF Models

The script expects quantized models such as:

```
Meta-Llama-3.1-8B-Instruct-Q2_K.gguf
Meta-Llama-3.1-8B-Instruct-Q3_K_M.gguf
Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf
Meta-Llama-3.1-8B-Instruct-Q6_K.gguf
```

Create a directory for models:

```bash
mkdir -p ~/models/gguf
```

Place all `.gguf` files inside that folder.

Example:

```
~/models/gguf/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
```

---

# 5. Configure Paths

Open:

```
inference.sh
```

Set the following variables near the top of the file.

Example configuration:

```bash
PYTHON="$SCRIPT_DIR/venv/bin/python"
ENERGIBRIDGE="$HOME/tools/energibridge"
MODEL_DIR="$HOME/models/gguf"
```

Explanation:

**PYTHON**
Path to the Python interpreter inside your virtual environment.

**ENERGIBRIDGE**
Path to the EnergiBridge executable.

**MODEL_DIR**
Folder containing GGUF models.

---

# 6. Run the Experiment

Make the script executable:

```bash
chmod +x inference.sh
```

Start the experiment:

```bash
./inference.sh
```

The script will automatically:

1. Run warmup iterations
2. Execute multiple inference runs
3. Measure energy consumption
4. Collect timing statistics
5. Save results

---

# 7. Output Structure

After running, the repository will contain:

```
results/
    CPU_runs.csv
    energibridge_runs/
        model_r1.csv
        model_r2.csv
        ...
logs/
warmup/
inference/
```

`CPU_runs.csv` contains the aggregated metrics for all runs.

---

# 8. Plot and Analyze Results

Run:

```bash
python plot_stats.py CPU_runs.csv
python plot_stats.py GPU_runs.csv
```

The script generates:

```
summary_before_mean_ci95_std.csv
summary_after_mean_ci95_std.csv

violin_box_*_before_outliers.png
violin_box_*_after_outliers.png

final_results_before_outliers.csv
final_results_after_outliers.csv
```

It also prints statistical tests in the terminal.

---

# 9. Running Inference in Google Colab

If you prefer running the model in Colab:

1. Open `llma.ipynb`
2. Run the cells
3. Export the generated CSV
4. Copy the file back to your machine

Then analyze locally:

```bash
python plot_stats.py GPU_runs.csv
```

---

# 10. Adjusting Experiment Parameters

Inside `inference.sh` you can change:

```
ROUNDS=30
WARMUP=3
COOLDOWN_SECONDS=60

Meaning:

**ROUNDS**
Measured runs per model.

**WARMUP**
Warmup runs before measurements.

**COOLDOWN_SECONDS**
Pause between runs to stabilize thermals.

