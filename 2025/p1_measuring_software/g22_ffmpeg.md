---
author: Student1 first and last name, Student2, Student3
title: "Comparing H.264 and H.265 video decoding energy consumption"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
  abstract Lorem ipsum dolor sit amet, consectetur adipisicing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
  reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
  pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
  culpa qui officia deserunt mollit anim id est laborum.
---

## Introduction
Video decoding is a process that occurs almost constantly in everyday digital life. Whether watching videos on streaming platforms like YouTube or Netflix, participating in video calls,  or scrolling through social media, video decoding happens continuously across billions of devices worldwide. 

As video streaming and high-definition content become increasingly prevalent, the energy efficiency of video decoding has become a critical concern. With the rise of mobile devices, cloud-based streaming services, and embedded systems, understanding the power consumption of video decoding is essential for minimizing environmental impact, reducing overall energy costs, and optimizing battery life.

Two widely used video compression standards, H.264 (AVC) and H.265 (HEVC), dominate modern video encoding. H.265, the newer standard, promises superior compression efficiency, reducing bandwidth usage while maintaining visual quality. However, its increased computational complexity raises questions about its energy efficiency during decoding. While H.265 is more efficient in terms of storage and transmission, its impact on energy consumption during playback remains an open question.

By measuring and comparing the energy consumption of H.264 and H.265 video decoding on different CPU's, this study aims to provide insights into the sustainability of modern video technologies. The findings could help software developers, hardware manufacturers, and content distributors make informed decisions about choosing the optimal codec for energy-conscious and environmentally responsible applications.

### Research Question  

How does the energy consumption of video decoding compare between the H.264 and H.265 formats,  
and what are the implications for device efficiency and environmental sustainability?

## Experiment Setup
### Hardware & Software
We will conduct tests on:
<!--computer, fixed environment settings, CPU, RAM and etc-->

### Tools & Methods
To measure energy consumption, we will use:

### Metrics <!--Data Collection-->
We will measure:
- **Encoding Power Consumption:** 
- **Decoding Power Consumption:** 

## Decoding Experiment
### Methodology

### Metrics Collected
- **Energy Consumption:** 
- **Decoding Time:** Time taken to decode each format.

### Results

# Energy Consumption at 480p: H.264 vs. H.265

## Initial Observations
We visualized our results using a combination of violin plots and box plots, which provided a clear picture of energy consumption distribution for both codecs. The majority of H.264 decoding instances clustered around 25 J, while H.265 decoding results were centered around 36 J. However, both distributions contained some higher-energy outliers, particularly in H.265, where some values reached 39 J.

![Energy Consumption Violin + Box Plot for H.264 tests](experiment_plots/Gijs_violin_box_decode_480p_h264.png)

![Energy Consumption Violin + Box Plot for H.265 tests](experiment_plots/Gijs_violin_box_decode_480p_h265.png)


One immediate takeaway is that H.265 consistently required more energy than H.264 for 480p decoding. 

![Energy Consumption Violin + Box Plot Comparison](experiment_plots/Gijs_combined_violin_box_decode_480p.png)



But how significant is this difference? To dig deeper, we needed to validate these observations with statistical tests.

## Checking for Normality
Since our data did not visually appear normally distributed, we conducted the Shapiro-Wilk test to formally test normality:

- **H.264**: W = 0.8023, p-value = 0.0001  
- **H.265**: W = 0.5708, p-value = 0.0000  

With p-values well below 0.05, both distributions deviate significantly from normality. This confirms our suspicion that a simple parametric test assuming normality wouldn't be appropriate.

## Outlier Removal & Data Distribution
To ensure extreme values weren’t skewing our results, we applied outlier removal using a Z-score threshold of 3 (within standard deviations). Interestingly, this step had minimal impact—suggesting that most of our data points were valid and not extreme anomalies. We verified this by comparing histograms before and after filtering, which showed no major changes in distribution.

![Energy Consumption Violin + Box Plot Comparison](experiment_plots/Gijs_combined_violin_box_decode_480p_filtered_results.png)



### Discussion
<!-- - Does H.265’s complexity increase playback power consumption?
- What are the implications for streaming platforms like YouTube? -->


## Summary & Key Takeaways
### Recap of Findings


### Trade-offs Between Compression Efficiency and Decoding Energy
<!-- - Efficient compression saves storage and bandwidth.
- Higher computational complexity may increase device power consumption. -->

### Impact on Global Energy Consumption
- Streaming billions of hours of video significantly contributes to energy usage.
- Optimizing codecs can reduce power demand in video streaming.

### Potential Improvements
<!-- if decoding H.265 is similar to H.264 and the file size is smaller and this the network transmission will consume less energy then H.265 should become a new standard. (Devices also should support this compression method) -->

---

## Replication Package
### How to Reproduce the Experiment


### Resources Provided

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

