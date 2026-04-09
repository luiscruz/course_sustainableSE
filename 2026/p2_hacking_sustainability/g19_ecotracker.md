---
author: "Adomas Bagdonas, Georgi Dimitrov, Kristian Hristov, Stilyan Penchev, Daniel Rachev"
title: "EcoTracker: An Application-Level Carbon Scheduling Framework for LLMs"
image: "img/g19_ecotracker/cover.png"
summary: "The rapid growth of Large Language Models has intensified concerns about the environmental cost of AI inference. Currently, developers using third-party LLM APIs lack plug-and-play solutions to actively mitigate their footprint. To address this, we developed EcoTracker, an open-source Python framework published on PyPI for application-level carbon-aware execution of delay-tolerant LLM workloads. EcoTracker combines forecast-guided temporal shifting with stochastic jitter to prevent artificial demand spikes. It also includes policy mechanisms such as dynamic model downgrading and carbon-budget enforcement. To ensure reproducible evaluation, we benchmarked the tool using a fixed carbon-intensity trace across 1,392 scheduling scenarios over 29 days. Relative to immediate execution, EcoTracker successfully reduced total emitted carbon by 9.99% and captured 76.9% of the savings achieved by an oracle policy with perfect hindsight, proving that meaningful emissions reductions can be achieved at the application layer."
paper: "../papers/g19_ecotracker.pdf"
source: "https://github.com/DanielRachev/llm-eco-tracker"
website: https://pypi.org/project/llm-eco-tracker/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 19
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---
