import pandas as pd
import numpy as np
from scipy.stats import shapiro

df = pd.read_csv("summary_new.csv")

def descriptive_stats(data, label):
    print(f"\n--- {label} ---")
    print(f"n = {len(data)}")
    print(f"Mean = {np.mean(data):.4f}")
    print(f"Std Dev = {np.std(data, ddof=1):.4f}")
    print(f"Median = {np.median(data):.4f}")

# -----------------------
# CPU %
# -----------------------

meet_cpu = df[df["platform"] == "meet"]["avg_cpu_percent"]
teams_cpu = df[df["platform"] == "teams"]["avg_cpu_percent"]

descriptive_stats(meet_cpu, "Meet - CPU %")
descriptive_stats(teams_cpu, "Teams - CPU %")

# -----------------------
# Energy (J)
# -----------------------

meet_energy = df[df["platform"] == "meet"]["energy_cpu_joules"]
teams_energy = df[df["platform"] == "teams"]["energy_cpu_joules"]

descriptive_stats(meet_energy, "Meet - Energy (J)")
descriptive_stats(teams_energy, "Teams - Energy (J)")

# -----------------------
# Normality test
# -----------------------

def normality_test(data, label):
    stat, p = shapiro(data)
    print(f"\nShapiro test for {label}")
    print(f"Statistic = {stat:.4f}, p-value = {p:.4f}")

normality_test(meet_cpu, "Meet - CPU %")
normality_test(teams_cpu, "Teams - CPU %")

normality_test(meet_energy, "Meet - Energy")
normality_test(teams_energy, "Teams - Energy")

# -----------------------
# Statistical test
# -----------------------

from scipy.stats import mannwhitneyu

# CPU %
u_stat, p_val = mannwhitneyu(meet_cpu, teams_cpu, alternative='two-sided')
print("\nMann-Whitney U Test CPU %")
print(f"U-stat = {u_stat:.4f}, p-value = {p_val:.4f}")

# Energy (J)
u_stat, p_val = mannwhitneyu(meet_energy, teams_energy, alternative='two-sided')
print("\nMann-Whitney U Test Energy")
print(f"U-stat = {u_stat:.4f}, p-value = {p_val:.4f}")

def rank_biserial(u, n1, n2):
    return 1 - (2 * u) / (n1 * n2)

n1 = len(meet_energy)
n2 = len(teams_energy)

r_cpu = rank_biserial(102.5, 29, 29)
r_energy = rank_biserial(0.0, 29, 29)

print("Rank-biserial CPU:", r_cpu)
print("Rank-biserial Energy:", r_energy)