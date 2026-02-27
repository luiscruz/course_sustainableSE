---
author: Ayush Khadka, Carolyn Alcaraz, Nicolas Loaiza Atehortua, Benas Pranauskas
group_number: 35
title: "Comparing the difference in Power Consumption between Video Conference Applications Microsoft Teams and Zoom"
image: "img/gX_template/project_cover.png"
date: 27/02/2026
summary: |-
  This project is about comparing the energy usage of Microsoft Teams and Zoom. We compare the energy impact of enabling different variations of video-call features on both applications: camera on/off, blur on/off, and screen-share on/off. We run 30 iterations per feature pair, per application, and measure the energy costs over time. We use Energibridge for measuring the data, and develop automated scripts to run the experiments reproducibly. 
  
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

Body lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

This problem takes another level if we are counting on these measurements to make **groundbreaking research contributions** in this area. Some research projects in the past have underestimated this issue and failed to produce replicable findings. Hence, this article presents a roadmap on how to properly set up a scientific methodology to run energy efficiency experiments. It mostly stems from my previous work on [doing research and publishing](/publications) on Green Software.


This article is divided into two main parts: 1) how to set up energy measurements with minimum bias, and 2) how to analyse and take scientific conclusions from your energy measurements.
Read on so that we can get your paper accepted in the best scientific conference.

--- 
#### 👉 Note 1:
If you are a **software developer** enthusiastic about energy efficiency but you are not particularly interested in scientific experiments, this article is still useful for you. It is not necessary to do "everything by the book" but you may use one or two of these techniques to reduce the likelihood of making wrong decisions regarding the energy efficiency of your software.

--- 

## Unbiased Energy Data ⚖️

There are a few things that need to be considered to minimise the bias of the energy measurements. Below, I pinpoint the most important strategies to minimise the impact of these biases when collecting the data.

### Zen mode 🧘🏾‍♀️

The first thing we need to make sure of is that the only thing running in our system is the software we want to measure. Unfortunately, this is impossible in practice – our system will always have other tasks and things that it will run at the same time. Still, we must at least minimise all these competing tasks:

- all applications should be closed, notifications should be turned off;
- only the required hardware should be connected (avoid USB drives, external disks, external displays, etc.);
- turn off notifications;
- remove any unnecessary services running in the background (e.g., web server, file sharing, etc.);
- if you do not need an internet or intranet connection, switch off your network;
- prefer cable over wireless – the energy consumption from a cable connection is more stable than from a wireless connection.

### Freeze your settings 🥶

It is not possible to shut off the unnecessary things that run in our system. Still, we need to at least make sure that they will behave the same across all sets of experiments. Thus, we must fix and report some configuration settings. One good example is the brightness and resolution of your screen – report the exact value and make sure it stays the same throughout the experiment. Another common mistake is to keep the automatic brightness adjustment on – this is, for example, an awful source of errors when measuring energy efficiency in mobile apps.

---

### 

