---
author: Arnas Venskūnas, Dibyendu Gupta, Nick van Luijk, Sophie Schaaf
group_number: 25
title: "Energy Compare Project - Doomscrolling Reels vs. Shorts"
image: "img/g25_energy_compare/proposal_cover.png"
date: 12/02/2026
summary: |-
    Screen time is often discussed in terms of productivity and mental health, but what about energy usage? In this post, we compare the system energy usage for different frequency of scrolling while doomscrolling Tiktok versus YouTube Shorts.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Introduction

In 2025, people spent on average 141 minutes per day on social media[^time-spent]. That adds up to over 850 hours per person per year, much of it spent watching short-form content. A short break can easily turn into an endless session of watching a stream of recommended videos, a phenomenon known as "doomscrolling."

Every swipe has a cost beyond attention. The energy consumed by our devices to load, decode and play these videos is not something you might think about. In this project, we measure the total system power consumption while doomscrolling Instagram Reels and YouTube Shorts to understand the energy usage of our social media habits.

If you're going to doomscroll, you might as well do it in an energy-efficient way.

## Motivation

## Methodology

We'll describe the various methodological aspects and their respective justifications that were chosen for this project.

### Design Choices of the Experiments

The design of the experiment was one of the most important steps of the experimental setup. During the design phase, we contemplated and debated between various approaches to perform the experiment. The choice of approach affects the implementation and results of the experiment, hence they needed to be critically discussed and justified. 

#### <u>Frequency of Scrolling</u>

The design of the experiment also tries to mimic the actions of users, while keeping it consistent so that it's scientifically measurable and reproducible. An example of this choice was the frequency of scrolling - non-randomized (scrolling consistently after every 2, 5, and 10 seconds). In reality, the frequency of scrolling depends on different factors (attention capture of the video, user preference, network constraints, etc.) and is hence naturally random. However, to attain scientific basis for our experiments, we chose to make scrolling consistent.

#### <u>Moment of Energy Consumption Measurement</u>

Another key design choice was when we start measuring the energy used by the system. We know energy tests are flaky, and energy measurement had to be malleable to ensure room for error (network issues or delay, start-up time for the browser, warm up time, killing background processes of the system, etc.). Energy measurement began after:
- closing all popups (INSERT SCREENSHOT FOR CLOSING DIFFERENT POPUPS)
- "rejecting optional cookies"
- closing random popups while scrolling (since we are not logged into any of the social media apps)
- warm up time of 5 seconds (for any other browser processes to be completed)

Other factors such as brightness, sound of the system, size of the browser window, stable wired WiFi connection, room temperature remained constant during in experiments to not skew the energy consumption of the system.

#### <u>Warm-up Time</u>



### Experimental Setup


### Hardware/Software Details

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

## Results

Violin + Box plots, expect the shape and outliers of the data.

## Statistical Tests

### Shapiro-Wilk Normality Tests

### Parametric Significance Test - Welch's t-test

## Discussion



## Conclusion

## Future work

## References

[^time-spent]: B. Elad, "Average Time Spent On Social Media By App, Country, Region And Trend (2025)," *ElectroIQ*, Jun. 30, 2025. [Online]. Available: [https://electroiq.com/stats/average-time-spent-on-social-media/](https://electroiq.com/stats/average-time-spent-on-social-media/). [Accessed: Feb. 24, 2026].

