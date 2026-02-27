"""Reusable helpers for loading EnergiBridge CSVs and computing energy metrics."""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


COLS_TO_KEEP = ["Delta", "Time", "CORE0_ENERGY (J)", "CPU_ENERGY (J)"]


def load_run(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    keep = [c for c in COLS_TO_KEEP if c in df.columns]
    return df[keep].copy()


def _robust_energy_delta(series: pd.Series) -> float:
    """Sum only positive increments to handle counter resets / glitches."""
    diffs = series.diff().iloc[1:]
    return float(diffs[diffs > 0].sum())


def summarise_run(csv_path: str | Path) -> dict:
    df = load_run(csv_path)
    duration_ms = df["Time"].max() - df["Time"].min()
    duration_s = duration_ms / 1000.0

    cpu_energy_j = _robust_energy_delta(df["CPU_ENERGY (J)"])
    core0_energy_j = _robust_energy_delta(df["CORE0_ENERGY (J)"])
    avg_cpu_power_w = cpu_energy_j / duration_s if duration_s > 0 else np.nan

    return {
        "file": Path(csv_path).name,
        "duration_s": duration_s,
        "cpu_energy_j": cpu_energy_j,
        "core0_energy_j": core0_energy_j,
        "avg_cpu_power_w": avg_cpu_power_w,
    }


def load_all_runs(folder: str | Path, pattern: str = "energy_*_run*.csv") -> pd.DataFrame:
    folder = Path(folder)
    files = sorted(folder.glob(pattern))
    rows = [summarise_run(f) for f in files]
    return pd.DataFrame(rows)


#outlier removal

def iqr_mask(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Return boolean mask where True = inlier."""
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    return (series >= q1 - k * iqr) & (series <= q3 + k * iqr)


def remove_outliers(
    df: pd.DataFrame,
    metrics: list[str] = ("duration_s", "cpu_energy_j", "core0_energy_j"),
    k: float = 1.5,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Remove rows that are outliers in *any* of the given metrics.

    Returns (clean_df, outlier_df).
    """
    mask = pd.Series(True, index=df.index)
    for col in metrics:
        mask &= iqr_mask(df[col], k)
    return df[mask].copy(), df[~mask].copy()


#stat tests

def _cohens_d(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = len(a), len(b)
    pooled_std = np.sqrt(((na - 1) * a.std(ddof=1) ** 2 + (nb - 1) * b.std(ddof=1) ** 2) / (na + nb - 2))
    return float((a.mean() - b.mean()) / pooled_std) if pooled_std > 0 else np.nan


def _cliffs_delta(a: np.ndarray, b: np.ndarray) -> float:
    """Cliff's delta effect size for ordinal / non-normal data."""
    more = sum(1 for x in a for y in b if x > y)
    less = sum(1 for x in a for y in b if x < y)
    n = len(a) * len(b)
    return (more - less) / n if n > 0 else np.nan


def compare_groups(json_vals: np.ndarray, orjson_vals: np.ndarray) -> dict:
    """Run normality check → appropriate test → effect size for one metric."""
    _, p_norm_json = stats.shapiro(json_vals)
    _, p_norm_orjson = stats.shapiro(orjson_vals)
    both_normal = p_norm_json > 0.05 and p_norm_orjson > 0.05

    if both_normal:
        stat, p_val = stats.ttest_ind(json_vals, orjson_vals, equal_var=False)
        test_name = "Welch t-test"
        effect = _cohens_d(json_vals, orjson_vals)
        effect_name = "Cohen's d"
    else:
        stat, p_val = stats.mannwhitneyu(json_vals, orjson_vals, alternative="two-sided")
        test_name = "Mann-Whitney U"
        effect = _cliffs_delta(json_vals, orjson_vals)
        effect_name = "Cliff's delta"

    return {
        "test": test_name,
        "statistic": stat,
        "p_value": p_val,
        "shapiro_p_json": p_norm_json,
        "shapiro_p_orjson": p_norm_orjson,
        "both_normal": both_normal,
        "effect_size": effect,
        "effect_name": effect_name,
        "json_mean": float(json_vals.mean()),
        "json_std": float(json_vals.std(ddof=1)),
        "orjson_mean": float(orjson_vals.mean()),
        "orjson_std": float(orjson_vals.std(ddof=1)),
    }
