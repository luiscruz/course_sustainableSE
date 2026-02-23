---
author: Ceylin Ece, Georgios Markozanis, Kunal Narwani, Amy van der Meijden
group_number: 7
title: "Measuring the True Energy Cost of Correct LLM Inference"
image: "img/g7_llm_quantization/project_cover.png"
date: 02/12/2026
summary: |- # TODO: check these when submitting
    Quantization is widely recommended as the standard technique for energy-efficient
    local LLM deployment — but efficient at what, exactly? This project challenges the
    common practice of measuring inference energy in isolation by introducing correctness
    as a first-class metric. We benchmark three recent small LLMs from distinct model
    families (Llama 3.2, Qwen 2.5, Ministral-3B) all at 4-bit quantization (Q4_K_M)
    against the MBPP coding benchmark, measuring not just energy per token but energy
    per correct solution. Our findings aim to reveal whether the most energy-efficient
    model is truly the most energy-effective one, with direct implications for sustainable
    local AI deployment decisions.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Project Topic: Measuring the True Energy Cost of Correct LLM Inference

### Introduction
Large Language Models have become ubiquitous in modern software systems, but their energy consumption raises sustainability concerns. Model quantization, that is reducing the numerical precision of weights and activations, is widely adopted to make LLMs more efficient, yet its real-world energy impact remains poorly quantified. While quantization may reduce energy usage, it remains unclear how well the models perform and how energy-efficient they are at producing a certain number of correct answers. This project addresses that gap directly by introducing **energy per correct solution** as the central measurement, evaluated
across three current-generation small LLMs at 4-bit quantization on a real coding benchmark.

**How does model quantization affect energy consumption and their testing accuracy?**

### Methodology

**Models**: 
We select three general-purpose instruction-tuned models from distinct model families: [Qwen 2.5](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF), [Llama 3.2](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF), and [Ministral 3](https://huggingface.co/bartowski/mistralai_Ministral-3-3B-Instruct-2512-GGUF). They are all at
approximately 3 billion parameters and run in Q4_K_M GGUF format via llama.cpp. All models
are general instruction-tuned variants, not coding-specialized, ensuring a fair comparison
where no model has a systematic advantage from domain-specific fine-tuning. 

These three models represent architecturally distinct families (Llama, Qwen2, Mistral3) from
three different organizations, all released within the same three-month window of late 2024.
By fixing quantization format (Q4_K_M), parameter scale (~3B), task type (general instruction),
and inference backend (llama.cpp), we isolate architectural differences as the primary variable
of interest.

**Dataset**: We use the MBPP (Mostly Basic Python Problems) benchmark, specifically the sanitized MBPP+
variant which provides cleaner unit tests than the original. MBPP consists of approximately 500
entry-level Python programming problems, each accompanied by a natural language description and
unit tests that enable objective binary correctness assessment — a hard requirement for our
primary metric. We select a representative subset of tasks to keep total experiment runtime
feasible on consumer hardware while maintaining statistical validity.

MBPP is well-suited for this study because its unit tests provide an unambiguous pass/fail
signal per problem, which is the foundation of our energy-per-correct-solution metric. Unlike
open-ended generation tasks, coding benchmarks with automated tests allow correctness to be
measured objectively and at scale without human evaluation.

**Hardware**: Apple MacBook with M1 chip, 16GB unified memory. All models run via llama.cpp
with Metal acceleration enabled. Experiments run as root to allow EnergiBridge access to
system energy counters via powermetrics on macOS.

**Setup**: We will run identical standardized prompt sets through both model variants on the same hardware, measuring energy consumption (Joules), energy per token, inference throughput, and output quality. Each configuration will be run multiple times to ensure statistical validity, following best practices from the course (zen mode, fixed system settings, controlled environment).

- Zen mode
- Wifi turned off
- Auto brightness turned off
- CPU warmed up by ...
- Model is randomly picked on every iterations
- One minute (?) of rest between the tasks

We do 20 runs per model, since 30 iterations would be too time-consuming when using our own laptops. # More explanation #

**Quality assessment**: To evaluate whether quantization degrades output, we will use a combination of automated benchmarks and manual comparison of generated outputs.





### Results
### Discussion
### Limitations & Future Work

### Reproducibility
The code of the experiment can be found [here](https://github.com/ceylin-ece/sustainableSE-A1).