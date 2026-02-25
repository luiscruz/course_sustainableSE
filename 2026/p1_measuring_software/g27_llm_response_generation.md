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

# LLM Prompting: an energy consumption study

## Introduction

In November 2022, OpenAI released ChatGPT ([Matt Casey, 2023](https://snorkel.ai/large-language-models)) - arguably the first Large Language Model (LLM) available to the general public. This, alongside the recent Artificial Intelligence (AI) revolution, marked a real turn in what we perceive computers to be capable of - no longer could programs only deal with scenarios pre-defined by a programmer; they now also (appeared to) reason for themselves. 

However, with subsequent research into the LLM-production pipeline, LLM developers have received a vast amount of criticism for the negative social and environmental impact that LLMs and their production cause. Arguably the most common criticism of LLMs developers is the unethical and oftentimes illegal sourcing of training data for their models. These claims often touch base on the infringement of copyright or GDPR to prove the wrong-doings of LLM developers. However, another aspect that must be considered is the environmental impact of LLMs - specifically, the energy consumed to both test and train these LLMs. [Jacob Morrison et al.](https://arxiv.org/pdf/2503.05804) found that training a 13 billion parameter model from the OLMo model family consumed an estimated 230 MWh of electricity - which they state is enough to power the average US home for 21 years.

This study will analyse the energy consumption of LLMs. Specifically, it is our goal to address two specific questions - first, we will study how the length of a question input prompt affects the energy consumption of an LLM producing its response. Second, we will compare three different 8 Billion parameter models, rjn-1, Llama 3.1 and Deepseek-r1 (developed by Essential AI, Meta and Deepseek respectively) in terms of their energy efficiency when evaluating on the same prompts.

## Methodology

Before we begin our tests, we must minimise the effect of external factors on our test results. Thus, the following measures have been to reduce confounding variables:

- Adaptive screen brightness disabled
- Monitor set to 50% brightness
- All applications aside from VS Code and Ollama (used to run our LLMs) closed
- Wi-Fi and BlueTooth disabled (no ethernet)
- Power Plan set to balanced
- Notifications disabled
- Only a mouse and keyboard are plugged in

Additionally, all of our tests will be run on the same computer with the following hardware:

- **CPU:**
- **GPU:**
- **RAM:**

Before running the tests, the computer must be warmed up. This is done because higher temperature results in higher energy consumption due to the higher electrical resistance of electrical conductors - thus, for a fair test, we must make sure the computer is sufficiently warmed up for our tests to take place under the same thermal conditions. To accomplish this, we ran a CPU-intensive task (in our case, calculating fibonacci numbers) for 5 minutes before the start of our tests.

The prompts tested were taken from dataset-factoid-webquestions ([Petr Baudis et at.](https://github.com/brmson/dataset-factoid-webquestions/blob/master/main/trainmodel.json)), a dataset licensed under the CC-BY 4.0 License. This dataset was modified to only include each prompt alongside the count of words for said prompt. To perform energy consumption measurements, we will use [EnergiBridge](https://github.com/tdurieux/EnergiBridge), an energy measurement utility, which will record the energy used per LLM response in Joules. All of the evaluated LLMs will be run locally via [Ollama](https://ollama.com/).

### Part 1: The significance of a prompt's length on an LLM's energy efficiency

Our first test will consist of evaluating how much of an effect the length of a prompt has on the energy consumed by an LLM while generating an answer. It is our assumption that a longer prompt will result in an LLM consuming a greater amount of energy, however we are not sure exactly what kind of relation there will be.

For this part, we chose to use Deepseek's deepseek-r1 7 Billion parameter model. This is the only model we will be using for this test to limit the effect of model infrastructure, parameter size and any other confounding variables that could affect this test.

The data for our test will consist of 18 total prompts: three prompts of 5 through 10 words inclusive. Each prompt will be evaluated 30 times to ensure a valid energy measurement is obtained.

### Part 2: How efficient are different developers at producing energy-efficient LLMs?

For this test, we wanted to see how efficient different LLM models made by different companies were. To select our LLMs, we looked for 8B parameter LLMs that were released within at most 1.5 years of each other. We chose three different 'types' of LLM developers - a relatively small LLM developer, Essential AI, a medium-sized developer, Deepseek, and a large developer, Meta AI; we thus chose the 8 Billion rnj-1, deepseek-r1 and llama3.1 models respectively.

To perform this test, we will sample five seven-word prompts at random from our dataset (note: we use random_state=0 for reproducibility). For each prompt, 30 executions of said prompt will be repated on each of the three chosen LLMs.

## Results

### Part 1

### Part 2

## Analysis

## Limitations

Despite our best attempts to make the study as robust as possible, there are certain parts of our research that were limited and could be improved upon. The first limitation we faced is the fact that Energibridge captures the total energy consumption of a system - despite our attempts to limit confounding variables (see methodology), certain background operating system processes could not be stopped or the impact of them measured. Additionally, the tests were only performed on one operating system, Windows 11 - the reliability of our results could be further improved by repeating the tests on different operating systems such as MacOS or Ubuntu linux and averaging out the result from all the operating systems.

Another limitation is the use of a single prompt of each length for our first test. The reason for this is because we test six total prompts, of lengths five to ten inclusive, 30 times each. This results in a total of 180 total response generations, which already takes a significant amount of time.

Another limitation was the release date of the different LLM compared in part two. We primarily selected our LLMs based on the parameter size, while looking for LLMs that were released roughly within 1.5 years of one another. With LLMs becoming publicly available within the last decade, 1.5 years may still be considered a relatively long time - thus, our experiment could be improved by using newer LLMs released within a shorter timeframe of one another.

## Conclusion

Conclusion goes here.


## Code

All of the code used for this study can be found [here](https://github.com/Fedor-Baryshnikov/SustainableSE-Project1).
