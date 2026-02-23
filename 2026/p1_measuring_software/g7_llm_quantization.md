---
author: Ceylin Ece, Georgios Markozanis, Kunal Narwani, Amy van der Meijden
group_number: 7
title: "Energy Efficiency of Quantized vs Full-Precision LLM Inference"
image: "img/g7_llm_quantization/project_cover.png"
date: 02/12/2026
summary: |- # TODO: check these when submitting
  Large Language Models are energy-intensive, but quantization techniques promise
  to reduce their computational demands. This project compares the energy consumption
  of running identical prompts through small LLMs (Llama 3.2 1-3B) in both full-precision
  (fp16) and 4-bit quantized (GGUF) formats. We will measure energy consumption, throughput,
  and quality trade-offs to provide empirical data for sustainable AI deployment decisions. 
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Project Topic: Testing accuracy of different quantized LLMs

### Introduction

Large Language Models have become ubiquitous in modern software systems, but their energy consumption raises sustainability concerns. Model quantization, that is reducing the numerical precision of weights and activations, is widely adopted to make LLMs more efficient, yet its real-world energy impact remains poorly quantified. While quantization may reduce energy usage, it remains unclear how well the models perform and how energy-efficient they are at producing a certain number of correct answers. To investigate this, we evaluate different quantized LLMs and compare their accuracies by measuring the energy required per correct test. For this experiment, we use the "Mostly Basic Python Problems Dataset," which provides prompts for the LLMs along with unit tests to verify the correctness of their responses.

**How does model quantization affect energy consumption during LLM inference?**

### Methodology

**Models**: Small open-source LLMs such as Llama 3.2 (1B or 3B parameters) that can run on consumer hardware.

**Setup**: We will run identical standardized prompt sets through both model variants on the same hardware, measuring energy consumption (Joules), energy per token, inference throughput, and output quality. Each configuration will be run multiple times to ensure statistical validity, following best practices from the course (zen mode, fixed system settings, controlled environment).

- Zen mode
- Wifi turned off
- Auto brightness turned off
- CPU warmed up by ...
- Model is randomly picked on every iterations
- One minute (?) of rest between the tasks

We do ... runs per LLM, since 30 iterations would be too time-consuming. # More explanation #

**Quality assessment**: To evaluate whether quantization degrades output, we will use a combination of automated benchmarks and manual comparison of generated outputs.





### Results
### Discussion
### Limitations & Future Work