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

Power and energy are often conflated, but they answer different questions:

- **Power (W)** describes how much energy is drawn *at a moment*  
- **Energy (J)** captures the *total cost* of completing a task  

Because watching a YouTube Short is a bounded interaction with a clear start and end, **total
energy consumption is the most appropriate primary metric**. Two configurations may draw
similar average power, yet differ substantially in energy if one sustains that power for longer
or exhibits higher load during playback.

In this study, **energy (J)** is therefore the primary comparison metric. Power measurements
are used secondarily to explain *why* energy differences arise, particularly through sustained
load or transient behavior.

---

## Experimental Design

### Factors and conditions

| Factor | Levels |
|---|---|
| Browser | Chrome, Firefox |
| Video quality | Auto, HD720 |

This results in a **2×2 experimental design** with four configurations.

Each configuration is executed **30 times**, with the execution order randomized to avoid
systematic bias (e.g., thermal or caching effects).

### Environment and controls

| Component | Setting |
|---|---|
| OS | Ubuntu 24.04 LTS |
| CPU | Intel Core i7-14650HX |
| RAM | 16 GB |
| GPUs | Intel Raptor Lake UHD + NVIDIA RTX 4060 (Mobile) |
| Power | Plugged into mains |
| Controls | Fixed window size, fixed playback alignment |
| Noise mitigation | Randomized runs + rest interval between runs |

No user interaction occurred during measurements, and background activity was minimized to
isolate browser and quality effects.

---

## Automation and Replication Pipeline

To ensure fairness and reproducibility, the entire experiment is fully automated.

A scripted campaign runner generates a randomized run plan and executes each run sequentially.
For every run:
1. The browser is launched via Playwright
2. The same YouTube Short is loaded
3. Consent dialogs are handled automatically
4. Playback quality is enforced (HD720 when required) and verified
5. Measurement is aligned to **actual video playback**, not page load
6. CPU package energy is recorded using EnergiBridge

All measurements are written to CSV files, enabling full replication of the experiment from raw
data to final plots.

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
| EDP | Energy–delay product |
| EDP² | Stronger penalty for slow, energy-hungry runs |

EDP and EDP² are used as supporting metrics to capture efficiency trade-offs between energy
and execution time.

---

## Results

### Summary statistics (n = 30 per configuration)

| Configuration | Mean Energy (J) | Std (J) | Mean Power (W) | Mean EDP² |
|---|---:|---:|---:|---:|
| Chrome–Auto | 361.6 | 3.1 | 11.25 | 373,579 |
| Chrome–HD720 | 377.7 | 3.9 | 11.41 | 413,700 |
| Firefox–Auto | 354.3 | 31.2 | 10.40 | 415,011 |
| Firefox–HD720 | 384.1 | 27.4 | 10.81 | 489,118 |

---

### Energy distribution across configurations

<img src="img/g28_yt_quality_browser_comparison/energy-dist.png" width="1500"/>

**Figure 1:** Distribution of total CPU package energy (J).

Chrome exhibits **very tight energy distributions** in both quality modes, indicating stable and
predictable behavior across runs. Firefox, in contrast, shows **substantially wider violin plots**,
especially under Auto quality. This suggests higher sensitivity to transient effects such as
background scheduling, buffering behavior, or adaptive bitrate decisions.

The wider Firefox distributions imply that while mean energy may be comparable or even lower
in some cases, **individual runs can be significantly more expensive**, which is undesirable from
both predictability and energy efficiency perspectives.

---

### Energy vs playback duration

<img src="img/g28_yt_quality_browser_comparison/energy_vs_duration.png" width="1500"/>

**Figure 2:** Energy consumption versus runtime.

Chrome runs cluster tightly around 32–33 seconds, while Firefox runs exhibit noticeably higher
spread, with some runs extending beyond 36–38 seconds. Since energy increases roughly
linearly with duration, this runtime variability directly contributes to Firefox’s higher variance
in total energy consumption.

---

### Power behavior over time

<img src="img/g28_yt_quality_browser_comparison/power.png" width="1500"/>

**Figure 3:** Average CPU package power over time (30-run average).

Chrome shows a pronounced **initial power burst** during video startup, followed by a lower,
stable power phase. Firefox, by contrast, exhibits **smoother but more sustained power draw**
throughout playback. This sustained load explains why Firefox’s total energy can be higher even
when peak power appears lower.

Forcing HD720 increases sustained power in both browsers, explaining the consistent energy
increase observed earlier.

---

### Efficiency via EDP²

<img src="img/g28_yt_quality_browser_comparison/edp2_violin.png" width="1500"/>

**Figure 4:** EDP² distribution (lower is better).

Chrome’s EDP² values remain tightly clustered, while Firefox shows large penalties in slower,
energy-heavy runs—particularly under HD720. This reinforces the observation that **predictability
and stability matter for efficiency**, not just average power.

---

## Statistical Significance

Shapiro–Wilk tests indicate that normality cannot be assumed for all configurations. Accordingly,
we use **Mann–Whitney U tests** for pairwise comparisons.

Key findings:
- Auto vs HD720 shows statistically significant energy differences
- Chrome vs Firefox under HD720 is statistically significant
- Chrome vs Firefox under Auto shows weaker statistical evidence due to Firefox’s high variance

---

## Discussion

Two main effects emerge clearly from the results.

First, **forcing HD720 consistently increases energy consumption** on both browsers. Power
analysis shows that this increase is driven by sustained higher load rather than brief spikes,
making higher quality selection an energy-relevant choice even for short videos.

Second, **browser implementation strongly affects consistency**. Chrome’s execution is highly
stable across runs, while Firefox exhibits large variability in both duration and energy. This
suggests differences in how browser engines handle decoding, buffering, and scheduling under
short, bursty workloads such as YouTube Shorts.

While the energy cost of a single short video is small, these differences scale with repeated use
and massive user populations, making them relevant from a sustainability perspective.

---

## Limitations

This study is limited to a single machine and a single YouTube Short. Results may differ across
hardware platforms, codecs, or content types. Additionally, only CPU package energy is measured;
display, network, and GPU energy are not included.

---

## Conclusion

This project shows that **everyday software choices have measurable energy consequences**.
Forcing higher video quality increases energy use, and browser choice affects both average energy
and variability. Chrome’s predictability contrasts with Firefox’s higher variance, highlighting
that stability is an important dimension of energy efficiency.

Treating energy as a first-class evaluation metric—alongside performance and quality—can help
guide more sustainable software design decisions, especially for high-volume consumer workloads
such as short-form video streaming.
