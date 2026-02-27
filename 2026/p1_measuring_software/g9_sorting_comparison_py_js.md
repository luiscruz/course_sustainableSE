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

# THIS IS A START FOR MOTIVATION
Cloud computing has fundamentally reshaped how software is deployed. Among its forms, serverless computing - also known as Function as a Service (FaaS) - has gained significant traction [^hellerstein2019]. Services such as AWS Lambda, Azure Functions, and Google Cloud Functions enable developers to execute code on-demand without managing any underlying infrastructure. There exists a clear duopoly in the serverless computing market, where Python and JavaScript (Node.js) are the dominant programming languages [^eismann2022]. This makes the choice between them a routinely decision for cloud developers worldwide.

This decision is almost never made with energy consumption in mind, yet the environmental impact of software is becoming increasingly important. As serverless functions are used at massive scale, even small differences in energy usage can become a signficant cumulative power draw. As companies seek to reduce their carbon footprints, understanding the energy implications of their software is crucial for achieving their sustainability goals. This process starts with the choice of what programming language to use to develop their software.

Sorting is among the most fundamental operations in computer science [^cormen2009]. It is a common task performed in various applications, including serverless functions. The energy cost of such sorting tasks depends not only on the algorithmic complexity, but also on the programming language that runs it. Python and JavaScript have different runtime characteristics that can lead to varying energy consumption for similar tasks. By directly comparing the energy usage of three among the most used sorting algorithms - merge sort, quicksort, and heapsort - in both Python and JavaScript across datasets of varying sizes, we aim to provide insights into how language choice in serverless functions can impact the energy consumption of cloud applications.

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
  

# References

[^hellerstein2019]: Hellerstein, J. M., Faleiro, J., Gonzalez, J., Schleier-Smith, J., Sreekanti, V., Tumanov, A., & Wu, C. (2019). Serverless computing: One step forward, two steps back. *9th Biennial Conference on Innovative Data Systems Research (CIDR '19)*. [https://arxiv.org/abs/1812.03651](https://arxiv.org/abs/1812.03651)

[^eismann2022]: Eismann, S., Scheuner, J., van Eyk, E., Schwinger, M., Grohmann, J., Herbst, N., Abad, C. L., & Iosup, A. (2022). The state of serverless applications: Collection, characterization, and community consensus. *IEEE Transactions on Software Engineering*, *48*(10), 4152–4166. [https://doi.org/10.1109/TSE.2021.3113940](https://doi.org/10.1109/TSE.2021.3113940)

[^cormen2009]: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.