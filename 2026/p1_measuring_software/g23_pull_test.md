---
author: Andrei Paduraru, Antoni Nowakowski, 
group_number: 23
title: "Comparing the Energy Efficiency of Standard JSON and orjson"
image: "img/gX_template/project_cover.png"
date: 27/03/2026
summary: |-
  This project comapres the energy conumption of data serialization in Python, namely how the standard json library compares to the orjson alternative. 
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

Data serialization is a core operation in modern software as it is used for everything ranging from web APIs to local data storage implementations. In Python, the json library is the default choice; however, it is often considered slow and CPU-intensive, especially when handling large datasets. This study investigates the potential of changing to an alternative called orjson.

As a high-performance, Rust-powered alternative, orjson is reported to be significantly faster—up to 10 times faster than the built-in module for certain tasks. This speed is achieved through the use of SIMD (Single Instruction, Multiple Data) instructions, which allow a single CPU instruction to process multiple pieces of data simultaneously. This study explores the potential for energy optimization by swapping the standard library for orjson. We aim to determine if this increased computational speed results in a "Race to Sleep"—allowing the CPU to finish its task faster and return to a low-power idle state sooner—thereby reducing the total Joules consumed by the system.

---

## Research Questions

To define the scope of our analysis, we have formulated the following research questions:

**RQ1.** How does the total energy consumption (in Joules) of the `orjson` library compare to the standard Python `json` library when performing large-scale serialization and deserialization tasks?

**RQ2.** How do the energy-saving benefits of `orjson` scale as the volume of the dataset increases (e.g., comparing 10MB vs. 100MB files)?

---

## Methodology

### Experimental Setup
The experiment will be conducted on a Windows 11 machine. To access the CPU's energy registers (RAPL), we will utilize **EnergiBridge** in conjunction with an elevated (Administrator) terminal. Because Windows 11 often restricts access to Model Specific Registers (MSRs), we will ensure the necessary hardware drivers are active to allow the profiler to log the **PP0 Energy Consumption** (CPU energy) at a sampling rate of 200ms.

### The Reproducible Scenario
We have developed a Python-based automated scenario that handles both serialization and deserialization. The script will:
1. Load a pre-generated 100MB dummy dataset into memory.
2. **Serialize** the data into a JSON string 50 times to create a measurable load.
3. **Deserialize** the JSON string back into a Python object 50 times.

We will compare two versions: Version 1 (Baseline) using the standard json library and Version 2 (Improved) using orjson. To ensure statistical significance, we will perform 30 repeated trials for each version.