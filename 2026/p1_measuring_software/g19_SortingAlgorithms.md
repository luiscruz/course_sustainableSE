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
Algorithmic time complexity is a fundamental aspect of code analysis and a universal measure across computer science, typically depicted using "Big O" notation (we will assume worst case Big O, going forward). While this measurement method should  yield reliable results, perfect conditions are rarely achievable in the real world. In this article, we will examine how our expected trends will compare to actual measurements taken across a variety of algorithms using implementations in both Rust and Python.


---

### Experiment Setup


#### Algorithm selection

The first step was the selection of algorithms to implement for our experiment. We tried to identify a set of algorithms which would span a range of complexities and operational methods. We selected these algorithms to cover a wide span of theoretical complexity and memory behaviour, since our research question can not solely be covered by only asymptotic runtime, as energy effects are also driven by allocation patterns and cache locality. In order to also explore how programming languages affect this, we decided to test with Rust and Python, and for this we needed a mix of algorithms that can be implemented consistently across both languages so that we can separate algorithm effects from language and runtime effects. We decided that half of the algorithms would have a cross language implementation, and the rest would just be in Python.

The following are the chosen algorithms for the experiment:
- **Merge Sort:** It provides a stable baseline with worst case $O(n log n)$ behaviour and a predictable access pattern. It usually allocates extra arrays during merging, so it represents an algorithm with higher memory allocation and copying. We implemented it in both Rust and Python to support our cross language comparison for a non in place algorithm.
- **Quick Sort:** We included it because its worst case complexity is $O(n^2)$ which is essential for our plan to compare quadratic worst case behaviour to $O(n log n)$. It mostly sorts in place and uses a partitioning step that accesses data differently than Merge Sort, so it helps isolate how in place operation and locality affect energy. We implemented it in Rust and Python so that we get a second cross language comparison with a different memory profile than Merge Sort.
- **Radix Sort:** Has a complexity of $O(n log n)$ and was chosen because it is non comparison based and works by repeated digit passes rather than pairwise comparisons. This makes its work pattern very different, with repeated full array scans and bucket grouping, which can increase cache misses and memory traffic. Implemented only in Python. 
- **Heap Sort:** Although it has the same theoretical complexity as Merge Sort $O(n log n)$, it moves elements across the array in a less sequential way, which can increase cache misses and memory traffic. This makes it useful for observing energy costs linked to weaker cache locality. Also implemented only in Python.

### Data Analysis

We chose to record the energy measurements of our experiment as the primary metric rather than the power as sorting algorithms are specific instances you run as opposed to a software application which essentially runs as long as the user desires. As mentioned previously, we intend to collect in excess of 30 data points per measurement (in reality, much much higher than 30) so that we can test for a Normal/Gaussian distribution of our data. 

#### Measurement boundary and instrumentation

In our setup, EnergiBridge measures energy for the whole benchmark command, including Python start up, imports, and reading and writing files. Our runtime timer measures only the time spent inside the sorting function. We do this on purpose, because we care most about the real energy cost of running a sorting task end to end, not only the energy used by the in memory sorting step.

#### Dataset generation, persistence, and reproducibility

For each configuration, defined by algorithm, input size and distribution, we generate an input array deterministically and make it persist to the disk. We also configured subsequent repetitions to reuse the exact same dataset file, since htis reduces variance caused by different random inputs and allows strict run to run comparability. We also control randomness via a deterministic seeding strategy so that the same configuration always maps to the same dataset. For replication purposes, we decided to store the input datasets as JSON to make the replication package easy to inspect and language independent.

We use multiple input distributions:

- random
- sorted
- reverse sorted
- almost sorted, defined as a sorted array with a small fraction of elements swapped at random positions

#### Execution order, warmup, and cooldown

To reduce bias from run order effects, we randomised the execution order of the full configuration matrix before running measurements. Also we decided to execute warmup runs that are not recorded, in order to stabilise CPU frequency scaling and OS power states. Between recorded runs, we enforce a fixed cooldown period so that any pre-generated energy and thermal carry over effects are reduced.

#### Correctness checks and failure handling

Each run includes a correctness check that verifies the output array is sorted. In the case that a run fails the correctness check, it is flagged and excluded from analysis, and the failure is recorded in the logs. This ensures that energy results are not reported for incorrect implementations or unstable runs.

#### System controls and machine state

To keep all experiments fair, we executed them all on a single machine under the same fxied environment.

- The device remains plugged in throughout the experiment session 
- Background tasks are minimised by closing non essential applications
- Display brightness remains fixed throughout the session
- Network usage is kept stable, and no large downloads or updates are allowed during runs

#### Hypotheses

As mentioned previously, energy consumption per run per set size will the primary metirc for our analysis. We are examining two relationships, between different complexity algorithms and between the same algorithms acorss langauages. To show the noramality of our data we expect
- **Algorithmic Complexity Energy Analysis:**
  - To prove the normality of the data, we will use a set of Shapiro-Wilk tests:
  $$H_0^{(i)}: p \geq 0.05, Data\ is\ normally\ distributed\ \forall i \in {Algorithms}$$
  $$H_A^{(i)}: P < 0.05, Data\ is\ NOT\ noramlly\ distributed\ \forall i \in {Algorithms}$$

  - To compare each test set we use **<Chosen Method>**:
  $$ TODO $$

- **Language Energy Comparison**
  - Again, we utilize the Shapiro-Wilk Test to show normality:
  $$H_0^{(i)}: p \geq 0.05, Data\ is\ normally\ distributed\ \forall i \in {SharedAlgos}$$
  $$H_A^{(i)}: P < 0.05, Data\ is\ NOT\ noramlly\ distributed\ \forall i \in {SharedAlgos}$$

  - As we are comparing only two elements here, we can apply a two-sided t-test:
  $$H_0: E_{Rust} = E_{Python}$$
  $$H_A: E_{Rust} \neq E_{Python}$$

#### Experiment Runs

We created a simple Python CLI tool to perform the experiment by defining arguments for algorithm type, test set size, test set distribution and the number of runs to be performed. We performed **X** runs of each algorithm with a set size of **Y** and a **Z** distribution. The experiment run was automated with a 10 second "cool off" period between tests to try account for tail energy consumption. This period was chosen after some initial experimentation to show no tail impact and because of the relative simplicity of the test operations. The experiment was performed in one block on a single machine running MacOS with background tasks minimized and after a power intensive task to ensure the CPU was "warmed up."

```bash
$ python runner.py --algo algorithms/radix_sort.py --size 10000 --runs 5 --distribution reversed
```

---

#### Machine Specification
The exact specs of the machine we used are outlined below. This can be useful when comparing to results you have gotten yourself. 

#### Other Points to Note

---


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

