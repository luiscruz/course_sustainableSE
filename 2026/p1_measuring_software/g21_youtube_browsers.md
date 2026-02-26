---
author: Leonidas Hadjiyiannis, Ivan Ivanov, Noky Soekarman, Yuchen Sun
group_number: 21
title: "Youtube Energy Consumption on Different Browsers with or without Hardware Acceleration"
image: "img/g21/cover.png"
date: 12/02/2026
summary: In this project, we analyze the power consumption of YouTube video playback across three browsers (Chrome, Edge, and Firefox) on Windows 11 using an AMD Ryzen 7 4800H system. We compare configurations with hardware acceleration enabled and disabled, using average total power (W) as the primary metric. The goal is to evaluate whether hardware acceleration improves energy efficiency during video streaming.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Youtube Energy Consumption on Different Browsers with or without Hardware Acceleration

## **Introduction**

### Why Energy Efficiency Matters in Browsing?
In the modern digital era, the web browser has evolved from a simple tool into the fundamental infrastructure of our daily lives. Whether for professional productivity or personal leisure, the browser is often the most frequently used and long-running application on any system. In Europe, the prevalence and active usage time of browsers have reached staggering levels, making browser energy consumption a critical factor in digital sustainability.

Because of this massive reach, even a minor improvement in a browser's energy efficiency can yield a significant global impact when multiplied by billions of users. For developers and researchers alike, the pursuit of "Green Software" is not just about extending laptop battery life, it is a vital step toward reducing the carbon footprint left by our digital activities.

### The Hidden Cost of Video Streaming
Among all browsing activities, video playback is arguably the most power hungry. As the world’s most popular video platform, **YouTube’s** influence extends far beyond entertainment, serving as a global hub for education, skill sharing, and information exchange. Its massive user base means that every second, millions of pixels are being rendered across diverse devices worldwide.

However, the high-quality decoding and rendering behind these streams carry a hidden environmental cost. Since video playback is one of the most intensive tasks a user performs in a browser, investigating the energy efficiency differences across different browsers under the same YouTube workload is of high practical and scientific value.

### To GPU or Not to GPU?
To optimize video performance, modern browsers utilize "Hardware Acceleration". From a technical perspective, this feature is designed to offload the heavy lifting of video decoding and rendering from the Central Processing Unit (CPU) to a specialized Graphics Processing Unit (GPU).

Theoretically, because GPUs are more efficient at handling parallel computations and dedicated codec logic (such as VP9 or AV1 formats), this should lower the total system energy consumption. However, does the activation of the GPU introduce additional driver overhead, memory copy costs, or scheduling latencies? In a complex web environment like YouTube, whether "Hardware Acceleration" truly achieves a win-win for both performance and energy saving remains a subject of ongoing debate and empirical investigation.

### Our Mission
This study aims to provide empirical evidence on how browser environments truly influence the energy efficiency of video playback. By conducting a comparative analysis of three major browsers (Chrome, Microsoft Edge, and Firefox) we explore the following core question:

The Reality of Hardware Acceleration: Analyzing the specific impact of enabling vs. disabling GPU acceleration on Average Total Power (W), Average CPU Power (W) and Average GPU Power (W) across four specific YouTube Shorts.

## **Methodology**

### 1. Experimental Subjects and Variables
#### 1.1 Browser Selection
This experiment selected three representative web browsers: Google Chrome, Microsoft Edge, and Firefox. The selection was based on the following criteria:

Kernel Diversity: Chrome and Edge are based on the Chromium engine, while Firefox utilizes the independent Gecko engine. Comparing different engines under identical workloads provides significant scientific insight into energy optimization strategies.

Market Share: These three browsers account for the vast majority of desktop users globally.

Vendor Specific Optimizations: Since Edge is deeply integrated with the Windows OS and Chrome is the most popular cross platform browser, comparing them allows us to observe how different vendors optimize hardware acceleration.

#### 1.2 Hardware Acceleration States
For each browser, we tested two distinct configurations:

Hardware Acceleration Enabled: The default browser state where tasks are offloaded to the GPU.

Hardware Acceleration Disabled: Forced via Selenium startup arguments (e.g., --disable-gpu and --disable-software-rasterizer), requiring the CPU to handle all video decoding and rendering tasks.
This comparison aims to quantify the actual energy efficiency gains (or losses) of hardware offloading in video playback scenarios.

