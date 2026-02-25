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

This section describes the setup used for the experiments. We took inspiration from the rigorous guide provided by Cruz, who argued that energy measurements are determined by a multitude of factors, and thus require careful bias control and automation [11].

### Hardware and Software Environment

All experiments are executed on the same machine and OS. Below is a table summarizing the specifications of the machine used.

| Category | Specification |
|---|---|
| Machine / Laptop model | `<e.g., Lenovo ThinkPad ... / custom desktop>` |
| CPU | `<e.g., Intel Core i7-12700H / AMD Ryzen ...>` |
| CPU cores / threads | `<e.g., 14 cores (6P+8E) / 20 threads>` |
| CPU base / boost frequency | `<if known>` |
| RAM | `<e.g., 16 GB DDR4>` |
| Storage | `<e.g., 512 GB NVMe SSD>` |
| Operating system | `<e.g., Linux Mint 22.x (Ubuntu 24.04 base)>` |
| Kernel version | `<e.g., Linux 6.x>` |
| Power mode | `<e.g., plugged in, performance mode / balanced>` |
| EnergiBridge version | `<version>` |
| GNU gzip version | `<e.g., gzip 1.12 / 1.13 / 1.14>` |
| C++ compiler | `<e.g., g++ 13.x>` |
| Java runtime / compiler | `<e.g., OpenJDK 17.0.x (java/javac)>` |
| Go version | `<e.g., go1.22.x>` |
| Python version | `<e.g., Python 3.12.x>` |

### Experimental Design and Conditions

We evaluate four language implementations (`cpp`, `java`, `go`, `python`) under two dataset types and two operation modes, namely:

* **Language:** C++, Java, Go, Python
* **Dataset type:** compressible, incompressible
* **Operation:** compress, decompress

This results in **4 experiment groups** (dataset × operation):

1. compressible + compress
2. compressible + decompress
3. incompressible + compress
4. incompressible + decompress


### Input Preparation and Decompression Fairness

Input files are generated automatically at the start of each experiment using the existing deterministic generator (`data/generate_input.py`):

* one **compressible** dataset (`.jsonl`)
* one **incompressible** dataset (`.bin`)

with a fixed size of 256MB.

For decompression experiments, the script generates a **single reference gzip file per dataset** using **GNU gzip** at compression level 6 with header normalization:

```bash
gzip -6 -n -c INPUT > ref.gz
```

The `-n` option removes filename and timestamp metadata from the gzip header, thus making reproducibility better. We do this to ensure that all languages decompress the **same exact `.gz` bytes**.

### Measurement Tooling and Execution Procedure

Energy measurements are collected with **EnergiBridge**. For each run, the experiment script invokes EnergiBridge as a wrapper around the language-specific command:

```bash
energibridge -o <run.csv> -i <interval_us> --summary -- <language_command>
```

The script records:

* EnergiBridge summary output in a per-run CSV file (`raw/run_k.csv`)
* stdout/stderr in a log file (`raw/run_k.log`)
* wall-clock runtime (`wall_time_s`) measured by the Python orchestrator

We use an EnergiBridge sampling interval of 100 µs to capture finer details of energy consumption. 
After each run, the script parses the EnergiBridge CSV and computes per-column deltas between the first and last recorded values for numeric counters. This helps in eliminating noise from transient power fluctuations and system stabilization effects.

### Bias Mitigation and Experimental Protocol

A key motivation for our protocol is Cruz’s observation that software energy measurements can be strongly affected by thermal state, background processes, and temporal drift [11]. To reduce these sources of bias, the runner implements the following controls.

#### Warm-up runs

Before recording measurements, the script performs **3 warm-up runs** for each condition and language. These warm-up runs are discarded their purpose is to reduce **cold-start effects** by allowing the system to stabilize thermally.

#### Repeated measurements

We measure each condition 30 times, as recommended by Cruz [11], in order to achieve statistically significant results.

#### Rest between runs

We use rest periods of 60 seconds after each measured run, again, as recommended by Cruz [11].

#### Shuffled execution order

Within each dataset-operation group, runs are executed in blocks, with each language being run exactly once per block. 
The language order is shuffled using a deterministic random seed. 
As Cruz [11] notes, shuffling the order of execution reduces the risk of confounding effects, 
thus making our comparisons more reliable.

### Manual Controls and Remaining Sources of Bias

Before running long experiments, we aim to keep the environment stable by:

* closing unnecessary applications and browser tabs,
* disabling notifications and updates,
* keeping hardware peripherals constant,
* maintaining fixed screen brightness/resolution and power settings,
* avoiding unrelated network activity when possible.

These steps correspond to Cruz’s “Zen mode” and “freeze your settings” recommendations [11]. Even with automation, residual noise from background tasks and environmental changes may remain, which is considered in the later analysis and limitations discussion.


## Implementation Details

We standardize the same algorithm design across all languages. Each implementation provides a small command-line interface of the form `mode input_file output_file`, with the `mode` being either compression or decompression. The `gzip` compression level is fixed at 6 for all languages, which matches the default setting [8]. All files are processed in binary mode, and compression is done using each language's standard library in a streaming fashion, without system calls or external tools, so that the measurements reflect purely the behavior of the language. If applicable, we also use a buffer size of 32 KB to keep memory usage and I/O behavior comparable.


### Java

The Java implementation uses the standard `java.util.zip` package [10], with `GZIPOutputStream` for compression and `GZIPInputStream` for decompression. Files are processed in a streaming manner using buffered I/O and fixed 32 KB chunks, avoiding full-file loads into memory to keep memory usage stable and comparable across input sizes. To enforce **gzip level 6**, we use a small custom subclass of `GZIPOutputStream` that sets the internal `Deflater` level after construction.

### C++

The C++ implementation directly uses the `zlib` library [9] for compression and decompression, both of which are performed with matching parameters through `deflateInit2` and `inflateInit2`, respectively. Data is processed incrementally, in fixed-size chunks, by feeding the input buffers into the stream and writing the output until the stream ends. We chose to use chunked streaming so that we could avoid loading the entire file into memory, and so manage to keep the memory usage stable across file sizes. This also happens to be a typical design for C++ applications. 

### Python

### Go


## Metrics

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

[10] M. Grand, J. B. Knudsen, and P. Ferguson, *Java Fundamental Classes Reference*, 1st ed. Sebastopol, CA, USA: O’Reilly & Associates, Inc., 1997.

[11] L. Cruz, “Green Software Engineering Done Right: a Scientific Guide to Set Up Energy Efficiency Experiments,” blog post, Oct. 10, 2021. [Online]. Available: http://luiscruz.github.io/2021/10/10/scientific-guide.html. doi: 10.6084/m9.figshare.22067846.v1.