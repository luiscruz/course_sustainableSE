"""
Energy Measurement Wrapper — measures energy consumption while bots are in a video call.

Uses EnergiBridge (https://github.com/tdurieux/EnergiBridge) for accurate, hardware-level
energy measurement via SYSTEM_POWER readings. EnergiBridge supports macOS (Intel + Apple
Silicon), Linux (RAPL), and Windows.

Fallback: psutil-based CPU power estimation if EnergiBridge binary is not found.
"""

import argparse
import csv
import os
import re
import signal
import subprocess
import sys
import time
import threading
from datetime import datetime
from pathlib import Path

import psutil
import pandas as pd

from bot_manager import BotConfig, run_bots

import logging

log = logging.getLogger("energy_measure")

# ---------------------------------------------------------------------------
# EnergiBridge binary discovery
# ---------------------------------------------------------------------------

def _find_energibridge_binary() -> str | None:
    """Find the EnergiBridge binary. Checks common locations."""
    candidates = [
        # Built from source in project directory
        os.path.join(os.path.dirname(__file__), "..", "EnergiBridge", "target", "release", "energibridge"),
        # System-wide install
        "energibridge",
    ]
    for path in candidates:
        full = os.path.abspath(path) if not path == "energibridge" else path
        try:
            result = subprocess.run(
                [full, "--version"], capture_output=True, timeout=5
            )
            if result.returncode == 0:
                return full
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return None


ENERGIBRIDGE_BIN = _find_energibridge_binary()

if ENERGIBRIDGE_BIN:
    log.info(f"EnergiBridge found: {ENERGIBRIDGE_BIN}")
else:
    log.warning("EnergiBridge not found — will fall back to psutil estimation")


# ---------------------------------------------------------------------------
# EnergiBridge integration
# ---------------------------------------------------------------------------

class EnergiBridgeMonitor:
    """
    Runs EnergiBridge as a background process to measure energy consumption.

    Approach:
      1. Start `energibridge --summary -o output.csv sleep 9999` in background
      2. When stop() is called, send SIGINT to trigger graceful shutdown
      3. Parse the output CSV for SYSTEM_POWER readings
      4. Parse stdout for total energy summary
    """

    def __init__(self, output_csv: str, interval_us: int = 200):
        self.output_csv = output_csv
        self.interval_us = interval_us
        self._process: subprocess.Popen | None = None
        self._total_energy_joules: float = 0.0
        self._duration_s: float = 0.0

    def start(self):
        cmd = [
            ENERGIBRIDGE_BIN,
            "-o", self.output_csv,
            "-i", str(self.interval_us),
            "--summary",
            "sleep", "9999",
        ]
        self._process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        log.info(f"EnergiBridge started (PID {self._process.pid})")

    def stop(self):
        if not self._process:
            return

        # Send SIGINT for graceful shutdown (saves CSV + prints summary)
        self._process.send_signal(signal.SIGINT)
        try:
            stdout, stderr = self._process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            self._process.kill()
            stdout, stderr = self._process.communicate()

        # Parse summary from stdout: "Energy consumption in joules: 49.52 for 3.05 sec"
        output = stdout.decode("utf-8", errors="replace")
        match = re.search(
            r"Energy consumption in joules:\s*([\d.]+)\s*for\s*([\d.]+)\s*sec",
            output,
        )
        if match:
            self._total_energy_joules = float(match.group(1))
            self._duration_s = float(match.group(2))
            log.info(f"EnergiBridge: {self._total_energy_joules:.2f} J over {self._duration_s:.2f} s")
        else:
            log.warning(f"Could not parse EnergiBridge summary: {output}")

        self._process = None

    def get_results(self) -> dict:
        """Return energy measurement results."""
        result = {
            "energy_cpu_joules": round(self._total_energy_joules, 4),
            "energy_duration_s": round(self._duration_s, 2),
            "energy_method": "energibridge",
        }

        # Parse CSV for average power and per-core CPU stats
        if os.path.exists(self.output_csv):
            csv_stats = self._parse_csv()
            result.update(csv_stats)

        return result

    def _parse_csv(self) -> dict:
        """Parse EnergiBridge CSV for detailed stats."""
        try:
            df = pd.read_csv(self.output_csv)
        except Exception as e:
            log.warning(f"Could not parse EnergiBridge CSV: {e}")
            return {}

        stats = {}

        # Average system power
        power_col = "SYSTEM_POWER (Watts)"
        if power_col in df.columns:
            stats["avg_power_watts"] = round(df[power_col].mean(), 2)
            stats["max_power_watts"] = round(df[power_col].max(), 2)

        # Average CPU usage across all cores
        cpu_cols = [c for c in df.columns if c.startswith("CPU_USAGE_")]
        if cpu_cols:
            stats["avg_cpu_percent"] = round(df[cpu_cols].mean(axis=1).mean(), 2)
            stats["max_cpu_percent"] = round(df[cpu_cols].mean(axis=1).max(), 2)

        # Average CPU temperature
        temp_cols = [c for c in df.columns if c.startswith("CPU_TEMP_")]
        if temp_cols:
            stats["avg_cpu_temp_c"] = round(df[temp_cols].mean(axis=1).mean(), 2)

        # Memory
        if "USED_MEMORY" in df.columns:
            stats["avg_memory_mb"] = round(df["USED_MEMORY"].mean() / 1e6, 1)

        return stats


