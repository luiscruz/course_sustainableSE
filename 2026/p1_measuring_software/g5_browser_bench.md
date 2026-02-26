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

### **Introduction**

Web browsers are among the most widely used software applications today, yet we know surprisingly little about how much energy they actually consume. The ICT sector accounts for roughly 5% of global energy consumption, and browsers sit at the center of that since they run on nearly every device and handle everything from simple pages to complex web applications. Despite this, most energy estimates for software still rely on "constant-power" models that assume hardware draws the same wattage no matter what task is running. These models tend to overestimate actual usage and miss the differences between browser engines and operating systems.

This matters to several groups. IT managers need accurate per-application energy data to report carbon footprints, web developers want to know whether their framework choices affect battery life, and policy makers are starting to set efficiency standards for software, thus needing real measurements to base those on. Finally, for everyday users, the difference between browsers can mean the difference between a laptop lasting a full day or needing a charge by lunch.

To get concrete numbers, we use **EnergiBridge**, a cross-platform tool that measures power draw on Windows, Linux, and macOS. We run three standardized BrowserBench benchmarks — **MotionMark** (graphics), **Speedometer** (interactivity), and **JetStream 2** (computation) — on both Google Chrome and Firefox, and compare their energy consumption, power draw, temperature, and execution time across operating systems.

---

### **macOS**

The macOS testing phase involved 30 measurement rounds and 5 warmup rounds per benchmark. Warmup rounds ensured hardware temperatures were stabilized and background processes settled, eliminating "tail energy" artifacts that could skew results. Brightness was set to 50% for all tests (auto-brightness disabled) refresh rate was set to 60Hz, with screen saver, auto-lock and display-sleep disabled. The order of the actual test rounds was randomized to prevent systematic bias from ordering effects, and a 30-second cooldown period was enforced between consecutive runs to allow the CPU to return to a stable thermal state.

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

The Windows experiments followed the same structure as macOS: 5 warmup rounds and 30 measured rounds per benchmark. Warmup runs were used to stabilize CPU frequency scaling, thermal conditions, and background OS activity. All unnecessary background applications were closed, and system updates, indexing, and power-saving features were disabled where possible to reduce noise.

Unlike macOS, Windows relies on the RAPL (Running Average Power Limit) interface exposed via a kernel driver (used by EnergiBridge). This introduces slightly higher variability due to OS-level scheduling and driver interaction, which is reflected in some of the observed outliers.


#### **Comparative Results Summary**

The table below presents the metrics collected across the three BrowserBench benchmarks and the control run. Positive difference values indicate Firefox consumed/scored higher than Chrome, whereas negative values indicate Chrome did. Cohen's D captures practical significance, while Mann–Whitney U and independent t-test p-values indicate statistical significance (p < 0.05).

