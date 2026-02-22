"""
Analysis & Visualization — reads experiment CSVs and generates comparison charts.

Generates:
1. Energy consumption bar chart: Meet vs Teams
2. Energy per participant scaling (line chart)
3. CPU usage over time (line chart)
4. Network traffic comparison (bar chart)
5. Power over time (Watts) from EnergiBridge data
"""

import argparse
import csv
import glob
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.use("Agg")  # non-interactive backend

# Chart style
sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
COLORS = {"meet": "#00897B", "teams": "#5C6BC0"}
PLATFORM_LABELS = {"meet": "Google Meet", "teams": "Microsoft Teams"}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_combined_results(data_dir: str) -> pd.DataFrame:
    """Load the most recent combined experiment JSON."""
    json_files = sorted(glob.glob(os.path.join(data_dir, "experiment_combined_*.json")))
    if not json_files:
        print(f"No experiment_combined_*.json found in {data_dir}")
        print("Looking for individual summary CSVs instead...")
        return _load_individual_summaries(data_dir)

    latest = json_files[-1]
    print(f"Loading: {latest}")
    with open(latest) as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Filter out failed runs
    if "error" in df.columns:
        failed = df["error"].notna().sum()
        if failed > 0:
            print(f"Excluding {failed} failed runs")
            df = df[df["error"].isna()].copy()

    return df


def _load_individual_summaries(data_dir: str) -> pd.DataFrame:
    """Fallback: load all individual *_summary.csv files."""
    csv_files = sorted(glob.glob(os.path.join(data_dir, "*_summary.csv")))
    if not csv_files:
        print(f"No summary CSVs found in {data_dir}")
        sys.exit(1)

    frames = []
    for f in csv_files:
        try:
            df = pd.read_csv(f)
            frames.append(df)
        except Exception as e:
            print(f"Skipping {f}: {e}")

    return pd.concat(frames, ignore_index=True)


def load_timeseries(data_dir: str, platform: str, num_bots: int) -> list[pd.DataFrame]:
    """Load all time-series CSVs matching a platform/bot count."""
    pattern = os.path.join(data_dir, f"{platform}_{num_bots}bots_*_timeseries.csv")
    files = sorted(glob.glob(pattern))
    frames = []
    for f in files:
        try:
            df = pd.read_csv(f)
            # Normalize column names (handle typos like cpuy_percent → cpu_percent)
            rename_map = {}
            for col in df.columns:
                if "cpu" in col.lower() and "percent" in col.lower() and col != "cpu_percent":
                    rename_map[col] = "cpu_percent"
                if "memor" in col.lower() and "percent" in col.lower() and col != "memory_percent":
                    rename_map[col] = "memory_percent"
            if rename_map:
                df = df.rename(columns=rename_map)
            frames.append(df)
        except Exception:
            pass
    return frames


def load_energibridge_timeseries(data_dir: str, platform: str, num_bots: int) -> list[pd.DataFrame]:
    """Load all EnergiBridge CSVs matching a platform/bot count."""
    pattern = os.path.join(data_dir, f"{platform}_{num_bots}bots_*_energibridge.csv")
    files = sorted(glob.glob(pattern))
    frames = []
    for f in files:
        try:
            df = pd.read_csv(f)
            # Convert Delta (ms between samples) to elapsed seconds
            if "Delta" in df.columns:
                df["elapsed_s"] = df["Delta"].cumsum() / 1000.0
            frames.append(df)
        except Exception:
            pass
    return frames


# ---------------------------------------------------------------------------
# Chart 1: Energy consumption bar chart (Meet vs Teams)
# ---------------------------------------------------------------------------

def plot_energy_bar(df: pd.DataFrame, output_dir: str):
    """Bar chart comparing total energy consumption: Meet vs Teams."""
    fig, ax = plt.subplots(figsize=(10, 6))

    grouped = df.groupby(["platform", "num_bots"])["energy_cpu_joules"].agg(["mean", "std"]).reset_index()

    bot_counts = sorted(df["num_bots"].unique())
    x = np.arange(len(bot_counts))
    width = 0.35

    for i, platform in enumerate(["meet", "teams"]):
        pdata = grouped[grouped["platform"] == platform]
        if pdata.empty:
            continue
        pdata = pdata.set_index("num_bots").reindex(bot_counts)

        bars = ax.bar(
            x + (i - 0.5) * width,
            pdata["mean"],
            width,
            yerr=pdata["std"],
            label=PLATFORM_LABELS.get(platform, platform),
            color=COLORS.get(platform, None),
            capsize=4,
            alpha=0.85,
        )

    ax.set_xlabel("Number of Participants (Bots)")
    ax.set_ylabel("Energy Consumption (Joules)")
    ax.set_title("Energy Consumption: Google Meet vs Microsoft Teams")
    ax.set_xticks(x)
    ax.set_xticklabels(bot_counts)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, "energy_bar_comparison.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Chart 2: Energy per participant scaling (line chart)
