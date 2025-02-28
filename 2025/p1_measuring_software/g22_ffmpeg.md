

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

How does the energy consumption of video decoding compare between the H.264 and H.265 codecs,  and what are the implications for device efficiency and environmental sustainability?

## Experimental Setup

### Environment
We will conduct tests on:
<!--computer, fixed environment settings, CPU, RAM and etc-->


During these experiments, we minimized background activity to reduce external interference. Wi-Fi and Bluetooth were disabled, and airplane mode was enabled. The screen was turned off, and the device remained connected to the charger throughout the experiment to ensure consistent power conditions.

### Tools & Methods
We evaluate the energy consumption of the H.264 and H.265 codecs by encoding a single video at different resolutions using both codecs in MP4 format. We then decode the entire video to measure and compare the energy consumption associated with the decoding process for each codec.

Encoding and decoding were performed using [FFmpeg](https://www.ffmpeg.org/), a free and open-source software suite used for handling multimedia files. Both H.264 and H.265 are lossy compression formats, where the Constant Rate Factor (CRF) determines the level of quality loss—lower values retain higher quality at the cost of larger file sizes. Additionally the preset controls the trade-off between encoding speed and compression efficiency. For this experiment, videos were encoded using **CRF 23** and the **medium preset**, which are the default settings in FFmpeg. These values provide a balanced trade-off between compression efficiency, encoding speed, and output quality.


We measure energy consumption using [EnergiBridge](https://github.com/tdurieux/EnergiBridge). Each decoding experiment is repeated 30 times, with a 1-minute break between runs to prevent residual CPU activity from affecting subsequent measurements.

Energy consumption is measured from the start of decoding until completion. To prevent file writing from affecting the results, the decoded video is directed to a null output, avoiding delays caused by writing large uncompressed video files. This approach aligns with real-world use cases, where videos are typically buffered and displayed on-screen rather than written to disk.

We chose this method over playing the actual video to isolate the decoding process. However, in real-world scenarios, video decoding may not always occur all at once, as streaming and playback often involve partial or on-demand decoding.

### Video specifications and encoding results
The video used for the experiment was downloaded from the TU Delft YouTube channel in 4K resolution and can be found [here](https://www.youtube.com/watch?v=rlVE2fivjs4). It has a duration of 1 minute and 44 seconds with a frame rate of 25 fps. Originally encoded in VP9, the video was transcoded into H.264 and H.265 at three different resolutions: 480p, 720p, and 1080p. This resulted in the following set of videos:

| **Encoding** | **Resolution** | **Bitrate** | **File Size** | 
|-|-|-|-| 
| VP9 (Original)| 3840x2160 |7731 kbps | 95.9 MB |
| H.264 | &nbsp; 854x480 | 700 &nbsp; kbps | 8.76 MB | 
| H.264 | 1280x720 | 1291 kbps | 16.0 MB | 
| H.264 | 1920x1080 | 2689 kbps | 33.4 MB | 
| H.265 | &nbsp; 854x480 | 619 &nbsp; kbps | 7.76 MB |
| H.265 | 1280x720 | 1026 kbps | 12.8 MB |
| H.265 | 1920x1080 | 1853 kbps | 23.0 MB |

We observe that H.265 indeed achieves better compression, particularly at higher resolutions. While we cannot guarantee that the video quality of H.264 and H.265 is exactly the same, using a fixed constant rate factor (CRF) and preset ensures that the quality remains comparable across both codecs.

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
<!-- A comparison of energy consumption when decoding both formats. -->

### Discussion
<!-- - Does H.265’s complexity increase playback power consumption?
- What are the implications for streaming platforms like YouTube? -->

## Limitations
### **Impact of File Size**
H.265 offers significantly more efficient compression, resulting in smaller file sizes. This reduction can lower energy consumption in areas not measured in our experiments, such as networking and disk access, beyond just reducing storage requirements. Future research could further investigate these aspects to better understand the overall energy impact and determine the optimal codec choice for different use cases.

### **Limited generalization**
Our study was conducted using a single video, which may limit the generalizability of the results. Additionally, we only tested the default constant rate factor and preset settings, meaning performance and energy consumption may vary under different encoding configurations. Future research should investigate a broader range of videos and encoding parameters to provide more comprehensive insights.

### **Hardware dependant**


### **Hardware acceleration**
This study did not take advantage of hardware acceleration. Utilizing specialized hardware such as GPUs or dedicated video encoding/decoding units could lead to different energy consumption results. Future work could include testing with hardware acceleration to assess its impact on energy efficiency.

## Challenges Encountered
During our experiments, we attempted to measure the energy consumption of the video **encoding** tasks with **EnergiBridge**, but unfortunately, we encountered issues that prevented the tool from functioning as expected. Despite multiple troubleshooting attempts, we were unable to gather reliable data from these trials.

### Corner cases?


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
Instructions on how to reproduce the experiment can be found on our [GitHub Repository](https://github.com/JamilaSeyidova/sse-group22).

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

