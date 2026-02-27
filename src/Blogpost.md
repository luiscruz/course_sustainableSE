# Is Google Meet or Microsoft Teams Greener? Measuring the Energy Cost of Video Calls

**Course:** Sustainable Software Engineering — TU Delft, 2026  
**Authors:** Ocean Wang, Erkin Başol, Yasar Kocdas, Alexia Neatu
**Replication package:** GH link

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Background](#2-background)
3. [Experimental Design](#3-experimental-design)
4. [Threats to Validity](#4-threats-to-validity)
5. [Results](#5-results)
6. [Discussion](#6-discussion)
7. [Conclusion](#7-conclusion)
8. [Replication](#8-replication)

---

## 1. Introduction

Pick any medium-sized company. Its employees probably spend two to three hours a day on video calls. Multiply that by the number of employees, and then by the number of companies doing the same thing, and you have a workload that runs continuously, at massive scale, on hardware that people rarely think of as having an energy cost.

The choice of platform is usually made once, at the IT level, and then forgotten. But Google Meet and Microsoft Teams are not the same product under the hood. They make different engineering decisions about how to encode video, how to manage the call state in the browser, and how much JavaScript runs while you sit in a meeting. Those decisions affect how hard your CPU works. A harder CPU draws more power. More power, over enough users and enough hours, adds up.

Nobody seems to have measured whether this difference is real, or how large it is. That is what this study does. We ran 60 automated, hardware-measured experiments, 30 per platform, and recorded the energy consumed by a single browser participant in a standard two-minute call. Our research question is simple: **which platform costs more energy per call, and by how much?**

---

## 2. Background

### 2.1 Software Energy Measurement

The energy a piece of software consumes depends on which hardware resources it exercises and for how long. For a browser-based video call the main contributors are CPU load from video encoding and decoding, JavaScript execution, and DOM rendering, along with network I/O and memory bandwidth. CPU is typically the largest contributor.

Measuring this accurately is harder than it sounds. The obvious approach is to estimate from CPU utilisation: multiply CPU percentage by the chip's rated power draw (TDP) and by time. This is unreliable because it ignores frequency scaling, thermal states, and the fact that not all CPU work draws equal power. Hardware power sensors are the better option. They report what the chip is actually drawing, not what a model predicts it should draw.

### 2.2 Prior Work on Video Call Energy

The closest study to ours is Wattenbach et al. [5], published at MOBILESoft 2022. They compared Google Meet and Zoom on Android using an automated experiment with 20 runs per treatment, measuring energy via Android's Batterystats profiler. Their main finding was that Zoom consumed about 4% less energy than Meet on average, though the difference was statistically significant only at a medium effect size (Cliff's delta = −0.344). They also found that camera use had by far the largest impact on energy, increasing consumption by over 274% compared to a camera-off call, while microphone use had negligible effect.

Their work is directly relevant to ours but leaves two gaps. First, it targets Android mobile apps, not desktop browsers, and mobile energy dynamics differ from laptop CPU workloads. Second, it does not include Microsoft Teams. Our study fills both gaps: we measure browser-based sessions on a desktop machine and compare Meet against Teams rather than Zoom.

One methodological difference is worth noting. Wattenbach et al. used Batterystats, which is a software-based energy estimator. They acknowledge this is less precise than hardware measurement. We use [EnergiBridge](https://github.com/tdurieux/EnergiBridge), which reads directly from hardware power sensors, giving us more accurate absolute figures.

### 2.3 EnergiBridge

EnergiBridge [6] is a cross-platform energy measurement tool developed by Thomas Durieux that reads power sensors directly from the hardware. On Apple Silicon it reads total system power via Apple's SMC through `powermetrics`. On Intel chips and Linux it reads CPU package and DRAM power via Intel's RAPL interface. On Windows it uses LibreHardwareMonitor.

EnergiBridge samples at up to 5 Hz and produces both a time-series of instantaneous power in Watts and a total energy figure in Joules. We use Joules as our primary metric because it combines power draw and time: a platform that draws slightly more watts but for a shorter active period could end up using less total energy than one that draws less but stays busy longer.

### 2.4 Why These Two Platforms Might Differ

Both Google Meet and Microsoft Teams (specifically the consumer `teams.live.com` version) run inside Chrome. They share the same browser runtime, the same JavaScript engine, and the same WebRTC APIs for peer-to-peer media. On the surface this makes them look equivalent. They are not.

Google Meet is a Google product running inside a Google browser. Google has direct influence over both VP9 codec integration and Chrome's WebRTC implementation, and Meet is built to take advantage of that. Its UI is comparatively lean: a call in progress does not do much beyond rendering video tiles and a control bar.

Teams is built on a heavier frontend stack. The consumer web client wraps a React-based framework and carries more JavaScript than Meet. A larger JS bundle means more parsing, more execution, and more ongoing framework overhead during the call. Teams also handles the pre-join flow differently: guests wait in a lobby until admitted, which means the browser is running call-related code before the call has technically started.

The prior mobile findings from Wattenbach et al. showed Meet consuming more energy than Zoom. Whether that pattern holds when comparing Meet against Teams on desktop is an open question, but the architectural differences above give us a prior expectation: **we expect Teams to consume more energy per session than Meet.** The question is whether the difference is large enough to be meaningful, or whether it gets lost in measurement noise.

---

## 3. Experimental Design

### 3.1 Overview

We measure the client-side energy consumed by a single browser participant in a 120-second call, on each platform, repeated 30 times in randomised order. 

### 3.2 Experiment Setting
For each platform, we deployed five additional participant bots using an automation script to better
simulate a real-life environment. To avoid interfering with the client-side machine used for measurements, the bots ran on a separate machine.
The number of bots per platform was determined by the hardware capacity of the bot-hosting machine.
### 3.2 Browser Automation

We use Selenium WebDriver to control real Chrome browser instances.
Human interaction introduces timing variability that automation removes.
Each bot joins the meeting, waits exactly 120 seconds, and leaves.
Between runs, the temporary Chrome profile is deleted so no cached state carries over.

Chrome is configured with `--use-fake-device-for-media-stream`, which supplies a synthetic camera
and microphone signal rather than a real one. 
Both platforms receive an identical media input, 
so any difference in codec workload comes from how each platform processes that input,
not from what was in the video.
### 3.3 Energy Measurement

**EnergiBridge** runs as a background process from just before the bot joins to just after it leaves. It writes a high-frequency power time-series to CSV and prints total energy consumed when it exits.

Alongside it, a Python thread samples **`psutil`** every second for CPU%, memory, and network bytes in both directions. Together, these give us hardware-level power data at 5 Hz and a complete system-level view at 1 Hz.

### 3.4 Controls

**Randomised run order.** The 60 experiments were split into four batches (8, 9, 9, and 4 runs) due to the one-hour session limit of Google Meet. Before each batch, the full sequence was shuffled to distribute time-of-day effects, background activity, and thermal drift evenly across platforms.

**Cooldown between runs.** A 60-second pause was introduced between runs to allow the CPU to cool down. Between batches, reconnecting to Google Meet added an additional ~4-minute delay. All experiments were conducted within a single four-hour window.

**Isolated Chrome profiles.** Each run used a fresh Chrome profile that was deleted afterwards to prevent state carryover.

**Zen Mode.** All non-essential applications and background processes were closed, external devices disconnected, and the laptop remained plugged in at 100% battery. No interaction occurred during execution, and brightness remained constant.

**System warm-up.** A Fibonacci script was executed for five minutes before the first run to stabilise system temperature.

**Environment control.** Room temperature was kept constant, with windows closed.

**Consistent meeting setup.** A human host created calls on Google Meet and Microsoft Teams. The host and four bots remained connected throughout; only the experimental bot joined and left per run, ensuring consistent meeting conditions.
### 3.5 Experimental Matrix

| Parameter | Value |
|---|---|
| Platforms | Google Meet, Microsoft Teams |
| Participants per call | 1 experiment bot + 5 additional participants (1 host and 4 bots)|
| Call duration | 120 seconds |
| Repetitions per platform | 30 |
| Total runs | 60 |
| Cooldown between runs | 60 seconds |
| Browser | Google Chrome (latest), visible mode |
| Media stream | Synthetic (fake device) |
| Run order | Randomised  |
| Energy tool | EnergiBridge |
| OS / Hardware | [macOS 26.3, Apple M4, 16 GB RAM] |

---

## 4. Threats to Validity

**Fake media streams are a lower bound.** A synthetic camera feed produces a simple, static signal. A real webcam with motion and lighting variation requires more codec work from both platforms. Our results underestimate real-world consumption, and the gap between platforms could be larger or smaller under realistic conditions.

**Network I/O is system-wide.** `psutil.net_io_counters()` captures all traffic on the machine, not just Chrome's. Background OS processes can inflate the figures. We closed non-essential applications before running, but cannot eliminate this entirely.

**Single hardware configuration.** All measurements were taken on one machine. Absolute energy figures will differ on different hardware. The relative comparison between platforms should hold directionally, but we cannot verify this without testing on additional machines.

---

## 5. Results

Originally, we ran 60 experiments. After removing outliers, values more than three standard deviations from the mean, we were left with 27 repeated runs for Google Meet and Microsoft Teams
Every video call lasted two minutes, with identical hardware and browser conditions across all runs. Since normality assumptions were violated for multiple variables (Shapiro–Wilk p < 0.05), we report Mann–Whitney U tests with α = 0.05.

### 5.1 Energy Consumption & CPU Usage

#### Results Averaged Over 27 Runs

| Metric         | Google Meet (Mean ± SD) | Microsoft Teams (Mean ± SD) | Google Meet (Median) | Microsoft Teams (Median) | Relative Difference | Mann–Whitney p-value |
| -------------- | ----------------------- | --------------------------- | ------------------- | ----------------------- | ----------------- | ------------------- |
| CPU Energy (J) | 662.98 ± 13.59          | 772.80 ± 14.48              | 662.75              | 772.24                  | **+16.6%**        | < 0.001             |
| Avg Power (W)  | 5.30 ± 0.10             | 5.71 ± 0.11                 | 5.29                | 5.71                    | **+7.7%**         | < 0.001             |
| Avg CPU (%) | 6.22 ± 0.74             | 7.28 ± 0.43                 | 5.95                | 7.25                    | **+21.8%**                  | < 0.001             |


| Energy (J) | Average Power (W) | CPU Usage (%) |
|------------|-------------------|---------------|
| ![Energy (J)](energyJoule.png) | ![Average Power (W)](avgPowWatts.png) | ![CPU Usage (%)](cpuPercentage.png) |

Each video call lasted 120 seconds on both Google Meet and Microsoft Teams,
ensuring identical workload conditions.
However, the overall experiment duration was longer for Teams due to slower loading times,
which naturally increased total recorded energy (Joules).
To ensure a fair comparison, we therefore focused not only on total energy consumption but also on per-second metrics,
including average power draw and average CPU usage. 
Even when normalized per second, Teams consistently consumed more resources.
- Median CPU usage was 5.95% for Meet and 7.25% for Teams, meaning Teams required approximately 17% more CPU utilization. This difference was statistically significant (Mann–Whitney U = 65.5, p < 0.001) with a very large effect size (r = 0.82).
- In terms of energy, Teams consumed on average 109.8 Joules more per experimental run about 16.6% higher than Meet, and the distributions did not overlap at all (U = 0.0, p < 0.001; rank-biserial r = 1.0), meaning every Teams run consumed more energy than every Meet run. 
- Average power was also significantly higher for Teams (approximately 8% higher; U = 3.0, p < 0.001; r ≈ 0.99). All differences across CPU usage, total CPU energy, and average power were statistically significant (p < 0.001), with large to near-maximal effect sizes. 

These results indicate a consistent and substantial energy gap between the two platforms under identical workload conditions. Consequently, the difference cannot be attributed solely to longer experiment durations.


### 5.2 Network Traffic


| Metric             | Google Meet (Mean ± SD) | Microsoft Teams (Mean ± SD) | Relative Difference | p-value |
| ------------------ | ----------------------- | --------------------------- | ------------------- | ------- |
| Sent Data (MB)     | 3.47 ± 0.18             | 3.13 ± 0.08                 | **−9.9%**           | < 0.001 |
| Received Data (MB) | 60.18 ± 18.24           | 92.26 ± 4.71                | **+53.3%**          | < 0.001 |

Median received data:
- Meet: 67.38 MB
- Teams: 91.94 MB

Teams consistently received substantially more network data than Meet. The rank-biserial correlation for received bytes was 1.0, indicating complete separation between platforms.

| Sent Data (Bytes) | Received Data (Bytes) |  |
|------------------|---------------------|--|
| ![Sent](sentData.png) | ![Received](recvData.png) |  |

---

## 6. Discussion

Our results provide strong evidence that Microsoft Teams consumes more energy than Google Meet during browser-based desktop calls under controlled conditions.
We believe the primary reason for this energy gap lies in how the two applications are architected and delivered.

Microsoft Teams is designed as a comprehensive collaboration platform rather than just a video conferencing tool. In addition to video calls, it integrates chat, file management, calendars, and team workspaces into a single environment. Microsoft Teams is built on React [4], which uses a component and state-based architecture to keep different parts of the app like Chat, Teams lists, and Calendar in sync as things change. This makes the experience feel seamless and integrated, but all that real-time magic comes with a bit of extra computational overhead.

In contrast, Google Meet is a comparatively lightweight, browser-native service. It runs directly within an existing browser tab and is built around WebRTC — a standardized set of real-time communication APIs embedded in modern web browsers for audio and video streaming [1]. Because Meet primarily focuses on delivering video conferencing rather than an extensive suite of collaboration tools, we expected it to consume less energy. Our results strongly support that expectation.

The most important finding is the 16–17% increase in total CPU energy consumption observed in Microsoft Teams. Unlike a small percentage difference that can be statistically significant but negligible in practice, this magnitude is substantial. Given that video calls can last for hours and occur daily across millions of users, a 16% per-session difference will scale into a meaningful cumulative energy impact.
The Mann–Whitney U test further reinforces this conclusion. For both energy consumption and network reception, we obtained U = 0.0, indicating complete separation between the distributions. In practical terms, every single Teams run consumed more energy than every Meet run under our test conditions. This level of consistency strengthens the reliability of the findings.

The energy difference aligns with architectural expectations. 
Prior research has shown that frontend framework complexity [2] and network load [3] are strong predictors of energy consumption.

Teams demonstrated Higher average CPU utilization, Higher sustained power draw, higher incoming network traffic.
Notably, Teams received over 50% more data than Meet. This suggests differences in encoding strategies, bitrate targets, or buffering mechanisms. Increased decoding workload and additional JavaScript processing overhead likely translate into higher sustained CPU activity.
Interestingly, outgoing traffic was slightly lower in Teams than in Meet. This indicates that the primary workload difference lies in receiving and processing video streams rather than transmitting them.

From a sustainable software engineering perspective, these findings highlight how architectural and frontend design decisions can significantly influence energy consumption. While functionality and integration provide value to users, they also carry measurable environmental costs.
However, it is important to acknowledge that the relative difference may vary across different hardware configurations or when using real webcam feeds instead of controlled test inputs.


---

## 7. Conclusion, Limitations and Future Work
   

This study measured the energy cost of browser-based video calls on Google Meet and Microsoft Teams via EnergiBridge.

Under controlled, repeatable experimental conditions:

- Microsoft Teams consumed approximately 16% more CPU energy per session than Google Meet.
- Teams required higher sustained CPU utilisation and power draw.
- Teams received substantially more network data during calls.

All differences were statistically significant with large effect sizes. Although the absolute energy per session is small at the individual level, video conferencing operates at a global scale. Having this in mind, even small per-session increases add up across millions of daily meetings, which means that platform selection has measurable environmental implications.
Our findings suggest that, under the tested configuration, Google Meet is the more energy-efficient option for desktop browser-based video calls.

Although we were able to obtain significant results, it is important to acknowledge the limitations encountered throughout the experiments.
Meetings exceeding 60 minutes had to be restarted due to subscription restrictions on Google Meet, which introduced the possibility of human error.
Additionally, hardware constraints, limited the simulation to five participants per platform, which may not accurately represent larger, real-world meeting scenarios.

We suggest that the Future work could evaluate:
- Real webcam input instead of synthetic streams
- Longer meeting durations
- Multiple hardware configurations
- Mobile devices
- Multi-participant scaling effects

---
## 8. Replication

The full replication package is available at: GH url

```bash
git clone [repo-url]
cd SSE-26
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd EnergiBridge && cargo build -r && cd ..
cp .env.example .env  # add your Meet and Teams URLs
cd src
python run_experiment.py --meet-url "$MEET_URL" --teams-url "$TEAMS_URL" \
  --repeats 30 --duration 120 --visible
python analyze.py --data-dir ../data --output-dir ../figures
```

See `README.md` for full prerequisites and troubleshooting.

## 9. Resources
[1] Leo. (2026, February 14). Five best online meeting services: Latency, Efficiency & Accessibility ranked. https://lifetips.alibaba.com/tech-efficiency/five-best-online-meeting-services

[2] Angular or react: Which one consumes less energy? – BL Research. (2026, February 16). https://www.research-bl.com/angular-or-react-which-one-consumes-less-energy/

[3] R. Horn et al., "Native vs Web Apps: Comparing the Energy Consumption and Performance of Android Apps and their Web Counterparts," 2023 IEEE/ACM 10th International Conference on Mobile Software Engineering and Systems (MOBILESoft), Melbourne, Australia, 2023, pp. 44-54, doi: 10.1109/MOBILSoft59058.2023.00013. keywords: {Energy consumption;Video on demand;Volume measurement;Memory management;Energy measurement;Telecommunication traffic;Time measurement;Energy consumption;Android;Mobile Web;Performance;Empirical Software Engineering},

[4] Sumi_Singh. (2023, June 5). Microsoft Teams: Advantages of the new architecture. TECHCOMMUNITY.MICROSOFT.COM. https://techcommunity.microsoft.com/blog/microsoftteamsblog/microsoft-teams-advantages-of-the-new-architecture/3775704

[5] Wattenbach, L., Aslan, B., Fiore, M. M., Ding, H., Verdecchia, R., & Malavolta, I. (2022). Do You Have the Energy for This Meeting? An Empirical Study on the Energy Consumption of the Google Meet and Zoom Android apps. In MOBILESoft '22: Proceedings of the 9th IEEE/ACM International Conference on Mobile Software Engineering and Systems (pp. 6-16). Institute of Electrical and Electronics Engineers Inc.. https://doi.org/10.1145/3524613.3527812

[6] Sallou, J., Cruz, L., & Durieux, T. (2023). EnergiBridge: Empowering software sustainability through cross-platform energy measurement (arXiv:2312.13897). arXiv. https://doi.org/10.48550/arXiv.2312.13897