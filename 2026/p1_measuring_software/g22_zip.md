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

This project investigates that question through a controlled case study. We will examine the energy consumption of a typical software engineering task: file compression and decompression using the `gzip` format [5]. Every second, massive amounts of data are compressed and decompressed, measurements showing that 90.5% of websites rely on it, with `gzip` alone accounting for 49.5% of all sites [6]. Web servers compress HTTP responses, databases archive backups, package managers transfer compressed artifacts, and cloud services are constantly moving compressed artifacts between storage and computation tiers. Compression is one of the most common tasks in today’s computing world, which makes even small differences in its energy efficiency significant from a sustainability perspective.

The case study was intentionally chosen so as to be simple and easy to understand. Instead of comparing the relative merits of various compression algorithms, we chose to focus on the well-known example of `gzip` in order to examine how different programming languages complete the same exercise. We will compare file compression implementations written in Python, Java, Go, and C++, implemented using each language's standard libraries and typical runtime characteristics as much as possible. That is because, in a real-world setting, developers tend not to write their own low-level algorithms but rely instead on the abstractions provided by the language. Our comparison will thus allow us to realistically analyze the sustainability implications of choosing one language environment over another for a common task.

This is a practical study for software developers. In a large-scale system where compression is performed millions of times, even small percentage differences per call can result in large total energy costs. On the other hand, if the differences are trivial, then software developers can focus on other factors, such as ease of development, without worrying about sustainability implications. With more and more companies setting sustainability goals and reporting on environmental metrics, software design decisions must be supported by empirical evidence rather than intuition or anecdotal experience, a need underscored by McGuire *et al* [7], who found that the academic literature is surprisingly lacking in this context. To provide such evidence, this study aims to scientifically quantify the impact of language efficiency in a concrete and widely relevant scenario.


# Research Questions

Through this study, we seek to answer a practical question: when two systems perform the same task, how much does the choice of programming language matter for energy efficiency? To that end, we use our case study of `gzip` file compression and decompression to narrow down our scope to three aspects of the problem. First, we examine whether there are any systematic energy differences between language ecosystems. Second, we explore whether these differences are consistent across workload characteristics, and, more importantly, whether they are statistically significant rather than incidental. Third, we investigate the relationship between runtime and energy, given that runtime is commonly used as a proxy for efficiency. We thus propose the following research questions:

**1.** Do Python, Java, Go, and C++ differ significantly in energy consumption when performing identical `gzip` compression and decompression tasks under controlled conditions?

**2.** Are the observed energy differences consistent across data types (compressible vs. incompressible) and operations (compression vs. decompression), and how statistically significant are these differences?

**3.** Is the language that achieves the lowest runtime also the most energy efficient for `gzip` compression and decompression?


# Methodology

This section explains the experimental design we used to measure and compare the energy consumption of `gzip` compression and decompression for different programming languages. We discuss the design of the input data, the experimental setup, the implementation details for each programming language, and the statistical analysis that has been performed on the results.

## Data

We generate fully deterministic synthetic input data both for the purpose of reproducibility and to make sure that the differences in energy consumption can be attributed solely to the language ecosystems and not to the variability of our input datasets. All inputs are created by a custom Python script (`data/generate_input.py`), which takes a fixed seed and a size in megabytes, then produces exactly the same sequence of bytes every time. The script also prints the SHA-256 hash of every file it produces, so that it can be determined whether the input data used in a later replication attempt is exactly the same as the one in our experiment.

We examine two workload types, which represent the extremes of the compression spectrum. The first type of workload contains highly *compressible data*, modeled after unstructured logs. The data is represented as JSONL (JSON Lines) records with the same structure and repeated fields (log level, service, region, action, etc). The values of each field are varied deterministically by using a seeded SHA-256 counter-mode pseudo-random number generator (PRNG). The second type of workload contains *incompressible data*, which is generated as a uniform byte stream using the same deterministic PRNG and stored in a binary file. This simulates data that has very little redundancy, such as encrypted or already-compressed data. We chose to include both types of workloads so that we could observe how different languages perform under both optimal and worst-case conditions. Lastly, we generate two independent datasets for each category to see if our results are generalizable.


## Experimental Setup

## Implementation Details

We standardize the same algorithm design across all languages. Each implementation provides a small command-line interface of the form `mode input_file output_file`, with the `mode` being either compression or decompression. The `gzip` compression level is fixed at 6 for all languages, which matches the default setting [8]. All files are processed in binary mode, and compression is done using each language's standard library in a streaming fashion, without system calls or external tools, so that the measurements reflect purely the behavior of the language. If applicable, we also use a buffer size of 32 KB to keep memory usage and I/O behavior comparable.