# ---------------------------------------------------------------------------
# System metrics collector (runs alongside energy tool for network I/O)
# ---------------------------------------------------------------------------

class SystemMetricsCollector:
    """Collects CPU, memory, and network metrics over time."""

    def __init__(self, sample_interval: float = 1.0):
        self.sample_interval = sample_interval
        self.samples: list[dict] = []
        self._running = False
        self._thread: threading.Thread | None = None

    def start(self):
        self._running = True
        psutil.cpu_percent(interval=None)  # prime the counter
        self._thread = threading.Thread(target=self._sample_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=5)

    def _sample_loop(self):
        while self._running:
            net = psutil.net_io_counters()
            self.samples.append({
                "timestamp": time.time(),
                "cpu_percent": psutil.cpu_percent(interval=None),
                "memory_mb": psutil.virtual_memory().used / 1e6,
                "memory_percent": psutil.virtual_memory().percent,
                "net_bytes_sent": net.bytes_sent,
                "net_bytes_recv": net.bytes_recv,
            })
            time.sleep(self.sample_interval)

    def save_timeseries(self, filepath: str):
        """Save time-series samples to CSV."""
        if not self.samples:
            return

        base_time = self.samples[0]["timestamp"]
        base_sent = self.samples[0]["net_bytes_sent"]
        base_recv = self.samples[0]["net_bytes_recv"]

        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "elapsed_s", "cpu_percent", "memory_mb", "memory_percent",
                "net_sent_mb_cumulative", "net_recv_mb_cumulative",
            ])
            for s in self.samples:
                writer.writerow([
                    round(s["timestamp"] - base_time, 2),
                    round(s["cpu_percent"], 1),
                    round(s["memory_mb"], 1),
                    round(s["memory_percent"], 1),
                    round((s["net_bytes_sent"] - base_sent) / 1e6, 2),
                    round((s["net_bytes_recv"] - base_recv) / 1e6, 2),
                ])

    def get_summary(self) -> dict:
        if not self.samples:
            return {}
        return {
            "total_net_sent_mb": round(
                (self.samples[-1]["net_bytes_sent"] - self.samples[0]["net_bytes_sent"]) / 1e6, 2
            ),
            "total_net_recv_mb": round(
                (self.samples[-1]["net_bytes_recv"] - self.samples[0]["net_bytes_recv"]) / 1e6, 2
            ),
        }


# ---------------------------------------------------------------------------
# Main measurement function
# ---------------------------------------------------------------------------

