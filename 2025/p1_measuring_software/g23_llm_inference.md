---
author: Victor Hornet, Elena Mihalache, Andreea Mocanu, Alexandru Postu, Kian Sie
title: 'Comparing the energy efficiency of different LLM inference runtimes' #TODO
image: '../img/p1_measuring_software/g23_llm_inference/cover.png'
date: 19/02/2025
summary: |-
    As the adoption of LLMs continues to grow across various applications, selecting the most energy-efficient runtime is crucial for optimizing their resource usage. This article compares different LLM runtimes in terms of energy usage and performance to identify the most efficient options. Our findings aim to provide practical recommendations for developers and organizations looking to balance performance with energy efficiency.
---

### Introduction
Artificial Intelligence (AI) is a technology that has been gaining widespread attention, particularly when considering Large Language Models (LLMs). Despite taking off rapidly and being used in various development contexts, LLMs faced criticism pertaining to sustainability. Concretely, LLMs are now known to pollute as far as ... is concerned (TODO: source). Despite such criticisms, there are no signs of investments in LLM technology slowing down. Thus, there is a need for solutions that make them more energy efficient. 

This boom in LLM-based technologies has led to the rise of Large Language Models (LLMs) for code, which help speed up development processes. Despite their advantages, users may have fears related to data privacy, more specifically regarding how personal data is used when models are queried through official interfaces. This led individuals to run models locally by leveraging existing backend solutions. Ever since the propulsion of LLMs into the mainstream, researchers have investigated their sustainability. However, to the best of our knowledge, there is no research comparing energy consumption across different backends. 

Meaningfully tackling the topic of LLM sustainability is a two-step process in which the different stages must happen in this specific order. Firstly, one needs to understand how (un)sustainable current LLMs are by performing empirical evaluations. Only after can academics start working on solutions that contribute to improving sustainability in this field. Our report tackles the first step. In particular, we focus on LLMs for code.

This study evaluates how LLMs for code perform across two different backends. In particular, we test ..., ..., and ... with ... and .... For both backends, we run these models against the HumanEval, an industry-standard benchmark, and measure their energy consumption per token. The primary argument for choosing these models is that they are open source. However, we deemed it essential to include DeepSeek in our research due to two considerations: (1) given the current political landscape, Western users exhibit increased privacy concerns, making them more likely to run this model locally, and (2) DeepSeek's public research suggests that this model was cheaper to develop, a fact which motivates us to investigate if it is also more energy efficient.



### Relevant Literature

### Methodology

To evaluate the energy efficiency of Large Language Models (LLMs) for code, we designed an experiment involving six distinct configurations. Our study examines three models, Ollama [cite], Deepseek [cite], and Mistral [cite], each executed on two different backend setups [actually mention]. The selection of these models is motivated by their parameter parity (approximately 7B parameters) and open-source availability. By limiting our experiments to these combinations, we aim to isolate the effects of model architecture and backend processing on energy consumption.

To reduce confounding variables, all experiments were executed on the same device under identical conditions [insert device specifications maybe??? and actual conditions]. This controlled environment ensures that differences in energy consumption can be attributed primarily to the model and backend characteristics rather than hardware or system optimizations.

Our primary metric is energy consumption measured as energy per token generated, in order to differentiate between single-token and multi-token settings. We used the measurement tool provided in the lab [insert footnote/link to the tool] to capture the energy metric.

The HumanEval benchmark [insert link to github or whatever else source] was selected as the dataset to evaluate the models on code generation tasks. This benchmark provides standardized test cases to assess correctness and also enables us to quantify energy consumption per generated token in a reproducible manner.

After conducting the experiment, both descriptive and inferential statistical analyses [actually mention which statistics but elaborate upon in the following section] were performed on the collected data. Descriptive statistics summarize the tendencies and variability of energy consumption across different configurations, while inferential statistics assess the significance of differences observed between models and backend types.

### Results

### Discussion

### Limitations

### Conclusion

### Reproducibility

