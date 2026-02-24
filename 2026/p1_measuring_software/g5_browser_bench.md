---
author: Brewen Couaran, Valantis Andreas, Arnav Biswas, Alex Hautelman
group_number: 5
title: "Cross-Platform Browser Energy Benchmarking"
image: "img/g5_browser_bench/project_cover.png"
date: 12/02/2026
summary: |-
  This project examines how operating systems impact browser energy consumption by comparing Google Chrome and Firefox on macOS, Windows, and Linux using a standardized BrowserBench workload measured with EnergiBridge.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Cross-Platform Browser Energy Benchmarking

### **Introduction**

Web browsers are among the most widely used software applications today, yet we know surprisingly little about how much energy they actually consume. The ICT sector accounts for roughly 7–10% of global energy consumption, and browsers sit at the center of that since they run on nearly every device and handle everything from simple pages to complex web applications. Despite this, most energy estimates for software still rely on "constant-power" models that assume hardware draws the same wattage no matter what task is running. These models tend to overestimate actual usage and miss the differences between browser engines and operating systems.

This matters to several groups. IT managers need accurate per-application energy data to report carbon footprints, web developers want to know whether their framework choices affect battery life, and policy makers are starting to set efficiency standards for software, thus needing real measurements to base those on. Finally, for everyday users, the difference between browsers can mean the difference between a laptop lasting a full day or needing a charge by lunch.

To get concrete numbers, we use **EnergiBridge**, a cross-platform tool that measures power draw on Windows, Linux, and macOS. We run three standardized BrowserBench benchmarks — **MotionMark** (graphics), **Speedometer** (interactivity), and **JetStream 2** (computation) — on both Google Chrome and Firefox, and compare their energy consumption, power draw, temperature, and execution time across operating systems.

---

### **macOS**

The macOS testing phase involved 30 measurement rounds and 5 warmup rounds per benchmark. Warmup rounds ensured hardware temperatures were stabilized and background processes settled, eliminating "tail energy" artifacts that could skew results. Brightness was set to 50% for all tests (auto-brightness disabled) refresh rate was set to 60Hz, with screen saver, auto-lock and display-sleep disabled.

#### **Comparative Results Summary**

The table below presents the metrics collected across the three BrowserBench benchmarks. Positive difference values indicate Firefox consumed or scored higher, whereas negative values indicate Chrome did. Cohen's D quantifies practical significance, while the Mann-Whitney U and T-Test p-values establish statistical significance (p < 0.05).

| Test Category | Metric | Chrome Mean | Firefox Mean | Diff (%) | Cohen's D | Mann-Whitney p | T-Test p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **MotionMark** | Energy (J) | 6429.62 | 5962.65 | −7.26% | 2.878 | 4.98e-11 | 4.78e-16 |
| | Avg Watts | 19.75 | 18.93 | −4.18% | 1.781 | 2.83e-08 | 4.37e-09 |
| | Peak Watts | 30.30 | 31.58 | +4.25% | −0.547 | 2.00e-05 | 0.038 |
| | Max Temp (°C) | 84.02 | 78.25 | −6.86% | 2.864 | 2.37e-10 | 5.78e-16 |
| | Avg RAM (GB) | 19.90 | 19.50 | −2.02% | 0.681 | 1.61e-06 | 0.011 |
| | Duration (s) | 325.52 | 315.05 | −3.22% | 3.819 | 5.57e-10 | 2.43e-21 |
| **Speedometer** | Energy (J) | 424.20 | 509.53 | +20.12% | −2.057 | 8.35e-08 | 6.98e-11 |
| | Avg Watts | 12.96 | 14.17 | +9.29% | −1.502 | 7.60e-07 | 2.74e-07 |
| | Peak Watts | 20.14 | 24.12 | +19.78% | −1.923 | 8.89e-10 | 5.15e-10 |
| | Max Temp (°C) | 63.38 | 66.74 | +5.29% | −1.449 | 4.82e-08 | 5.90e-07 |
| | Avg RAM (GB) | 19.83 | 19.71 | −0.62% | 0.232 | 9.21e-05 | 0.372 |
| | Duration (s) | 32.91 | 36.13 | +9.77% | −0.725 | 2.13e-04 | 0.007 |
| **JetStream 2** | Energy (J) | 685.64 | 1134.40 | +65.45% | −33.882 | 3.02e-11 | 1.87e-73 |
| | Avg Watts | 17.99 | 17.37 | −3.44% | 2.629 | 1.21e-10 | 1.59e-14 |
| | Peak Watts | 38.41 | 38.10 | −0.80% | 0.172 | 0.464 | 0.508 |
| | Max Temp (°C) | 80.24 | 82.77 | +3.15% | −1.266 | 1.75e-05 | 7.95e-06 |
| | Avg RAM (GB) | 20.09 | 19.74 | −1.76% | 1.025 | 1.20e-08 | 2.02e-04 |
| | Duration (s) | 38.10 | 65.29 | +71.35% | −69.757 | 3.02e-11 | 1.30e-91 |