Nevertheless, using statistical metrics to measure effect size is not enough – there should be a discussion of the **practical effect size**. More important than demonstrating that we came up with a new version that is more energy efficient, you need to demonstrate that the benefits will actually be reflected in the overall energy efficiency of normal usage of the software. For example, imagine that the results show that a given energy improvement was only able to save one joule of energy throughout a whole day of intensive usage of your cloud software. This perspective can hardly be captured by classic effect-size measures. The statistical approach to effect size (e.g., mean difference, Cohen's-*d*, and so on) is agnostic of the context of the problem at hand.

# Introduction
## Context and Motivation
Six years ago, the COVID-19 pandemic began, prompting nations around the world to enforce a lockdown with the intention of reducing virus transmission. People were strongly advised to stay home and as a consequence, this led to a considerable increase in work from home (WFH) arrangements with **video conferencing** becoming a core part of daily work. 

According to Adrjan et al., WFH job postings have quadrupled across 20 countries from 2020 to 2023, with these kind of postings still remaining popular despite a lifting of pandemic restrictions. Naturally, video conference applications rose in popularity and because of this, it is imperative to consider the energy usages of these applications as the number of people transitioning to remote working during this time increases significantly. 

From a user perspective, the energy efficiency of video conferencing software matters because it directly affects the experience of working on a laptop. Online meetings can be long and frequent, and if an application draw more power, the **laptop will drain faster**. This would require more frequent charging, and may force users to adapt their workday around power availability by, for example, staying near outlets or carrying chargers. Higher power draw can also increase heat and fan activity, impacting comfort and potentially influencing audio quality if fan noise is captured by the microphones. Over time, frequent high-power usage by contribute to **faster battery wear**, reducing the lifespan of a device. 

Beyond individual devices, energy usage also has **system-level implications**. Video conferencing can be used at **massive scale across organizations**, with even modest per-hour difference in power consumption accumulating across users. Understanding how application choice and feature configuration affects power demand can support recommendations for more sustainable digital work practices. 

While the number of people transitioning to remote working has recently seemed to stabilized in Europe and in other places around the world, as reported by Eurofound researcher Oscar Vargas Llave, "The possibility of working from home hasn’t [been] sedimented in European workplaces". Thus, research into the energy usages of video conference applications remains relevant in this day and age.

For the purposes of this research, the video conference applications to be investigated for energy usage are **Zoom Workplace** and **Microsoft Teams**. Both applications have native apps, and share similar features that will be experimented on, namely, the turning on and off of the camera, the sharing of screens, and the blurring of the background. 

## Research Objectives

The primary research objective of this piece is to compare the two aforementioned applications in power usage.

The more specific objectives of this study are to:
- Measure and analyze the baseline power consumption of Zoom Workplace and Microsoft Teams during a video call with the camera turned off. 
- Compare the difference in power usage of Zoom Workplace and Microsoft Teams with the camera turned off versus with the camera turned on. 
- Evaluate the impact of screen sharing on the power consumption across the two different platforms. 
- Evaluate the impact of background blurring on the power consumption across the two different platforms.
- And lastly, identify which of the two applications is more energy-efficient under different feature configurations and provide insights into how specific features affect the energy consumption of of video conference applications and their implications for sustainable work from home practices.

# Methodology 

## Experimental setup

The experiment was conducted in a controlled environment on a single computer with the following device specifications:


- **Processor:** AMD Ryzen 7 7730U with Radeon Graphics (2.00 GHz) 
- **Installed RAM:** 16.0 GB
- **System Type:** 64-bit operating system, x64-based processor
- **Operating System:** Windows 11 home, version 25H2

Moreover, the following sofware was used to run the experiment:

- **Automation Environment:** Python, version 3.14
- **Applications Under Test:** Microsoft Teams, version 26032.208.4399.5; Zoom Workplace, version 6.6.11 (23272)
- **Monitoring Tool:** Energibridge, version 0.0.7


## Variables and Metrics

We categorize the experimental parameters into dependent and independent variables, in order to measure how toggling different video-call features influences the power demands of the system.

**Independent Variables:**

- **Applications:** Microsoft Teams vs. Zoom Workplace.
- **Feature States:** Camera On/Off, Blur On/Off, Screen-share On/Off.

**Dependent Variables:**

- **Mean Power (W):** the rate of energy consumption during the trial.
- **Total Energy (J):** the total amount of energy consumed in 30 seconds.
- **Energy Delay Product (J·s):** trade-off between energy efficiency and the time taken to complete the task.

Next, we establish a controlled testing environment, to achieve as accurate and reproducible results as possible.


## Controlled Testing Environment
The experiment was conducted in "Zen mode" to minimize bias.

All non-essential applications were stopped, and device notifications disabled. The only application open on the device was ``cmd.exe`` terminal with administrative power. The computer used wireless internet connection, and was plugged into a power source throughout the experiment. The brightness of the screen was set to 100%, and the volume to 30%.

In the following subsection, we describe the step-by-step testing procedure and the automation of the experiment.


## Automation & Testing Procedure 

The experiment is driven by a single automation script that imports two platform-specific automation modules. Once started, it requires no manual intervention.

**Warm-up.** A 5-minute CPU-intensive task (Fibonacci sequence) stabilises CPU thermals before any measurement begins, reducing cold-start variance.

**Randomised scheduling.** For each task, the script must complete 15 iterations per platform. Instead of running them sequentially, it randomly selects which platform to test next from whichever still has remaining iterations. This shuffling mitigates ordering effects such as room temperature changes or background OS activity, that could systematically bias one platform's results.

**Iteration lifecycle.** Each iteration follows a fixed sequence:

1. **Launch**: the selected application opens and joins a pre-configured meeting automatically.
2. **Baseline measurement**: EnergiBridge records system-level energy consumption for 30 seconds under the baseline condition (e.g., camera off, no blur, no screen share).
3. **Feature measurement**: the script toggles the feature (e.g., enables camera, blur, or screen sharing) and EnergiBridge records for another 30 seconds.
4. **Restart**: the application is force-killed to ensure a clean state for the next iteration.
5. **Cooldown**: a 60-second waiting period is executed to prevent tail energy consumption between iterations.


### Replication Package

For the experiments, the replication package can be found in the following [repository](https://github.com/ayushhhkha/SSE_TeamsVsZoom).

## Data Collection & Processing 
Each 30-second EnergiBridge run creates a CSV containing timestamped energy readings, producing 360 files across all iterations. From each reading we derive the dependent variable values: mean power (W), total energy (J), and the Energy Delay Product (J·s). Outliers are removed using a z-score filter, and the appropriate statistical test (Welch t-test or Mann–Whitney U) is selected based on a Shapiro-Wilk normality check.


# Results

This section will present the findings of the different power consumption and energy delay product values across the different video conference applications and features.

As mentioned previously, EnergiBridge was used to measure energy consumption. The tool provides the following relevant metrics:
- Delta
- CPU_Energy (Joules)

With the metrics above, the key metrics to be calculated per trial were:
1. Total Energy Consumption (J): Calculated by computing the difference of the cumulative energy metric. 
2. Average Power Consumption (W): Calculated by dividing the total energy consumption over the duration of the trial.
3. Energy Delay Product: Calculated by multiplying energy by the total duration of the trial.


## Outlier detection

Before diving into the experimental results we removed anomalies to improve data reliability. We used a Z-Score threshold of 3.0 to determine the outliers. The reason why we picked 3 is due to how it covers 99.7% of normal data which lies within 3 standard deviations. Another reason why we picked 3.0 is because a thereshold of 3.0 ensures that only extreme measurements error are removed while it keeps normal variability intact. Based on the application, our experiment flagged outliers between 0 and 1 per group of 30 iterations. In total, only 5 outliers were removed. Based on this it confirms that our data was generally stable and that only extreme measurement errors were detected. Since the number of identified outliers were negligible, we decided that we will not demonstrate visualization or data processing with outliers since these outliers were negligible and will do not demonstrate a significant reflection of our data.


## Experimental results

After the removal of outliers, the results can be seen illustrated below. Each figure compares Zoom and Microsoft Teams under the specified feature ON vs OFF conditions. The violin plots show the full distribution of the measurements across the 30 runs, while the embedded box plots indicate the mean and interquartile range.

### Power and EDP Comparison for camera on vs camera off

<div style="display: flex; gap: 20px;">

  <div style="flex: 1;">
    <strong>Power</strong><br>
    <img src="img/g35_teams_zoom/camera_avg_power_W_combined.png" width="100%">
    <p style="text-align: center; font-style: italic; margin-top: 6px;">
    <strong>Figure 1</strong>: Average Power Consumption values for features camera on vs camera off.
    </p>
  </div>

  <div style="flex: 1;">
    <strong>EDP</strong><br>
    <img src="img/g35_teams_zoom/camera_EDP_Js_combined.png" width="100%">
    <p style="text-align: center; font-style: italic; margin-top: 6px;">
    <strong>Figure 2</strong>: EDP values for features camera on vs camera off.    
    </p>
  </div>

</div>

### Power and EDP Comparison for background blurring on vs off

<div style="display: flex; gap: 20px;">

  <div style="flex: 1;">
    <strong>Power</strong><br>
    <img src="img/g35_teams_zoom/blur_avg_power_W_combined.png" width="100%">
    <p style="text-align: center; font-style: italic; margin-top: 6px;">
    <strong>Figure 3</strong>: Average Power Consumption values for features background blurring on vs off.
    </p>
  </div>

  <div style="flex: 1;">
    <strong>EDP</strong><br>
    <img src="img/g35_teams_zoom/blur_EDP_Js_combined.png" width="100%">
    <p style="text-align: center; font-style: italic; margin-top: 6px;">
    <strong>Figure 4</strong>: EDP values for features background blurring on vs off.
    </p>
  </div>
</div>

### Power and EDP Comparison for screen sharing on vs off

<div style="display: flex; gap: 20px;">

  <div style="flex: 1;">
    <strong>Power</strong><br>
    <img src="img/g35_teams_zoom/share_avg_power_W_combined.png" width="100%">
    <p style="text-align: center; font-style: italic; margin-top: 6px;">
    <strong>Figure 5</strong>: Average Power Consumption values for features screen sharing on vs off.
    </p>
  </div>

  <div style="flex: 1;">
    <strong>EDP</strong><br>
    <img src="img/g35_teams_zoom/share_EDP_Js_combined.png" width="100%">
    <p style="text-align: center; font-style: italic; margin-top: 6px;">
    <strong>Figure 6</strong>: EDP values for features screen sharing on vs off.
    </p>
  </div>

</div>

Across all the features, it can be observed that enabling the feature generally results in higher average power consumption compared to disabling it. This effect can be seen for both applications, with the exactl magnitude and variability differing between Zoom and Microsoft Teams. Note that the width and shape of the violins show that feature-enabled conditions often exhibit greater variability, suggesting less stable energy behaviour when additional processing, such as video effects and sharing, is active. 

## Statistical Analysis

### Normality testing
To determine the kind of statistical tests to conduct, the normality of the data destribution was evaluated using the **Shapiro-Wilk test**.

The test was applied separately to each group, with a significance level of `a = 0.05` being used:
- if `p >= 0.05`: the data was normally distributed
- if `p < 0.05`: the data was not normally distributed

Generally speaking, most of the groups revealed to have data that is not normally distributed. The groups that were revealed to be normally distributed are: TEAMS_CAM_ON_PW, TEAMS_CAM_OFF_PW, TEAMS_SHARE_ON_PW, ZOOM_CAM_ON_EDP, TEAMS_CAM_ON_EDP, and TEAMS_CAM_OFF_EDP. Note that the first three concern the average power consumption, while the last three concern the energy delay product values. 

Depending on the result, the choice of statistical test was made as described below.

| Name | Type | Shapiro-Wilk (W) | p-value |
|---|---|---:|---:|
| TEAMS_CAM_ON_PW | ON | 0.000 | 0.000 |
| TEAMS_CAM_OFF_PW | ON | 0.000 | 0.000 |
| TEAMS_SHARE_ON_PW | ON | 0.000 | 0.000 |
| ZOOM_CAM_ON_EDP | OFF | 0.000 | 0.000 |
| TEAMS_CAM_ON_EDP | OFF | 0.000 | 0.000 |
| TEAMS_CAM_OFF_EDP | OFF | 0.000 | 0.000 |

*Table 1: Features*

| Name | Type | Shapiro-Wilk (W) | p-value |
|---|---|---:|---:|
| TEAMS_CAM_ON_PW | ON | 0.000 | 0.000 |
| TEAMS_CAM_OFF_PW | ON | 0.000 | 0.000 |
| TEAMS_SHARE_ON_PW | ON | 0.000 | 0.000 |
| ZOOM_CAM_ON_EDP | OFF | 0.000 | 0.000 |
| TEAMS_CAM_ON_EDP | OFF | 0.000 | 0.000 |
| TEAMS_CAM_OFF_EDP | OFF | 0.000 | 0.000 |

*Table 2: App and Features*


### Significance Testing
Two independent-sample significance tests were considered in this case. 

**Welch's t-test** was used in the case both groups passed the normality test. This is because this test compares mean differences, making it appropriate for when distributional assumptions are met. 

When at least one group violated the normality assumptions, the **Mann-Whitney U test** was used instead because this test does not rely on distributional assumptions and compares rank other, making it more robust to skewed distributions and outliers. 

| Name | Test Name | Effect Value | 
|---|---|---:|
| TEAMS_CAM_ON_PW | ON | 0.000 | 
| TEAMS_CAM_OFF_PW | ON | 0.000 | 
| TEAMS_SHARE_ON_PW | ON | 0.000 | 
| ZOOM_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_OFF_EDP | OFF | 0.000 | 

*Table 3: Features*

| Name | Test Name  | Effect Value | 
|---|---|---:|
| TEAMS_CAM_ON_PW | ON | 0.000 | 
| TEAMS_CAM_OFF_PW | ON | 0.000 | 
| TEAMS_SHARE_ON_PW | ON | 0.000 | 
| ZOOM_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_OFF_EDP | OFF | 0.000 | 

*Table 4: App*



### Effect size estimation
In addition to statistical significance, **effect sizes** should be computed to help indicate the practical relevance of an observed difference. 

For Welch's t-test, **Cohen's d** was used to quantify standardized mean differences. For the Mann-Whitney U test, the **common language effect size** was computed, representing the probability that a randomly selected observation from one group exceeds an observation from another group. 

These measures are meant to provide insight into the magnitude of observed effects, independent of sample size. 

| Name | Effect Name | Effect Value | 
|---|---|---:|
| TEAMS_CAM_ON_PW | ON | 0.000 | 
| TEAMS_CAM_OFF_PW | ON | 0.000 | 
| TEAMS_SHARE_ON_PW | ON | 0.000 | 
| ZOOM_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_OFF_EDP | OFF | 0.000 | 

*Table 5: Features*

| Name | Effect Name | Effect Value | 
|---|---|---:|
| TEAMS_CAM_ON_PW | ON | 0.000 | 
| TEAMS_CAM_OFF_PW | ON | 0.000 | 
| TEAMS_SHARE_ON_PW | ON | 0.000 | 
| ZOOM_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_ON_EDP | OFF | 0.000 | 
| TEAMS_CAM_OFF_EDP | OFF | 0.000 | 

*Table 6: App and Features*

(Queue in depth explanation between the applications)


# Discussion
## Interpretation of Results

## Potential Explanations
TODO
## Implications
TODO
# Limitations

There are some limitations that will be briefly discussed in this section:

### Limited Test Duration: 

In an actual conference call, it usually lasts more then 10 minutes. However, the experiment was conducted with a 30 second duration in which this interval is quite short and does not reflect the real life usage of the application. Based on this we cannot clearly have results that can have system wide implications in order for certain companies to pick the most energy efficient application.

### Singular Hardware System: 
Another limitation is that this experiment was conducted in a single machine in which results could vary in different machines. The energy consumption can vary depending on the computers, CPU architecture, GPU, the battery health and power management.

### Operating Systems:
Only the Windows OS was used in which compared to MacOS and Linux, it can have different power management policies and task scheduling mechanism which can influence the energy consumption. Depending on the OS, certain background processes can be running which can impact the energy consumptions. Depending on the OS, certain features tested can have optimizations made for that specific OS. 

# Future Work

For additional work, it would be interesting to observe the experimentation being conducted on a Windows laptop and a MacOS which can lead to an interesting analysis of cross platforms and to determine which application is the most energy efficient in both OS. Another interesting work that can be done is testing out more application in demand such as Google Meet and Slack in order to effectively analyse each video conferencing application and determine the most energy efficient. One more additional work that can be conducted would be to increase the intervals which will increase experimentation time but this will align better with real life situations were video conferencing application are meant for longer usage. With our replication package, the future work can immediately begin.

# Conclusion

Our paper discusses the energy usage between **Zoom Workplace** and **Microsoft Teams**. The features that are being experimented on are turning on/off camera, blur and screen share.


# References

1. Sweigart, Al. “Welcome to PyAutoGUI’s Documentation! — PyAutoGUI 1.0.0 Documentation.” Readthedocs.io, 2014, pyautogui.readthedocs.io/en/latest/.
2. “The Empirical Rule (68-95-99.7).” Dmaic.com, 2 Oct. 2025, www.dmaic.com/faq/empirical-rule/. Accessed 26 Feb. 2026.
3. “Z-Score (Standard Score).” Dmaic.com, 8 Oct. 2025, www.dmaic.com/faq/z-score-standard-score/. Accessed 26 Feb. 2026.

