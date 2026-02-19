---
author: Rebecca Andrei, Boris Annink, Paul Anton, Kevin Ji Shan
group_number: 22
title: "Energy Consumption of File Compression Across Programming Languages"
image: "img/g22_zip/project_cover.png"
date: 27/02/2026
summary: |-
  Something to be re-written later.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Introduction

Software powers the world. Every sent message, every stored dataset, and every archived log is processed by layers of software that execute on energy-consuming hardware. As digital infrastructure grows, the environmental impact of software has emerged as a prominent theme in computing research [1]. Data centers account for an increasingly larger portion of global electricity consumption [2], and software design choices influence how effectively hardware resources are used [3]. 

Recent studies suggest that the choice of programming language is one such decision. Pereira *et al.* [4] report substantial differences in runtime and energy consumption for equivalent workloads, which they ascribe to language-specific memory management and compiler optimization. A very simple design choice can have tangible effects on the environment when it is considered over millions of executions. This observation leads to an important question: when software developers choose a language ecosystem for a given task, are they implicitly making an energy choice as well?

This project investigates that question through a controlled case study. We will examine the energy consumption of a typical software engineering task: file compression and decompression using the `gzip` format [5]. Every second, massive amounts of data are compressed and decompressed, recent measurements showing that 90.5% of websites rely on it, with `gzip` alone accounting for 49.5% of all sites [6]. Web servers compress HTTP responses, databases archive backups, package managers transfer compressed artifacts, and cloud services are constantly moving compressed artifacts between storage and computation tiers. Compression is one of the most common tasks in today’s computing world, which makes even small differences in its energy efficiency significant from a sustainability perspective.

The case study was intentionally chosen so as to be simple and easy to understand. Instead of comparing the relative merits of various compression algorithms, we chose to focus on the well-known example of `gzip` in order to examine how different programming languages complete the same exercise. We will compare file compression implementations written in Python, Java, Go, and C++, implemented using each language's standard libraries and typical runtime characteristics as much as possible. That is because, in a real-world setting, developers tend not to implement their own low-level algorithms but would instead rely on the abstractions provided by the language. Our comparison will thus allow us to realistically analyze the sustainability implications of choosing one language environment over another for a common task.

This is a practical study for software developers. In a large-scale system where compression is performed millions of times, even small percentage differences per call can result in large total energy costs. On the other hand, if the differences are small, then software developers can focus on other factors, such as ease of development, without worrying about sustainability implications. With more and more companies setting sustainability goals and reporting on environmental metrics, software design decisions must be supported by empirical evidence rather than intuition or anecdotal evidence. To provide such evidence, this study aims to scientifically quantify the impact of language efficiency in a concrete and widely relevant scenario.


# Research Questions

Through this study, we seek to answer a practical question: when two systems perform the same task, how much does the choice of programming language matter for energy efficiency?



# Methodology

## Data

## Experimental Setup

## Implementation Details

## Evaluation Metrics

## Analysis Procedure


# Results


# Discussion

## Interpretation of Results

## Practical Implications


# Conclusion

## Reflection

## Limitations

## Future Work


# References

[1] P. Pathania, N. Bamby, R. Mehra, S. Sikand, V. S. Sharma, V. Kaulgud, S. Podder, and A. P. Burden, “Calculating software’s energy use and carbon emissions: A survey of the state of art, challenges, and the way ahead,” in *Proc. 2025 IEEE/ACM 9th Int. Workshop on Green and Sustainable Software (GREENS)*, Apr. 2025, pp. 92–99, doi: 10.1109/GREENS66463.2025.00018.

[2] International Energy Agency, *What the data centre and AI boom could mean for the energy sector*, IEA, Oct. 18, 2024. Available: https://www.iea.org/commentaries/what-the-data-centre-and-ai-boom-could-mean-for-the-energy-sector

[3] D. Connolly Bree, “The impact of software design on energy performance,” Ph.D. dissertation, School of Computer Science, University College Dublin, Dublin, Ireland, 2025.

[4] R. Pereira, M. Couto, F. Ribeiro, R. Rua, J. Cunha, J. P. Fernandes, and J. Saraiva, “Energy efficiency across programming languages: How do energy, time, and memory relate?” in *Proc. 10th ACM SIGPLAN Int. Conf. Software Language Engineering (SLE)*, Vancouver, BC, Canada, 2017, pp. 256–267, doi: 10.1145/3136014.3136031.

[5] Free Software Foundation, “GNU Gzip,” *GNU Operating System*. [Online]. Available: https://www.gnu.org/software/gzip/.

[6] W3Techs, “Usage statistics of compression for websites,” *W3Techs – Web Technology Surveys* [Online]. Available: https://w3techs.com/technologies/details/ce-compression.