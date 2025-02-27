---
author: Victor Hornet, Elena Mihalache, Andreea Mocanu, Alexandru Postu, Kian Sie
title: 'Comparing the energy efficiency of different LLM inference runtimes' #TODO
image: '../img/p1_measuring_software/g23_llm_inference/cover.png'
date: 19/02/2025
summary: |-
    As the adoption of LLMs continues to grow across various applications, selecting the most energy-efficient runtime is crucial for optimizing their resource usage. This article compares different LLM runtimes in terms of energy usage and performance to identify the most efficient options. Our findings aim to provide practical recommendations for developers and organizations looking to balance performance with energy efficiency.
---

### Introduction
Artificial Intelligence (AI) technology has gained widespread attention, particularly when considering Large Language Models (LLMs). Despite taking off rapidly and being used in various development contexts, LLMs faced criticism pertaining to sustainability. Previously, Gebru equated the carbon footprint of training one BERT model to that of a transatlantic flight [(2021)](https://dl.acm.org/doi/10.1145/3442188.3445922), while more recent research shows that the carbon footprint of one ChatGPT query is 20 times higher than that of a web search query [(Ding and Shi, 2024)](https://ieeexplore.ieee.org/abstract/document/10765824). Despite such criticisms, there are no signs of investments in LLM technology slowing down, a fact which makes it essential for scientists to investigate how LLMs can be developed to be more energy efficient. 

This boom in LLM-based technologies was swiftly followed by the rise of Large Language Models (LLMs) for code, which helps speed up development processes. Despite the advantages of using such tools, users may have fears related to data privacy [(Yao et al., 2023)](https://arxiv.org/abs/2312.02003). We suspect this may lead to an increased interest in running LLMs on a local backend. Thus, while we can identify notable research into the energy consumption of LLM technologies (citations), we find it equally important to investigate these aspects for local inference processes.

Generally, meaningfully tackling the topic of LLM sustainability is a two-step process in which the different stages must happen in this specific order. Firstly, one needs to understand how (un)sustainable current LLMs are by performing empirical evaluations. Only after can one work on solutions that contribute to improving sustainability in this field. Our blog post tackles the first step. In particular, we focus on local LLM inference processes.

This study evaluates the energy consumption of local LLM inference. In particular, we test the inference process of [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct), [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B), [CodeLlama-7b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf), and [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3), with [llama.cpp](https://github.com/ggml-org/llama.cpp) as backend. We run these models against the HumanEval dataset, measuring their energy consumption per token for every query. The primary argument for choosing these models is that they are open source. Moreover, we deemed it essential to include DeepSeek in our research due to two assumptions: (1) given the current political landscape, Western users exhibit increased privacy concerns for technology originating from China, making them more likely to run Deepseek locally, and (2) DeepSeek's public research suggests that this model was cheaper to develop, a fact which motivates us to investigate if it is also more energy efficient.

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

Our results of the analysis of energy consumption across the four models provide valuable insights into their energy efficiency characteristics. These findings are relevant for both developers and users of LLMs, as we [ i need to sleep ]

Codellama emerged as the most energy-efficient model, both in terms of total energy consumption and energy per token. This suggests Codellama could result in reduced environmental impact and cost savings in large-scale deployments. However, its wide range of total energy consumption (36.27–216.62 J) indicates that its efficiency can vary significantly depending on the task. This variability may come from differences in task complexity or the model's adaptability to specific tasks.  This suggests it may require careful monitoring to avoid energy spikes in practice.

In contrast, Deepseek and Mistral demonstrated consistency, although higher energy consumption overall. Our results suggest that Deepseek operates with a high but predictable energy demand, which could be advantageous in environments predictability is valued over efficiency, especially if Deepseek gives a performance advantage (eg higher accuracy of response) on certain tasks. Mistral, on the other hand, not only consumed a similar amount of total to Deepseek, but also had the highest energy per token. This makes Mistral the least efficient model on a per-token basis, which could be a significant drawback in applications requiring extensive text generation. Deepseek seems to be a better alternative in this case.

Qwen occupied an intermediate position, with moderate scores for both metrics. Its balanced performance makes it a viable option for users seeking a compromise between efficiency and capability. However, its moderate variability suggests that its energy demands can still fluctuate depending on the task at hand.


### Limitations

Initially, we wanted to compare the energy consumption across different models, but with different backends. LLaMa, MistralRS and vLLM were considered, as [ some motivation ]. However, we found MistralRS’ documentation to be lacking and could not get it to work on time.  [ also saw in notes that deepseek not supported– on which one? ] For vLLM, since it does not support GPU acceleration on Mac, we could not run LLaMa on it [ or is it just slow? unclear ]. Due to time constraints, we opted for using just the LLaMa.cpp backend for all four models, instead of spending more time trying to get the backends working on Linux/Windows. [ mention hardware eg using just one laptop as a limitation explicitly? kind of inferred frmo here ]

Another limitation is the fact that our analysis is based on a specific set of tasks, namely HumanEval, and the results may not generalize over other datasets. Therefore, our results might be different for another set of tasks, and we cannot conclude which model is generally most energy efficient, but just within this given context. This also limits ourselves from drawing conclusions about which models are most energy efficient for which type of tasks, as we do not compare different subsets.

[ One other limitation is that we used an external tool, namely EnergiBridge, to calculate energy consumption while running the models. Thus, energy consumption of the models was measured in isolation, which might have resulted in imprecise results and slightly higher measurements. However, for the scope of this study and comparing the different models, the precision of numerical results can be neglected. ]

Additionally, our study focuses solely on energy efficiency and does not take into consideration performance metrics, such as accuracy of generated code or speed of generation. This way, we can only reason about which model uses the least amount of energy to generate its responses, but not whether the response is relevant or correct and the trade-off between correctness and energy efficiency.

[ temperature of computer ? ]

### Future work
Since we solely compared the power output of 3 models there is a large variety of options that could be available for future work. The first is the most straightforward, namely, comparing a larger variety of models, with more varied parameters as well. The models we looked at gave a good idea of their power usage, however, 7 billion parameter models are used in much smaller quantities, as their performance typically does not measure up to their larger counterparts in exchange for their efficiency. Additionally, there are models such as ChatGPT and Gemini which may be more commonly used, compared to the open-source alternatives we investigated.

Furthermore, one aspect we initially intended to look into was the power consumption of different-back ends, such as [mistral.rs](https://github.com/EricLBuehler/mistral.rs), [vLLM](https://docs.vllm.ai/en/latest/#), [mlx-lm](https://pypi.org/project/mlx-lm/) and [exllamav2](https://github.com/turboderp-org/exllamav2) alongside [llama.cpp](https://github.com/ggml-org/llama.cpp) that we ended up using. As running models locally becomes increasingly common, so too does the utilization of open-source back-ends to employ these LLMs. Different back-ends have minimal to no impact on the model ouput itself, however, can have a large impact on generation speed. There are many aspects related to speedup (i.e. parallelization/concurrency, batching, etc.) that can be optimized and improved on, which would likely carry over into energy efficiency as well. For instance a faster program may have a higher burst of energy consumption, however due to the reduced time it results in a lower total energy consumption. Measuring the impact of these back-ends, and potentially what optimizations can be made to improve energy efficiency would likely have benefits particularly in battery powered devices, which are commonly used to access LLMs. 

One aspect that was also not considered due to time constraints was the HumanEval scores themselves. This meant we were unable to consider the actual outputs of the LLMs. Future studies could have large benefits from including this aspect, as an incredibly power-efficient model with unusable outputs provides incredibly limited utility. Conversely, it is also easier to weigh if performance improvements are worth higher energy consumption. For instance, as Deepseek typically utilizes more tokens than the other models, the total output power may be higher than its energy per token could suggest. Investigating whether this correlates with higher benchmark scores would provide valuable insight. Additionally, analyzing how models generate computationally efficient code could help clarify trade-offs between inference cost and long-term execution efficiency.

Finally, we simply measured the energy consumption of the code generation itself. Another option, however, is to measure the energy consumption of the generated code itself. There have been studies like this one, for instance by [Cursaru, Duits, et al. (2024)](https://arxiv.org/abs/2405.03616), however, the focus of the study was solely on code generated by Codellama. Combining results from the energy efficiency of the model itself, along with the energy efficiency of the code generated would paint a much more complete picture and could be conducted on a wider variety of models as well. 

### Conclusion

### Reproducibility