| Test Category | Metric | Chrome Mean | Firefox Mean | Diff (%) | Cohen's D | Mann-Whitney p | T-Test p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **MotionMark** | Energy (J) | 17721.30 | 17360.92 | -2.03% | 0.448 | 5.57e-10 | 0.0881 |
|  | Avg Watts | 55.44 | 55.37 | -0.12% | 0.026 | 1.85e-08 | 0.92 |
|  | Peak Watts | 100520.44 | 87626.17 | -12.83% | 0.577 | 5.09e-06 | 0.0293 |
|  | Max Temp (°C) | 0.00 | 0.00 | — | 0.000 | 1 | — |
|  | Avg RAM (GB) | 9.46 | 9.10 | -3.76% | 3.944 | 1.83e-17 | 4.56e-43 |
|  | Duration (s) | 319.67 | 313.51 | -1.93% | 2.111 | 1.83e-17 | 1.33e-26 |
| **Speedometer** | Energy (J) | 1232.26 | 1720.69 | +39.64% | -4.934 | 1.83e-17 | 1.69e-40 |
|  | Avg Watts | 42.19 | 49.22 | +16.65% | -1.982 | 9.76e-16 | 2.97e-25 |
|  | Peak Watts | 79562.26 | 81280.72 | +2.16% | -0.183 | 0.00537 | 0.441 |
|  | Max Temp (°C) | 0.00 | 0.00 | — | 0.000 | 1 | — |
|  | Avg RAM (GB) | 9.52 | 9.73 | +2.16% | -1.212 | 1.91e-07 | 0.000221 |
|  | Duration (s) | 29.62 | 35.31 | +19.20% | -2.573 | 2.1e-11 | 7.02e-25 |
| **JetStream 2** | Energy (J) | 2031.55 | 3088.30 | +52.01% | -14.983 | 1.83e-17 | 8.72e-63 |
|  | Avg Watts | 49.17 | 48.55 | -1.25% | 0.303 | 0.00106 | 0.231 |
|  | Peak Watts | 114189.52 | 95827.65 | -16.08% | 0.711 | 4.99e-05 | 0.00577 |
|  | Max Temp (°C) | 0.00 | 0.00 | — | 0.000 | 1 | — |
|  | Avg RAM (GB) | 9.66 | 9.78 | +1.26% | -0.445 | 4.04e-05 | 0.0434 |
|  | Duration (s) | 41.31 | 63.18 | +52.93% | -14.847 | 1.83e-17 | 2.63e-61 |
| **Control** | Energy (J) | 319.01 | 340.64 | +6.78% | -0.401 | 3.35e-06 | 0.112 |
|  | Avg Watts | 21.23 | 20.95 | -1.32% | 0.457 | 3.61e-11 | 0.0681 |
|  | Peak Watts | 43337.59 | 46271.79 | +6.77% | -0.316 | 0.00133 | 0.211 |
|  | Max Temp (°C) | 0.00 | 0.00 | — | 0.000 | 1 | — |
|  | Avg RAM (GB) | 9.17 | 8.83 | -3.01% | 1.944 | 5.68e-13 | 5.18e-24 |
|  | Duration (s) | 15.03 | 15.03 | -0.00% | 0.000 | 1 | — |
> Note: Temperature values are zero due to lack of reliable sensor exposure via EnergiBridge on Windows.
#### **Visualizations**

![Energy Consumption Comparison](img/g5_browser_bench/energy_joules_comparison_boxplot_windows.png)

Energy usage is consistently higher for Firefox in JetStream and Speedometer. MotionMark is the only benchmark where Firefox slightly outperforms Chrome.

![Average Power Draw Comparison](img/g5_browser_bench/avg_watts_comparison_boxplot_windows.png)

Average wattage is similar across browsers, but Firefox tends to draw slightly more power in Speedometer and control scenarios, indicating less efficient idle and interactive behavior.

![Peak Power Draw Comparison](img/g5_browser_bench/peak_watts_comparison_boxplot_windows.png)

Peak power shows high variance, especially in JetStream and Speedometer. Chrome exhibits larger spikes in some runs, likely due to aggressive boosting behavior from the Windows scheduler.

![Duration Comparison](img/g5_browser_bench/duration_sec_comparison_boxplot_windows.png)

Firefox takes significantly longer in JetStream and Speedometer, which directly explains its higher total energy consumption despite similar average power.

![Metric Difference Heatmap](img/g5_browser_bench/metric_difference_heatmap_windows.png)

The heatmap highlights a clear pattern: Firefox is less efficient in computation-heavy and interactive workloads, while differences in graphics workloads are minimal.

Temperature data is effectively zero due to lack of reliable temperature reporting via EnergiBridge on this setup, so no conclusions can be drawn here.

#### **Analysis**

The Windows results reveal a consistent pattern, that **execution time dominates energy consumption**.

In JetStream, Firefox takes over 50% longer to complete the benchmark, leading to a corresponding ~52% increase in total energy usage. This is the same in the macOS findings but is even more pronounced on Windows. Chrome’s V8 engine benefits from aggressive just-in-time (JIT) optimizations and faster execution pipelines, allowing it to complete workloads quickly and return the CPU to idle sooner.

Speedometer shows a similar trend. Firefox consumes ~40% more energy and runs ~19% longer, while also drawing slightly higher average power. This suggests that Firefox’s event handling and DOM update pipeline is less optimized under Windows, possibly due to differences in how Gecko interacts with the Windows graphics and scheduling subsystems.

MotionMark, however, shows different results. Firefox is slightly more efficient (~2% less energy), indicating that its graphics pipeline performs competitively on Windows. Unlike macOS, where Firefox benefits from Core Animation, Windows relies on DirectX, and both browsers appear similarly optimized for this stack.

The control benchmark reveals that Firefox consumes more power even when idle (~6–7% higher). This suggests higher background activity or less aggressive power-saving behavior compared to Chrome.