### Java

### C++

The C++ implementation directly uses the `zlib` library [9] for compression and decompression, both of which are performed with matching parameters through `deflateInit2` and `inflateInit2`, respectively. Data is processed incrementally, in fixed-size chunks, by feeding the input buffers into the stream and writing the output until the stream ends. We chose to use chunked streaming so that we could avoid loading the entire file into memory, and so manage to keep the memory usage stable across file sizes. This also happens to be a typical design for C++ applications. 

### Python
The python implementation uses the built-in `gzip` module, which is a wrapper around the `zlib` library you would find in C++. The API is very straightforward, and is representative of how Python developers would typically perform compression and decompression tasks. The three simple methods `open`, `compress`, and `decompress` are used to read and write files in a streaming fashion. The `gzip` module also allows us to set the compression level, which we fix at 6 to match the other implementations.



## Metrics
To evaluate the sustainability and performance of the selected languages mentioned above, we measure several metrics that capture different aspects of their behavior. These metrics allow us to compare the energy efficiency and runtime performance of the implementations in a comprehensive manner.

Energy consumption (E) measured in Joules (J) is the primary metric of interest, as it directly relates to the sustainability implications of software applications. We use EnergiBridge to capture the energy consumption of the entire package. This represents the total work performed by the hardware to execute the compression and decompression tasks, including CPU and integrated graphics package. Minimizing E is the direct goal of reducing carbon footprint of the software [10]. In our scenario, measuring E is more suitable than measuring power (P) in Watts (W), which represents the rate of energy consumption, because we are interested in the total energy used for a given task rather than the continuous power draw.

Execution time (T) is measured in seconds (s) using wall-clock time. This metric captures the performance of the implementations. It is particulary relevant when considering the trade-off between energy efficiency and runtime, as some implementations may be more energy efficient but take longer to execute. Minimizing T is important for user experience and operational efficiency. We could also penalize implementations that are energy efficient but have long runtimes using the Energy Delay Product (EDP) measured in Joule * seconds (J·s), which is calculated as E multiplied by T [12]. This metric captures the trade-off between energy efficiency and runtime performance, and minimizing EDP can lead to more balanced solutions.

Compression ratio (CR) is a metric calculated as the size of the compressed file divided by the size of the original file. This metric captures the effectiveness of the compression algorithm in reducing file size. A lower CR indicates better compression efficiency, which can lead to reduced storage requirements and potentially at the cost of increased energy consumption due to more calculations [12][13].

Energy per megabyte measured in Joules per megabyte (J/MB) is calculated as the total energy consumed (E) divided by the size of the input file in megabytes. This metric provides a normalized measure of energy efficiency, allowing us to compare the normalized energy efficiency. A lower E/MB indicates better energy efficiency per unit of data processed.





## Statistical Analysis


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

[7] S. McGuire, E. Schultz, B. Ayoola, and P. Ralph, “Sustainability is stratified: Toward a better theory of sustainable software engineering,” in *Proc. 2023 IEEE/ACM 45th Int. Conf. Software Engineering (ICSE)*, May 2023, pp. 1996–2008, doi: 10.1109/ICSE48619.2023.00169.

[8] J.-L. Gailly and Free Software Foundation, *GNU Gzip Manual*, version 1.14, Feb. 2025. [Online]. Available: https://www.gnu.org/software/gzip/manual/gzip.html.

[9] J.-L. Gailly and M. Adler, *zlib.h -- interface of the 'zlib' general purpose compression library*, version 1.3.2, Feb. 2026. [Online]. Available: https://zlib.net.

[10] Software Improvement Group, “Green IT: How green software development can reduce your carbon footprint,” Software Improvement Group Blog, Nov. 11, 2024. [Online]. Available: https://www.softwareimprovementgroup.com/blog/green-software-development/.

[11] Wikipedia Contributors, “Power–delay product,” Wikipedia, Jun. 27, 2024.

[12] A. C. Fowler, “Energy cost of data compression in sensor networks,” in Proceedings of the IEEE Conference on Information Sciences and Systems (CISS), 2003. [Online]. Available: https://ws.binghamton.edu/fowler/Fowler%20Personal%20Page/Publications_files/Fowler%20CISS%202003%20Sensor%20Net.pdf

[13] “Data compression ratio,” Wikipedia. [Online]. Available: https://en.wikipedia.org/wiki/Data_compression_ratio 