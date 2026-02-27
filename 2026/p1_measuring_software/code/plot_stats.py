import re
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from itertools import combinations

DEFAULT_CSV_PATH = "CPU_runs.csv"
OUT_DIR = "./"
ZTHRESH = 3.0

ALPHA = 0.05
DROP_NEG_ENERGY = True

def normalize_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Make the script work with multiple CSV schemas by creating/standardizing:
      - run (from 'run', 'round', or row index)
      - tokens (from 'tokens' or 'gen_tokens')
      - energy_j (from 'gen_energy_j' or 'energy_j')
      - quant (use existing 'quant' else extract from 'model')
      - j_per_token (compute if missing)
    """
    df = df.copy()

    if "run" not in df.columns:
        if "round" in df.columns:
            df["run"] = df["round"]
        else:
            df["run"] = np.arange(1, len(df) + 1)

    if "tokens" not in df.columns:
        if "gen_tokens" in df.columns:
            df["tokens"] = df["gen_tokens"]
        elif "output_tokens" in df.columns:
            df["tokens"] = df["output_tokens"]

    if "energy_j" not in df.columns:
        if "gen_energy_j" in df.columns:
            df["energy_j"] = df["gen_energy_j"]

    if "quant" not in df.columns or df["quant"].isna().all():
        if "model" in df.columns:
            df["quant"] = df["model"].astype(str).str.extract(r"(Q\d(?:_[A-Za-z0-9]+)?)")
        else:
            df["quant"] = np.nan

    if "j_per_token" not in df.columns:
        if "energy_j" in df.columns and "tokens" in df.columns:
            with np.errstate(divide="ignore", invalid="ignore"):
                df["j_per_token"] = df["energy_j"] / df["tokens"]
        else:
            df["j_per_token"] = np.nan

    return df

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV_PATH
df0 = pd.read_csv(CSV_PATH)
df0 = normalize_schema(df0)

plot_specs = [
    ("seconds", "Inference Time (s)", "Seconds"),
    ("tok_per_sec", "Tokens per Second", "Tokens / Second"),
    ("energy_j", "Energy per Inference (J)", "Energy (J)"),
    ("j_per_token", "Energy per Token (J/token)", "J / Token"),
]

metrics = [c for c, _, _ in plot_specs if c in df0.columns]

if "energy_j" in df0.columns:
    neg_energy_runs = df0.loc[df0["energy_j"] < 0, ["run", "model", "energy_j"]].copy() if "model" in df0.columns else df0.loc[df0["energy_j"] < 0, ["run", "energy_j"]].copy()
    df_before = df0[df0["energy_j"] >= 0].copy()
else:
    neg_energy_runs = pd.DataFrame()
    df_before = df0.copy()

removed_rows = []

def zscore_filter(group: pd.DataFrame, metric: str) -> pd.DataFrame:
    g = group.copy()
    if metric not in g.columns:
        return g

    vals = g[metric].to_numpy(dtype=float)

    # Only filter if we have enough samples and some variability
    if len(vals) < 3 or np.nanstd(vals) == 0:
        return g

    z = np.abs(stats.zscore(vals, nan_policy="omit"))
    keep = (z < ZTHRESH) | np.isnan(z)

    cols = ["run", "quant", metric] + (["model"] if "model" in g.columns else [])
    removed = g.loc[~keep, cols].copy()
    if len(removed) > 0:
        removed_rows.append(removed.assign(metric=metric))

    return g.loc[keep].copy()

df_after = df_before.copy()
for q in sorted(df_after["quant"].dropna().unique()):
    mask = df_after["quant"] == q
    g = df_after.loc[mask].copy()
    for m in metrics:
        g = zscore_filter(g, m)
    df_after = pd.concat([df_after.loc[~mask], g], ignore_index=True)

removed_rows_df = pd.concat(removed_rows, ignore_index=True) if removed_rows else pd.DataFrame()

def make_plots(df, suffix):
    quant_order = sorted(df["quant"].dropna().unique())
    saved = []

    for col, title, ylabel in plot_specs:
        if col not in df.columns:
            continue

        data = [
            df.loc[df["quant"] == q, col].dropna().to_numpy(dtype=float)
            for q in quant_order
        ]

        plt.figure(figsize=(7, 5))
        plt.violinplot(data, showmeans=False, showmedians=False)
        plt.boxplot(data, widths=0.18)
        plt.xticks(range(1, len(quant_order) + 1), quant_order)
        plt.xlabel("Quantization")
        plt.ylabel(ylabel)
        plt.title(f"{title} ({suffix})")
        plt.tight_layout()

        out_path = os.path.join(OUT_DIR, f"violin_box_{col}_{suffix}.png")
        plt.savefig(out_path, dpi=200)
        saved.append(out_path)
        plt.show()

    return saved

saved_before = make_plots(df_before, "before_outliers")
saved_after  = make_plots(df_after,  "after_outliers")

def summary_mean_ci95_std(df):
    quant_order = sorted(df["quant"].dropna().unique())
    rows = []
    for col, _, _ in plot_specs:
        if col not in df.columns:
            continue
        for q in quant_order:
            g = df.loc[df["quant"] == q, col].dropna().to_numpy(dtype=float)
            n = len(g)
            mean = float(np.mean(g)) if n else np.nan
            std = float(np.std(g, ddof=1)) if n > 1 else np.nan
            ci95 = float(stats.sem(g) * stats.t.ppf(0.975, n - 1)) if n > 1 else np.nan
            rows.append({"metric": col, "quant": q, "mean": mean, "std": std, "ci95": ci95, "n": n})
    return pd.DataFrame(rows)

before_csv_path = os.path.join(OUT_DIR, "final_results_before_outliers.csv")
after_csv_path  = os.path.join(OUT_DIR, "final_results_after_outliers.csv")
before_sum_path = os.path.join(OUT_DIR, "summary_before_mean_ci95_std.csv")
after_sum_path  = os.path.join(OUT_DIR, "summary_after_mean_ci95_std.csv")

df_before.to_csv(before_csv_path, index=False)
df_after.to_csv(after_csv_path, index=False)

summary_before = summary_mean_ci95_std(df_before)
summary_after  = summary_mean_ci95_std(df_after)

summary_before.to_csv(before_sum_path, index=False)
summary_after.to_csv(after_sum_path, index=False)

print("\n==============================")
print("STD (after outlier removal) — from summary_after_mean_ci95_std.csv")
print("==============================")
if len(summary_after):
    std_table = summary_after.pivot(index="quant", columns="metric", values="std")
    with pd.option_context("display.width", 140, "display.max_columns", 50):
        print(std_table.round(6).to_string())
else:
    print("No summary rows available.")

print("\n=== Input CSV ===")
print(CSV_PATH)

print("\n=== Negative-energy runs removed (excluded from BOTH plot sets) ===")
print(neg_energy_runs.to_string(index=False) if len(neg_energy_runs) else "None")

print(f"\n=== Z-score outliers removed for AFTER plots (|z| >= {ZTHRESH}) ===")
print(
    removed_rows_df.sort_values(["metric", "quant", "run"]).to_string(index=False)
    if len(removed_rows_df) else "None"
)

print("\nCounts per quant (before):")
print(df_before.groupby("quant").size())

print("\nCounts per quant (after):")
print(df_after.groupby("quant").size())

print("\nSaved BEFORE plots:")
for p in saved_before:
    print(p)

print("\nSaved AFTER plots:")
for p in saved_after:
    print(p)

print("\nSaved CSVs:")
print(before_csv_path)
print(after_csv_path)

print("\nSaved summaries:")
print(before_sum_path)
print(after_sum_path)

def cohens_d(x, y):
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    x = x[~np.isnan(x)]; y = y[~np.isnan(y)]
    nx, ny = len(x), len(y)
    if nx < 2 or ny < 2:
        return np.nan
    sx, sy = np.std(x, ddof=1), np.std(y, ddof=1)
    sp = np.sqrt(((nx-1)*sx*sx + (ny-1)*sy*sy) / (nx+ny-2))
    if sp == 0:
        return np.nan
    return (np.mean(x) - np.mean(y)) / sp

def holm_correction(pvals):
    pvals = np.asarray(pvals, dtype=float)
    m = len(pvals)
    order = np.argsort(pvals)
    adj = np.empty(m)

    for k, idx in enumerate(order):
        adj[idx] = min((m - k) * pvals[idx], 1.0)

    adj_sorted = adj[order]
    for i in range(1, m):
        adj_sorted[i] = max(adj_sorted[i], adj_sorted[i - 1])
    adj[order] = adj_sorted
    return adj


def rank_biserial_from_u(u, n1, n2):
    return 1.0 - (2.0 * u) / (n1 * n2)

def pairwise_conditional(df, metric, groups, normality, alpha=0.05):
    """Pairwise tests:
      - If BOTH groups pass Shapiro (normal=True): Welch t-test + Cohen's d
      - Else: Mann–Whitney U (two-sided) + rank-biserial correlation

    Applies Holm correction to p-values.
    """
    pairs = list(combinations(groups, 2))
    rows, pvals = [], []

    for a, b in pairs:
        xa = df.loc[df["quant"] == a, metric].dropna().to_numpy(dtype=float)
        xb = df.loc[df["quant"] == b, metric].dropna().to_numpy(dtype=float)

        if len(xa) < 2 or len(xb) < 2:
            continue

        normal_a = bool(normality.get(a, False))
        normal_b = bool(normality.get(b, False))

        if normal_a and normal_b:
            stat, p = stats.ttest_ind(xa, xb, equal_var=False)
            test = "welch_t"
            effect = cohens_d(xa, xb)
            effect_name = "cohens_d"
        else:
            stat, p = stats.mannwhitneyu(xa, xb, alternative="two-sided")
            test = "mannwhitney_u"
            effect = rank_biserial_from_u(stat, len(xa), len(xb))
            effect_name = "rank_biserial"

        rows.append({"A": a, "B": b, "test": test, "stat": stat, "p_raw": p, effect_name: effect})
        pvals.append(p)

    if not rows:
        return pd.DataFrame(columns=["A","B","test","stat","p_raw","p_holm","significant","cohens_d","rank_biserial"])

    p_holm = holm_correction(pvals)
    for i in range(len(rows)):
        rows[i]["p_holm"] = p_holm[i]
        rows[i]["significant"] = p_holm[i] < alpha

    return pd.DataFrame(rows).sort_values("p_holm")


def print_df(df, floatfmt="{:.6f}"):
    with pd.option_context(
        "display.max_rows", 200,
        "display.max_columns", 50,
        "display.width", 140,
        "display.float_format", lambda x: floatfmt.format(x)
    ):
        print(df.to_string(index=False))

df = df_after.copy()

if DROP_NEG_ENERGY and "energy_j" in df.columns:
    df = df[df["energy_j"].isna() | (df["energy_j"] >= 0)].copy()

quant_order = sorted(df["quant"].dropna().unique())

print("\n" + "="*50)
print("OUTPUT DETERMINISM VERIFICATION")
print("="*50)

det_ok = True
if "generated_text" not in df.columns:
    print("No 'generated_text' column found; cannot verify determinism.")
else:
    for q in quant_order:
        texts = df.loc[df["quant"] == q, "generated_text"].dropna().astype(str).tolist()
        if not texts:
            print(f"  {q}: (no text to compare)")
            continue
        first = texts[0]
        same = all(t == first for t in texts)
        mark = "✓" if same else "✗"
        det_ok = det_ok and same
        print(f"  {q}: {mark} {'DETERMINISTIC' if same else 'NON-DETERMINISTIC'} ({len(first)} chars)")

print("\n" + ("✓ All outputs deterministic." if det_ok else "✗ Some outputs are NOT deterministic."))

df_runs = df.copy()
metrics_cols = ["seconds", "tokens", "tok_per_sec", "energy_j", "j_per_token"]
present = [c for c in metrics_cols if c in df_runs.columns]

df_mean = df_runs.groupby("quant")[present].mean().reindex(quant_order).reset_index()
print_df(df_mean, floatfmt="{:.6f}")

print("\n" + "="*50)
print("Shapiro–Wilk + Kruskal–Wallis + Pairwise (Welch if normal else Mann–Whitney) (Holm) + Effect Size")
print("="*50)

TEST_METRICS = [
    ("seconds", "Inference Time (s)"),
    ("tok_per_sec", "Tokens per Second"),
    ("energy_j", "Energy per Inference (J)"),
    ("j_per_token", "Energy per Token (J/token)"),
]

for met, title in TEST_METRICS:
    if met not in df_runs.columns:
        continue

    print(f"\n--- {title} ---")
    print("Shapiro–Wilk (per quant):")

    groups = []
    normality = {}
    for q in quant_order:
        g = df_runs.loc[df_runs["quant"] == q, met].dropna().to_numpy(dtype=float)
        groups.append(g)
        if len(g) < 3:
            print(f"  {q}: n={len(g)} skipped")
            continue
        W, p = stats.shapiro(g)
        normality[q] = (p > ALPHA)
        print(f"  {q}: n={len(g)}  W={W:.4f}  p={p:.4g}  normal={normality[q]}")

    kw_groups = [g for g in groups if len(g) > 0]
    if len(kw_groups) >= 2:
        H, p_kw = stats.kruskal(*kw_groups)
        print(f"Kruskal–Wallis: H = {H:.6f}, p = {p_kw:.6e}, significant = {p_kw < ALPHA}")
    else:
        print("Kruskal–Wallis: not enough data")
        continue

    pw = pairwise_conditional(df_runs, met, quant_order, normality, alpha=ALPHA)
    cols = ["A","B","test","stat","p_raw","cohens_d","rank_biserial","p_holm","significant"]
    pw_disp = pw.reindex(columns=cols)
    print_df(pw_disp, floatfmt="{:.6e}")

print("\n" + "="*50)
print("RUNS PER QUANT")
print("="*50)
print(df_runs.groupby("quant").size().to_string())
