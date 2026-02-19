---
author: Atharva Dagaonkar, Kasper van Maasdam, Ignas Vasiliauskas, Stefan Bud
group_number: 10
title: "The 'Daemon' Tax: An Energy Analysis of Docker and Podman across RESTful and Computational Workloads."
image: "img/gX_template/Docker vs Podman.jpg"
date: 12/02/2026
summary: |-
  This project evaluates the energy efficiency of containerization by comparing Docker’s daemon-based architecture against Podman’s daemonless and "pod-centric" model. By utilizing EnergiBridge to monitor CPU, DRAM, and GPU power draw, the study investigates whether Podman’s lower idle footprint is offset by potential overhead during high-intensity workloads, such as REST API networking, CPU-heavy π calculations, and GPU-accelerated matrix multiplication. Furthermore, the experiment expands into orchestration efficiency, comparing the energy consumption of Docker Compose against native Podman Pods across different operating systems to determine the most sustainable infrastructure choice for both microservices and intensive computational tasks.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---
