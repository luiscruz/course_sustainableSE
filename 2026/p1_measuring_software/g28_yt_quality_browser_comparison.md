---
author: Uddhav Pisharody, Job Stouthart, Vasil Chirov, Georgi Dimitrov, Horia Zaharia
group_number: 28
title: "Energy Consumption of YouTube Short-Form Video Playback: Auto vs HD720 on Chrome and Firefox"
image: "img/gX_template/project_cover.png"
date: 27/02/2026
summary: |-
  We investigate the energy consumption of short-form video playback on YouTube under controlled conditions. Specifically, we analyze how browser choice (Google Chrome vs Mozilla Firefox) and video quality settings (automatic quality selection vs forced 720p playback) affect energy usage. Using the same YouTube Short video across all experiments, we construct a 2×2 experimental design consisting of Chrome–Auto, Chrome–HD720, Firefox–Auto, and Firefox–HD720 configurations. Energy consumption is measured using EnergiBridge at the CPU package level while automating video playback via Playwright. Each configuration is executed 30 times in randomized order to mitigate system noise.
identifier: p1_measuring_software_2026
all_projects_page: "../p1_measuring_software"
---

# Energy Consumption of YouTube Short-Form Video Playback  
### Auto vs HD720 on Chrome and Firefox

## Introduction

Short-form video has become a default browsing activity. Users scroll through YouTube Shorts
multiple times a day, frequently switching browsers and video quality settings—often without
being aware of the underlying system-level consequences of these choices. While performance
and visual quality are highly optimized and visible, **energy consumption remains largely
invisible to users**.

This project investigates whether two everyday software choices—**browser selection**
(Google Chrome vs Mozilla Firefox) and **video quality selection** (automatic quality vs forced
720p)—lead to measurable differences in energy consumption for the same YouTube Short.
We focus on short-form content because it represents a bounded, repeatable task that is consumed
at massive scale.

We evaluate four configurations, each executed 30 times under controlled conditions:
- Chrome–Auto
- Chrome–HD720
- Firefox–Auto
- Firefox–HD720

Even small per-play differences may accumulate into a substantial energy footprint when scaled
to millions of users and repeated daily interactions.

---

## Why energy (J) instead of power (W)?

Power and energy answer different questions:

- **Power (W)** describes how much energy is drawn *at a moment*  
- **Energy (J)** captures the *total cost* of completing a task  

Because watching a YouTube Short is a bounded interaction with a clear start and end, **total
energy consumption is the most appropriate primary metric**. Two configurations may draw
similar average power, yet differ substantially in energy if one sustains that power longer or
executes less predictably.

In this study, **energy (J)** is therefore the primary comparison metric. Power is analyzed
secondarily to explain *why* energy differences arise.

---

## Experimental Design

### Factors and conditions

| Factor | Levels |
|---|---|
| Browser | Chrome, Firefox |
| Video quality | Auto, HD720 |

Each configuration is executed **30 times**, with randomized execution order to reduce
systematic bias (e.g., thermal or caching effects).

### Environment and controls

| Component | Setting |
|---|---|
| OS | Ubuntu 24.04 LTS |
| CPU | Intel Core i7-14650HX |
| RAM | 16 GB |
| GPUs | Intel Raptor Lake UHD + NVIDIA RTX 4060 (Mobile) |
| Power | Plugged into mains |
| Controls | Fixed window size, aligned playback |
| Noise mitigation | Randomized runs + rest interval |

---

## Automation and Replication Pipeline

The entire experiment is fully automated to ensure fairness and reproducibility.

For each run:
1. The browser is launched via Playwright
2. The same YouTube Short is loaded
3. Consent dialogs are handled automatically
4. Playback quality is enforced (HD720 when required) and verified
5. Measurement is aligned to **actual video playback**
6. CPU package energy is recorded using EnergiBridge

All runs produce CSV logs, enabling full replication from raw data to plots.

---

## Measurement and Metrics

Energy is measured using **EnergiBridge**, which records cumulative CPU package-level energy
directly from hardware counters.

From raw measurements, we derive:

| Metric | Meaning |
|---|---|
| Total energy (J) | Energy cost of playback |
| Duration (s) | Runtime of playback |
| Average power (W) | Energy / duration |

Duration and power are used to **explain energy differences**, not as primary optimization goals.

---

## Results

### Summary statistics (n = 30 per configuration)

| Configuration | Mean Energy (J) | Std (J) | Mean Power (W) |
|---|---:|---:|---:|
| Chrome–Auto | 361.6 | 3.1 | 11.25 |
| Chrome–HD720 | 377.7 | 3.9 | 11.41 |
| Firefox–Auto | 354.3 | 31.2 | 10.40 |
| Firefox–HD720 | 384.1 | 27.4 | 10.81 |

---

### Energy distribution across configurations

<img src="img/g28_yt_quality_browser_comparison/energy-dist.png" width="1500"/>

**Figure 1:** Distribution of total CPU package energy (J).

Chrome exhibits **very tight energy distributions** in both quality modes, indicating stable and
predictable behavior across runs. Firefox, in contrast, shows **substantially wider violin plots**,
particularly under Auto quality.

This suggests that Firefox is more sensitive to transient effects such as adaptive bitrate
decisions, buffering behavior, or scheduling variability. While its *mean* energy may be
competitive, individual runs can be significantly more expensive, which is undesirable from an
efficiency and predictability standpoint.

---

### Energy vs playback duration

<img src="img/g28_yt_quality_browser_comparison/energy-scatter.png" width="1500"/>

**Figure 2:** Energy consumption versus runtime.

Chrome runs cluster tightly around 32–33 seconds, while Firefox runs exhibit much larger spread,
with some executions extending beyond 36–38 seconds. Since energy increases approximately
linearly with runtime, this duration variability directly explains Firefox’s wider energy
distribution.

---

### Power behavior over time

<img src="img/g28_yt_quality_browser_comparison/power.png" width="1500"/>

**Figure 3:** Average CPU package power over time (30-run average).

Chrome shows a pronounced **initial power burst** during startup, followed by a lower, stable
power phase. Firefox exhibits **smoother but more sustained power draw** across playback.

This sustained load explains why Firefox can consume more total energy despite lower peak
power. Forcing HD720 increases sustained power in both browsers, accounting for the consistent
energy increase observed earlier.

---

## Discussion

Two key effects emerge from the results.

First, **forcing HD720 consistently increases energy consumption** on both browsers. Power
analysis shows that this increase is driven by sustained higher load rather than brief spikes,
making quality selection an energy-relevant choice even for short videos.

Second, **browser implementation strongly affects consistency**. Chrome executes the workload
in a highly predictable manner, while Firefox exhibits substantial variability in both runtime and
energy. This suggests differences in how browser engines manage decoding, buffering, and task
scheduling under short, bursty workloads.

Although the energy cost of a single short video is small, these differences scale with repeated
use and massive user populations, making them relevant from a sustainability perspective.

---

## Limitations

This study is limited to a single machine and a single YouTube Short. Results may differ across
hardware platforms, codecs, or content types. Only CPU package energy is measured; display,
network, and GPU energy are not included.

---

## Conclusion

This project demonstrates that **everyday software choices have measurable energy
consequences**. Forcing higher video quality increases energy usage, and browser choice affects
both average energy and variability.

Chrome’s predictability contrasts with Firefox’s higher variance, highlighting that **stability is
an important dimension of energy efficiency**, especially for high-volume consumer workloads
such as short-form video streaming.
