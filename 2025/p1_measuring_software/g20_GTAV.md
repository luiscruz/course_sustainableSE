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
For this experiment Vsync was turned on for both graphic settings. This setting caps the framerate at the monitor refresh rate, 60hz in this case for the computers. If this setting is left off, the game will try to render as many frames as possible, which means the GPU will be at or near maximum utilization regardless of graphic settings.

## Graphics Settings
The number of available options for each graphics setting varies, ranging from 2 to 6 choices.
Most settings have options such as *Normal*, *High*, and *Very High*, while some also include *Ultra* and others are limited to simple *On-Off* options.  

To ensure a clear difference between runs, settings with *On-Off* options were set to *Off* for the low graphics run and *On* for the high graphics run.
For settings with more than two options, we selected the lowest computationally demanding option (*Normal*) for the low run and increased it by two levels for the high run, which was typically *Very High*. 

This selection method was designed to create a noticeable difference in power consumption that could be reliably detected.
The specific settings used are included in appendix A to ensure the replicability of our results.  

## Experiment procedure
Our experiment procedure is outlined below, to ensure the results are reproducable. The experiment first has a startup procedure, followed by a segment to be repeated 15 times for each setting to take the measurements.

1. Ensure notifications are turned off
2. Everything closed (including background applications) except for the Rockstar Launcher and GPU-Z. Running background services (indicated by taskbar icons) are limited to Windows Defender, the Nvidia app and the audio driver
3. Only connected devices are a keyboard, mouse and a monitor
4. The computer is connected to the internet using an ethernet cable (GTA V needs an internet connection to launch)
5. Power mode set to "best performance" in windows
6. Start GTA V
7. Run Benchmark test without measurement
8. GTA V closes automatically after benchmark

Repeat 15 times for low settings and 15 times for high settings:

9. Start a new logging file in GPU-Z with appropriate naming
10. GTA V restarts automatically after benchmark
11. Run benchmark test
12. GTA V closes automatically after benchmark


## Data collection
During the course the software EnergiBridge was recommended for use during the project. We found EnergiBridge to be unsuitable for our purposes as it is less focused on measuring GPU power consumption and therefore started looking for alternative software. We decided instead to use GPU-Z, which records GPU statistics, this fits our purposes as we are running a GPU intensive task and less a CPU intensive task. 

## Hardware/Software Details
The trials were run on two different computer to ensure our findings are consistent. The results of both computers were compared and combined to achieve our final results

### Computer 1: 
- Intel Core i5-9600k
- 16GB DDR4 RAM
- Nvidia GeForce RTX 2060
- Samsung 970 Evo Plus M.2 SSD

### Computer 2: 
- Intel Core i7-7700k
- 16GB DDR4 RAM
- EVGA GeForce GTX 1070
- Samsung 970 Evo Plus M.2 SSD

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

### Low number of experiments
For optimal results it would be desirable to have more than two computers run the experiments. In practice this is not achievable as computers capable of running GTA V come at great cost and we were therefore limited to the amount of capable systems available to us.  

### Only measuring GPU power consumption
To get a more realistic picture of the total power consumption of a game it is desirable to measure the energy consumption of the entire computer while running the game. However, doing so would require a physical device to measure the power consumed by the computer at the wall outlet. This kind of equipment is beyond the scope of this project and therefore it was decided to only measure GPU power consumption, as this is possible using software tools and the GPU is the most strained component while running the game.

# Conclusion


# Appendix

## A: Graphics Settings

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
