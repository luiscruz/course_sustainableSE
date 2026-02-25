---
author: Conall Lynch, Arjun Rajesh Nair, Viktor Shapchev, Coen Werre
group_number: 19
title: "Energy Consumption of Sorting Algorithms: Impact of Algorithmic Complexity and Memory Behavior"
image: "img/gX_template/project_cover.png"
date: 12/02/2026
summary: |-
  In this project, we propose to measure and compare the energy consumption of different sorting algorithms under varying input sizes and data distributions. Sorting is a fundamental building block in modern software systems, used in databases, analytics pipelines, and backend processing tasks. We will implement multiple sorting strategies (e.g., Bubble Sort, Merge Sort, and Quick Sort) and evaluate how algorithmic complexity (O(n²) vs O(n log n)) and memory behavior (in-place vs additional memory allocation) influence energy consumption.
  Experiments will be conducted using EnergiBridge on controlled workloads with increasing input sizes (e.g., 10³ to 10⁶ elements) and different data distributions (random, sorted, reverse-sorted). For each configuration, we will collect energy consumption and runtime measurements across multiple runs to ensure statistical reliability.
  Our goal is to analyze whether theoretical time complexity trends are reflected in energy usage, and to investigate how memory access patterns and input characteristics affect software energy efficiency. All experiments will be automated and provided in a replication package with scripts and documentation.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---
### Introduction
Algorithmic time complexity is a fundamental aspect of code analysis and a universal measure across computer science, typically depicted using "Big O" notation (we will assume worst case Big O, going forward). While this measurement method should  yeild reliable results, perfect conditions are rarely achievable in the real world. In this article, we will examine how our expected trends will compare to actual measurements taken across a variety of algorithms using implementations in both Rust and Python.


---


### Experiment Setup


#### Algorithm selection
The first step was the selection of algorithms to implement for our experiment. We tried to identify a set of algorithms which would span a range of complexities and operational methods. The following are the chosen algorithms for the experiment:
- **Merge Sort:**  Has a complexity of $O(n log n)$. Implemented in Rust and Python
- **Quick Sort:** Has a complexity of $O(n^2)$. Implemented in Rust and Python.
- **Radix Sort:** Has a complexity of $O(n log n)$. Implemented in Python. Chosen as it has a unique operation method where it performs iterative sorting on each significant digit of all values in the set.
- **Heap Sort:** Has a complexity of $O(n log n)$. Implemented in Python. Also has a unique operation whereby the root of the heap is removed on recursive heapify calls.


#### Experiment Runs
We created a simple Python CLI tool to perform the experiment by defining arguments for algorithm type, test set size, test set distribution and the number of runs to be performed. We performed **X** runs of each algorithm with a set size of **Y** and a **Z** distribution. The experiment run was automated with a one minute "cool off" period between tests to try account for tail energy consumption. The experiment was performed in one block on a single machine with background tasks minimized.

### Data Collection
We chose to record the energy measurements of our experiment rather than the power as sorting algorithms are specfic instances you run as opposed to a software application which essentially runs as long as the user desires. As mentioned previously, we intend to collect in excess of 30 data points per measurement so that we can assume a Normal/Gaussian distribution of our data as per the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem).

## Unbiased Energy Data ⚖️

There are a few things that need to be considered to minimise the bias of the energy measurements. Below, I pinpoint the most important strategies to minimise the impact of these biases when collecting the data.

### Zen mode 🧘🏾‍♀️

The first thing we need to make sure of is that the only thing running in our system is the software we want to measure. Unfortunately, this is impossible in practice – our system will always have other tasks and things that it will run at the same time. Still, we must at least minimise all these competing tasks:

- all applications should be closed, notifications should be turned off;
- only the required hardware should be connected (avoid USB drives, external disks, external displays, etc.);
- turn off notifications;
- remove any unnecessary services running in the background (e.g., web server, file sharing, etc.);
- if you do not need an internet or intranet connection, switch off your network;
- prefer cable over wireless – the energy consumption from a cable connection is more stable than from a wireless connection.

### Freeze your settings 🥶

It is not possible to shut off the unnecessary things that run in our system. Still, we need to at least make sure that they will behave the same across all sets of experiments. Thus, we must fix and report some configuration settings. One good example is the brightness and resolution of your screen – report the exact value and make sure it stays the same throughout the experiment. Another common mistake is to keep the automatic brightness adjustment on – this is, for example, an awful source of errors when measuring energy efficiency in mobile apps.

---

### 

Nevertheless, using statistical metrics to measure effect size is not enough – there should be a discussion of the **practical effect size**. More important than demonstrating that we came up with a new version that is more energy efficient, you need to demonstrate that the benefits will actually be reflected in the overall energy efficiency of normal usage of the software. For example, imagine that the results show that a given energy improvement was only able to save one joule of energy throughout a whole day of intensive usage of your cloud software. This perspective can hardly be captured by classic effect-size measures. The statistical approach to effect size (e.g., mean difference, Cohen's-*d*, and so on) is agnostic of the context of the problem at hand.

