---
author: Leonidas Hadjiyiannis, Ivan Ivanov, Noky Soekarman, Yuchen Sun
group_number: 21
title: "Youtube Energy Consumption on Different Browsers"
image: "img/gX_template/project_cover.png"
date: 12/02/2026
summary: For our project 1 we will be analyzing the energy consumption of the CPU when running the same youtube short on two different browsers (firfox & google chrome) on ubuntu24.04.3LTS using AMD Ryzen 7 4800H
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Youtube Energy Consumption on Different Browsers

## **Introduction**

### Why Energy Efficiency Matters in Browsing?
In the modern digital era, the web browser has evolved from a simple tool into the fundamental infrastructure of our daily lives. Whether for professional productivity or personal leisure, the browser is often the most frequently used and long-running application on any system. In Europe, the prevalence and active usage time of browsers have reached staggering levels, making browser energy consumption a critical factor in digital sustainability.

Because of this massive reach, even a minor improvement in a browser's energy efficiency can yield a significant global impact when multiplied by billions of users. For developers and researchers alike, the pursuit of "Green Software" is not just about extending laptop battery life; it is a vital step toward reducing the carbon footprint left by our digital activities.

### The Hidden Cost of Video Streaming
Among all browsing activities, video playback is arguably the most power-hungry. As the world’s most popular video platform, **YouTube’s** influence extends far beyond entertainment, serving as a global hub for education, skill-sharing, and information exchange. Its massive user base means that every second, millions of pixels are being rendered across diverse devices worldwide.

However, the high-quality decoding and rendering behind these streams carry a hidden environmental cost. Since video playback is one of the most intensive tasks a user performs in a browser, investigating the energy efficiency differences across different browsers under the same YouTube workload is of high practical and scientific value.

### To GPU or Not to GPU?
To optimize video performance, modern browsers utilize "Hardware Acceleration." From a technical perspective, this feature is designed to offload the heavy lifting of video decoding and rendering from the General Purpose Processor (CPU) to a specialized Graphics Processing Unit (GPU).

Theoretically, because GPUs are more efficient at handling parallel computations and dedicated codec logic (such as VP9 or AV1 formats), this should lower the total system energy consumption. However, does the activation of the GPU introduce additional driver overhead, memory copy costs, or scheduling latencies? In a complex web environment like YouTube, whether "Hardware Acceleration" truly achieves a win-win for both performance and energy saving remains a subject of ongoing debate and empirical investigation.

### Our Mission
This study aims to provide empirical evidence on how browser environments truly influence the energy efficiency of video playback. By conducting a comparative analysis of three major browsers—Chrome, Microsoft Edge, and Firefox—we explore the following core questions:

The Reality of Hardware Acceleration: Analyzing the specific impact of enabling vs. disabling GPU acceleration on Total Energy (J) and the Energy-Delay Product (EDP) across four specific YouTube Shorts.

Cross-Kernel Efficiency: Investigating the resource allocation strategies (CPU vs. GPU) between Chromium-based browsers (Chrome, Edge) and the independent Gecko engine (Firefox).

Performance vs. Energy Trade-offs: Verifying whether hardware acceleration increases the system’s electrical burden without providing a significant gain in execution efficiency (Runtime).

Through rigorous automated testing and statistical analysis, we aim to provide clearer configuration recommendations for users and data-driven insights for the development of Green Software.

## **Methodology**

### Experimental Subjects and Variables
#### Browser Selection
This experiment selected three representative web browsers: Google Chrome, Microsoft Edge, and Mozilla Firefox. The selection was based on the following criteria:

Kernel Diversity: Chrome and Edge are based on the Chromium engine, while Firefox utilizes the independent Gecko engine. Comparing different engines under identical workloads provides significant scientific insight into energy optimization strategies.

Market Share: These three browsers account for the vast majority of desktop users globally.

Vendor-Specific Optimizations: Since Edge is deeply integrated with the Windows OS and Chrome is the most popular cross-platform browser, comparing them allows us to observe how different vendors optimize hardware acceleration.

#### Hardware Acceleration States
For each browser, we tested two distinct configurations:

Hardware Acceleration Enabled: The default browser state where tasks are offloaded to the GPU.

Hardware Acceleration Disabled: Forced via Selenium startup arguments (e.g., --disable-gpu and --disable-software-rasterizer), requiring the CPU to handle all video decoding and rendering tasks.
This comparison aims to quantify the actual energy efficiency gains (or losses) of hardware offloading in video playback scenarios.

#### YouTube Workload
We manually selected four YouTube Shorts, each with an average duration of approximately 30 seconds. These videos were organized into a dedicated playlist and played sequentially during each experimental run. Shorts were chosen because their compact nature and frequent rendering changes better reflect the dynamic energy fluctuations of modern web video content.

### Environmental Control and Fairness
#### Hardware Information


#### Zen Mode


#### Freeze Settings


#### Baseline Collection
Baseline energy consumption represents the background power usage of the system in an idle state with the browser open. Subtracting the baseline is essential to isolate the specific energy cost of "video playback" from the energy required to keep the system and browser running.

[How did we collect the baseline data?]

### Measurement Infrastructure
#### Automation: Selenium
This experiment utilized Selenium WebDriver for full automation. Compared to manual operation, the key advantages include:

Precise Timing: Ensures that video playback duration is exactly consistent across every run.

Elimination of Human Error: Prevents additional energy spikes caused by unintended mouse movements, clicks, or operational delays.

Fairness: Every browser loads the same set of URLs through identical script logic.

#### Energy Monitoring: Energybridge
We utilized Energybridge for hardware-level data acquisition.

Integration: Energybridge was launched and terminated in synchronization with the Selenium script via a master loop script (.ps1 or .sh).

Data Source: The tool reads directly from hardware interfaces (such as Intel RAPL) to capture CPU energy counters and instantaneous GPU power draw.

### Data Acquisition Process
#### Sampling Strategy and the "N+2" Principle
For each configuration (e.g., Chrome with GPU enabled), we performed 32 independent runs.

**Why 32 runs?** Hardware energy consumption is subject to unavoidable fluctuations caused by thermal changes and minor background system activities.

**Warmup Logic:** We primarily analyze the data from 30 of these runs. The first two runs are treated as "warmup runs" to allow the hardware to reach a stable operating temperature and ensure all browser components are fully loaded, preventing initial spikes from skewing the statistical accuracy.

#### Data Structure
The resulting CSV files contain several key metrics used for analysis:
| Metric | Unit | Description | Importance |
| :--- | :--- | :--- | :--- |
| `Time` | ms | Absolute system time | Used for synchronizing data points. |
| `Delta` | ms | Time difference between samples | Validates the stability of the sampling frequency. |
| `CPU_ENERGY (J)` | Joules | **Core Metric**. Cumulative CPU energy | The primary data for calculating CPU power consumption. |
| `GPU0_POWER (mWatts)` | mWatts | **Core Metric**. Instantaneous GPU power | Must be integrated over time to calculate total GPU energy. |
| `PACKAGE_TEMPERATURE` | °C | Hardware temperature | Used to monitor for potential thermal throttling. |

## **Result**

## **Discussion**

## **Limitations and future work**

## **Replication Package**

## **Conclusion**