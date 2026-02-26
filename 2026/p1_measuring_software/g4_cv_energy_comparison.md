---
author: Anhar Al Haydar, Tom Clark, Moniek Tummers, Andriana Tzanidou
group_number: 4
title: "Comparing Energy Consumption in Computer Vision Across Different Model Architectures"
image: "img/g4_cv_energy_comparison/g4_project_cover.png"
date: 12/02/2026
summary: |-
  In this project, we aim to investigate how different computer vision AI architectures affect energy consumption. We want to compare two open-source models, RF-DETR and YOLOv8, to see how transformer-based versus CNN-based designs impact energy usage. Identical use cases will be run across both models while measuring energy consumption with tools like EnergiBridge. 
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---
# Introduction

Object detection using computer vision AI models is becoming increasingly common in modern technologies, including autonomous vehicles, medical imaging systems, warehouse robotics, and traffic monitoring. Continuous improvements to these models have led to higher detection accuracy and overall performance. However, these performance gains come with increased computational cost. Training and deploying large neural networks require substantial energy resources, and as AI adoption continues to scale, understanding the energy implications of model design choices becomes increasingly important.

YOLOv8 (You Only Look Once version 8) is an open-source computer vision model developed by Ultralytics and introduced at the beginning of 2023. It is used for object detection tasks and image classification. The architecture consists of two major parts. The first part is the backbone, which consists of sequential convolutional layers that extract features from the input image. The second part is the head, which uses convolutional layers to estimate bounding boxes and class probabilities using the features extracted by the backbone.[^2] The model is available in multiple parameter sizes, ranging from Nano (3.2 million parameters) to Extra Large (68.2 million parameters).[^1] 

RF-DETR (Roboflow Detection Transformer) is an open-source computer vision model designed by Roboflow and introduced in 2026. Similar to the YOLOv8 model, the RF-DETR model has two main parts. The backbone uses DINOv2 pre-trained weights to extract features of the input image.[^4] DINOv2 is a pre-trained self-supervised visual model trained using a Vision Transformer.[^5] The second part is the head, which uses a set of learned query tokens that attend to the features from the backbone through a Transformer decoder. Each query predicts the location of an object, its class, and optionally a segmentation mask.[^4] The model is available in multiple parameter sizes, ranging from Nano (30.5 million parameters) to 2XL (126.9 million parameters).[^3]

In this study, energy consumption will be measured using the same set of images to determine how different model architectures affect energy usage. Comparing RF-DETR and YOLOv8 at similar model sizes allows us to isolate the impact of architectural design on energy efficiency while keeping parameter counts roughly consistent. Energy usage will be measured using EnergiBridge on the same hardware with identical software settings to ensure a fair comparison between the two models.

Based on the experimental setup, we pose the following research questions:
1. How does model architecture affect energy consumption in object detection under similar model sizes?
2. Is there a significant difference in energy consumption between CNN-based and transformer-based architectures during inference under identical conditions?

We hypothesize that RF-DETR and YOLOv8 will differ in energy consumption even when their model sizes are similar, due to differences in architectural design and computational patterns.

# Methodology
To understand how different computer vision architectures influence energy consumption we conducted an experiment comparing YOLOv8m and RF-DETR Medium. For the experiment we chose the medium size of both models to represent a mid-range design within each architecture family. The models differ slightly in parameter count (25.9M vs 33.7), but this is expected as their architectural design is different and thus we treat it as part of the comparison. 

