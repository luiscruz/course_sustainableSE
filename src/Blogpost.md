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

The closest study to ours is Wattenbach et al. (2022), ["Do You Have the Energy for This Meeting?"](https://dl.acm.org/doi/10.1145/3524613.3527812), published at MOBILESoft 2022. They compared Google Meet and Zoom on Android using an automated experiment with 20 runs per treatment, measuring energy via Android's Batterystats profiler. Their main finding was that Zoom consumed about 4% less energy than Meet on average, though the difference was statistically significant only at a medium effect size (Cliff's delta = −0.344). They also found that camera use had by far the largest impact on energy, increasing consumption by over 274% compared to a camera-off call, while microphone use had negligible effect.

Their work is directly relevant to ours but leaves two gaps. First, it targets Android mobile apps, not desktop browsers, and mobile energy dynamics differ from laptop CPU workloads. Second, it does not include Microsoft Teams. Our study fills both gaps: we measure browser-based sessions on a desktop machine and compare Meet against Teams rather than Zoom.

One methodological difference is worth noting. Wattenbach et al. used Batterystats, which is a software-based energy estimator. They acknowledge this is less precise than hardware measurement. We use [EnergiBridge](https://github.com/tdurieux/EnergiBridge) [Durieux, 2023], which reads directly from hardware power sensors, giving us more accurate absolute figures.

### 2.3 EnergiBridge

EnergiBridge is a cross-platform energy measurement tool developed by Thomas Durieux that reads power sensors directly from the hardware. On Apple Silicon it reads total system power via Apple's SMC through `powermetrics`. On Intel chips and Linux it reads CPU package and DRAM power via Intel's RAPL interface. On Windows it uses LibreHardwareMonitor.

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

### 3.2 Browser Bots

We use Selenium WebDriver to control real Chrome browser instances. Human interaction introduces timing variability that automation removes. Each bot joins the meeting, waits exactly 120 seconds, and leaves. Between runs, the temporary Chrome profile is deleted so no cached state carries over.

Chrome is configured with `--use-fake-device-for-media-stream`, which supplies a synthetic camera and microphone signal rather than a real one. Both platforms receive an identical media input, so any difference in codec workload comes from how each platform processes that input, not from what was in the video. We also set `page_load_strategy = "eager"` because Meet uses a persistent WebSocket connection and never fires the standard browser load event; without this, Selenium would wait indefinitely.

Chrome runs in visible mode. Google Meet rejects headless Chrome outright, so this is not a choice but a constraint.

### 3.3 Energy Measurement

EnergiBridge runs as a background process from just before the bot joins to just after it leaves. It writes a high-frequency power time-series to CSV and prints total energy consumed when it exits. Alongside it, a Python thread samples `psutil` every second for CPU%, memory, and network bytes in both directions. Together these give us hardware-level power data at 5 Hz and a complete system-level view at 1 Hz.

### 3.4 Controls

**Randomised run order.** The full sequence of 60 experiments is shuffled before execution. This spreads time-of-day effects, background system activity, and thermal drift evenly across both platforms.

**Cooldown between runs.** We wait 60 seconds between experiments so the CPU can return to a resting thermal state before the next measurement starts.

**Isolated Chrome profiles.** Each run starts with a clean profile directory that is deleted afterwards, so no browser state accumulates across runs.

**Consistent meeting setup.** A human host stays in the meeting throughout all runs for each platform. The bot always joins an active call.

### 3.5 Experimental Matrix

| Parameter | Value |
|---|---|
| Platforms | Google Meet, Microsoft Teams |
| Participants per call | 1 bot + 1 human host |
| Call duration | 120 seconds |
| Repetitions per platform | 30 |
| Total runs | 60 |
| Cooldown between runs | 60 seconds |
| Browser | Google Chrome (latest), visible mode |
| Media stream | Synthetic (fake device) |
| Run order | Randomised (fixed seed) |
| Energy tool | EnergiBridge |
| OS / Hardware | [INSERT: e.g., macOS 14, Apple M2, 16 GB RAM] |

### 3.6 Analysis

We compute per-platform means and standard deviations and run (Mann-Whitney U or Welch's t-test) to test whether the difference is statistically significant at α = 0.05. We produce four charts: energy per session, system power over time, CPU usage over time, and network traffic.

---

## 4. Threats to Validity

**Fake media streams are a lower bound.** A synthetic camera feed produces a simple, static signal. A real webcam with motion and lighting variation requires more codec work from both platforms. Our results underestimate real-world consumption, and the gap between platforms could be larger or smaller under realistic conditions.

**Network I/O is system-wide.** `psutil.net_io_counters()` captures all traffic on the machine, not just Chrome's. Background OS processes can inflate the figures. We closed non-essential applications before running, but cannot eliminate this entirely.

**Teams lobby timing.** Teams routes guest participants through a lobby before admitting them. The wait time depends on how quickly the host responds. Google Meet was configured to admit participants instantly. This introduces a small, variable difference in the time the browser spends running call-related code before the call formally starts.

**Single hardware configuration.** All measurements were taken on one machine. Absolute energy figures will differ on different hardware. The relative comparison between platforms should hold directionally, but we cannot verify this without testing on additional machines.

**Teams leave is macOS-only.** Our leave implementation for Teams sends `Cmd+Shift+H`. This shortcut does not exist on Linux or Windows. The failure is non-fatal and does not affect the energy measurement, but replication on other operating systems requires adjusting this part of the code.

---

## 5. Results

*To be completed after experiments are run.*

### 5.1 Energy Consumption



### 5.2 System Power Over Time



### 5.3 CPU Usage


### 5.4 Network Traffic


---

## 6. Discussion

*To be completed after experiments are run.*

---

## 7. Conclusion

*To be completed after experiments are run.*

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