Peak power behavior is more erratic on Windows, with large outliers in both browsers. This is likely due to:
- Windows CPU boosting (Turbo Boost / Precision Boost)
- OS scheduler variability
- Driver-level measurement noise from RAPL

In summary, on Windows, Chrome is consistently more energy-efficient for computation-heavy tasks (JetStream), and Interactive workloads (Speedometer). Firefox only shows a marginal advantage in graphics workloads (MotionMark). The results indicate that Windows amplifies performance differences between browser engines. Chrome’s faster execution leads to significantly lower energy consumption, making it the more energy-efficient choice for most workloads on this platform.

---

### **Linux**

The Linux testing phase involved 30 measurement rounds and 5 warmup rounds per benchmark, following the same protocol as macOS and Windows. Brightness, refresh rate, and display settings were configured identically. The test environment used a standard Linux desktop with Wayland graphics support (Fedora/KDE). One notable limitation: Linux did not report CPU temperature data during testing, due to the fact that CPU MSRs on Linux do not give access to it. 

#### **Comparative Results Summary**

The table below presents the metrics collected across the three BrowserBench benchmarks on Linux. Like the macOS/Windows results, positive difference values indicate Firefox consumed or scored higher, whereas negative values indicate Chrome did. Cohen's D and statistical tests (Mann-Whitney U and T-Test p < 0.05) establish both practical and statistical significance.

| Test Category | Metric | Chrome Mean | Firefox Mean | Diff (%) | Cohen's D | Mann-Whitney p | T-Test p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **MotionMark** | Energy (J) | 14700.94 | 13774.30 | −6.30% | 11.884 | 8.91e-07 | 1.26e-29 |
| | Avg Watts | 46.06 | 43.82 | −4.86% | 13.786 | 8.91e-07 | 5.97e-32 |
| | Peak Watts | 58088.51 | 728089.43 | +1153.41% | −0.530 | 0.0156 | 0.135 |
| | Max Temp (°C) | 0.0 | 0.0 | — | — | — | — |
| | Avg RAM (GB) | 3.995 | 4.215 | +5.49% | −3.311 | 8.91e-07 | 1.61e-11 |
| | Duration (s) | 319.19 | 314.33 | −1.52% | 1.969 | 4.03e-06 | 1.73e-06 |
| **Speedometer** | Energy (J) | 1076.34 | 1498.89 | +39.26% | −2.508 | 7.05e-07 | 1.10e-09 |
| | Avg Watts | 38.93 | 41.04 | +5.43% | −2.620 | 7.68e-08 | 3.70e-10 |
| | Peak Watts | 52010.72 | 54434.22 | +4.66% | −2.324 | 1.05e-06 | 6.87e-09 |
| | Max Temp (°C) | 0.0 | 0.0 | — | — | — | — |
| | Avg RAM (GB) | 4.071 | 4.756 | +16.84% | −8.486 | 7.68e-08 | 4.10e-27 |
| | Duration (s) | 27.81 | 36.53 | +31.34% | −1.602 | 7.05e-07 | 1.03e-05 |
| **JetStream 2** | Energy (J) | 1953.25 | 3321.23 | +70.04% | −81.037 | 1.46e-06 | 2.86e-61 |
| | Avg Watts | 44.68 | 43.60 | −2.41% | 5.263 | 1.46e-06 | 2.03e-17 |
| | Peak Watts | 77252.55 | 77731.97 | +0.62% | −0.614 | 0.289 | 0.091 |
| | Max Temp (°C) | 0.0 | 0.0 | — | — | — | — |
| | Avg RAM (GB) | 4.313 | 4.769 | +10.56% | −6.449 | 1.46e-06 | 2.28e-20 |
| | Duration (s) | 43.72 | 76.17 | +74.23% | −190.692 | 1.46e-06 | 2.18e-75 |

#### **Visualizations**

![Energy Consumption Comparison](img/g5_browser_bench/energy_joules_comparison_boxplot_linux.png)

Firefox consumed 70% more total energy than Chrome in JetStream 2, compared to only 6% less in MotionMark. The Speedometer gap is also significant, with Firefox using 39% more energy despite similar average power draw, which is a clear sign that execution time dominates the energy difference.

![Average Power Draw Comparison](img/g5_browser_bench/avg_watts_comparison_boxplot_linux.png)