def measure_experiment(
    config: BotConfig,
    output_dir: str = "data",
    experiment_label: str = "",
) -> dict:
    """
    Run bots while measuring energy and system metrics.
    Returns a dict with energy readings and system metrics.
    """
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    label = experiment_label or f"{config.platform}_{config.num_bots}bots"
    base_name = f"{label}_{timestamp}"

    # System metrics collector (always runs — needed for network I/O)
    metrics = SystemMetricsCollector(sample_interval=1.0)

    # Choose energy measurement approach
    use_energibridge = ENERGIBRIDGE_BIN is not None

    eb_monitor = None
    psutil_monitor = None

    eb_csv_path = os.path.join(output_dir, f"{base_name}_energibridge.csv")

    if use_energibridge:
        log.info("Energy tool: EnergiBridge (hardware power measurement)")
        eb_monitor = EnergiBridgeMonitor(output_csv=eb_csv_path)
        
    # Start measurement
    metrics.start()
    start_time = time.time()

    if eb_monitor:
        eb_monitor.start()
    if psutil_monitor:
        psutil_monitor.start()

    # --- Run the actual bots ---
    bot_results = run_bots(config)

    # Stop measurement
    end_time = time.time()
    total_duration = end_time - start_time

    if eb_monitor:
        eb_monitor.stop()
    if psutil_monitor:
        psutil_monitor.stop()

    metrics.stop()

    # Save time-series metrics (psutil — includes network)
    timeseries_path = os.path.join(output_dir, f"{base_name}_timeseries.csv")
    metrics.save_timeseries(timeseries_path)
    log.info(f"Saved time-series to {timeseries_path}")

    # Compile results
    result = {
        "platform": config.platform,
        "num_bots": config.num_bots,
        "call_duration_config": config.call_duration,
        "total_experiment_duration_s": round(total_duration, 2),
        "bots_successful": sum(1 for r in bot_results if r.success),
        "bots_failed": sum(1 for r in bot_results if not r.success),
        "timestamp": timestamp,
        "timeseries_file": timeseries_path,
    }

    # Add energy data
    if eb_monitor:
        result.update(eb_monitor.get_results())
        result["energibridge_csv"] = eb_csv_path
    elif psutil_monitor:
        result.update(psutil_monitor.get_results())

    # Add network metrics from SystemMetricsCollector
    result.update(metrics.get_summary())

    # Save experiment summary
    summary_path = os.path.join(output_dir, f"{base_name}_summary.csv")
    _save_summary_csv(result, summary_path)
    log.info(f"Saved summary to {summary_path}")

    return result


def _save_summary_csv(result: dict, filepath: str):
    """Save a single-row summary CSV."""
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=result.keys())
        writer.writeheader()
        writer.writerow(result)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Energy measurement wrapper for video call bot experiments"
    )
    parser.add_argument("--platform", choices=["meet", "teams"], required=True)
    parser.add_argument("--url", required=True, help="Meeting URL")
    parser.add_argument("--bots", type=int, default=2)
    parser.add_argument("--duration", type=int, default=120, help="Call duration in seconds")
    parser.add_argument("--join-min", type=int, default=5)
    parser.add_argument("--join-max", type=int, default=15)
    parser.add_argument("--visible", action="store_true")
    parser.add_argument("--output-dir", default="data", help="Output directory for results")
    parser.add_argument("--label", default="", help="Experiment label")
    args = parser.parse_args()

    config = BotConfig(
        platform=args.platform,
        meeting_url=args.url,
        num_bots=args.bots,
        call_duration=args.duration,
        join_interval_min=args.join_min,
        join_interval_max=args.join_max,
        headless=not args.visible,
    )

    result = measure_experiment(config, output_dir=args.output_dir, experiment_label=args.label)

    print("\n=== Experiment Results ===")
    for key, val in result.items():
        print(f"  {key}: {val}")


if __name__ == "__main__":
    main()
