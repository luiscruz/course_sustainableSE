---
author: "Ion Tulei, Alexandru Verhovetchi, Horia Zaharia, Dragos Erhan, Joost Weerheim"
title: "Dockerfile Carbon Optimizer"
image: "img/g228_dockerfile_carbon/cover.png"
summary: "A CLI tool that analyzes Dockerfiles for energy-wasteful patterns, estimates carbon cost per finding, and auto-fixes them."
paper: "../papers/g22_dockerfile_carbon.pdf"
source: "https://github.com/cs4575-g228/cs4575-g228-implementation"
group_number: 22
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## Dockerfile Carbon Optimizer (DCO)

DCO is a Python CLI tool that scans Dockerfiles for energy-wasteful patterns, estimates the monthly CO2 cost of each finding, and automatically rewrites the Dockerfile to fix them.

It detects six common anti-patterns: oversized base images, uncombined RUN layers, dev dependencies left in production, missing .dockerignore files, absent multi-stage builds, and unpinned image tags. Carbon estimates use the Aslan et al. (2018) network energy model combined with IEA grid intensity data and Docker Hub pull counts.

We validated DCO against ten real-world GitHub repositories across five languages (Python, Node.js, Java, Go, PHP), measuring image size, build time, and energy consumption before and after optimization. The largest single-image saving was 355 MB, with measurable energy reductions confirmed via CodeCarbon hardware monitoring.

[Read the paper](../papers/g22_dockerfile_carbon.pdf) | [Source code](https://github.com/cs4575-g228/cs4575-g228-implementation)