Chrome draws slightly less average power in MotionMark (4.86% less), while Firefox draws more in Speedometer (5.43% more) and JetStream 2 (slightly less, −2.41%). This reveals that the energy differences are not primarily driven by power spikes but by how long each browser takes to complete the work.

![Memory Consumption Comparison](img/g5_browser_bench/avg_ram_gb_comparison_boxplot_linux.png)

Firefox consistently uses more RAM across all benchmarks: 5.5% more in MotionMark, 16.8% more in Speedometer, and 10.6% more in JetStream 2. This suggests Firefox's memory model is less efficient on Linux, possibly due to differences in garbage collection tuning or heap fragmentation compared to macOS.

![Duration Comparison](img/g5_browser_bench/duration_sec_comparison_boxplot_linux.png)

Chrome is significantly faster: 1.5% faster in MotionMark, 31% faster in Speedometer, and 74% faster in JetStream 2. These speed differences directly translate to energy savings, since the CPU can return to idle sooner when work completes faster.

![Metric Difference Heatmap](img/g5_browser_bench/metric_difference_heatmap_linux.png)

The heatmap illustrates Chrome's advantage in computation-heavy workloads (deep red in JetStream) and Firefox's modest advantage in graphics (light color in MotionMark). Overall, Firefox tends to draw less power despite some usage spikes in RAM.

#### **Analysis**

The results on Linux expose a larger performance gap between browsers than macOS, and reveal different root causes for each benchmark type.

**Graphics Performance (MotionMark):**
Firefox achieved a 6.3% energy advantage on Linux, comparable to its 7.3% advantage on macOS but markedly better than its 2.0% advantage on Windows. This pattern suggests Firefox's graphics pipeline benefits from more direct hardware access on Unix-like systems (macOS and Linux) compared to Windows's DirectX abstraction layer.

On macOS, Firefox leverages Core Animation and IOSurfaces for GPU-accelerated rendering. On Linux, both browsers likely use OpenGL or Vulkan directly through X11 or Wayland. Firefox's consistent 6–7% advantage across macOS and Linux suggests its compositing strategy is genuinely more efficient for graphics workloads, independent of platform-specific APIs. The minimal advantage on Windows (2%) indicates that DirectX may level the playing field between Gecko and Blink's graphics implementations, or that Windows's scheduler affects graphics performance differently.

Across all platforms, MotionMark is the only benchmark where Firefox is more energy-efficient, which makes it a clear win for users prioritizing graphical responsiveness and battery life during more media-heavy browsing.

**Computation Performance (JetStream 2 and Speedometer):**
On Linux, Chrome is fairly dominant, and notably more than on Windows or macOS. Firefox consumes 70% more energy in JetStream 2 on Linux and completes 74% slower, compared to 52% more energy and 53% slower on Windows, and 65% more energy and 71% slower on macOS. This growing gap across platforms, which is worst on Linux, intermediate on Windows, and second-worst on macOS, suggests that **Linux's environment amplifies V8's compilation advantages over SpiderMonkey**.

Chrome's V8 JavaScript engine uses multi-tier Just-In-Time (JIT) compilation, which is most effective when the CPU scheduler and memory hierarchy align with its optimization strategy. Linux's simpler scheduler and lower-level hardware access may expose these advantages more directly than Windows's abstracted scheduling or macOS's more conservative power management.

In Speedometer, the pattern is similar: Firefox takes 31% longer on Linux (36.5 vs 27.8 seconds), 19% longer on Windows (35.3 vs 29.6 seconds), and 9.8% longer on macOS (36.1 vs 32.9 seconds). The execution gap widens on Linux and Windows but narrows on macOS, suggesting that **macOS's I/O subsystem and event handling is more balanced between browsers**, while Linux and Windows more heavily penalize SpiderMonkey's simpler JIT strategy. This directly causes 39% more energy consumption on Linux, 39.6% on Windows, and 20% on macOS for Firefox in Speedometer.

The pattern strongly suggests a **compiler optimization gap that worsens under less-abstracted operating systems**.

**Memory Consumption:**
Firefox uses 5–17% more RAM across all benchmarks on Linux, compared to 1–4% on Windows and less than 2% on macOS. The growing  memory footprint on Linux suggests that:
- Firefox's garbage collection is less aggressively tuned for Linux than for macOS
- Linux system allocators (glibc) may fragment differently than macOS allocators
- Firefox's layer compositing overhead is highest on Linux due to direct graphics API usage
- Windows's memory management (intermediate abstraction) sits between Linux's and macOS's efficiency

