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
What if I told you that simply choosing the wrong programming language for a basic sorting algorithm could consume **10 times** more real-world energy? We set out to measure the actual physical cost of classic sorting algorithms, and the results completely upended our expectations about efficiency.

To investigate this, we looked at algorithmic time complexity. This fundamental aspect of code analysis and a universal measure across computer science, is typically depicted using "Big O" notation (we will assume worst case Big O, going forward). While this measurement method should  yield reliable results, perfect conditions are rarely achievable in the real world. In this article, we will examine how our expected trends will compare to actual measurements taken across a variety of algorithms using implementations in both Rust and Python.


---
### Experiment Setup


#### Algorithm selection

We did not choose these sorting algorithms randomly. The goal of the experiment was not just to compare which one is “fastest,” but to understand why different algorithms consume different amounts of energy. To do that properly, we needed a set of algorithms that differ in meaningful ways: theoretical time complexity, whether they work in-place or require extra memory, how predictable their performance is across inputs, and how they interact with the CPU cache. Prior research shows that execution time explains a large share of energy consumption, but it is not the whole story. Memory traffic, cache misses, and locality also affect how much energy a program uses in practice, especially when two algorithms have similar asymptotic complexity [1][2][3].

That is why we selected Merge Sort, Quick Sort, Radix Sort, and Heap Sort. Together, these four algorithms give us a useful spread across the design space. They let us compare stable versus unstable behavior, in-place versus non-in-place strategies, comparison-based versus non-comparison-based methods, and cache-friendly versus cache-unfriendly memory access patterns. In other words, this set was chosen so that each algorithm highlights a different performance and energy trade-off rather than all behaving in roughly the same way [3][4].

Here is a quick overview of how our chosen algorithms stack up against each other:

| Algorithm | Average Time Complexity | Worst Case | Memory / In-Place | Cache Friendliness |
| :--- | :--- | :--- | :--- | :--- |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | Not in-place | Predictable |
| **Quick Sort** | $O(n \log n)$ | $O(n^2)$ | In-place | High |
| **Radix Sort** | $O(nk)$ | $O(nk)$ | Not in-place | Requires full scans |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | In-place | Low (jumpy access) |

The following are the chosen algorithms for the experiment:
- **Merge Sort:** We chose Merge Sort because it is one of the clearest examples of a theoretically strong and highly predictable algorithm. Its running time stays at $O(n log n)$ regardless of whether the input is random, sorted, or nearly sorted, which makes it a **reliable baseline**. That consistency is useful in an energy experiment because it reduces the risk that strange input cases dominate the results. At the same time, Merge Sort is usually **not in-place**, so it needs extra memory for the merge step. That means it generates **additional copying, allocation, and memory traffic** compared with algorithms that mostly rearrange values inside the original array. This makes Merge Sort a good candidate for studying the cost of “clean” theoretical efficiency when it comes with higher memory overhead [3]
- **Quick Sort:** We included Quick Sort because it gives almost the opposite profile. On average, it is also $O(n log n)$, and in practice it is often extremely efficient. However, unlike Merge Sort, its performance depends much more on how the pivot is chosen and how the data is distributed. In a bad case, Quick Sort can degrade to $O(n^2)$. That sensitivity makes it interesting because it shows how an algorithm that is usually excellent can become much worse under unfavorable conditions. We also chose it because Quick Sort is **mostly in-place** and tends to benefit from **good locality** during partitioning. That makes it useful for testing whether lower memory overhead and better cache behavior translate into lower energy consumption compared with a more allocation-heavy algorithm like Merge Sort [3][4]
- **Radix Sort:** We selected Radix Sort because we did not want the experiment to contain only comparison-based algorithms. Radix Sort works in a fundamentally different way: instead of repeatedly comparing elements, it sorts values digit by digit or bit by bit. For integer data, that can make it very fast and in some cases very energy-efficient. But its execution pattern is also quite different from Quick Sort or Merge Sort. It **repeatedly scans the full array** and distributes values into buckets or counting structures, which can produce a **different kind of memory-access behavior**. That matters because the experiment is not just about counting operations on paper; it is about observing what happens when those operations interact with real hardware. Radix Sort therefore helps us study whether an algorithm that looks attractive in theory for certain data types still behaves efficiently when memory access patterns become more scattered or repetitive [3]. 
- **Heap Sort:** We included Heap Sort because it provides another important contrast. Like Merge Sort, it guarantees $O(n log n)$ worst-case time, and like Quick Sort, it is **in-place**. On paper, that combination sounds very attractive. But in practice, Heap Sort is often slower than those alternatives because its memory-access pattern is **less cache-friendly**. Maintaining the heap causes the algorithm to **jump around the array** in a way that hurts locality. We chose Heap Sort specifically because it helps separate time complexity on paper from practical efficiency on hardware. If two algorithms have similar asymptotic complexity but different locality, then any energy difference between them becomes much more informative. Heap Sort is therefore useful as a kind of stress test for the impact of poor cache behavior [3].

