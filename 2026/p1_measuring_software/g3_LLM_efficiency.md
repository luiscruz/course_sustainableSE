---
author: Maciej Bober, Jeroen Chu, Bill Vi, Joost Weerheim
group_number: 3
title: "Comparing Local LLM Inference Energy Consumption"
image: "img/p1_measuring_software/g3_LLM_efficiency/energy_by_context_size.png"
date: 12/02/2026
summary: |-
    Large language models (LLMs) are increasingly used with supplementary context such as lecture notes, documentation, or retrieved passages to improve output quality. However, the energy cost of processing larger context windows during local inference is poorly understood. This project investigates how varying context sizes (0, 2k, 5k, 10k, and 20k tokens) affect the CPU and GPU energy consumption of a locally deployed 20B-parameter LLM (gpt-oss-20b) answering multiple-choice exam questions. Using EnergiBridge for CPU energy measurement and amd-smi for GPU power monitoring, we conducted 150 automated runs (30 per context size) in a controlled environment. We report total energy consumption, average power draw, and energy-delay product across all context sizes, and apply statistical testing (Shapiro-Wilk, Welch's t-test / Mann-Whitney U) with effect size analysis to assess the significance and magnitude of the observed differences.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

<!-- 
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

Nevertheless, using statistical metrics to measure effect size is not enough – there should be a discussion of the **practical effect size**. More important than demonstrating that we came up with a new version that is more energy efficient, you need to demonstrate that the benefits will actually be reflected in the overall energy efficiency of normal usage of the software. For example, imagine that the results show that a given energy improvement was only able to save one joule of energy throughout a whole day of intensive usage of your cloud software. This perspective can hardly be captured by classic effect-size measures. The statistical approach to effect size (e.g., mean difference, Cohen's-*d*, and so on) is agnostic of the context of the problem at hand. -->

# Introduction
Large Language Models (LLMs) has been prominent for years. Users from different fields want to get the best performance from their LLM model. Now that agentic LLMs are very powerful, many users don't realise what the cost is of running high reasoning models. There is a cost that not many users realise: energy consumption. This is a hidden cost since most LLMs are not locally run but on the cloud. 

Many AI companies have been fine-tuning their LLMs a lot. By optimizing the many hyperparameters the LLM models have, providing task specific data sets, reinforcing fine-tuning, and many more. Users also try to fine-tune their chats with LLM models by providing context in a form of text, images, and files. Users tend to do this so they can get an answer which fits in the context they have provided. Some would argue that this may improve accuracy of the LLMs output. It is not very known if the model is more efficient if the needed context is given for a task. Are LLMs more energy efficient when more context is given?

Let's sketch this scenario: a student has a difficult problem to tackle and he wants to use a LLM model to assist him. Since the problem is part of a graded assignment he wants to get the best possible output of the LLM. He doubts if he wants to provide no context, only the relevant lecture slides for the problem or all the slides of the course. At the end, he assumes that providing the most context will give him the best possible answer of the LLM. Is this assumption right? Will the LLM provide a better answer when no context is given? User chat optimisation by providing context is an integral part of use of LLM models. Hence, measuring the energy consumption of various context size is more relevant than ever.

In this blog post, we will explore how much energy the LLM uses with varying context sizes provided. In our experiment:
* We use the same model with the same model size. In this case, gpt-oss-20b.
* Multiple choice exam questions are given which only one question is right.
* For every question, no context is given or a 2k, 5k, 10k, or 20k tokens context is given.

With this study, we aim to show the energy consumptions for those who wants to fine tune the model with various context sizes.

# Methodology
We have designated a specific system to measure the energy consumption of different context sizes. We aimed to capture the CPU metrics and its energy usage. This section describes the steps taken to ensure consistent and reproducible results.

## Experiment hardware setup
Our chosen LLM model is ran in a specific locally controlled environment. This is to gather unbiased energy data and eliminate variations in results due to using different machines.

The hardware of the machine used for experiments:
* Processor: AMD Ryzen 7 5700X3D @ 3.00Hz
* GPU: AMD Radeon RX 9070 XT 16GB
* Memory: 32GB RAM DDR4 3200 MT/s
* Operating System: Ubuntu 24.04.3 LTS
* Power Monitoring Tool: EnergiBridge

We ran this machine also in similar environment conditions, taking into account the room temperature and run the entire experiment in one execution. This is to reduce the external factors which can influence the results of the experiment. Before we conducted the experiment, all programs which deemed not necessary was properly closed. We only kept the basic tasks running for example, bare minimum operating system services and ethernet connection. In the operation system, we only had a terminal running our Python experiment and LMstudio, which runs our chosen LLM model.

## Chosen model and sizes of context
For our experiment, only one model is used to keep the experiment consistent. We wanted a model with powerful reasoning and can run agentic tasks. This is to ensure that the model will reason with the context provided. Hence we chose for **gpt-oss-20b** (11.28 GB). This model has agentic capabilities and full chain-of-thought. We found this important because we wanted a model with the latest relevant features. This is to ensure our experiment is close to the real-world usage of LLM models. Then, we have fed the LLM model with multiple choice exam questions of CSE1305: Algorithms and Data Structures and one of the summaries of the course.

We have chosen 5 different summary sizes which can serve as context for the exam questions:
1. No summary (0 kB)
2. 2k token summary (12 kB)
3. 5k token summary (31 kB)
4. 10k token summary (61 kB)
5. 20k token summary (121 kB)

Each run with energy measurements ran the same LLM with one of the five summary sizes. The entire experiment is fully automonous for simplicity. Each run outputs a CSV with energy measurements provided by Energibridge.

## Experiment procedure
Our experiment goes as follows:
1. Close all unnecessary programs which can interfere with the energy measurements.
2. Start up the LMstudio daemon.
3. Load gpt-oss-20b and set the max context size on 30k tokens.
4. Run "run_experiment.sh" which includes the Python script feeding the LLM with exam questions and summaries, and Energibridge which gives the energy measurements of the CPU. It has first a 5 minute warmup and a 10 second sleep time between questions. 
5. Retrieve all CSV files. 

## Data integrity
To protect data integrity, we ensure to only generate unbiased data and the external factors has minimal influence with the measurements. For every summary, the experiment is repeared 30 times and we monitored that there is at least an answer for every exam question.
