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
## Research Objectives

# Methodology
## Hardware and Software Environment
Include the different hardware and software variables, as well as our energy measurement tools (energibridge)
## Controlled Testing Environment
Include zen mode and freeze settings from template
Any other things to note like consistent screen brightness, or closing non-essential apps, turning off notifications, etc. etc.
## Testing Protocol
### Warm up
### Automated testing procedure
Include some cool down to allow environment to return to baseline conditions

# Results
## Experimental results

- Violet and Box Plot
- Violet and Box Plot without outliers
## Statistical Analysis

- Shapiro-Wilk
- Welch’s T Test

# Discussion
## Interpretation of Results
## Implications

# Limitations and Future Work

There were some limitations that should be addressed which was the limited test duration. In an actual conference call, it usually lasts more then 10 minutes. However, the experiment was conducted with a 30 second duration in which this interval is quite short and does not reflect the real life usage of the application. Another limitation is the use of wireless connection in which a wired connection would offer a more stable energy reading but this does not reflect real life scenarios since most video conferencing applications work through wireless connections. Another limitation is that this experiment was conducted in a single machine in which results could vary in different machines such as a Mac or Linux computer. 

Some future work can include the experiment being conducted in two devices in order to reduce the bias and provide an intersting analysis of cross platforms. Increasing the duration into longer intervals can demonstrate real life situations. Testing out more applications in demand such as google meet and slack would provide interesting discussions.

# Conclusion

# References

1. Sweigart, Al. “Welcome to PyAutoGUI’s Documentation! — PyAutoGUI 1.0.0 Documentation.” Readthedocs.io, 2014, pyautogui.readthedocs.io/en/latest/.

