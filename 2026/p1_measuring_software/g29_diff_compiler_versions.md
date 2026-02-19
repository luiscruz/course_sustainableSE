---
author: Tess Hobbes, Kristian Hristov, Nina Semjanova
group_number: 29
title: "Comparing the energy consumption of running oxipng benchmarks using different Rust compiler versions"
image: "img/gX_template/project_cover.png"
date: 12/02/2026
summary: |-
  TODO
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---
### Proposal for the project
## Why oxipng
1. Contains benchmarks
2. The Rust compiler version is hopefully not too hard to switch out programmatically
3. The project is not too big

Maybe we should find another codebase that also meets the requirements but that is also guaranteed to be compilable on Rust versions released a long time ago. 

Plan:
1. Rent a server or run it on our own hardware (preference goes out to the server to have less variability between tests; if it’s a server, maybe try and see if we can rent it somewhere with renewable power in the spirit of the course). 
2. Compile the program that we want to measure using the different Rust versions. 
3. To keep the power usage equal between runs, warm up the CPU using an artificial load, while monitoring the temperature, until it starts to throttle. 
4. Run the benchmarks back-to-back, using the built-in CPU power meters we measure the power consumed by running the different benchmarks benchmark. 

Basic version:
1. Skip out on the warming of the CPU. Just use two different Rust compilers, possibly the oldest and the newest. 
2. Run the benchmarks, making sure there’s a bit of time between the runs, measuring the power consumed by running the benchmarks using the built-in CPU power meters. 

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

