---
author: Ayush Khadka, Carolyn Alcaraz, Nicolas Loaiza Atehortua, Benas Pranauskas
group_number: 35
title: "Comparing the difference in Power Consumption between Video Conference Applications Microsoft Teams and Zoom"
image: "img/gX_template/project_cover.png"
date: 03/03/2022
summary: |-
  This project is about comparing the energy usage of Microsoft Teams and Zoom. We will run both applications for 1  minute for 15-30 iterations. We will measure the cpu power over time. We will use Energibridge. 
  
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
Around six years ago, the COVID-19 pandemic began, prompting nations around the world to enforce a lockdown with the intention of reducing virus transmission. People were strongly advised to stay home and as a consequence, this led to a considerable increase in work from home (WFH) arrangements. 

According to Adrjan et al., WFH job postings have quadrupled across 20 countries from 2020 to 2023, with these kind of postings still remaining popular despite a lifting of pandemic restrictions. Naturally, video conference applications rose in popularity and because of this, it is imperative to consider the energy usages of these applications as the number of people transitioning to remote working during this time increases significantly. 

While this number has recently seemed to stabilized in Europe and in other places around the world, as reported by Eurofound researcher Oscar Vargas Llave, "The possibility of working from home hasn’t [been] sedimented in European workplaces". Thus, research into the energy usages of video conference applications remains relevant in this day and age.

For the purposes of this research, the video conference applications to be investigated for energy usage are Zoom Workplace and Microsoft Teams. Both applications have native apps, and share similar features that will be experimented on, namely, the turning on and off of the camera, the sharing of screens, and the blurring of the background. 

## Research Objectives

The primary research objective of this piece is to compare the two aforementioned applications in power usage.

The more specific objectives of this study are to:
- Measure and analyze the baseline power consumption of Zoom Workplace and Microsoft Teams during a video call with the camera turned off. 
- Compare the difference in power usage of Zoom Workplace and Microsoft Teams with the camera turned off versus with the camera turned on. 
- Evaluate the impact of screen sharing on the power consumption across the two different platforms. 
- Evaluate the impact of background blurring on the power consumption across the two different platforms.
- And lastly, identify which of the two applications is more energy-efficient under different feature configurations and provide insights into how specific features affect the energy consumption of of video conference applications and their implications for sustainable work from home practices.

# Methodology
Include independent and independent variables somewhere

## Experimental setup

### Hardware and Software Environment
Include the different hardware and software variables, as well as our energy measurement tools (energibridge)

Processor: AMD Ryzen 7 7730U with Radeon Graphics (2.00 GHz) 
Installed RAM: 16.0 GB
System Type: 64 Bit operating system, x64-based processor

Windows Specification:
Edition: Windows 11 home
Version: 25H2

## Experiment Design

- What we compare (zoom camera on vs off, etc)
- What they measure (joules etc)
- Saying that we ran 30 tests on each, for reliability etc.

### Controlled Testing Environment
Include zen mode and freeze settings from template
Any other things to note like consistent screen brightness, or closing non-essential apps, turning off notifications, etc. etc.
Mention the shuffling!

And the settings we are using is 100% brightness, volume 30%, using wireless connection, all non essential apps and notifications have been closed. Laptop was left charging. Only thing open is cmd.exe terminal with administrative power.


## Automation and testing procedure 

- 1 script talking to 2 others and energibridge to achieve some functionality
- the cooldowns/fibonacci, the random selection
- Saying we run energibridge for 30s for each test (2) in each iteration

### Replication Package

For the experiments, the replication package can be found in the following [repository](https://github.com/ayushhhkha/SSE_TeamsVsZoom).

## Data Collection and processing 
(2 sentences)


# Results

As mentioned previously, EnergiBridge was used to measure energy consumption. The tool provides the following relevant metrics:
- Delta
- SYSTEM_POWER (Watts)

With the metrics above, the key metrics to be calculated per trial were:
1. Average Power Consumption (W): Calculated by averaging the power readings over the duration of the trial
2. Total Energy Consumption (J): Calculated by multiplying the power consumption by the delta and summing the results over all the samples in the CSV file. 
3. Energy Delay Product: Calculated by multiplying energy by the total time


## Experimental results

- Violet and Box Plot
- Outlier discussion with threshold
- Violet and Box Plot without outliers
## Statistical Analysis

- Shapiro-Wilk
- Welch’s T Test

# Discussion
## Interpretation of Results

## Potential Explanations

## Implications

# Limitations

There are some limitations that will be briefly discussed in this section:

### Limited Test Duration: 

In an actual conference call, it usually lasts more then 10 minutes. However, the experiment was conducted with a 30 second duration in which this interval is quite short and does not reflect the real life usage of the application. 

### Wired Connection: 
Another limitation is the use of wireless connection in which a wired connection would offer a more stable energy reading but this does not reflect real life scenarios since most video conferencing applications work through wireless connections. 

### Singular Operating System: 
Another limitation is that this experiment was conducted in a single machine in which results could vary in different machines such as a Mac or Linux computer. 

# Future Work

For additional work, it would be interesting to observe the experimentation being conducted on a Windows laptop and a MacOS which can lead to an interesting analysis of cross platforms and to determine which application is the most energy efficient in both OS. Another interesting work that can be done is testing out more application in demand such as Google Meet and Slack in order to effectively analyse each video conferencing application and determine the most energy efficient. One more additional work that can be conducted would be to increase the intervals which will increase experimentation time but this will align better with real life situations were video conferencing application are meant for longer usage. With our replication package, the future work can immediately begin.

# Conclusion

Our paper discusses the energy difference between 

# References

1. Sweigart, Al. “Welcome to PyAutoGUI’s Documentation! — PyAutoGUI 1.0.0 Documentation.” Readthedocs.io, 2014, pyautogui.readthedocs.io/en/latest/.

