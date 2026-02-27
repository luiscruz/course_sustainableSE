---
author: Norah Elisabeth Milanesi, Mohammed Nassiri, Jimmy Oei, Gonenc Turanlı
group_number: 9
title: "Sorting Out Energy: Comparing Merge Sort, Quick Sort, and Heap Sort in Python vs. JavaScript"
image: "img/g9/js_vs_py.png"
date: 12/02/2026
summary: |-
  This study compares the energy consumption of three widely used sorting algorithms - merge sort, quick sort, and heap sort - implemented in both Python and JavaScript (Node.js). By measuring energy usage across datasets of varying sizes, we gain insights into how language choice affects the energy efficiency of sorting operations. Our findings are particularly relevant to serverless cloud environments, where the language choice can have significant implications for the energy consumption of applications at scale.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

TODO: introduction here

## Energy Efficiency in Serverless Computing
Cloud computing has fundamentally reshaped how software is deployed. Among its forms, serverless computing - also known as Function as a Service (FaaS) - has gained significant traction [^hellerstein2019]. Services such as AWS Lambda, Azure Functions, and Google Cloud Functions enable developers to execute code on-demand without managing any underlying infrastructure. There exists a clear duopoly in the serverless computing market, where Python and JavaScript (Node.js) are the dominant programming languages [^eismann2022]. This makes the choice between them a routine decision for cloud developers worldwide.

This decision is almost never made with energy consumption in mind, yet the environmental impact of software is becoming increasingly important. As serverless functions are used at massive scale, even small differences in energy usage can become a significant cumulative power draw. As companies seek to reduce their carbon footprints, understanding the energy implications of their software is crucial for achieving their sustainability goals. This process starts with the choice of what programming language is used to develop their software, as prior research has shown this choice can have a measurable effect on energy consumption. Pereira et al. [^pereira2017] compared 27 languages and found that Node.js was considerably more energy efficient than Python. However, their study used general micro-benchmarks and did not examine specific algorithms or the serverless context.

Sorting is among the most fundamental operations in computer science [^cormen2009]. It is a common task performed in various applications, including serverless functions where they are especially used at scale for data processing: ingesting events, ETL pipelines, ranking records before storage, etc. Furthermore, sorting is a computationally intensive task that puts direct pressure on the language runtime, which makes it a good candidate for comparing energy efficiency across languages. By directly comparing the energy usage of sorting algorithms - merge sort, quicksort, and heapsort - in Python and JavaScript we aim to provide insights into how language choice in serverless functions can impact the energy consumption of cloud applications.


## Why Merge Sort, Quick Sort, and Heap Sort?
Merge sort, quick sort, and heap sort are among the most recognized and used sorting algorithms [^pizarrovasquez2020]. These three all share the same average time complexity of O(n log n), which makes their performance more comparable as the algorithmic efficiency is similar. However, the three algorithms also have different computational profiles as you can see in the table below. By controlling for time complexity, we can better isolate the differences between the computational profiles of the algorithms to see whether Python or Node.js affect them equally or favour specific ones.

| Algorithm | Best Case | Average Case | Worst Case | Memory | Computational Profile |
|-----------|-----------|--------------|------------|--------|-----------------------|
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Divide-and-conquer, recursive |
| Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | Divide-and-conquer, in-place |
| Heap Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | In-place, binary heap |

# Methodology
The experiment can be ran automatically by executing the ‘run_experiment.sh’ script, which measures the energy consumption for different sizes of datasets, with configurable aspects such as iteration count per dataset size and the sorting algorithm to be tested. Specifically, the script runs energibridge and measures the energy consumption of each implementation of the sorting algorithms, for both python and javascript.
While setting up and conducting our experiment, we followed the Scientific Guide to Set Up Energy Efficiency Experiments in order to ensure the accuracy, correctness and appropriateness of our results, and to reduce bias as much as possible. Whenever running the experiments, all other software, notifications and services was turned off. Settings of the machines running the experiment that might affect power consumption, such as screen brightness, were also frozen. The machines ran dummy tasks before the experiments were conducted as warm up. Due to the amount of time the experiments take, the number of repetetitions were kept at 10 for each sorting algorithm, which results in 30 total repetitions per experiment. The order of the sorting algorithms being subject to the experiment were also randomized, and the room temperature was kept stable. Once all these conditions were met, the automated script was run on the machines, once for each of the three sorting algorithms. Finally, the datasets being used in the experiment as the input for the sorting algorithms are simple input-n.txt files, which contain numbers in each row,going from 1 to n-1. The algorithms take these files, and sort their contents.
To ensure that we actually measure the energy consumption, and therefore the difference in amount of energy consumed, between python and javascript while minimizing all other factors that might affect energy consumption, our experimental variables were determined as follows:
- Independent: Programming languages (Python and JavaScript)
- Dependent: Energy consumption
- Controlled: Implementation of the sort algorithms, specs of the machines running the experiment, versions of the tools used in running the experiment

  - Python version: 3.13.7
  - Node version: v22.22.0
  - Specs: Apple M2, 16GB RAM + Apple M1, 16GB
  

## Results & Statistical Analysis

### *Language Comparison*

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

### *Algorithm Comparison*

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

### *Why Does This Happen?*

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

# References

[^hellerstein2019]: Hellerstein, J. M., Faleiro, J., Gonzalez, J., Schleier-Smith, J., Sreekanti, V., Tumanov, A., & Wu, C. (2019). Serverless computing: One step forward, two steps back. *9th Biennial Conference on Innovative Data Systems Research (CIDR '19)*. [https://arxiv.org/abs/1812.03651](https://arxiv.org/abs/1812.03651)

[^eismann2022]: Eismann, S., Scheuner, J., van Eyk, E., Schwinger, M., Grohmann, J., Herbst, N., Abad, C. L., & Iosup, A. (2022). The state of serverless applications: Collection, characterization, and community consensus. *IEEE Transactions on Software Engineering*, *48*(10), 4152–4166. [https://doi.org/10.1109/TSE.2021.3113940](https://doi.org/10.1109/TSE.2021.3113940)

[^pereira2017]: Pereira, R., Couto, M., Ribeiro, F., Rua, R., Cunha, J., Fernandes, J. P., & Saraiva, J. (2021). Ranking programming languages by energy efficiency. *Science of Computer Programming*, *205*, 102609. [https://doi.org/10.1016/j.scico.2021.102609](https://doi.org/10.1016/j.scico.2021.102609)

[^cormen2009]: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

[^pizarrovasquez2020]: Pizarro-Vasquez, G. O., Mejia Morales, F., Galvez Minervini, P., & Botto-Tobar, M. (2020). Sorting algorithms and their execution times: An empirical evaluation. In *Advances in Emerging Trends and Technologies — Proceedings of ICAETT 2020* (pp. 335–348). Springer. [https://doi.org/10.1007/978-3-030-63665-4_27](https://doi.org/10.1007/978-3-030-63665-4_27)

[1] Cormen, T. H. et al. (2009). Introduction to Algorithms 