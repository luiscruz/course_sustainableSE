---
author: Norah Elisabeth Milanesi, Nassiri Mohammed, Oei Jimmy, Turanlı Gonenc
group_number: 9
title: "Measuring the Energy Cost of Merge Sort: Python vs. JavaScript"
image: "img/g9/js_vs_py.png"
date: 12/02/2026
summary: |-
  This project investigates the energy consumption differences between Python and JavaScript when sorting large datasets using merge sort algorithm. By executing the same algorithm across datasets of varying sizes, we will analyze how programming language runtime characteristics influence energy usage and performance. Through this comparison, the study seeks to provide insights into the sustainability implications of language choice for computationally intensive tasks.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---


Body lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

This problem takes another level if we are counting on these measurements to make **groundbreaking research contributions** in this area. Some research projects in the past have underestimated this issue and failed to produce replicable findings. Hence, this article presents a roadmap on how to properly set up a scientific methodology to run energy efficiency experiments. It mostly stems from my previous work on [doing research and publishing](/publications) on Green Software.


This article is divided into two main parts: 1) how to set up energy measurements with minimum bias, and 2) how to analyse and take scientific conclusions from your energy measurements.
Read on so that we can get your paper accepted in the best scientific conference.

--- 

### Results & Statistical Analysis

#### *Language Comparison*

The most prominent finding is the large energy gap between Python and JavaScript. Averaged across all algorithms and dataset sizes, JavaScript consumed a mean of 3.94 J while Python consumed 26.24 J, a 6.7× difference. This gap is confirmed as statistically significant by a Mann-Whitney U test (U = 640, p < 0.0001), with a large effect size (rank-biserial r = −0.76, where |r| > 0.5 indicates a large effect). The Mann-Whitney test was chosen over a t-test because the energy distributions are right-skewed and span several orders of magnitude, violating the normality assumption. Figure 1 shows the mean energy growth across dataset sizes for each language–algorithm combination, and Figure 2 provides the overall distribution comparison.
<div align="center">
  <figure>
    <img src="img/g9/agg_energy_vs_size.png" width="780" alt="Mean energy vs dataset size">
    <figcaption><b>Figure 1.</b> Mean energy consumption vs dataset size (log scale), averaged across both devices. Lines represent each language–algorithm combination.</figcaption>
  </figure>
</div>
<br>
<div style="display: flex; justify-content: center; gap: 24px; flex-wrap: wrap;">
  <figure style="text-align: center; margin: 0;">
    <img src="img/g9/agg_violin_language.png" width="550" alt="Energy distribution per language">
    <figcaption><b>Figure 2.</b> Energy distribution per language.</figcaption>
  </figure>
  <figure style="text-align: center; margin: 0;">
    <img src="img/g9/agg_lang_vs_algo_bar.png" width="550" alt="Language comparison per algorithm">
    <figcaption><b>Figure 3.</b> Mean energy per language grouped by algorithm.</figcaption>
  </figure>
</div>
<br>

The energy gap grows non-linearly with dataset size. At small sizes (<= 125,000 elements) both languages remain below 10 J, but beyond 250,000 elements Python's energy diverges sharply. At 4,000,000 elements, Python Heapsort consumed 259.6 J compared to just 14.4 J for its JavaScript equivalent: an 18× difference at that scale. This divergence reflects Python's interpreted execution model, where each sorting operation incurs interpreter overhead that compounds at scale, whereas JavaScript's V8 JIT compiler optimises hot loops at runtime.

#### *Algorithm Comparison*