# ---------------------------------------------------------------------------

def plot_energy_scaling(df: pd.DataFrame, output_dir: str):
    """Line chart showing how energy scales with participant count."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Total energy
    for platform in ["meet", "teams"]:
        pdata = df[df["platform"] == platform]
        if pdata.empty:
            continue
        grouped = pdata.groupby("num_bots")["energy_cpu_joules"].agg(["mean", "std"]).reset_index()
        ax1.errorbar(
            grouped["num_bots"], grouped["mean"], yerr=grouped["std"],
            marker="o", label=PLATFORM_LABELS.get(platform, platform),
            color=COLORS.get(platform), capsize=4, linewidth=2,
        )

    ax1.set_xlabel("Number of Participants")
    ax1.set_ylabel("Total Energy (Joules)")
    ax1.set_title("Total Energy vs. Participant Count")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # Right: Energy per participant
    for platform in ["meet", "teams"]:
        pdata = df[df["platform"] == platform].copy()
        if pdata.empty:
            continue
        pdata["energy_per_bot"] = pdata["energy_cpu_joules"] / pdata["num_bots"]
        grouped = pdata.groupby("num_bots")["energy_per_bot"].agg(["mean", "std"]).reset_index()
        ax2.errorbar(
            grouped["num_bots"], grouped["mean"], yerr=grouped["std"],
            marker="s", label=PLATFORM_LABELS.get(platform, platform),
            color=COLORS.get(platform), capsize=4, linewidth=2,
        )

    ax2.set_xlabel("Number of Participants")
    ax2.set_ylabel("Energy per Participant (Joules)")
    ax2.set_title("Energy per Participant vs. Participant Count")
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, "energy_scaling.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Chart 3: CPU usage over time (line chart)
# ---------------------------------------------------------------------------

def plot_cpu_over_time(data_dir: str, output_dir: str, df: pd.DataFrame):
    """Line chart of CPU usage over time for each bot count."""
    bot_counts = sorted(df["num_bots"].unique())

    for num_bots in bot_counts:
        fig, ax = plt.subplots(figsize=(12, 6))
        has_data = False

        for platform in ["meet", "teams"]:
            ts_list = load_timeseries(data_dir, platform, num_bots)
            if not ts_list:
                continue

            has_data = True
            # Average across repeats
            max_len = max(len(ts) for ts in ts_list)
            all_cpu = np.full((len(ts_list), max_len), np.nan)
            for i, ts in enumerate(ts_list):
                if "cpu_percent" in ts.columns:
                    all_cpu[i, :len(ts)] = ts["cpu_percent"].values

            mean_cpu = np.nanmean(all_cpu, axis=0)
            elapsed = np.arange(max_len)

            ax.plot(
                elapsed, mean_cpu,
                label=f"{PLATFORM_LABELS.get(platform, platform)}",
                color=COLORS.get(platform),
                linewidth=1.5, alpha=0.85,
            )

            # Confidence band (only if multiple repeats)
            if len(ts_list) > 1:
                std_cpu = np.nanstd(all_cpu, axis=0)
                ax.fill_between(
                    elapsed, mean_cpu - std_cpu, mean_cpu + std_cpu,
                    color=COLORS.get(platform), alpha=0.15,
                )

        if not has_data:
            plt.close(fig)
            continue

        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("CPU Usage (%)")
        ax.set_title(f"CPU Usage Over Time ({num_bots} Participants)")
        ax.legend()
        ax.grid(alpha=0.3)

        plt.tight_layout()
        path = os.path.join(output_dir, f"cpu_over_time_{num_bots}bots.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Chart 4: Network traffic comparison
# ---------------------------------------------------------------------------

def plot_network_comparison(df: pd.DataFrame, output_dir: str):
    """Bar chart comparing network traffic: Meet vs Teams."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    bot_counts = sorted(df["num_bots"].unique())
    x = np.arange(len(bot_counts))
    width = 0.35

    # Received
    for i, platform in enumerate(["meet", "teams"]):
        pdata = df[df["platform"] == platform]
        if pdata.empty or "total_net_recv_mb" not in pdata.columns:
            continue
        grouped = pdata.groupby("num_bots")["total_net_recv_mb"].agg(["mean", "std"]).reset_index()
        grouped = grouped.set_index("num_bots").reindex(bot_counts)
        ax1.bar(
            x + (i - 0.5) * width, grouped["mean"], width,
            yerr=grouped["std"],
            label=PLATFORM_LABELS.get(platform, platform),
            color=COLORS.get(platform), capsize=4, alpha=0.85,
        )

    ax1.set_xlabel("Number of Participants")
    ax1.set_ylabel("Data Received (MB)")
    ax1.set_title("Network Download: Meet vs Teams")
    ax1.set_xticks(x)
    ax1.set_xticklabels(bot_counts)
    ax1.legend()
    ax1.grid(axis="y", alpha=0.3)

    # Sent
    for i, platform in enumerate(["meet", "teams"]):
        pdata = df[df["platform"] == platform]
        if pdata.empty or "total_net_sent_mb" not in pdata.columns:
            continue
        grouped = pdata.groupby("num_bots")["total_net_sent_mb"].agg(["mean", "std"]).reset_index()
        grouped = grouped.set_index("num_bots").reindex(bot_counts)
        ax2.bar(
            x + (i - 0.5) * width, grouped["mean"], width,
            yerr=grouped["std"],
            label=PLATFORM_LABELS.get(platform, platform),
            color=COLORS.get(platform), capsize=4, alpha=0.85,
        )

    ax2.set_xlabel("Number of Participants")
    ax2.set_ylabel("Data Sent (MB)")
    ax2.set_title("Network Upload: Meet vs Teams")
    ax2.set_xticks(x)
    ax2.set_xticklabels(bot_counts)
    ax2.legend()
    ax2.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, "network_comparison.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Chart 5: Power over time (Watts) from EnergiBridge
