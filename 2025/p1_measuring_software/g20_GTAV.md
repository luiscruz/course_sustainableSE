---
author: Seyidali Bulut, Student2, Student3
title: "Energy consumption comparison between different graphics settings in GTA V "
image: "../img/p1_measuring_software/g20_GTAV/cover.png"
date: 28/02/2025
summary: |-
  This experiment analyses the energy consumption of GTA V under different graphics settings to determine the increase in energy usage from low to high settings. To ensure our results are not dependent on a single computer, we use multiple machines to run the in-game integrated benchmark test 15 times for each graphics setting. The collected data highlights the differences in energy consumption across various graphical configurations.
---

# Introduction


The increased use of computers has led to a rise in global energy consumption. 
It is estimated that software will account for 51% of all electricity usage as early as 2030. 
This means that software will be responsible for 23% of global greenhouse gas emissions in the coming decades [(Andrae & Edler, 2015)](https://www.mdpi.com/2078-1547/6/1/117).
As a result, software companies are placing greater emphasis on sustainability to create long-term value without harming the environment.


A branch of existing software systems that is constantly growing is the gaming industry, with about 2.6 billion global gamers and gaming titles available on almost every digital device, making video games one of the most popular and enduring hobbies worldwide [(Topic: Video Gaming Worldwide, 2024)](https://www.statista.com/topics/1680/gaming/#topicOverview). 
To satisfy this massive player base, companies strive to develop games with greater realism, improved physics engines, and enhanced graphics, all of which require more computational power. 
This is evident in the gaming industry, where new games demand increasingly advanced GPUs as minimum requirements. 
Despite this vast player base, the gaming industry has not been as proactive in addressing environmental sustainability as other computing technology sectors [(Pérez et al., 2024)](https://arxiv.org/abs/2402.06346).  


As a result of the ever-growing impact of the gaming industry on the environment we decided to investigate the difference in energy consumption for high graphic settings in games in comparison to low graphic settings. To achieve this goal we decided to measure the difference in energy usage within a single game at different graphic settings. For this study, we selected *GTA V*, which still has 30 million active monthly players 12 years after its release [(Xoob & Xoob, 2024)](https://activeplayer.io/grand-theft-auto-v/). This game was not only selected for its relevance, but also because it is playable over a wide array of graphic settings, supporting both modern powerful GPU's and lower-tier older GPU's. 

To ensure the reproducibility of the experiment, we used the game's built-in benchmark test across multiple computers. Our results show that...............


# Methodology
During the experiment, it was crucial to measure the energy consumption of the selected game as accurately as possible while minimizing interference from other background programs.
This is essential for ensuring the reproducibility of our results across different computers.
A background program that significantly affects energy consumption in one test might not be running on another system, leading to inconsistencies in the results.
To achieve this, we closed all unnecessary programs, keeping only essential background services running.
These were indicated by taskbar icons and included Windows Defender, the NVIDIA app, Epic Games Launcher, Rockstar Launcher, and the audio driver.  

Furthermore, we placed emphasis on warming up the system before starting the experiment and allowing cooldown periods between each run.
This was achieved by running a non-recorded warm-up benchmark test before data collection and restarting the game between runs, which takes about a minute to ensure proper cooldown.  

We compared two different graphics settings, classified as a low graphics quality run and a high graphics quality run.
On each computer, we ran the benchmark test 15 times for both the low and high settings, totaling 30 runs per PC.
Initially, we considered running a higher number of tests per setting, but given that each benchmark test takes approximately 3 minutes per run, we realized this would require a significant amount of time.
To ensure reliable results, we conducted the same experiments on different PCs.
This allowed us to compare the results and determine whether the difference in energy consumption between low and high settings on a single PC was consistent across multiple systems.  

vsync

## Graphics Settings
The number of available options for each graphics setting varies, ranging from 2 to 6 choices.
Most settings have options such as *Normal*, *High*, and *Very High*, while some also include *Ultra* and others are limited to simple *On-Off* options.  

To ensure a clear difference between runs, settings with *On-Off* options were set to *Off* for the low graphics run and *On* for the high graphics run.
For settings with more than two options, we selected the lowest computationally demanding option (*Normal*) for the low run and increased it by two levels for the high run, which was typically *Very High*.  

This selection method was designed to create a noticeable difference in power consumption that could be reliably detected.
The specific settings used will be included in the appendix to ensure the replicability of our results.  
**To Do** 
Add screenshot/table of our settings for different runs.

## Experiment procedure
 **To Do**
 Write this section with the information below.
1. Everything closed except for GTAV and GPU-Z
2. Notifications off
3. Keyboard, mouse, monitors and ethernet are the only connected devices (someone said GTAV needs an internet connection to launch)
4. Background services (indicated by taskbar icons) are only windows defender, the nvidia app, epic games launcher, rockstar launcher and my audio driver
5. Power mode set to "best performance" in windows
6. One benchmark without any measurement as a warm-up run
7. Pause/sleep between executions achieved by having to restart GTAV after a benchmark and setting GPU-Z to log to a new file


## Data collection
 **To Do**
 Explain that we have used gpu-z and why we used it? 

## Hardware/Software Details
 **To Do**
 Explain that the used computers had different specifications. We can shortly mention the specification of each computer here. If the rapport exceeds the word count than this section can be replaced to appendix.

## Evaluation
**To Do**
Explain which formula and variables are used to calculate power consumption and why these were used. If it is possible, refer to sources.

# Results
**To Do**
Add results in different graphs

# Analysis
**To Do**
Explain shortly the difference in statistical and practical significance.

## Statistical significance
**To Do**
Is there a statistical significant difference in power consumption between the runs?

## Practical significance
**To Do**
Is this difference in power consumption big enough that it is also significant in real life? For example, when it is compared to average/total energy consumption of the game/pc?

# Discussion
##
**To Do**
Do the results show a significant difference in energy consumption and do we think that game industry should strive for more energy efficient games?

## Limitations & future work
**To Do**
Explain that this experient can be extended to mac, playstation, xbox etc. Cloud gaming can be included etc.

# Conclusion


# Appendix

## Graphics Settings

### Low Run
| Name | Setting | 
|---|---|
| FXAA | On |
| MSAA | x4 |
| NVIDIA TXAA | On |
| VSync | On |
| Pause Game On Focus Loss | On |
| Population Density | 100% |
| Population Variety | 100% |
| Distance Scaling | 100% |
| Texture Quality | Normal |
| Shader Quality | Normal | 
| Shadow Quality | Normal |
| Reflection Quality | Normal |
| Reflection MSAA | Off |
| Water Quality | Normal |
| Particles Quality | Normal |
| Grass Quality | Normal |
| Soft Shadows | Soft |
| Post FX | Normal |
| Motion Blur Strength | 0% |
| In-Game Depth Of Field Effects | Off |
| Anisotropic Filtering -| Off |
| Ambient Occlusion | Off |
| Tessellation | Off |

### High Run
| Name | Setting | 
|---|---|
| FXAA | On |
| MSAA | x4 |
| NVIDIA TXAA | On |
| VSync | On |
| Pause Game On Focus Loss | On |
| Population Density | 100% |
| Population Variety | 100% |
| Distance Scaling | 100% |
| Texture Quality | Very High |
| Shader Quality | Very High | 
| Shadow Quality | Very High |
| Reflection Quality | Very High |
| Reflection MSAA | x4 |
| Water Quality | Very High |
| Particles Quality | Very High |
| Grass Quality | Very High |
| Soft Shadows | Softest |
| Post FX | Very High |
| Motion Blur Strength | 0% |
| In-Game Depth Of Field Effects | On |
| Anisotropic Filtering -| x4 |
| Ambient Occlusion | High |
| Tessellation | Very High |
