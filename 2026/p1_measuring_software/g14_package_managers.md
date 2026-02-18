---
author: Calin Georgescu, Elia Jabbour, Wojciech Mundała, Daniel Rachev
group_number: 14
title: "Measuring the Energy Consumption of Python Package Managers: pip, uv, and poetry"
image: "img/gX_template/project_cover.png"
date: 12/02/2026
summary: |-
  This article investigates the energy consumption of three Python package
  managers: pip, uv, and poetry. We run controlled experiments across common
  dependency management tasks and compare their energy usage, execution time,
  and consistency. The goal is to identify which tool is the most energy-efficient
  under realistic development workflows.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## 1. Introduction & Problem Definition

Python is the undisputed king of data science and backend development, powering everything from simple scripts to massive enterprise platforms. However, this popularity comes with a hidden cost: its fragmented packaging ecosystem. Every time a developer initializes a project, or a CI/CD pipeline triggers a build, dependencies must be resolved, downloaded, and installed.

While the *speed* of these package managers is a frequent topic of benchmarks, the *energy cost* of these millions of daily installations is rarely quantified. In the context of Green Software Engineering, optimizing these high-frequency, repetitive tasks can lead to massive aggregate energy savings.

In this experiment, we pit the industry standards against a new challenger to determine the most energy-efficient tool for Python dependency management.

### The Contenders
*   **`pip`**: The ubiquitous standard tool included with Python. It is widely compatible but historically slower in resolution.
*   **`poetry`**: A developer-favorite known for its deterministic dependency resolution and developer experience, written in pure Python.
*   **`uv`**: The new challenger written in Rust, claiming extreme performance and aggressive parallelization.

### The Hypothesis
We hypothesize that **`uv`**, due to its compiled Rust architecture and efficient resource management (such as hardlinking), will consume significantly less energy than its Python-based counterparts (`pip`, `poetry`) across all scenarios.

### Research Questions
To validate this, we define three specific research questions:
*   **RQ1 (Installation):** How does energy consumption differ between tools during a **cold install** (network-heavy) versus a **warm install** (disk-heavy)?
*   **RQ2 (Correlation):** Is there a correlation between execution time and energy consumption? (i.e., *Is faster always greener?*)
*   **RQ3 (Resolution):** Is there a significant energy difference in the pure **dependency resolution (locking)** phase between Rust-based `uv`, Python-based `poetry`, and `pip-tools`?

---

## 2. Background & Motivation

### Scale & Impact
The scale of Python's ecosystem is massive. The Python Package Index (PyPI) serves billions of requests per day. Consider a standard CI/CD pipeline: for every commit, a fresh virtual environment is often created, and dependencies are installed from scratch. If a tool can reduce the energy footprint of this process by even 10%, the aggregate savings across millions of daily runs would be substantial. This aligns directly with the principles of **Green Software Engineering**: reducing the carbon intensity of software at the source.

### Developer Experience (DX) vs. Energy
Traditionally, developers optimize for "Time to Interactive." Waiting for dependencies to lock or install breaks the flow state. However, speed and energy are not always perfectly correlated. A tool might consume more power (Watts) to finish a task faster, potentially resulting in the same total energy (Joules). Our goal is to determine if `uv`'s speed advantage translates into a "Green Win-Win"—improving the developer experience while simultaneously reducing environmental impact.

### The Mechanics: Locking vs. Installing
To understand energy consumption, we must distinguish between the two phases of package management:
1.  **Resolution (Locking):** A CPU-intensive mathematical puzzle. The tool must traverse the dependency graph to find a set of package versions that satisfy all constraints (e.g., Package A needs `numpy>1.20` but Package B needs `numpy<1.25`).
2.  **Installation:** An I/O-intensive process. The tool downloads files from the network, unpacks wheels, and moves files to the site-packages directory.
3.  **Caching:** Modern tools use local caches to avoid redownloading. Efficient caching strategies (like reflink/hardlinks) can drastically reduce disk I/O and energy usage.

---

## 3. Methodology

To ensure scientific rigor, we designed a controlled experiment following the guidelines for reliable energy measurements.

### 3.1 The Workload
To ensure our results are applicable to real-world scenarios, we avoided trivial "Hello World" dependencies. Instead, we utilized the dependency tree of **Apache Airflow**.

This workload was selected because:
1.  **Complexity:** It contains **X** direct dependencies and over **Y** transitive dependencies.
2.  **Stress Test:** This level of complexity is required to stress-test the resolution algorithms (locking) and generate a measurable energy footprint that distinguishes the tools from background OS noise.

### 3.2 The Scenarios
We measured three distinct scenarios to isolate different computing resources (CPU vs. Network vs. Disk).

**Scenario A: Dependency Resolution (Locking)**
*   **Goal:** Measure the pure CPU efficiency of the solver algorithms.
*   **Action:** We generated the lock file from scratch using `poetry lock`, `uv lock`, and `pip-compile` (from `pip-tools`).

**Scenario B: Cold Install (Network + I/O)**
*   **Goal:** Simulate a fresh CI/CD pipeline run.
*   **Pre-condition:** Before every single run, we executed specific commands to **purge the local cache** (e.g., `pip cache purge`, `uv cache clean`).
*   **Action:** We measured the time and energy required to create a fresh virtual environment and install all dependencies from the internet.

**Scenario C: Warm Install (Disk I/O)**
*   **Goal:** Simulate local development or cached CI runners.
*   **Pre-condition:** The cache was fully populated, but the virtual environment was deleted.
*   **Action:** We measured the re-installation of dependencies using local artifacts.

### 3.3 Experimental Protocol
We adhered to a strict protocol to minimize confounding factors:

*   **Hardware:** All experiments were conducted on a **SPECS**.
*   **Measurement Tool:** We used **Energibridge**, an Intel RAPL wrapper, to record Energy (Joules), Power (Watts), and Time (ms).
*   **Sample Size:** We performed **30 repetitions** per tool, per scenario, to ensure statistical significance.
*   **Randomization:** The execution order was shuffled (e.g., `pip` → `uv` → `poetry` → `uv`...) to mitigate temporal biases such as thermal throttling or OS background tasks.
*   **Python Version:** All tools were restricted to use **Python 3.11** to ensure fairness.
*   **Zen Mode:**
    *   All non-essential applications were closed.
    *   Screen brightness was fixed at 0%.
    *   A **10-second cooldown** sleep was enforced between runs to allow CPU temperature to normalize.
