import pandas as pd
import numpy as np

df = pd.read_csv("summary_new.csv")

columns_to_check = [
    "total_net_recv_mb",
    "avg_cpu_percent",
    "energy_cpu_joules",
    "total_net_sent_mb",
    "avg_power_watts"
                    ]

# Create flag column
df["is_outlier"] = False

# Process each platform separately
for platform in df["platform"].unique():
    mask = df["platform"] == platform

    # Compute mean & std within platform
    means = df.loc[mask, columns_to_check].mean()
    stds = df.loc[mask, columns_to_check].std(ddof=1)

    # Avoid division by zero
    stds = stds.replace(0, np.nan)

    # Compute z-scores
    z_scores = (df.loc[mask, columns_to_check] - means) / stds

    # Flag rows where ANY column exceeds 3 std
    outlier_mask = (np.abs(z_scores) > 3).any(axis=1)

    # Assign safely (no .values needed)
    df.loc[mask, "is_outlier"] = outlier_mask

# Remove outliers
df_clean = df[~df["is_outlier"]].copy()
df_removed = df[df["is_outlier"]].copy()

# Drop helper column
df_clean.drop(columns=["is_outlier"], inplace=True)
df_removed.drop(columns=["is_outlier"], inplace=True)

# Save results
df_clean.to_csv("outlier_removed_summary.csv", index=False)
df_removed.to_csv("removed_outliers.csv", index=False)

# Print summary
print("Original runs:", len(df))
print("Removed runs:", len(df_removed))
print("Remaining runs:", len(df_clean))