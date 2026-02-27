import os, glob
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import (
    shapiro,
    zscore,
    ttest_ind,
    mannwhitneyu
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(SCRIPT_DIR, "results")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "analysis_plots")

CONDITIONS = ["auto_nc", "auto", "medium", "high_nc", "high", "very_high"]

Z_SCORE_THRESHOLD = 3
ALPHA = 0.05  # significance level

def load_all_runs(condition):
    pattern = os.path.join(RESULTS_DIR, f"{condition}_run_*.csv")
    files = sorted(glob.glob(pattern))

    dfs = []
    for filepath in files:
        df = pd.read_csv(filepath)
        df["condition"] = condition
        df["run_file"] = Path(filepath).name
        dfs.append(df)

    if not dfs:
        print(f"No files found for {condition}")
        return pd.DataFrame()

    return pd.concat(dfs, ignore_index=True)

def calculate_metrics(df):
    metrics = []

    for condition in CONDITIONS:
        cond_data = df[df["condition"] == condition]

        for run_file in cond_data["run_file"].unique():
            run_data = cond_data[
                cond_data["run_file"] == run_file
            ].reset_index(drop=True)
            
            execution_time = run_data["Delta"].sum() / 1000
            
            cumsum_delta = run_data["Delta"].cumsum()
            run_data = run_data[cumsum_delta >= 5000].reset_index(drop=True)
            
            if len(run_data) == 0:
                continue

            time_s = run_data["Delta"].cumsum() / 1000
            power_w = run_data["SYSTEM_POWER (Watts)"].values
            total_energy_j = np.trapz(power_w, time_s)

            avg_power = run_data["SYSTEM_POWER (Watts)"].mean()
            max_power = run_data["SYSTEM_POWER (Watts)"].max()

            cpu_cols = [c for c in run_data.columns if c.startswith("CPU_USAGE_")]
            avg_cpu_usage = run_data[cpu_cols].mean().mean()

            temp_cols = [c for c in run_data.columns if c.startswith("CPU_TEMP_")]
            avg_temp = run_data[temp_cols].mean().mean()

            metrics.append({
                "condition": condition,
                "run_file": run_file,
                "total_energy_j": total_energy_j,
                "avg_power_w": avg_power,
                "max_power_w": max_power,
                "execution_time_s": execution_time,
                "avg_cpu_usage_pct": avg_cpu_usage,
                "avg_temp_c": avg_temp,
            })

    return pd.DataFrame(metrics)

def test_normality(data):
    if len(data) < 3:
        return False, None
    stat, p_value = shapiro(data)
    return p_value >= ALPHA, p_value


def remove_outliers(data):
    if len(data) < 3:
        return data

    z_scores = np.abs(zscore(data))
    return data[z_scores <= Z_SCORE_THRESHOLD]

def cohens_d(a, b):
    mean_diff = np.mean(b) - np.mean(a)
    pooled_std = np.sqrt(
        (np.var(a, ddof=1) + np.var(b, ddof=1)) / 2
    )
    return mean_diff / pooled_std


def common_language_effect_size(u_stat, n1, n2):
    return u_stat / (n1 * n2)

def compare_conditions(data1, data2):
    normal1, p1 = test_normality(data1)
    normal2, p2 = test_normality(data2)

    if not normal1:
        data1 = remove_outliers(data1)
        normal1, _ = test_normality(data1)

    if not normal2:
        data2 = remove_outliers(data2)
        normal2, _ = test_normality(data2)

    both_normal = normal1 and normal2

    results = {}

    if both_normal:
        stat, p_value = ttest_ind(data1, data2, equal_var=False)
        effect = cohens_d(data1, data2)

        results.update({
            "test": "Welch t-test",
            "statistic": stat,
            "p_value": p_value,
            "effect_size": effect,
            "effect_type": "Cohen's d"
        })

    else:
        stat, p_value = mannwhitneyu(data1, data2, alternative="two-sided")
        effect = common_language_effect_size(stat, len(data1), len(data2))

        results.update({
            "test": "Mann-Whitney U",
            "statistic": stat,
            "p_value": p_value,
            "effect_size": effect,
            "effect_type": "Common Language ES"
        })

    results.update({
        "mean1": np.mean(data1),
        "mean2": np.mean(data2),
        "median1": np.median(data1),
        "median2": np.median(data2),
        "percent_diff": (
            (np.mean(data2) - np.mean(data1)) / np.mean(data1)
        ) * 100
    })

    return results