#### 1.3 YouTube Workload
We manually selected four YouTube Shorts, each with an average duration of approximately 30 seconds. These videos were organized into a dedicated playlist and played sequentially during each experimental run. Shorts were chosen because their compact nature and frequent rendering changes better reflect the dynamic energy fluctuations of modern web video content. The youtube videos that we used can be found in [this](https://www.youtube.com/watch?v=Ay8lynMZ4mE&list=PLmSezx7vjyA4vpDfHBdetncvcAlNc2IXs&pp=sAgC) playlist, because the YouTube shorts are added to a playlist, they are played in the normal YouTube player rather than the short player. Since the shorts are played in the normal environment, we could also change the resolution. The resolution of all the shorts were all set at 1080p.

### 2. Environmental Control and Fairness
#### 2.1 Hardware Information
The hardware that was used for the experiment is a Windows 11 laptop equipped with an AMD Ryzen 7 4800H CPU and an NVidia GeForce GTX 1650ti GPU.


#### 2.2 Zen Mode
The experiment was conducted with no other (background) applications running other than the ones strictly necessary. The only things running were: A powershell window which was used to launch the automation script, python for running the script which launched a browser with a specific config, energibridge for collecting the energy data, and the browser itself.


#### 2.3 Freeze Settings
To ensure that every test run was conducted under as close as possible to identical conditions, we put the laptop to max brightness, made sure it did not turn off the screen or itself after a certain amount of time, and made sure that the laptop was plugged into both power and ethernet during the entire duration of the experiment. We also tried to keep the room temperature at a constant 18 degrees Celsius to minimize the influence of thermal fluctuations on energy consumption. Finally, all the browsers were set to use the high performance NVidia GPU rather than the integrated one from the CPU.


### 3. Measurement Infrastructure
#### 3.1 Automation: Selenium
This experiment utilized [Selenium](https://www.selenium.dev/) WebDriver for full automation. Compared to manual operation, the key advantages include:

- **Precise Timing:** Ensures that video playback duration is exactly consistent across every run.

- **Elimination of Human Error:** Prevents additional energy spikes caused by unintended mouse movements, clicks, or operational delays.

- **Fairness:** Every browser loads the same set of URLs through identical script logic.

#### 3.2 Energy Monitoring: Energibridge
We utilized [Energibridge](https://github.com/tdurieux/energibridge) for hardware level data acquisition.

**Integration:** Energibridge was launched and terminated in synchronization with the Selenium script via a master loop script (.ps1 or .sh).

**Data Source:** The tool reads directly from hardware interfaces (such as Intel RAPL) to capture CPU energy counters and instantaneous GPU power draw.

### 4. Data Acquisition Process
#### 4.1 Sampling Strategy and the "N+2" Principle
For each configuration (e.g., Chrome with GPU enabled), we performed 32 independent runs.

**Why 32 runs?** Hardware energy consumption is subject to unavoidable fluctuations caused by thermal changes and minor background system activities.

**Warmup Logic:** We primarily analyze the data from 30 of these runs. The first two runs are treated as "warmup runs" to allow the hardware to reach a stable operating temperature and ensure all browser components are fully loaded, preventing initial spikes from skewing the statistical accuracy.

#### 4.2 Data Structure
The resulting CSV files contain several key metrics used for analysis:
| Metric | Unit | Description | Importance |
| :--- | :--- | :--- | :--- |
| `Time` | ms | Absolute system time | Used for synchronizing data points. |
| `Delta` | ms | Time difference between samples | Validates the stability of the sampling frequency. |
| `CPU_ENERGY` | Joules | Cumulative CPU energy | The primary data for calculating CPU power consumption. |
| `GPU0_POWER` | mWatts | Instantaneous GPU power | Must be integrated over time to calculate total GPU energy. |

## **Result**
Since we are comparing video streaming with a number of configurations, we are going to compare the average wattage consumed per configuration. This is done because video streaming is a continous load on a system rather than some task which eventually reaches the end.

Because we are checking whether ofloading some work to the GPU, we will present three plots, one where the CPU and GPU wattage is combined, and two that show the average wattage per component.

All the plots are acompanied by a table stating some statistical numbers. Some of these numbers compare hardware acceleration on vs off, the way this should be interpreted is that the numbers are for the "on" configs relative to the "off" configs. So when it states that there is 34 percent difference, that means the "on" config scored 34 percent higher on that metric compared to the "off" config.

### Data Cleaning and Outlier Handling
Before performing the core analysis, we ensured the integrity of the dataset by removing "warmup" runs and identifying anomalies. We followed the "N+2" principle, discarding the first two runs of every configuration to allow the hardware to reach a stable thermal state.

#### Special Finding
One Firefox run with hardware acceleration disabled (run 31) was identified as faulty, due to the fact that it produced unrealistically low energy consumption and only had a runtime of 10 seconds. As this run does not represent a valid experimental measurement, it was excluded from all subsequent analyses and visualizations.

---

The final distribution of valid samples is shown below:

| Browser | Hardware Acceleration | Sample Count (n) |
| :--- | :--- | :--- |
| Chrome | Off | 30 |
| Chrome | On | 30 |
| Edge | Off | 30 |
| Edge | On | 30 |
| Firefox | Off | 29 |
| Firefox | On | 30 |

*Table 1: Final Sample Counts per Configuration*

### Average Total Power Consumption

![Average Total Power(W)](./img/g21/Average_Total_Power.png)

In the above violin plot you can see the average power consumption in wattage per configuration for the CPU and GPU combined. Here you can see that for all browsers the power consumption is higher when hardware acceleration is turned on.

|   | browser | metric              | # runs with GPU on | # runs with GPU off | test          | p_value       | mean_off  | mean_on   | pct_change_on_vs_off | effect_size | effect_size_label     |
|---|---------|--------------------|-----------|----------|--------------|---------------|-----------|-----------|----------------------|-------------|-----------------------|
| 0 | chrome  | avg_total_power_w  | 30        | 30       | Mann–Whitney | 3.019859e-11  | 31.944582 | 42.889812 | 34.263181            | 1.0         | CLES P(on > off)      |
| 1 | edge    | avg_total_power_w  | 30        | 30       | Mann–Whitney | 3.019859e-11  | 31.959125 | 41.972643 | 31.332268            | 1.0         | CLES P(on > off)      |
| 2 | firefox | avg_total_power_w  | 29        | 30       | Mann–Whitney | 4.461750e-11  | 31.269099 | 42.086639 | 34.594986            | 1.0         | CLES P(on > off)      |

*Table 2: Statistical Comparison of Total Power (HW On vs. HW Off)*

### Average CPU Power Consumption

![Average CPU Power Consuption(W)](./img/g21/Average_CPU_Power.png)

The above violin plot shows the average power consumption in wattage per configuration for just the CPU. As you might notice, they are much closer together than in the previous plot. Yet there is still a small reduction in power consumption from hardware acceleration off to on. This can be simply explained, the CPU is giving some work to the GPU rather than doing it itself.

|   | browser | metric            | # runs with GPU on | # runs with GPU off | test          | p_value       | mean_off  | mean_on   | pct_change_on_vs_off | effect_size | effect_size_label |
|---|---------|------------------|-----------|----------|--------------|---------------|-----------|-----------|----------------------|-------------|-------------------|
| 0 | chrome  | avg_cpu_power_w  | 30        | 30       | Mann–Whitney | 8.890991e-10  | 13.451759 | 12.427455 | -7.614645            | 0.038889    | CLES P(on > off)  |
| 1 | edge    | avg_cpu_power_w  | 30        | 30       | Mann–Whitney | 2.601511e-08  | 13.476417 | 12.473504 | -7.441979            | 0.081111    | CLES P(on > off)  |
| 2 | firefox | avg_cpu_power_w  | 29        | 30       | Mann–Whitney | 8.615805e-01  | 11.617181 | 11.566381 | -0.437286            | 0.513793    | CLES P(on > off)  |

*Table 3: Statistical Comparison of CPU Power (HW On vs. HW Off)*

### Average GPU Power Consumption

![Average GPU Power(W)](./img/g21/Average_GPU_Power.png)

This final violin plot shows the average power consumpiton in wattage per configuration for just the GPU. Here we can see where the big difference comes from in the first plot. When hardware acceleration is turned off, all the browsers have almost the same GPU power consumption. This makes sense, because the browsers were the only process that were utilizing the high performance GPU during the experiments. So when the hardware acceleration is turned off, the GPU sits idle doing nothing. Only when the hardware acceleration is turned on, the GPU starts processing the video decoding workload.

|   | browser | metric            | # runs with GPU on | # runs with GPU off | test          | p_value       | mean_off  | mean_on   | pct_change_on_vs_off | effect_size | effect_size_label |
|---|---------|------------------|-----------|----------|--------------|---------------|-----------|-----------|----------------------|-------------|-------------------|
| 0 | chrome  | avg_gpu_power_w  | 30        | 30       | Mann–Whitney | 3.019859e-11  | 18.492823 | 30.462356 | 64.725293            | 1.0         | CLES P(on > off)  |
| 1 | edge    | avg_gpu_power_w  | 30        | 30       | Mann–Whitney | 3.019859e-11  | 18.482708 | 29.499139 | 59.603987            | 1.0         | CLES P(on > off)  |
| 2 | firefox | avg_gpu_power_w  | 29        | 30       | Mann–Whitney | 4.461750e-11  | 19.651918 | 30.520258 | 55.304224            | 1.0         | CLES P(on > off)  |

*Table 4: Statistical Comparison of GPU Power (HW On vs. HW Off)*

### Statistical Significance
To ensure our findings were robust, we conducted normality tests followed by non-parametric comparisons.

#### Special Finding
It can be observed from the results of the Shapiro–Wilk test that several configurations deviate significantly from normality (p < 0.05). Therefore, non-parametric statistical tests are used for subsequent comparisons.

For all three browsers, enabling hardware acceleration leads to a statistically significant increase in average total power consumption (p < 0.05, Mann–Whitney test). The mean power consumption increases by approximately 34% for Chrome, 31% for Edge, and 35% for Firefox. This indicates that hardware acceleration substantially increases power usage during video playback for this workload.

---

| Metric | Test Type | Findings |
| :--- | :--- | :--- |
| Normality | Shapiro-Wilk | Most groups failed (p < 0.05), requiring non-parametric tests. |
| Significance | Mann-Whitney U | All power increases were statistically significant (p < 0.05). |
| Effect Size | CLES | Very high probability that HW-On consumes more energy than HW-Off. |

*Table 5: Summary of Statistical Tests*

## **Discussion**

The results of this experiment challenge the common assumption that hardware acceleration is inherently more energy efficient. GPUs contain dedicated video decoding hardware that is generally considered more efficient than general purpose CPU decoding. However, our system wide power measurements show a different outcome for this workload.

Although enabling hardware acceleration slightly reduces CPU power consumption, it significantly increases GPU power usage. The increase in GPU power more than offsets the CPU savings, resulting in an overall rise in total system power consumption of approximately 30–35% across all browsers.

One possible explanation is the system level overhead introduced by offloading work to the GPU. In a browser environment, video decoding is not an isolated operation; it involves coordination between CPU processes, GPU drivers, memory transfers, and rendering pipelines. This additional cross component activity may introduce overhead that reduces the theoretical efficiency benefits of GPU decoding, particularly for short form or lightweight video streams.

From a Green Software perspective, these findings have practical implications. Hardware acceleration is enabled by default in modern browsers under the assumption that it improves performance and efficiency. However, for short video streaming workloads, our results indicate that this default configuration increases power consumption substantially. For laptop users, a 30–35% increase in power draw during frequent short form video playback may translate directly into reduced battery life and higher cumulative energy usage over time.

These findings suggest that the energy impact of hardware acceleration may depend on workload characteristics such as video duration and complexity. However, further experiments with longer videos would be required to evaluate this hypothesis.

## **Limitations and future work**
While our study gives us a clear look at how hardware acceleration hits the different computer components during YouTube Shorts, it’s important to remember that the type of video plays a massive role. Since we only focused on 30-second clips, at a resolution of 1080p, the GPU might not have hit it's crossover point where it is more efficient than the CPU. If users were watching content that was more decode intensive such as 4K or even 8K video, the GPU decoding might be more efficient than the CPU decoding. Even different video codecs could make a difference.

Another thing to keep in mind is that all our data comes from just one specific computer setup. In the real world, the difference between an integrated graphics chip and a beefy dedicated graphics card is huge. Everything from the hardware architecture to your power settings or even your driver version can change how much energy gets used. Future tests across a variety of computers would definitely help us see a broader picture. Also, browsers aren't always transparent about which video "language" or codec, they choose. One browser might pick VP9 while another goes for AV1, and that choice alone could explain some of the energy gaps we saw.

Finally, let’s talk about the "noise" of modern computers. Even though we tried to stay in "Zen Mode" by killing unnecessary apps, operating systems are always busy behind the scenes. There’s almost always some background task popping up that has nothing to do with the browser but still influences the power consumption. We used a strict 32-run strategy and tossed out the "warmup" runs to smooth things out, but at the end of the day, measuring energy in a real-world environment instead of a sterile lab is always going to have its limits.

## **Conclusion**
This experiment evaluated the power consumption of Chrome, Microsoft Edge, and Firefox during YouTube Shorts playback, with and without hardware acceleration enabled. The primary metric used in this analysis was average total power (W), as video playback represents a continuous workload where power consumption is more informative than runtime based metrics.

Our results show a clear and statistically significant pattern: enabling hardware acceleration increases total system power consumption across all browsers. Specifically, average power increases by approximately:

- 34% in Chrome

- 31% in Edge

- 35% in Firefox

Although hardware acceleration slightly reduces CPU power consumption, it dramatically increases GPU power usage (by over 55% across browsers). The GPU increase more than offsets the CPU savings, resulting in substantially higher overall power draw.

When hardware acceleration is disabled, Firefox exhibits the lowest average power consumption. However, this advantage largely disappears once GPU acceleration is enabled, as all browsers show similarly elevated power usage.

Hardware acceleration is enabled by default in modern browsers and is generally assumed to improve efficiency by offloading work from the CPU to the GPU. However, for the short form video workload tested in this experiment, this assumption does not hold. Instead, hardware acceleration significantly increases power consumption.

These findings highlight that energy efficiency is workload dependent. Neither hardware acceleration nor browser choice should be assumed to be energy efficient by default. In practice, this means that energy efficiency depends on the workload, and configurations should be assessed in the context in which they are used.

## Link to the Code Repository
https://github.com/MysticL2/Sustainable-Software-Engineering-Group-21-Code