Both models are evaluated on the same set of images drawn from the COCOval2017[https://cocodataset.org/#home], a very popular benchmark in object detection research. This dataset contains 5,000 images but we decided to run our experiment on a randomly selected subset, choosing 500 images for warmup purposes and 1500 for energy measurements, due to the limited resources and timeframe of the project. We used the same 1500 images and in the same order for both models to guarantee that each model processed the exact same workload under the same conditions. 

Before running any measurements, the pretrained weights for both models were downloaded to ensure that the energy measurements would not be influenced.

### Experiment Setup
All experiments were conducted on the same hardware and software environment to avoid confounding effects related to system configuration. 

#### Hardware and Software Specifications:
- **CPU:** Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
- **GPU:** NVIDIA Quadro T1000 Max-Q, 4GB VRAM (TDP 35W)
- **Memory:** 16GB RAM
- **Operating System**: Ubuntu 24.04.4
- **NVIDIA Driver:** 580.126.09 | CUDA 13.0

We measured energy consumption using Energibridge [https://github.com/tdurieux/EnergiBridge].Energibridge is an energy profiler which collects CPU and GPU energy usage data during program execution.

Before running the experiment, we had to minimize any confounding factors that could influence the energy measurements. For this we followed the "Zen mode" [https://luiscruz.github.io/2021/10/10/scientific-guide.html] strategy. We closed any applications or unnecessary background services that were running and made sure to turn off all notifications. Additionally, we disconnected all external hardware and turned off the wifi. Moreover, we froze our settings [https://luiscruz.github.io/2021/10/10/scientific-guide.html] by disabling automatic brightness adjustment, idle deeming and setting the brightness to the lowest end at 242. 
We kept the machine plugged into an external power source throughout the experiment to avoid power fluctuations. Lastly, we performed all experiments at a stable temperature of 23.5℃.

### Experiment Procedure
To avoid-cold start effects, we warmed up both the CPU and GPU for 5min each. For warming up the CPU we repeatedly ran a Fibonacci sequence and for warming up the GPU we ran the two models on the warmup dataset.

During the experiment, both YOLOv8m and RF-DETR Medium processed images one at a time rather than in batches. This decision was made to prevent computation costs across multiple images and to allow precise measurements of energy consumption and execution time per-image. 

We executed the experiment using a fixed sequence of inference  runs. We generated a shuffled list of 60 runs in advance, consisting of 30 executions of YOLOv8m and 30 executions of RF-DETR Medium to distribute the bias more evenly across the two executions. Before each execution run, the system was put to sleep for 30 seconds to prevent tail energy consumption from previous measurements. We chose a sleep of 30 seconds since each energy test for each model was less than 3min. For each interference run energy was measured using EnergiBridge. Once the measurements were complete, the results were saved to a SCV file for later analysis.



### Replication Package  
A replication package can be found [here](https://github.com/riritz/Sustainable_SE). 
# Results
# Discussion
# Conclusion
# References

[^1]: Ultralytics. (n.d.). YOLOv8 models documentation. Retrieved February 22, 2026, from https://docs.ultralytics.com/models/yolov8/

[^2]: Sohan, M., Sai Ram, T., Rami Reddy, C.V. (2024). A Review on YOLOv8 and Its Advancements. In: Jacob, I.J., Piramuthu, S., Falkowski-Gilski, P. (eds) Data Intelligence and Cognitive Informatics. ICDICI 2023. Algorithms for Intelligent Systems. Springer, Singapore. https://doi.org/10.1007/978-981-99-7962-2_39

[^3]: Roboflow. (n.d.). rf-detr [Computer software]. GitHub. Retrieved February 22, 2026, from https://github.com/roboflow/rf-detr

[^4]: Isaac Robinson, P. Robicheaux, M. Popov, Deva Ramanan, & N. Peri. (2026). RF-DETR: Neural architecture search for real-time detection transformers. arXiv. https://arxiv.org/abs/2511.09554

[^5]: Maxime Oquab, T. Darcet, T. Moutakanni, H. Vo, M. Szafraniec, V. Khalidov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby, M. Assran, N. Ballas, W. Galuba, R. Howes, P.-Y. Huang, S.-W. Li, I. Misra, M. Rabbat, V. Sharma, G. Synnaeve, H. Xu, H. Jégou, J. Mairal, P. Labatut, A. Joulin, & P. Bojanowski. (2024). DINOv2: Learning robust visual features without supervision. arXiv. https://arxiv.org/abs/2304.07193

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

