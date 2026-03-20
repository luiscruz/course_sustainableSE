---
author: "Ocean Wang, Nicholas Wu, Yasar Kocdas, Levi Ari Pronk, Madhav Chawla"
title: "LLM Energy Label"
image: "img/gX_template/cover.png"
summary: "A benchmarking tool that measures and compares energy consumption of local LLMs across task types, producing EU-style A to G energy labels to guide sustainable model selection."
group_number: 0
identifier: "p2_hacking_sustainability_2026"
all_projects_page: "../p2_hacking_sustainability"
---

Privacy-conscious organizations in healthcare, legal, finance, and government increasingly run LLMs locally to keep data in-house. When choosing which model to deploy, however, there is no standardized way to compare energy consumption. Model selection ends up driven purely by accuracy benchmarks, with sustainability left out of the picture entirely.

**LLM Energy Label** is a benchmarking tool that measures and compares the energy consumption of locally-run LLMs (via Ollama, vLLM, LM Studio) across standardized task categories. For each model and task combination, the tool produces a human-readable energy label on an A to G scale, inspired by EU appliance efficiency ratings. The goal is to help organizations match the right model to the right task, not just by capability, but by energy cost.

A lightweight model like Phi-3 Mini may handle simple classification tasks at a fraction of the energy cost of Llama 3 70B. Without a label, organizations default to the biggest model available. With one, they can make an informed trade-off.

**Research question:** Can we define a fair, reproducible methodology for comparing local LLM energy efficiency across task types, and translate this into actionable guidance for organizations choosing models for private deployment?
