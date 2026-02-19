---
author: Anhar Al Haydar, Tom Clark, Moniek Tummers, Andriana Tzanidou
group_number: 4
title: "Comparing Energy Consumption in Computer Vision Across Different Model Sizes"
image: "img/g4_cv_energy_comparison/g4_project_cover.png"
date: 12/02/2026
summary: |-
  In this project, we aim to investigate how different model sizes of a computer vision AI model affect energy consumption. We want to compare small, medium, large weight variants of the same open-source model such as RF-DETR or YOLOV8 to see how scaling impacts energy usage. Identical use cases will be run across all model sizes while measuring energy consumption with tools like EnergiBridge.  
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---
# Introduction

Object detection using computer vision AI models is becoming increasingly common in modern technologies, including autonomous vehicles, medical imaging systems, warehouse robotics, and traffic monitoring. Continuous improvements to these models have led to higher detection accuracy and overall performance. However, these performance gains come with increased computational cost. Training and deploying large neural networks require substantial energy resources, and as AI adoption continues to scale, understanding the energy implications of model design choices becomes increasingly important.

YOLOv8 is an open-source computer vision model designed for object detection tasks. It is available in multiple parameter sizes, ranging from Nano (3.2 million parameters) to Extra Large (68.2 million parameters). Larger variants containing more parameters achieve higher mean average precision, however, the increased number of parameters also requires more computations and memory access, which will decrease speed and can increase energy consumption. 

RF-DETR is an open-source computer vision model designed for object detection tasks. It is available in multiple parameter sizes, ranging from Nano (30.5 million parameters) to 2XL (126.9 million parameters). Larger variants containing more parameters achieve higher mean average precision, however, the increased number of parameters also requires more computations and memory access, which will decrease speed and can increase energy consumption.  

In this study, energy consumption and detection accuracy will be evaluated using the same set of images to determine how these metrics are affected by differences in parameter size when the model processes images. Comparing different sizes of the same architecture allows us to isolate the impact of model scaling while keeping the underlying design consistent. Energy usage will be measured using EnergiBridge while using the same hardware and keeping software settings the same to ensure a fair comparison across model sizes.

We hypothesize that energy consumption will increase with model size due to the greater computational workload required. However, this relationship may not be perfectly linear. Additionally, although larger models often achieve higher detection accuracy, the performance gains may not always justify the additional energy cost. Therefore, this study will analyze how increases in energy consumption relate to improvements in detection performance, providing insight into the trade-off between accuracy and energy efficiency.

# Methodology
# Results
# Discussion
# Conclusion
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

