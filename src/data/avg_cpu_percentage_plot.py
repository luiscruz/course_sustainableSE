import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("summary_new.csv")

meet_cpu = df[df["platform"] == "meet"]["avg_cpu_percent"]
teams_cpu = df[df["platform"] == "teams"]["avg_cpu_percent"]

data = [meet_cpu, teams_cpu]

fig, ax = plt.subplots()

# --- Violin Plot ---
violins = ax.violinplot(
    data,
    showmeans=False,
    showmedians=False,
    showextrema=False
)

# Custom colors
colors = ["#4C72B0", "#DD8452"]  # blue for meet, orange for teams

for i, pc in enumerate(violins["bodies"]):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor("black")
    pc.set_alpha(0.6)

# --- Box Plot Overlay ---
lineprops = dict(linewidth=1)
medianprops = dict(color="black", linewidth=1.2)

ax.boxplot(
    data,
    widths=0.15,
    patch_artist=True,
    whiskerprops=lineprops,
    boxprops=lineprops,
    medianprops=medianprops
)

# Labels
ax.set_xticks([1, 2])
ax.set_xticklabels(["Meet", "Teams"])
ax.set_ylabel("Average CPU Percent")
ax.set_title("CPU Usage Comparison: Meet vs Teams")

# Clean style
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()