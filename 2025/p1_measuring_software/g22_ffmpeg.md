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

#### Energy Consumption at 480p: H.264 vs. H.265

To evaluate the energy efficiency of H.264 and H.265 decoding, we analyzed energy consumption across 480p, 720p, and 1080p resolutions.

We visualized our results using a combination of violin plots and box plots, which provided a clear picture of energy consumption distribution for both codecs. 

![Energy Consumption Violin + Box Plot Comparison for 480p](experiment_plots/Gijs_combined_violin_box_decode_480p_filtered_results.png)

![Energy Consumption Violin + Box Plot Comparison for 720p](experiment_plots/Gijs_combined_violin_box_decode_720p_filtered_results.png)

![Energy Consumption Violin + Box Plot Comparison for 1080p](experiment_plots/Gijs_combined_violin_box_decode_1080p_filtered_results.png)


One immediate takeaway is that H.265 consistently required more energy than H.264 for all resolutions. But how significant is this difference? To dig deeper, we needed to validate these observations with statistical tests.

1. Checking **Normality**. We used the **Shapiro-Wilk** test to assess whether the energy consumption data followed a normal distribution. A p-value < 0.05 indicates significant deviation from normality, meaning the data is not normally distributed.

2. **Outlier Removal**. To ensure extreme values weren’t skewing our results, we applied outlier removal using a **Z-score** threshold of 3 (within standard deviations). Interestingly, this step had minimal impact—suggesting that most of our data points were valid and not extreme anomalies. We verified this by comparing results before and after filtering, which showed no major changes in distribution.


3. Then we chose the **Statistical Test**. If both distributions were normal, we applied **Welch’s T-test**, which compares means while accounting for unequal variances. Otherwise, we used the **Mann-Whitney U test**, a non-parametric test suitable for comparing medians.


| Resolution | Normality (H.264) | Normality (H.265) | Statistical Test Used | Energy Difference (J) | Relative Difference (%) |  
|------------|------------------|------------------|--------------------|-----------------|-----------------|  
| **480p**   | ❌ Non-normal (p = 0.0002) | ❌ Non-normal (p = 0.0000) | **Mann-Whitney U** | 10.72 J | **30.00%** (H.264 more efficient) |  
| **720p**   | ❌ Non-normal (p = 0.0010) | ✅ Normal (p = 0.6275) | **Mann-Whitney U** | 16.09 J | **25.18%** (H.264 more efficient) |  
| **1080p**  | ✅ Normal (p = 0.2624) | ✅ Normal (p = 0.9251) | **Welch’s T-test** | 24.58 J | **19.36%** (H.264 more efficient) |  

From the table above we can see that:
* H.264 is consistently more energy-efficient than H.265 across all tested resolutions.
* The percentage efficiency gap narrows as resolution increases, but the absolute difference in Joules increases.
* Statistical tests confirm a significant difference in all cases, proving that H.265 requires more energy to decode.


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

