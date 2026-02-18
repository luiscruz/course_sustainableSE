---
author: Maksym Ziemlewski, Frederik van der Els, Piotr Kranendonk
group_number: 12
title: "Comparing the Energy Consumption of Single-Threaded and Multi-Threaded Programs"
image: "img/gX_template/project_cover.png"
date: 17/02/2022
summary: |-
  Many tasks lend themselves for parallel programming, which can speed up the execution time of the program. Common ways to achieve this is by using multiple threads, and splitting the task into smaller tasks that can be executed in parallel on the different threads.
  
  While this indeed can speed up the execution time, it is very much possible that the overhead of multiple threads increases the energy consumption significantly. That is, despite the program being more efficient (taking less time), it could become more energy consuming.
  
  Our project would compare single-threaded and multi-threaded implementations of the same app. We will investigate how the number of threads used affects energy consumption, and what conclusions the developer should draw based on that.

identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Introduction
Most programs are initially written in a _single-threaded_ fashion. A single-threaded program has only one thread of execution. This means that the program performs one execution at a time, in a sequential matter. This makes developing, debugging and maintaining the program simple, as the program as a whole s easier to reason about. However, many modern operating systems have multi-core processors, which have the capability of executing many tasks in parallel. With single-threaded programs, most of these cores are left unused. This can become especially noticeable if _blocking_ requests are involved, where the execution of the entire program is halted until a task finishes.

A common solution to this program is to make the program _multi-threaded_. Multi-threaded programs run tasks concurrently, or in parallel. Each thread executes its own execution path of the program, allowing the program to execute multiple tasks at a time. Now, a blocking request could be executed on a different thread, allowing to program to continue execution without having to wait for the request to complete.

With many cores being available on modern operating systems, this paradigm becomes increasingly common. The increased efficiency of the program's execution seems like an obvious reason to take advantage of it. However, when making this change, energy consumption is often left out of the equation. In this report, we will investigate how single-threaded and multi-threaded programs compare in energy consumption, and what considerations a developer should take in mind when choosing between the two paradigms.

More specifically, we will investigate the memory usage of the same program differs when given a single-threaded and multi-threaded implementation. For this, we will take into account the transistor density, the overhead of creating a thread, the number of threads used and the effect of reusing threads.

# Methodology
We will use X/Y/Z as testing language. One should note that in this language, ...

We will measure the energy consumption using A/B/C.

# Implementation
To measure the differences in energy consumption, we will use the X/Y/Z as test program. This program lends itself well for this experiment because it is not easily optimised by the compiler/CPU, ...

# Hardware setup
The tests will be performed on Windows, ...

# Results
After running the tests, ...

# Statistical analysis of the results
We will use X/Y/Z to draw conclusions, ...

# Conclusion and future work
A.

# END OF REPORT

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