When aggregated across both languages, mean energy consumption ranked as: Heapsort (21.2 J) > Mergesort (13.5 J) > Quicksort (10.6 J). However, a Kruskal-Wallis test found no statistically significant difference between the three algorithms (H = 1.77, p = 0.41), and all pairwise Mann-Whitney comparisons between algorithms were also non-significant (all p > 0.24). This means the algorithm choice alone does not reliably predict energy consumption: the effect is dominated by the language.
<div style="display: flex; justify-content: center; gap: 24px; flex-wrap: wrap;">
  <figure style="text-align: center; margin: 0;">
    <img src="img/g9/agg_heatmap_algo_lang.png" width="400" alt="Heatmap of mean energy by algorithm and language">
    <figcaption><b>Figure 4.</b> Mean energy heatmap (algorithm x language).</figcaption>
  </figure>
  <figure style="text-align: center; margin: 0;">
    <img src="img/g9/agg_energy_ratio.png" width="650" alt="Energy ratio Python vs JavaScript">
    <figcaption><b>Figure 5.</b> Energy ratio (Python / JavaScript) per algorithm across dataset sizes.</figcaption>
  </figure>
</div>
<br>
Notably, the algorithm rankings reverse between languages at large scales. Within Python, Quicksort was the most efficient at 4M elements (102.9 J), followed by Mergesort (142.1 J) and Heapsort (259.6 J). Within JavaScript, Heapsort and Mergesort were nearly identical (14.4 J and 14.9 J), while Quicksort was the least efficient (17.9 J). This inversion is visible in Figure 5, where Quicksort's ratio dips below Heapsort's at large sizes, and suggests that JavaScript's JIT compiler benefits more from Heapsort's regular memory access patterns, whereas Python's interpreter penalises Heapsort's cache-unfriendly access pattern severely at scale.

#### **Energy vs Execution Time**

Power draw analysis (Figure 6) reveals that Python not only runs longer but also draws more power per second than JavaScript across all algorithms, meaning both dimensions contribute independently to its higher total energy.
<div align="center">
  <figure>
    <img src="img/g9/agg_power_draw.png" width="600" alt="Power draw per algorithm and language">
    <figcaption><b>Figure 6.</b> Mean power draw (Watts) per algorithm and language. Python sustains a higher instantaneous power draw in addition to longer execution times.</figcaption>
  </figure>
</div>

#### *Why Does This Happen?*

Before we dig in, a quick reminder of what we're actually measuring, because power and energy are not the same thing:

Power (Watts) is the instantaneous rate at which the CPU is consuming electricity. Energy (Joules) is the total electricity consumed over the entire execution. 

We compute it as:
<div align="center">
E = Σ P(t) × Δt
</div>

where P(t) is the power sampled at each timestep and Δt is the interval in seconds. Energibridge samples system power at ~200ms intervals.

So why does Python consume so much more of both? It comes down to how each runtime executes the code. CPython (Python's default interpreter) executes bytecode instruction-by-instruction, dynamic-typing every variable at every step. Each comparison in the sort loop goes through multiple layers of indirection. JavaScript's V8 engine watches that same loop, identifies it as "hot", and JIT-compiles it to optimised native machine code mid-execution. The result is that V8 runs the inner sort loop at near-native speed, CPython does not.

The algorithm differences are rooted in complexity and memory access patterns[1]:

- Heapsort thrashes the CPU cache: its heap operations jump non-sequentially through memory, triggering frequent cache misses. This is cheap in JavaScript (V8 handles it gracefully) but devastating in Python, where each miss multiplies the interpreter overhead.
- Mergesort allocates O(n) auxiliary memory per merge, which means more heap allocations and GC pressure, this shows up in Python's higher variance at large sizes.
- Quicksort's in-place, cache-friendly partitioning is why it wins in Python at scale. Fewer memory jumps means fewer expensive interpreter round-trips.


If you're running Python and sorting millions of records, Quicksort can be a good choice. But if energy efficiency is a hard requirement, the runtime choice matters far more than the algorithm: switching languages saves 6.7x on average, no sorting strategy required.

<div align="center">
<img src="img/g9/meme.png" width="450" alt="js over python meme">
</div>

### References

[1] Cormen, T. H. et al. (2009). Introduction to Algorithms 

#### 👉 Note 1:
If you are a **software developer** enthusiastic about energy efficiency but you are not particularly interested in scientific experiments, this article is still useful for you. It is not necessary to do "everything by the book" but you may use one or two of these techniques to reduce the likelihood of making wrong decisions regarding the energy efficiency of your software.

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

