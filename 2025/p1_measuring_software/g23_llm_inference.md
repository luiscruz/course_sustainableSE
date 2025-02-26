---
author: Victor Hornet, Elena Mihalache, Andreea Mocanu, Alexandru Postu, Kian Sie
title: 'Comparing the energy efficiency of different LLM inference runtimes' #TODO
image: '../img/p1_measuring_software/g23_llm_inference/cover.png'
date: 19/02/2025
summary: |-
    As the adoption of LLMs continues to grow across various applications, selecting the most energy-efficient runtime is crucial for optimizing their resource usage. This article compares different LLM runtimes in terms of energy usage and performance to identify the most efficient options. Our findings aim to provide practical recommendations for developers and organizations looking to balance performance with energy efficiency.
---

### Introduction
Artificial Intelligence (AI) technology has been gaining widespread attention, particularly when considering Large Language Models (LLMs). Despite taking off rapidly and being used in various development contexts, LLMs faced criticism pertaining to sustainability. Previously, Gebru equated the carbon footprint of training one BERT model to that of a transatlantic flight [(2021)](https://dl.acm.org/doi/10.1145/3442188.3445922), while more recent research shows that the carbon footprint of one ChatGPT query is 20 times higher than that of a web search query [(Ding and Shi, 2024)](https://ieeexplore.ieee.org/abstract/document/10765824). Despite such criticisms, there are no signs of investments in LLM technology slowing down, a fact which makes it essential for scientists to investigate how making LLMs more energy efficient. 

This boom in LLM-based technologies was swiftly followed by the rise of Large Language Models (LLMs) for code, which help speed up development processes. In spite of it being advantageous to use such tools, users may have fears related to data privacy [(Yao et al., 2023)](https://arxiv.org/abs/2312.02003). This, we suspect, may lead to an increased interest in running LLMs on a local backend. Thus, while we can identify notable research into energy consumption of LLM technologies (citations), we find it equally important to investigate these aspects for local inference processes.

Generally, meaningfully tackling the topic of LLM sustainability is a two-step process in which the different stages must happen in this specific order. Firstly, one needs to understand how (un)sustainable current LLMs are by performing empirical evaluations. Only after can one work on solutions that contribute to improving sustainability in this field. Our blog post tackles the first step. In particular, we focus on local LLM inference processes.

This study evaluates the energy consumption of local LLM inference. In particular, we test the inference process of Qwen2.5-7B-Instruct, DeepSeek-R1-Distill-Qwen-7B, CodeLlama-7b-Instruct, and Mistral-7B-Instruct, with LlamaCPP as backend. We run these models against the HumanEval dataset, measuring measure their energy consumption per token for every query. The primary argument for choosing these models is that they are open source. Moreover, we deemed it essential to include DeepSeek in our research due to two considerations: (1) given the current political landscape, Western users exhibit increased privacy concerns, making them more likely to run this model locally, and (2) DeepSeek's public research suggests that this model was cheaper to develop, a fact which motivates us to investigate if it is also more energy efficient.



### Relevant Literature

### Methodology

To evaluate the energy efficiency of Large Language Models (LLMs) for code, we designed an experiment involving four models, Codellama [cite], Deepseek [cite], Gwen [cite] and Mistral [cite]. The selection of these models is motivated by their parameter parity (approximately 7B parameters) and open-source availability. By limiting our experiments to these models, we aim to isolate the effects of model architecture on energy consumption.

To reduce confounding variables, all experiments were executed on the same device under identical conditions [insert device specifications maybe??? and actual conditions]. This controlled environment ensures that differences in energy consumption can be attributed primarily to the model characteristics rather than hardware or system optimizations.

The HumanEval benchmark [insert link to github or whatever else source] was selected as the dataset to evaluate the models on code generation tasks. This benchmark provides standardized test cases to assess correctness and also enables us to quantify energy consumption per generated token in a reproducible manner.

Our primary metrics are energy consumption measured as total energy per problem and energy per token generated for a problem, in order to differentiate between single-token and multi-token settings. We used the measurement tool provided in the lab [insert footnote/link to the tool] to capture the energy metric.

After conducting the experiment, descriptive statistical analyses [actually mention which statistics but elaborate upon in the following section] were performed on the collected data. Descriptive statistics summarize the tendencies and variability of energy consumption across different configurations.

### Results

After collecting the raw energy consumption data (total energy and energy per token for each model-task pair), we performed descriptive statistical analyses using Python [cite] and JASP [cite]. Specifically, for each of the four models we computed:

- **Mean** and **Standard Deviation (SD)** of energy consumption to capture average behavior and overall variability.  
- **Minimum** and **Maximum** values to observe the full range of consumption.  
- **Box plots** to visualize the distributions of both total energy and energy per token across all HumanEval tasks.  
- **Bar charts** with error bars (the standard deviations) to highlight differences in mean energy consumption among models.  

[View the detailed energy report](resources/aggregated_energy.html)

In total, we ran 164 HumanEval tasks per model, collecting two primary measures:

1. **Total Energy (in Joules) per task**  
2. **Energy per Token (in Joules) per task**  

Table 1 [from the JASP output] and Figures 1–4 [the bar and box plots] summarize the findings.

**Codellama** recorded the **lowest mean total energy** at approximately **125.45 J** (SD = 44.60). Its distribution ranged widely (36.27–216.62 J), indicating that while it often consumed low energy, some tasks required substantially more.  
**Deepseek** had the **highest mean total energy** of about **175.44 J** (SD = 14.32), with values ranging from 150.71 J to 226.70 J. Notably, its narrower range suggests more consistent consumption, albeit at a higher level.  
**Mistral** (mean = 174.30 J, SD = 16.86) also showed relatively high total energy consumption, comparable to Deepseek but with a slightly broader spread (139.49–242.13 J).  
**Qwen** fell between Codellama and Deepseek/Mistral in total energy usage (mean = 151.57 J, SD = 35.68), with a range of 48.47–222.113 J.

Overall, **Codellama** stands out for **lowest total energy** on average, while **Deepseek** and **Mistral** are at the higher end. **Qwen** remains in an intermediate position but with moderate variability.

When normalizing energy consumption by the number of tokens generated, **Codellama** again appears the most efficient, averaging **0.385 J/token** (SD = 0.086).  
**Deepseek** uses **0.582 J/token** (SD = 0.073).  
**Mistral** has the **highest average energy per token**, at **0.684 J/token** (SD = 0.123), although its total energy is similar to Deepseek’s.  
**Qwen** requires **0.499 J/token** (SD = 0.097), placing it between Codellama and Deepseek in terms of per-token consumption.

Hence, **Codellama** is consistently the most energy-efficient model—both in total energy and energy per token. **Mistral** stands out for having the highest per-token usage, and **Deepseek** ranks slightly below Mistral on that metric but shows the highest total energy consumption. **Qwen** tends to cluster between the extremes.

These results suggest that while Codellama maintains the lowest energy footprint overall, there can be task-level variability (as indicated by its wide range). Deepseek and Mistral consistently draw higher power, whether measured as total energy or on a per-token basis, with Mistral being the least efficient per token. Qwen generally remains in an intermediate position, as it balances moderate total consumption and moderate per-token usage.

### Discussion

### Limitations

### Conclusion

### Reproducibility