def run_statistical_tests(metrics_df, column):

    available_conditions = metrics_df["condition"].unique()
    results = {}

    for i in range(len(available_conditions)):
        for j in range(i + 1, len(available_conditions)):

            cond1 = available_conditions[i]
            cond2 = available_conditions[j]

            data1 = metrics_df[
                metrics_df["condition"] == cond1
            ][column].values

            data2 = metrics_df[
                metrics_df["condition"] == cond2
            ][column].values

            comparison = compare_conditions(data1, data2)

            results[f"{cond1}_vs_{cond2}"] = comparison

            print("\n")
            print(f"{cond1} vs {cond2}")
            print(f"Metric: {column}")
            print(f"Test used: {comparison['test']}")
            print(f"p-value: {comparison['p_value']:.6f}")
            print(f"Effect size ({comparison['effect_type']}): {comparison['effect_size']:.4f}")
            print(f"Percent difference: {comparison['percent_diff']:+.2f}%")

    return results

def create_violin_plot(metrics_df, column, ylabel, title, filename):

    fig, ax = plt.subplots(figsize=(12, 8))

    available_conditions = [
        cond for cond in CONDITIONS
        if cond in metrics_df["condition"].values
    ]

    condition_data = [
        metrics_df[metrics_df["condition"] == cond][column].values
        for cond in available_conditions
    ]

    parts = ax.violinplot(
        condition_data,
        positions=range(len(available_conditions)),
        widths=0.7,
        showmeans=False,
        showmedians=False,
        showextrema=False
    )

    for pc in parts["bodies"]:
        pc.set_facecolor("darkseagreen")
        pc.set_edgecolor("darkseagreen")
        pc.set_alpha(0.8)

    ax.boxplot(
        condition_data,
        positions=range(len(available_conditions)),
        widths=0.25,
        patch_artist=True,
        boxprops=dict(facecolor="white"),
        medianprops=dict(color="red", linewidth=2),
    )

    ax.set_xticks(range(len(available_conditions)))
    ax.set_xticklabels([
        f"{cond}\n(n={len(metrics_df[metrics_df['condition'] == cond])})"
        for cond in available_conditions
    ])

    ax.set_ylabel(ylabel)
    ax.set_title(title)

    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.close()

def get_next_filename(base_filename):
    if not os.path.exists(OUTPUT_DIR):
        return base_filename
    
    name, ext = os.path.splitext(base_filename)
    counter = 1
    new_filename = f"{name}_{counter}{ext}"
    
    while os.path.exists(os.path.join(OUTPUT_DIR, new_filename)):
        counter += 1
        new_filename = f"{name}_{counter}{ext}"
    
    return new_filename

def main():
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_data = pd.concat(
        [load_all_runs(cond) for cond in CONDITIONS],
        ignore_index=True
    )

    if all_data.empty:
        print("No data found.")
        return

    metrics_df = calculate_metrics(all_data)

    plots = [
        ('total_energy_j', 'Total Energy (J)', 'Total Energy Consumption', '01_energy.png'),
        ('avg_power_w', 'Average Power (W)', 'Average Power Consumption', '02_avg_power.png'),
        ('max_power_w', 'Peak Power (W)', 'Peak Power Consumption', '03_max_power.png'),
        ('avg_cpu_usage_pct', 'CPU Usage (%)', 'Average CPU Utilization', '05_cpu_usage.png'),
        ('avg_temp_c', 'Temperature (°C)', 'Average CPU Temperature', '06_temperature.png'),
    ]
    
    for column, ylabel, title, filename in plots:
        new_filename = get_next_filename(filename)
        create_violin_plot(metrics_df, column, ylabel, title, new_filename)

    print("\nSTATISTICAL ANALYSIS")
    run_statistical_tests(metrics_df, "total_energy_j")


if __name__ == "__main__":
    main()