#### **Visualizations**

![Energy Consumption Comparison](img/g5_browser_bench/energy_joules_comparison_boxplot_macos.png)

In JetStream 2, Firefox consumed 65% more total energy than Chrome, whereas in MotionMark Firefox uses about 7% less energy.

![Average Power Draw Comparison](img/g5_browser_bench/avg_watts_comparison_boxplot_macos.png)

Average wattage is similar between browsers for most benchmarks, with the exception of Speedometer where Firefox draws consistently higher average power, which lines up with its longer execution time.

![Peak Power Draw Comparison](img/g5_browser_bench/peak_watts_comparison_boxplot_macos.png)

Peak wattage is similar in JetStream 2, but Firefox shows higher spikes in Speedometer and MotionMark, pointing to more intensive short-burst GPU or CPU usage during those workloads.

![Max Temperature Comparison](img/g5_browser_bench/max_temp_c_comparison_boxplot_macos.png)

During MotionMark, Firefox keeps the machine about 6°C cooler, but it runs hotter in JetStream 2 and Speedometer. The lower temperature in MotionMark is likely related to Firefox's compositing pipeline being more efficient for graphics-heavy tasks.

![Duration Comparison](img/g5_browser_bench/duration_sec_comparison_boxplot_macos.png)

Chrome completes JetStream 2 in almost half the time Firefox needs, due to V8's compilation strategy. MotionMark durations are close, though Chrome runs slightly longer.

![Metric Difference Heatmap](img/g5_browser_bench/metric_difference_heatmap_macos.png)

The heatmap summarizes the relative differences across all metrics. Red cells indicate where Firefox is less efficient (computation), while cooler tones show where it has the advantage (graphics).

#### **Analysis**

The results show a workload-dependent trade-off between Blink (Chrome) and Gecko (Firefox). Chrome's V8 JavaScript engine uses a multi-tier compilation pipeline built for high throughput. In JetStream 2, this approach lets Chrome finish 71% faster, so the CPU returns to idle sooner and total energy consumption ends up 65% lower, even though average wattage is similar.

Firefox excels in graphics-intensive work. During MotionMark it consumed 7.26% less energy and kept the CPU about 6°C cooler than Chrome. This is a result of Firefox's integration with macOS Core Animation. Instead of redrawing the entire screen on every frame, Firefox uses the native layer system (CALayers) to update only the parts that changed, and it shares texture memory directly with the GPU through IOSurfaces rather than copying pixel data back and forth.

Memory consumption was similar between browsers across all benchmarks, with differences staying below 2%. Neither engine has a clear RAM-efficiency advantage on macOS.

In summary, browser choice on macOS should be workload-driven. Firefox is the better option for visually intensive browsing where thermal management matters, while Chrome is preferable for computation-heavy tasks and interactive responsiveness.

---

### **Windows**
To be added

---

### **Linux**
To be added

---

### **Conclusion**
To be added
