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
With the introduction of Python version 3.14, the documentation states that it utilizes a new type of interpreter that should provide significantly better performance. To be precise, preliminary numbers indicate anyway from '-3% to 30% faster [Python](https://docs.python.org/3.14/whatsnew/3.14.html) code. With this performance improvement kept in mind, we have decided to investigate this claim to see how the performance increase impacts the energy consumption.
We started by analyzing Python 3.14 default configuration, without any additional optimizations. The documentation also mentions an experimental feature called the tail call interpreter, which is expected to enhance performance further when enabled. [Tail call](https://docs.python.org/3.14/using/configure.html#cmdoption-with-tail-call-interp) interepreter should not be confused with [tail call optimization](https://en.wikipedia.org/wiki/Tail_call) of Python functions. However, this feature is opt-in, requires specific compiler versions (Clang 19+, x86-64 and AArch64 architectures), and remains unavailable in the default build. Despite our efforts, we could not enable it, because it is not working yet. Therefore, our current study concentrates on benchmarking Python 3.14’s default interpreter against Python 3.11 to assess energy efficiency under highly demanding tasks.

--- 
## Methodology 
To this end, the idea is to use the prerelease version of the Python 3.14 interpreter and compare the energy consumption for the same code snippet [**TODO: write about code snippet (check which)**] for both the new interpreter as well as an older Python interpreter (3.11.9). This should allow us to see whether the supposed faster speeds of the new interpreter impact energy consumption. 
To asses the energy consuption we used [EnergiBridge](https://github.com/tdurieux/EnergiBridge).

### Hardware 

### Experiment Procedure 

### Replication

## Results


## Future work 


---

##  Conclusion 


