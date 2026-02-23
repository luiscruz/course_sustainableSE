---
author: Fedor Baryshnikov, Jari de Keijzer, Tobias Veselka, Stilyan Penchev
group_number: 27
title: "Title of the Template blog"
image: "img/gX_template/project_cover.png"
date: 12/03/2026
summary: |-
  This study will focus on analysing the energy consumption of two LLM-related tasks. Firstly, we will analyse how the length of a question input prompt affects the energy consumption of an LLM generating a response. Secondly, we will study three different models by three different developers and compare their energy efficiency when generating a response to a question.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
<!-- ---
This problem takes another level if we are counting on these measurements to make **groundbreaking research contributions** in this area. Some research projects in the past have underestimated this issue and failed to produce replicable findings. Hence, this article presents a roadmap on how to properly set up a scientific methodology to run energy efficiency experiments. It mostly stems from my previous work on [doing research and publishing](/publications) on Green Software.

This article is divided into two main parts: 1) how to set up energy measurements with minimum bias, and 2) how to analyse and take scientific conclusions from your energy measurements.
Read on so that we can get your paper accepted in the best scientific conference.
---
<!-- #### 👉 Note 1:

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

Nevertheless, using statistical metrics to measure effect size is not enough – there should be a discussion of the **practical effect size**. More important than demonstrating that we came up with a new version that is more energy efficient, you need to demonstrate that the benefits will actually be reflected in the overall energy efficiency of normal usage of the software. For example, imagine that the results show that a given energy improvement was only able to save one joule of energy throughout a whole day of intensive usage of your cloud software. This perspective can hardly be captured by classic effect-size measures. The statistical approach to effect size (e.g., mean difference, Cohen's-*d*, and so on) is agnostic of the context of the problem at hand.  -->

# LLMs: an energy consumption study

## Introduction

In November 2022, OpenAI released ChatGPT(Matt Casey, 2023)[https://snorkel.ai/large-language-models] - arguably the first Large Language Model (LLM) available to the general public. This, alongside the recent Artificial Intelligence (AI) revolution, marked a real turn in what we perceive computers to be capable of - no longer could programs only deal with scenarios pre-defined by a programmer; they now also (appeared to) reason for themselves. However, LLM developers have notably received a vast amount of criticism for the hugh energy consumption required to run such LLMs.

This study will aim to analyse the energy consumption of LLMs. Specifically, it is our goal to address two specific questions - first, we will study how the length of a question input prompt affects the energy consumption of an LLM producing its response. Second, we will compare three different 8 Billion parameter models, rjn-1, Llama 3.1 and Deepseek-r1 (developed by Essential AI, Meta and Deepseek respectively) compare in terms of their energy efficiency when evaluating on the same prompts.

## Methodology

Before we begin our tests, we must minimise the effect of external factors on our test results. Thus, the following measures have been taken:

1. Monitor set to 50% brightness
2. All applications aside from VS Code and Ollama (used to run our LLMs) closed
3. Wi-Fi and BlueTooth disabled
4. 

Additionally, all of our tests will be run on the same hardware:

### Part 1: The significance of a prompt's length on an LLM's energy efficiency

For our first part, we chose to use Deepseek's deepseek-r1 1.5 Billion parameter model. This is the only model we will be using for this test to limit the effect of model infrastructure, parameter size and any other factors that could affect this test.

## Citations