Another reason these four algorithms were a strong set is that together they let us observe several comparisons at once. Merge Sort vs Quick Sort helps us compare predictable performance with lower-memory, in-place behavior. Quick Sort vs Heap Sort helps us compare two in-place algorithms that differ strongly in locality. Radix Sort vs the comparison sorts helps us test whether avoiding comparisons actually improves performance and energy use in practice, or whether memory behavior becomes the dominant issue. That means the set is not just four isolated algorithms; it is a group chosen to create meaningful pairwise comparisons [3][4].

Finally, this set also made sense from an implementation perspective. All four algorithms are well known, widely studied, and straightforward enough to implement consistently in both Python and Rust without introducing unnecessary complexity. That matters because the experiment is supposed to compare algorithmic behavior, not hide the conclusions inside overly specialized code. By choosing algorithms that are standard, recognizable, and theoretically distinct, we made it easier to explain the results and connect them back to the literature [1][3][4].

#### Existing Literature
There is some interesting existing work in this space, most notably [Towards understanding algorithmic factors affecting energy consumption: Switching complexity, randomness, and preliminary experiments](https://www.researchgate.net/publication/221406552_Towards_understanding_algorithmic_factors_affecting_energy_consumption_Switching_complexity_randomness_and_preliminary_experiments) a joint papaer released by researchers at Microsoft and Google. While their reasearch focuses on mobile devices, their definition of "Switching Complexity" (i.e., the frequency with which a piece of code will 'jump' between modules within the CPU) is very useful here as it gives some creadance to the idea that algorithms of equal time complexity can very substantially in their energy use. This greatly influced our algorithm selection process.


### Data Analysis

We chose to record the energy measurements of our experiment as the primary metric rather than the power as sorting algorithms are specific instances you run as opposed to a software application which essentially runs as long as the user desires. As mentioned previously, we intend to collect in excess of 30 data points per measurement (in reality, much much higher than 30) so that we can test for a Normal/Gaussian distribution of our data. 

#### Measurement Boundary: What Exactly Are We Measuring?

In our setup, EnergiBridge measures energy for the whole benchmark command, including Python start up, imports, and reading and writing files. Our runtime timer measures only the time spent inside the sorting function. We do this on purpose, because we care most about the real energy cost of running a sorting task end to end, not only the energy used by the in memory sorting step.

#### The Sandbox: Generating and Freezing the Data

For each configuration, defined by algorithm, input size and distribution, we generate an input array deterministically and make it persist to the disk. We also configured subsequent repetitions to reuse the exact same dataset file, since this reduces variance caused by different random inputs and allows strict run to run comparability. We also control randomness via a deterministic seeding strategy so that the same configuration always maps to the same dataset. For replication purposes, we decided to store the input datasets as JSON to make the replication package easy to inspect and language independent.

We use multiple input distributions:

- random
- sorted
- reverse sorted
- almost sorted, defined as a sorted array with a small fraction of elements swapped at random positions

#### Warming Up and Cooling Down: Executing the Experiment

To reduce bias from run order effects, we randomised the execution order of the full configuration matrix before running measurements. Also we decided to execute warmup runs that are not recorded, in order to stabilise CPU frequency scaling and OS power states. Between recorded runs, we enforce a fixed cooldown period so that any pre-generated energy and thermal carry over effects are reduced.

#### Did it actually sort? (Checking for Failures)

Each run includes a correctness check that verifies the output array is sorted. In the case that a run fails the correctness check, it is flagged and excluded from analysis, and the failure is recorded in the logs. This ensures that energy results are not reported for incorrect implementations or unstable runs.

#### Building the Perfect Sandbox: Eliminating Background Noise

To keep all experiments fair, we executed them all on a single machine under the same fixed environment.

- The device remains plugged in throughout the experiment session 
- Background tasks are minimised by closing non essential applications
- Low display brightness, remains fixed throughout the session
- Device is set to airplane mode with bluetooth turned off to reduce background traffic further

#### Hypotheses

As mentioned previously, energy consumption per run per set size will be the primary metric for our analysis. We are examining two relationships, between different complexity algorithms and between the same algorithms across languages. 
- **Algorithmic Complexity Energy Analysis:**
  - To prove the normality of the data, we will use a set of Shapiro-Wilk tests:
  $$H_0^{(i)}: p \geq 0.05, Data\ is\ normally\ distributed\ \forall i \in {Algorithms}$$
  $$H_A^{(i)}: P < 0.05, Data\ is\ NOT\ noramlly\ distributed\ \forall i \in {Algorithms}$$

  - To check if there is a significant difference between python algorithms we use a ANOVA comparison:
  $$H_0^{(i)}: p \geq 0.05, There\ is\ no\ difference\ in\ energy\ usage\ \forall i \in {Python\ Algorithms}$$
  $$H_A^{(i)}: P < 0.05, Data\ IS\ difference\ in\ energy\ usage\ \forall i \in {Python\ Algorithms}$$

- **Language Energy Comparison**
  - Again, we utilize the Shapiro-Wilk Test to show normality:
  $$H_0^{(i)}: p \geq 0.05, Data\ is\ normally\ distributed\ \forall i \in {SharedAlgos}$$
  $$H_A^{(i)}: P < 0.05, Data\ is\ NOT\ noramlly\ distributed\ \forall i \in {SharedAlgos}$$

  - As we are comparing only two elements here, we can apply a two-sided t-test:
  $$H_0: E_{Rust} = E_{Python}$$

  $$H_A: E_{Rust} \neq E_{Python}$$

#### Experiment Runs

We created a simple Python CLI tool to perform the experiment by defining arguments for algorithm type, test set size, test set distribution and the number of runs to be performed. We performed 30 runs for each distribution, with a set size of 500.000, totaling 120 runs per algorithm. The experiment run was automated with a 10 second "cool off" period between tests to try account for tail energy consumption. This period was chosen after some initial experimentation to show no tail impact and because of the relative simplicity of the test operations. The experiment was performed in one block on a single machine running MacOS with background tasks minimized and after a power intensive task to ensure the CPU was "warmed up."

```bash
$ python runner.py --algo algorithms/radix_sort.py --size 10000 --runs 5 --distribution reversed
$ python scripts/run_rust_energy.py -n 500000 --dataset-dir Results/tmp_datasets --runs 1 --sleep 10
```
### Results

First, lets start off with the python algorithms only:

| Algorithm | Mean energy usage | Std. Deviation |
| --- | ---| --- |
| Heapsort | 13.61 J | 9.81 |
| Mergesort | 5.26 J | 3.13 |
| **Radixsort** | **2.43 J** | 2.17 |
| Quicksort | 3.54 J | 1.03 |

Using the anova test we get a p value of roughly p = 6.82e-54 < 0.05, making it clear there is a significant statistical difference in energy usage between algorithms. Looking at the table (and in the image below), it is clear that Radixsort and Quicksort are the most energy-efficient, with mergesort not far behind and heapsort being the least efficient of all.

For the Rust-based algorithms, we can compare the quicksort and mergesort values to the python values: 

| Algorithm | Mean energy usage | Std. Deviation |
| --- | ---| --- |
| **Mergesort** | **0.58 J** | 0.28 |
| Quicksort | 0.68 J | 0.57 |

Even without the comparison, we can clearly see there is a significant difference between the languages. For Mergesort, Rust is more efficient by a factor of 10(!!), and for quicksort by roughly 5. The energy usage also fluctuates less. Performing a 2-sided t-test on the averages between the languages we get a p-value of p = 2.44e-64 < 0.05, again showing a significant difference between the languages in terms of efficiency. The differences are staggering, showing truly how efficient low-level languages like Rust are compared to Python.

![Violin plot, showing the energy usage between algorithms and languages](/2026/p1_measuring_software/img/image.png)
Violin plot of the different algorithms' energy usage. 

The figure illustrates the above points very well, with rusts' usage being so low that it's nearly impossible to see what values it averages at, with the highest outlier only slightly above the lowest mean for python. The difference is massive.

#### Conclusion
With this data in hand, we can put both hypotheses to sleep, and clearly state that there is a significant difference in energy usage based on what algorithm you pick as well as what language you use. As we expected, lower levels languages like Rust dramatically outpreform higher level language implementations. Furthermore, we see that time complexity alone is not sufficient data to compare imnplementations in terms of energy use. As the world and we as software engineers continue to focus more and more on the long term sustatinability of our work, keeping this relationship (or lack thereof) in mind when designing/maintianing systems. Wider adoption of the "Switching Complexity" definition and/or inscreased measurement of it would certainly help us to become better programmers, reduced CO2 emissions and save money.

#### Machine Specification
The exact specs of the machine we used are outlined below. This can be useful when comparing to results you have gotten yourself. 

Device: MacBook Pro 2017
Processor: 2,3 GHz Dual core Intel core i5
Graphics card: Intel Iris plus graphics 640 1536 MB 
Memory: 8 GB 2133MHz LPDDR3
Operating system: MacOS Ventura 13.7.8 

---

### Sources
[1] Carter et al., Energy and Time Complexity for Sorting Algorithms in Java
[2] Roy et al., An Energy Complexity Model for Algorithms
[3] LaMarca and Ladner, The Influence of Caches on the Performance of Sorting
[4] Schmitt et al., Energy-Efficiency Comparison of Common Sorting Algorithms
