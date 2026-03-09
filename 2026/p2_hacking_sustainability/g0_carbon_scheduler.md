---
author: "Arda Duyum, Yuvraj Singh Pathania, Brewen Couaran, Taeyong kwon, Elia Jabbour"
title: "Carbon-Aware Scheduling"
image: "img/gX_template/cover.png"
summary: "A carbon-aware scheduler that shifts batch AI jobs like training and inference to time windows with the cleanest electricity grid, leveraging real-time data from ElectricityMaps and WattTime."
paper: "../papers/gX_carbon_scheduler.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## Project Description
Our project aims to reduce the carbon footprint of AI workloads by developing a **carbon-aware scheduler** for batch processing. AI tasks such as model training, image generation, and offline inference are often resource-intensive but delay-tolerant. By decoupling the submission time from the execution time, we can optimize for environmental impact rather than just speed or cost.

## Problem
Standard job schedulers execute tasks immediately upon submission, disregarding the carbon intensity of the local electricity grid. This often results in high-energy jobs running during "dirty" hours when the grid relies heavily on fossil fuels (coal, gas), unnecessarily increasing the carbon emissions of AI development.

## Proposed Solution
We are building a scheduler that:
1.  **Monitors Grid Intensity:** Uses APIs like **ElectricityMaps** or **WattTime** to fetch real-time and forecasted carbon intensity data.
2.  **Optimizes Scheduling:** Maps the training server's location to grid data and identifies "clean energy windows."
3.  **Shifts Workloads:** Automatically pauses or delays batch AI jobs until the grid carbon intensity drops below a user-defined threshold.

By shifting these workloads to times when renewable energy (wind, solar) availability is high, we aim to significantly lower the operational carbon emissions of AI pipelines without requiring changes to the model architecture itself.