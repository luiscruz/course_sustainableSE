---
author: Luc Dop, Sabina Grădinariu, Nawmi Nujhat, Vincent van Vliet
title: "Energy Consumption Comparison: Python 3.14 vs Python 3.11"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 24/02/2025
summary: |-
   This study explores the energy consumption differences between Python 3.14 and Python 3.11, testing the claim that Python 3.14 has a 30% speed improvement over previous versions. We run the same computational tasks in controlled environments and measure power usage, execution time, and overall efficiency. 
   Our setup includes automation for both Linux and MacOS with system parameters that can be tweaked according to the need, ensuring replicability. Future work will involve the  --with-tail-call-interp flag once it is working.
--- 
## Introduction
As programmers, we use programming languages daily, often forgetting how much impact the chosen language, and sometimes even its version, can have on energy consumption and implicitly on the environment ( [check]( https://arxiv.org/html/2410.05460v1) ). Python is known to be one of the most used languages, but also, according to previous studies such as [Ranking programming languages by energy efficiency](https://www.sciencedirect.com/science/article/abs/pii/S0167642321000022?via%3Dihub), it is amongst the least green (energy efficient) due to its interpreted execution and dynamic typing.

With the introduction of Python version 3.14, the documentation states that it utilizes a new type of interpreter that should provide significantly better performance. To be precise, preliminary numbers indicate anywhere from '-3% to 30% faster [Python](https://docs.python.org/3.14/whatsnew/3.14.html) code. With this performance improvement kept in mind, we have decided to investigate this claim to see how the performance increase impacts the energy consumption.

We started by analyzing Python 3.14 default configuration, without any additional optimizations. The documentation also mentions an experimental feature called the tail call interpreter, which is expected to enhance performance further when enabled. [Tail call-interp](https://docs.python.org/3.14/using/configure.html#cmdoption-with-tail-call-interp) should not be confused with [tail call optimization](https://en.wikipedia.org/wiki/Tail_call) of Python functions. 

However, this feature is opt-in, requires specific compiler versions (Clang 19+ on x86-64 and AArch64 architectures), and remains unavailable in the default build. Despite our efforts, we could not enable it, because it is not working yet. Therefore, our current study concentrates on benchmarking Python 3.14’s default interpreter against Python 3.11 to assess energy efficiency under highly demanding tasks.

--- 
## Methodology 
To this end, the idea is to use the prerelease version of the Python 3.14 interpreter and compare the energy consumption for the same code snippet for both the new interpreter as well as an older Python interpreter (3.11.9). This should allow us to see whether the supposed faster speeds of the new interpreter impact energy consumption. 
To assess the energy consumption we used [EnergiBridge](https://github.com/tdurieux/EnergiBridge) as suggested in the [lectures](https://luiscruz.github.io/course_sustainableSE/2025/).

### Code Snippet Selection 
To make sure that the comparison is a meaningful one, we used computationally intensive code that will stress the CPU. We create multiple snippets that can be seen on [GitLab](https://github.com/vincentvvliet/sse-project-group-24). 
### Hardware 

### Experiment Procedure 

### Replication

## Results


## Future work 

Although Python 3.14 showed no significant performance or energy efficiency gains over Python 3.11 in our tests, future research should revisit this comparison when the *tail-call-interpreter* becomes functional.
To identify potential optimization opportunities in Python 3.14, we could also run demanding I/O scenarios and multi-threading executions.

---

##  Conclusion 
Our study examined the energy consumption and performance differences between Python 3.14 and Python 3.11. We assess if Python 3.14’s allegedly 30% speed improvement can be seen in energy efficiency. Using EnergiBridge, we measured power usage and execution time across computationally intensive operations.
Our results indicate that there is no statistically significant difference in energy consumption or execution time between Python 3.14 (in its default configuration) and Python 3.11. 

Given this, we see no convincing motivation to switch from the more stable and well-supported Python 3.11 to Python 3.14 (at this time). The experimental tail call interpreter, which could provide further optimizations, remains non-functional, limiting Python 3.14’s potential benefits.

