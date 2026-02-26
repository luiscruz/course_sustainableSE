import pandas as pd
import numpy as np
from scipy.stats import shapiro

df = pd.read_csv("outlier_removed_summary.csv")

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
# Total Net Sent (MB)
# -----------------------
meet_net_sent = df[df["platform"] == "meet"]["total_net_sent_mb"]
teams_net_sent = df[df["platform"] == "teams"]["total_net_sent_mb"]

descriptive_stats(meet_net_sent, "Meet - Total Net Sent (MB)")
descriptive_stats(teams_net_sent, "Teams - Total Net Sent (MB)")

# -----------------------
# Total Net Received (MB)
# -----------------------
meet_net_recv = df[df["platform"] == "meet"]["total_net_recv_mb"]
teams_net_recv = df[df["platform"] == "teams"]["total_net_recv_mb"]

descriptive_stats(meet_net_recv, "Meet - Total Net Received (MB)")
descriptive_stats(teams_net_recv, "Teams - Total Net Received (MB)")

# -----------------------
# Avg Power (Watts)
# -----------------------
meet_power = df[df["platform"] == "meet"]["avg_power_watts"]
teams_power = df[df["platform"] == "teams"]["avg_power_watts"]

descriptive_stats(meet_power, "Meet - Avg Power (W)")
descriptive_stats(teams_power, "Teams - Avg Power (W)")


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

normality_test(meet_power, "Meet - Power")
normality_test(teams_power, "Teams - Power")

normality_test(meet_net_sent, "Meet - Sent Bytes")
normality_test(teams_net_sent, "Teams - Sent Bytes")

normality_test(meet_net_recv, "Meet - Received Bytes")
normality_test(teams_net_recv, "Teams - Received Bytes")


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

u_stat, p_val = mannwhitneyu(meet_power, teams_power, alternative='two-sided')
print("\nMann-Whitney U Test Power %")
print(f"U-stat = {u_stat:.4f}, p-value = {p_val:.4f}")

# Energy (J)
u_stat, p_val = mannwhitneyu(meet_net_recv, teams_net_recv, alternative='two-sided')
print("\nMann-Whitney U Test Net Received Bytes")
print(f"U-stat = {u_stat:.4f}, p-value = {p_val:.4f}")

u_stat, p_val = mannwhitneyu(meet_net_sent, teams_net_sent, alternative='two-sided')
print("\nMann-Whitney U Test Net Sent Bytes %")
print(f"U-stat = {u_stat:.4f}, p-value = {p_val:.4f}")


def rank_biserial(u, n1, n2):
    return 1 - (2 * u) / (n1 * n2)

n1 = len(meet_energy)
n2 = len(teams_energy)

r_cpu = rank_biserial(65.5, n1, n2)
r_energy = rank_biserial(0.0, n1, n2)
r_power = rank_biserial(3.0, n1, n2)
r_received_bytes = rank_biserial(0.0, n1, n2)
r_sent_bytes = rank_biserial(690.5, n1, n2)

print("Rank-biserial CPU:", r_cpu)
print("Rank-biserial Energy:", r_energy)
print("Rank-biserial Power:", r_power)
print("Rank-biserial Sent Bytes:", r_sent_bytes)
print("Rank-biserial Received Bytes:", r_received_bytes)