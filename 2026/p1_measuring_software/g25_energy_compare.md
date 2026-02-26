---
author: Arnas Venskūnas, Dibyendu Gupta, Nick van Luijk, Sophie Schaaf
group_number: 25
title: "Energy Compare Project - Doomscrolling Reels vs. Shorts"
image: "img/g25_energy_compare/proposal_cover.png"
date: 12/02/2026
summary: |-
    Screen time is often discussed in terms of productivity and mental health, but what about energy usage? In this post, we compare the total system power while doomscrolling Instagram Reels versus YouTube Shorts.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Introduction

In 2025, people spent on average 141 minutes per day on social media[^time-spent]. That adds up to over 850 hours per person per year, much of it spent watching short-form content. A short break can easily turn into an endless session of watching a stream of recommended videos. This continuous video scrolling is also colloquially dubbed "Doomscrolling".

Every swipe has a cost beyond attention. The energy consumed by our devices to load, decode and play these videos is not something you might think about. In this project, we measure the total system power consumption while doomscrolling Instagram Reels and YouTube Shorts to understand the energy usage of our social media habits.

This research aims to provide insights on which platform to use in order to decrease your energy usage during a doomscrolling session.

Of course, using less energy during doomscrolling will be positive for the environment. However, there are more direct advantages to the community of doomscrollers.

Access to a charger is not always a given while in the midst of our doomscrolling sessions. When your device is low on battery, choosing the more energy-efficient platform might add extra time to keep scrolling. 

However, even if an energy source is available, the cost of energy has only been increasing over the last 5 years [^energy-prices]. Therefore, the findings in this research may allow you to reduce the price of your energy bill as well.

If you're going to doomscroll, you might as well do it in an energy-efficient way.

# Methodology
The aim is to quantify and compare the power consumption associated with doomscrolling. Therefore, we designed a comparative experiment analyzing the energy consumed by both TikTok as well as YouTube.

## Test Environment
All tests were conducted within a standard Linux-based Operating System, using the Google Chrome browser. 

Capturing the energy spent for each experiment was done using EnergiBridge. EnergiBridge is a cross-platform command-line utility that can analyze the performance directly from our machine's low-level hardware sensors.

The experiments consisted of standardized scrolling sessions with a length of 30 seconds. For both platforms, the experiments were repeated 30 times to ensure generalizability.

For these experiments, the scrolling process was automated. Scrolling frequency was varied between the options of two, five or 10 seconds. This allows us to evaluate the impact of the pace of the content consumption as well.

## Tests
**TODO: Finalized code blocks for the test cases.**

## Experimental Controls
Desktop computers often run numerous background processes that could skew our energy measurements. Therefore, we aimed to create a strictly controlled testing environment. 

To achieve this, we disabled wireless networks in favour of an Ethernet connection. Additionally, we unplugged all non-essential USB peripherals and terminated all background applications, including cloud syncing tools. Lastly, we locked the monitor to a fixed, medium brightness level. 

With these mitigations, external influences on the stability of the to-be-measured energy consumption of solely the Doomscrolling. Therefore, solely the power consumption of video rendering and network requests is measured. Becasue of this, the expectation is that the measurements will not differ significantly across platforms.

## Analysis
### Exploratory Analysis
Violin + Box plots, expect the shape and outliers of the data.

### Normality
After the measurements are taken, it is important to ensure that data is normal. To measure normality, Shapiro-Wilk's test was performed. If the results do not assume normality, the points of data, deviating by more than 3 standard deviations from the mean were excluded and the Shapiro-Wilk's test was conducted again. If the results still did not indicate normality, the experiment was repeated.

### Statistical Significance
Group differences were evaluated using the Welch’s t-test, which does not assume equal variances between groups. Statistical significance was determined using a α = 0.05.

### Effect Size
To evaluate the practical implication of the observed results, mean difference and percent change were calculated.
Cohen’s d was computed to measure statistical effect size. Effect sizes were interpreted according to conventional benchmarks:

Small effect: d ≈ 0.2

Medium effect: d ≈ 0.5

Large effect: d ≈ 0.8

While statistical difference is unlikely to arise by chance, the practical importance will be further evaluated in the discussion section.

# Results

## Analysis
### Exploratory Analysis
### Normality
### Statistical Significance
### Effect Size

# Discussion
## Practical importance

# Conclusion

# Future work

# References

[^energy-prices]: CBS, "Average energy prices for consumers", Accessed Feb. 26, 2026, https://opendata.cbs.nl/#/CBS/en/dataset/85592ENG/table
[^time-spent]: B. Elad, "Average Time Spent On Social Media By App, Country, Region And Trend (2025)," *ElectroIQ*, Jun. 30, 2025. [Online]. Available: [https://electroiq.com/stats/average-time-spent-on-social-media/](https://electroiq.com/stats/average-time-spent-on-social-media/). [Accessed: Feb. 24, 2026].

