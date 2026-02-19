---
author: Arda Duyum, Caio Miranda Haschelevici, Ion Tulei, Radu Andrei Vasile
group_number: 16
title: "The Energy Cost of 'Free' Internet: Do AdBlockers Save Power?"
image: "img/gX_template/project_cover.png" # Placeholder
date: 11/02/2026
summary: |-
  Online advertisements are ubiquitous, often running heavy scripts and animations that degrade user experience. 
  Group 16 investigates the hidden energy cost of these ads and whether using an AdBlocker can significantly 
  reduce the carbon footprint of web browsing.
identifier: p1_measuring_software_2026
all_projects_page: "../p1_measuring_software"
---

## Problem Statement

The modern web is funded by advertising. However, the cost of "free" content is often paid in hardware resources. Advertisements are no longer simple images; they are complex software applications running inside our browsers, executing heavy JavaScript, tracking scripts, and animations.

While the impact on loading times and data usage is well documented, the **energy impact** is often overlooked. If millions of users browse news sites daily, the aggregate energy waste from rendering unsolicited ads could be massive. This project aims to quantify that cost.

## Research Question

**RQ1:** What is the impact of AdBlockers on the energy consumption of a web browser when visiting media-heavy websites?

**RQ2:** Can we quantify the energy savings per page load when advertisements are suppressed?

## Methodology

To answer these questions, we will design an experiment using **EnergiBridge** to measure the energy consumption of the client machine during automated browsing sessions.

### The Setup
*   **Hardware:** A standard laptop (specifications to be detailed in the final report).
*   **Tools:** 
    *   **EnergiBridge** for precise energy measurement (RAPL counters).
    *   **Selenium / Playwright** (optional) or manual consistent scrolling for browsing simulation.
*   **Subject:**
    *   **Website:** We will target **DailyMail.co.uk** or **CNN.com**, known for their high density of advertisements and tracking scripts.
    *   **Browser:** Google Chrome (Latest Version).
    *   **Extension:** uBlock Origin (or similar standard AdBlocker).

### The Experiment Script
We will perform a comparative experiment:
1.  **Scenario A (Baseline):** Open the target website **without** any ad blocker. Scroll through the front page for 60 seconds.
2.  **Scenario B (Intervention):** Open the same website **with uBlock Origin** enabled. Scroll through the front page for 60 seconds.

We will repeat each scenario 20 times to ensure statistical significance and account for network variability. Between runs, the browser cache will be cleared to ensure a "cold" load, or preserved to simulate "warm" browsing (to be decided).

### Hypothesis
We hypothesize that **using an AdBlocker will result in statistically significant energy savings**, potentially reducing energy consumption by 10-20% due to the reduction in CPU usage required to render third-party scripts and animations.

---
*Note: This is a preliminary proposal for Project 1.*