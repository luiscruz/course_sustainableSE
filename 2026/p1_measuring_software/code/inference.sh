#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON="$SCRIPT_DIR/venv/bin/python" #your venv
ENERGIBRIDGE="" # The path to your energybridge executable
MODEL_DIR="" # The path where your LLM models are stored
INFER_SCRIPT="$SCRIPT_DIR/run.py"

ROUNDS=30
WARMUP=3
SEED=42
COOLDOWN_SECONDS=60

INTERVAL_US=100000
MAX_EXECUTION_SECONDS=0

MODELS=(
  "$MODEL_DIR/Meta-Llama-3.1-8B-Instruct-Q2_K.gguf"
  "$MODEL_DIR/Meta-Llama-3.1-8B-Instruct-Q3_K_M.gguf"
  "$MODEL_DIR/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
  "$MODEL_DIR/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf"
  "$MODEL_DIR/Meta-Llama-3.1-8B-Instruct-Q6_K.gguf"
)

# Checks
[[ -x "$PYTHON" ]] || { echo "ERROR: python not executable: $PYTHON"; exit 1; }
[[ -x "$ENERGIBRIDGE" ]] || { echo "ERROR: energibridge not executable: $ENERGIBRIDGE"; exit 1; }
[[ -f "$INFER_SCRIPT" ]] || { echo "ERROR: run.py missing: $INFER_SCRIPT"; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "ERROR: jq missing (sudo apt install -y jq)"; exit 1; }

mkdir -p results inference warmup logs results/energibridge_runs

FINAL_CSV="results/final_results.csv"
echo "model,run,tokens,seconds,tok_per_sec,gen_energy_j,generated_text" > "$FINAL_CSV"

csv_escape_text() {
  local s="${1:-}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\t'/\\t}"
  s="${s//\"/\"\"}"
  printf '"%s"' "$s"
}

# compute energy
package_energy_delta_from_csv() {
  local csv="$1"
  awk -F',' '
    NR==1 {
      for (i=1;i<=NF;i++) gsub(/\r$/, "", $i)
      for (i=1;i<=NF;i++) if ($i=="PACKAGE_ENERGY (J)") pkg=i
      next
    }
    pkg>0 && NF>=pkg {
      if (!seen) { first=$pkg; seen=1 }
      last=$pkg
    }
    END {
      if (!seen) { print "0"; exit }
      printf "%.10f\n", (last - first)
    }
  ' "$csv"
}

run=1

# warmup
for ((w=1; w<=WARMUP; w++)); do
  for model_path in "${MODELS[@]}"; do
    [[ -f "$model_path" ]] || continue
    model="$(basename "$model_path" .gguf)"
    infer_json="warmup/${model}_w${w}.json"
    py_log="logs/${model}_w${w}_python.log"

    echo "Warmup $w/$WARMUP: $model"
    "$PYTHON" "$INFER_SCRIPT" --model "$model_path" --seed "$SEED" --output "$infer_json" >"$py_log" 2>&1
    echo "Cooling CPU for ${COOLDOWN_SECONDS}s..."
    sleep "$COOLDOWN_SECONDS"
  done
done

# runs
for ((r=1; r<=ROUNDS; r++)); do
  for model_path in "${MODELS[@]}"; do
    [[ -f "$model_path" ]] || { echo "WARNING: missing model: $model_path"; continue; }

    model="$(basename "$model_path" .gguf)"
    infer_json="inference/${model}_r${run}.json"
    py_log="logs/${model}_r${run}_python.log"
    eb_csv="results/energibridge_runs/${model}_r${run}.csv"
    eb_log="logs/${model}_r${run}_energibridge.log"

    echo "Run $run: $model"

    rm -f "$infer_json" "$py_log" "$eb_csv" "$eb_log"

    "$ENERGIBRIDGE" \
      --output "$eb_csv" \
      --interval "$INTERVAL_US" \
      --max-execution "$MAX_EXECUTION_SECONDS" \
      -- \
      /bin/bash -lc 'exec sleep infinity' \
      >"$eb_log" 2>&1 &
    EB_PID=$!

    for _ in {1..80}; do
      if [[ -s "$eb_csv" ]] && [[ "$(wc -l < "$eb_csv" | tr -d ' ')" -ge 2 ]]; then
        break
      fi
      sleep 0.1
    done

    if ! kill -0 "$EB_PID" 2>/dev/null; then
      echo "ERROR: energibridge died at start for $model run $run"
      tail -n 200 "$eb_log" || true
      exit 1
    fi

    "$PYTHON" "$INFER_SCRIPT" \
      --model "$model_path" \
      --seed "$SEED" \
      --output "$infer_json" \
      >"$py_log" 2>&1

    kill "$EB_PID" 2>/dev/null || true
    wait "$EB_PID" 2>/dev/null || true

    if [[ ! -s "$infer_json" ]]; then
      echo "ERROR: inference JSON missing for $model run $run"
      tail -n 200 "$py_log" || true
      exit 1
    fi
    if [[ ! -s "$eb_csv" ]] || [[ "$(wc -l < "$eb_csv" | tr -d ' ')" -lt 3 ]]; then
      echo "ERROR: energibridge CSV too small (no samples) for $model run $run"
      echo "CSV lines: $(wc -l < "$eb_csv" | tr -d ' ')"
      tail -n 200 "$eb_log" || true
      exit 1
    fi

    gen_energy="$(package_energy_delta_from_csv "$eb_csv")"

    tokens="$(jq -r '.gen_tokens' "$infer_json")"
    seconds="$(jq -r '.seconds' "$infer_json")"
    tokps="$(jq -r '.tok_per_sec' "$infer_json")"

    gen_text_raw="$(jq -r '.generated_text // ""' "$infer_json")"
    gen_text_csv="$(csv_escape_text "$gen_text_raw")"

    echo "$model,$run,$tokens,$seconds,$tokps,$gen_energy,$gen_text_csv" >> "$FINAL_CSV"

    run=$((run + 1))

    echo "Cooling CPU for ${COOLDOWN_SECONDS}s..."
    sleep "$COOLDOWN_SECONDS"
  done
done

echo "Done. Results: $FINAL_CSV"
echo "EnergiBridge per-run CSVs: results/energibridge_runs/"