The fact that macOS shows minimal RAM differences suggests that Firefox is well-optimized for macOS's memory model, moderately optimized for Windows, and least optimized for Linux. This supports the hypothesis that Firefox development prioritizes macOS compatibility.

**Why the Differences Are Larger on Linux Than Windows and macOS:**

Several factors explain why the Chrome/Firefox gap is widest on Linux, intermediate on Windows, and smallest on macOS:

1. **Graphics APIs & Abstraction Levels**: 
   - macOS: Core Animation (deeply integrated, heavily optimized for both browsers)
   - Windows: DirectX (medium abstraction, somewhat balanced between engines)
   - Linux: X11/Wayland + OpenGL/Vulkan (fragmented, lowest-level access)
   
   Linux's lower-level graphics APIs expose browser engine differences more directly, allowing V8's optimizations to shine while revealing SpiderMonkey's weaker implementation.

2. **V8 Optimization Priorities**:
   Google with Chrome has invested heavily in V8 optimizations for Linux servers (Node.js, Deno, cloud infrastructure) and Linux desktops. Whereas Firefox's SpiderMonkey is primarily tuned for interactive browsing on Windows and macOS, with Linux as a secondary concern. Windows benefits from better Windows-specific tuning, while macOS's power management somewhat masks SpiderMonkey's weaknesses.

3. **CPU Scheduler Alignment**:
   - Linux: Simple, scheduler-centric design where CPU affinity and cache locality directly impact performance. Chrome's threading model aligns naturally with this, giving it measurable advantages during JIT compilation.
   - Windows: Abstract scheduling layer (IOCP, thread pool) that mediates browser behavior, somewhat leveling the field.
   - macOS: Power-aware scheduler that can throttle aggressive workloads, reducing peak performance differences.

4. **Memory & System Library Integration**:
   - Firefox on macOS links to tightly integrated frameworks, benefiting from optimized memory management.
   - Firefox on Windows uses more abstracted system calls, reducing but not eliminating inefficiency.
   - Firefox on Linux links against system libraries (glibc, GTK, fontconfig) with variable availability and performance, leading to the highest overhead.
   - Chrome on all platforms bundles dependencies, ensuring consistent behavior regardless of system configuration.

**Cross-Platform Summary:**
- **MotionMark (Graphics)**: Firefox 7% better on macOS, 6% better on Linux, 2% better on Windows. -> Unix systems favor Firefox; Windows narrows the gap.
- **JetStream 2 (Computation)**: Chrome 65% better on macOS, 52% better on Windows, 70% better on Linux. -> Linux amplifies Chrome's advantages the most.
- **Speedometer (Interactivity)**: Chrome 20% better on macOS, 40% better on Windows and Linux. -> Windows and Linux both heavily penalize Firefox, with computation becoming the bottleneck.

**Implications and Recommendations:**

For **Linux users**, Chrome is the clear choice for energy efficiency and responsiveness, especially for computational and interactive workloads. The 70% energy penalty in JetStream 2 and 31% slowdown in Speedometer are substantial and will be felt in real-world performance. Firefox's 6% graphics advantage is marginal and unlikely to offset these disadvantages for typical web browsing.

For **power-constrained environments** (laptops, embedded systems): If Linux is the platform, Chrome is strongly preferred. The energy savings in computation-heavy tasks, with 70% less energy in JetStream 2, translate directly to longer battery life.

For **workload-specific choice**: Only if your browsing is *exclusively* graphics-focused (e.g., media editing, 3D visualization) should you consider Firefox on Linux. Otherwise, Chrome is objectively more efficient across all major workload categories on Linux.

For **comparison to other platforms**: Linux users experience the worst Firefox performance relative to Chrome across all three platforms. This suggests that browser developers (especially Mozilla) deprioritize Linux optimization compared to macOS and Windows, or that Linux's lower-level system access naturally exposes engine differences that macOS's abstraction layers and Windows's balancing mechanisms reduce.

---

### **Conclusion**
To be added

**Our Code**

Our code for the replication of the experiments is available at [https://github.com/SSE-Group-5/browser-bench](https://github.com/SSE-Group-5/browser-bench)