# ---------------------------------------------------------------------------

def plot_power_over_time(data_dir: str, output_dir: str, df: pd.DataFrame):
    """Line chart of system power (Watts) over time from EnergiBridge data."""
    power_col = "SYSTEM_POWER (Watts)"
    bot_counts = sorted(df["num_bots"].unique())

    for num_bots in bot_counts:
        fig, ax = plt.subplots(figsize=(12, 6))
        has_data = False

        for platform in ["meet", "teams"]:
            eb_list = load_energibridge_timeseries(data_dir, platform, num_bots)
            if not eb_list:
                continue

            # Filter to those that have the power column
            eb_list = [eb for eb in eb_list if power_col in eb.columns]
            if not eb_list:
                continue

            has_data = True
            max_len = max(len(eb) for eb in eb_list)
            all_power = np.full((len(eb_list), max_len), np.nan)
            for i, eb in enumerate(eb_list):
                all_power[i, :len(eb)] = eb[power_col].values

            mean_power = np.nanmean(all_power, axis=0)
            # Use elapsed_s from first file for x-axis, or generate from index
            if "elapsed_s" in eb_list[0].columns:
                elapsed = eb_list[0]["elapsed_s"].values[:max_len]
            else:
                elapsed = np.arange(max_len) * 0.2  # default 200µs interval

            ax.plot(
                elapsed, mean_power,
                label=PLATFORM_LABELS.get(platform, platform),
                color=COLORS.get(platform),
                linewidth=1.5, alpha=0.85,
            )

            if len(eb_list) > 1:
                std_power = np.nanstd(all_power, axis=0)
                ax.fill_between(
                    elapsed, mean_power - std_power, mean_power + std_power,
                    color=COLORS.get(platform), alpha=0.15,
                )

        if not has_data:
            plt.close(fig)
            continue

        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("System Power (Watts)")
        ax.set_title(f"System Power Over Time ({num_bots} Participants)")
        ax.legend()
        ax.grid(alpha=0.3)

        plt.tight_layout()
        path = os.path.join(output_dir, f"power_over_time_{num_bots}bots.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Summary statistics table
# ---------------------------------------------------------------------------

def print_summary_statistics(df: pd.DataFrame, output_dir: str):
    """Print and save summary statistics."""
    metrics = ["energy_cpu_joules", "avg_power_watts", "avg_cpu_percent", "total_net_recv_mb", "total_net_sent_mb"]
    available_metrics = [m for m in metrics if m in df.columns]

    summary = df.groupby(["platform", "num_bots"])[available_metrics].agg(["mean", "std", "count"])

    print("\n=== Summary Statistics ===")
    print(summary.to_string())

    # Save to CSV
    path = os.path.join(output_dir, "summary_statistics.csv")
    summary.to_csv(path)
    print(f"\nSaved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Analyze experiment results and generate charts")
    parser.add_argument("--data-dir", default="data", help="Directory containing experiment CSVs")
    parser.add_argument("--output-dir", default="figures", help="Directory for output charts")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # Load data
    df = load_combined_results(args.data_dir)
    print(f"Loaded {len(df)} experiment runs")
    print(f"Platforms: {df['platform'].unique().tolist()}")
    print(f"Bot counts: {sorted(df['num_bots'].unique().tolist())}")

    # Generate all charts
    if "energy_cpu_joules" in df.columns:
        plot_energy_bar(df, args.output_dir)
        plot_energy_scaling(df, args.output_dir)
    else:
        print("Warning: no energy_cpu_joules column — skipping energy charts")

    plot_cpu_over_time(args.data_dir, args.output_dir, df)
    plot_power_over_time(args.data_dir, args.output_dir, df)
    plot_network_comparison(df, args.output_dir)
    print_summary_statistics(df, args.output_dir)

    print(f"\nAll charts saved to {args.output_dir}/")


if __name__ == "__main__":
    main()
