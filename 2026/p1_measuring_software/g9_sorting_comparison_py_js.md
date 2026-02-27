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


# References

[^hellerstein2019]: Hellerstein, J. M., Faleiro, J., Gonzalez, J., Schleier-Smith, J., Sreekanti, V., Tumanov, A., & Wu, C. (2019). Serverless computing: One step forward, two steps back. *9th Biennial Conference on Innovative Data Systems Research (CIDR '19)*. [https://arxiv.org/abs/1812.03651](https://arxiv.org/abs/1812.03651)

[^eismann2022]: Eismann, S., Scheuner, J., van Eyk, E., Schwinger, M., Grohmann, J., Herbst, N., Abad, C. L., & Iosup, A. (2022). The state of serverless applications: Collection, characterization, and community consensus. *IEEE Transactions on Software Engineering*, *48*(10), 4152–4166. [https://doi.org/10.1109/TSE.2021.3113940](https://doi.org/10.1109/TSE.2021.3113940)

[^pereira2017]: Rui Pereira, Marco Couto, Francisco Ribeiro, Rui Rua, Jácome Cunha, João Paulo Fernandes, João Saraiva,
Ranking programming languages by energy efficiency,
Science of Computer Programming,
Volume 205,
2021,
102609,
ISSN 0167-6423,
https://doi.org/10.1016/j.scico.2021.102609.

[^cormen2009]: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

[^pizarrovasquez2020]: Pizarro-Vasquez, G. O., Mejia Morales, F., Galvez Minervini, P., & Botto-Tobar, M. (2020). Sorting Algorithms and Their Execution Times an Empirical Evaluation. In L.-K. Lee, L. H. U, F. L. Wang, S. K. Cheung, O. Au, & K. C. Li (Eds.), Advances in Emerging Trends and Technologies - Proceedings of ICAETT 2020 (pp. 335-348). (Advances in Intelligent Systems and Computing; Vol. 1302). Springer. https://doi.org/10.1007/978-3-030-63665-4_27