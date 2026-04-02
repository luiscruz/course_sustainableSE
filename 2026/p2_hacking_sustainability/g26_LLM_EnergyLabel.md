---
author: "Levi Ari Pronk, Ocean Wang, Nicholas Wu, Madhav Chawla, Yasar Saltuk Bugra Kocdas"
title: "Towards LLM Energy Labels: Accuracy and Energy Efficiency"
summary: "We propose Energy Per Correct Answer (EPCA), a metric combining energy cost and accuracy, and a proof-of-concept tool that benchmarks LLMs across coding, math, and logical reasoning domains."
paper: "../papers/group26_LLM_Energy_Labels.pdf"
source: "https://github.com/NCHWU/Energy_Label"
group_number: 26
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

We propose Energy Per Correct Answer (EPCA), a composite metric that jointly captures inference energy cost and task accuracy for LLMs. Inspired by the EU energy labelling framework for appliances, we built a proof-of-concept tool that benchmarks locally hosted LLMs by measuring GPU energy consumption via NVIDIA power telemetry, evaluating correctness, and assigning an A-G energy label. We tested our tool across three domains: LeetCode-style coding problems (pass@1), mathematical reasoning, and logical reasoning (exact-match accuracy). Our tool, including a web-based leaderboard, is publicly available to encourage transparent reporting of LLM energy efficiency.
