---
author: Victor Hornet, Elena Mihalache, Andreea Mocanu, Alexandru Postu, Kian Sie
title: 'Comparing the energy efficiency of different LLM inference runtimes' #TODO
image: '../img/p1_measuring_software/g23_llm_inference/cover.png'
date: 19/02/2025
summary: |-
    As the adoption of LLMs continues to grow across various applications, selecting the most energy-efficient runtime is crucial for optimizing their resource usage. This article compares different LLM runtimes in terms of energy usage and performance to identify the most efficient options. Our findings aim to provide practical recommendations for developers and organizations looking to balance performance with energy efficiency.
---

### Introduction
As society progresses, many of today's challenges are intrinsically related to coding. Consequently, the recent boom in LLM-based technologies has led to the rise of Large Language Models (LLMs) for code, which help developers produce code at a faster pace. This technology took off rapidly and is now used in various development contexts. However, LLMs faced criticism pertaining to sustainability. Concretely, LLMs are now known to pollute as far as ... is concerned (TODO: source). Despite such criticisms, there are no signs of investments in LLM technology slowing down. Thus, there is a need for solutions that make them more energy efficient. 

Meaningfully tackling the topic of LLM sustainability is a two-step process in which the different stages must happen in this specific order. Firstly, one needs to understand how (un)sustainable current LLMs are by performing empirical evaluations. Only after can academics start working on solutions that contribute to improving sustainability in this field. Our report tackles the first step. In particular, we focus on LLMs for code.

The recent boom in LLM-based technologies has led to the rise of Large Language Models (LLMs) for code, which help speed up development processes. Despite their advantages, users may have fears related to data privacy: indeed, they are worried about how personal data is used when models are queried through their official interfaces (TODO: how would u reword this?). This led individuals to run models locally by leveraging existing backend solutions. Ever since the propulsion of LLMs into the mainstream, researchers have investigated their sustainability. However, to the best of our knowledge, there is no research comparing energy consumption across different backends. 

This study evaluates how LLMs for code perform across two different backends. In particular, we test ..., ..., and ... with ... and .... For both backends, we run these models against the HumanEval, an industry-standard benchmark, and measure their energy consumption per token. The primary argument for choosing these models is that they are open source. However, we deemed it essential to include DeepSeek in our research due to two considerations: (1) given the current political landscape, Western users exhibit increased privacy concerns, making them more likely to run this model locally, and (2) DeepSeek's public research suggests that this model was cheaper to develop, a fact which motivates us to investigate if it is also more energy efficient.



### Relevant Literature

### Methodology

### Results

### Discussion

### Limitations

### Conclusion

### Reproducibility

