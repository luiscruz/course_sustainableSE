---
author: Luc Dop, Sabina Grădinariu, Nawmi Nujhat, Vincent van Vliet
title: "Energy Consumption Comparison: Python 3.14 vs Python 3.11"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 24/02/2025
summary: |-
   This study explores the energy consumption differences between Python 3.14 and Python 3.11, testing the claim that Python 3.14 has a 30% speed improvement over previous versions. We run the same computational tasks in controlled environments and measure power usage, execution time, and efficiency. Our setup includes automation, Docker containers, and system configurations to ensure replicability.
---
We decide to investigate the claim that python 3.14 has an improvements of up to 30% in speed and how that impacts the energy consumption. To investigate this idea is to use the prerelease version of 3.14 python interpreter and compare the energy consumption for a code snippet of this interpreter vs an older interpreter, to see whether faster speeds impact energy consumption

[//]: # (This article is divided into two main parts: 1&#41; how to set up energy measurements with minimum bias, and 2&#41; how to analyse and take scientific conclusions from your energy measurements.)

[//]: # (Read on so that we can get your paper accepted in the best scientific conference.)

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

