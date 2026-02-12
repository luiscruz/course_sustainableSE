---
author: Ceylin Ece, Georgios Markozanis, Kunal Narwani, Amy van der Meijden
group_number: 7
title: "Energy Efficiency of Quantized vs Full-Precision LLM Inference"
image: "img/g7_llm_quantization/project_cover.png"
date: 02/12/2026
summary: |-
  Large Language Models are energy-intensive, but quantization techniques promise
  to reduce their computational demands. This project compares the energy consumption
  of running identical prompts through small LLMs (Llama 3.2 1-3B) in both full-precision
  (fp16) and 4-bit quantized (GGUF) formats. We will measure energy consumption, throughput,
  and quality trade-offs to provide empirical data for sustainable AI deployment decisions.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Project Topic: Energy Efficiency of Quantized vs Full-Precision LLM Inference

### Motivation

Large Language Models have become ubiquitous in modern software systems, but their energy consumption raises sustainability concerns. Model quantization, that is reducing the numerical precision of weights and activations, is widely adopted to make LLMs more efficient, yet its real-world energy impact remains poorly quantified.

### Research Question

**How does model quantization affect energy consumption during LLM inference?**

We will compare:
- **Full-precision models** (fp16) as our baseline
- **4-bit quantized models** (GGUF format) as the optimized variant

### Experimental Approach

**Models**: Small open-source LLMs such as Llama 3.2 (1B or 3B parameters) that can run on consumer hardware.

**Setup**: We will run identical standardized prompt sets through both model variants on the same hardware, measuring energy consumption (Joules), energy per token, inference throughput, and output quality. Each configuration will be run multiple times to ensure statistical validity, following best practices from the course (zen mode, fixed system settings, controlled environment).

**Quality assessment**: To evaluate whether quantization degrades output, we will use a combination of automated benchmarks and manual comparison of generated outputs.

### Expected Outcomes

We expect quantization to meaningfully reduce energy consumption while maintaining acceptable output quality, providing practical insights for sustainable LLM deployment decisions.