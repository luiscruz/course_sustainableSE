import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("summary_new.csv")

meet_energy = df[df["platform"] == "meet"]["energy_cpu_joules"]
teams_energy = df[df["platform"] == "teams"]["energy_cpu_joules"]

data = [meet_energy, teams_energy]

fig, ax = plt.subplots()

violins = ax.violinplot(
    data,
    showmeans=False,
    showmedians=False,
    showextrema=False
)

colors = ["#4C72B0", "#DD8452"]

for i, pc in enumerate(violins["bodies"]):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor("black")
    pc.set_alpha(0.6)

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

ax.set_xticks([1, 2])
ax.set_xticklabels(["Meet", "Teams"])
ax.set_ylabel("CPU Energy Consumption (J)")
ax.set_title("Energy Consumption Comparison: Meet vs Teams")

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()