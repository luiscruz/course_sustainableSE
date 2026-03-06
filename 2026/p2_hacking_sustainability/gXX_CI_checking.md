---
author: "Cristian Benghe, Antoni Nowakowski, Andrei Paduraru, Poyraz Temiz, Tess Hobbes"
title: "Carbon-Aware CI/CD Scheduler"
image: "img/g0_carbon_cicd/cover.png"
summary: "A tool that measures CI/CD pipeline energy usage and schedules builds during low-carbon electricity periods using the Carbon Aware SDK to reduce the environmental impact of software development."
paper: "../papers/g0_carbon_cicd.pdf"
source: "https://github.com/Green-Software-Foundation/carbon-aware-sdk"
website: "https://github.com/Green-Software-Foundation/carbon-aware-sdk"
video: ""
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## Carbon-Aware CI/CD Scheduler

Continuous Integration and Continuous Deployment (CI/CD) pipelines can consume significant computational resources, particularly during large or nightly builds. Despite their high energy usage, these pipelines are typically executed without considering the environmental impact of the electricity used.

In this project, we explore how **carbon-aware computing** can make software development more sustainable. Our tool has two main goals:

1. **Measure the energy consumption of CI/CD pipelines** to provide developers with insight into how much energy their builds consume.
2. **Schedule pipelines during periods of lower carbon intensity** using the Carbon Aware SDK from the Green Software Foundation.

By combining energy measurement with carbon-intensity data, the system can shift flexible workloads—such as nightly builds or non-urgent pipelines—to times when cleaner energy sources are more available.

This approach helps development teams **reduce the carbon footprint of their CI/CD infrastructure while maintaining development productivity**. Our prototype demonstrates how carbon-aware scheduling and energy transparency can be integrated into modern CI/CD workflows.
