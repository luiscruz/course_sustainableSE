---
author: "Alex Hautelman, Daniel Rugge, Yanzhi Chen, Yi Wu, Sydney Kho "
title: "Carbon-Aware Compute Task Scheduler"
image: "img/gX_template/cover.png"
summary: "Dynamic location and timeframe selection for scheduled compute tasks to optimize CO2 emissions. Evaluating impact and utility tools for companies."
paper: "../papers/gX_template.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

This project aims to investigate how dynamically selecting the location and timeframe for scheduled compute tasks can optimize CO2 emissions. As cloud computing continues to grow, the environmental impact of data centers becomes increasingly significant. By leveraging differences in carbon intensity across different regions and times, we can potentially reduce the carbon footprint of computational workloads.

Our goal is to evaluate the impact of such a solution and determine what sort of utility tools can help companies curb their emissions. We will explore existing strategies and potentially develop a prototype or framework to demonstrate the feasibility and benefits of carbon-aware scheduling. The specifics of the implementation are still being defined, but the core focus remains on sustainable software engineering practices in the context of job scheduling.

Currently, we have identified the following main questions we want to investigate:

*   Is there an existing paper or project that actively uses the Carbon Aware SDK to schedule tasks in a production-like CI/CD environment?
*   How can we reliably convert the relative scores or ratings from the SDK into an absolute carbon estimate (e.g., in grams of CO₂) for a variety of scheduled tasks?
*   Is there a real need to automate the setup of the Carbon Aware SDK for users, and is it feasible to do so for a more seamless experience?
*   What are the barriers to adoption for tools like the Carbon Aware SDK in industry? Which companies currently use it, and which do not?
*   How can we accurately estimate the data transfer cost (in terms of energy and carbon) for moving a CI/CD job? Can we design a simple yet effective heuristic for this if a precise model is too complex?
