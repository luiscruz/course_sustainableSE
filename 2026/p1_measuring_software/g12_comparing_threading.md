---
author: Maksym Ziemlewski, Frederik van der Els, Piotr Kranendonk
group_number: 12
title: "Comparing the Energy Consumption of Single-Threaded and Multi-Threaded Programs"
image: "img/gX_template/project_cover.png"
date: 27/02/2022
summary: |-
  Many tasks lend themselves for parallel programming, which can speed up the execution time of the program. Common ways to achieve this is by using multiple threads, and splitting the task into smaller tasks that can be executed in parallel on the different threads.
  
  While this indeed can speed up the execution time, it is very much possible that the overhead of multiple threads increases the energy consumption significantly. That is, despite the program being more efficient (taking less time), it could become more energy consuming.
  
  Our project would compare single-threaded and multi-threaded implementations of the same app. We will investigate how the number of threads used affects energy consumption, and what conclusions the developer should draw based on that.

identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Introduction
Most programs are initially written in a _single-threaded_ fashion. A single-threaded program has only one thread of execution. This means that the program performs one execution at a time, in a sequential matter. This makes developing, debugging and maintaining the program simple, as the program as a whole is easier to reason about. However, many modern operating systems have multi-core processors, which have the capability of executing many tasks in parallel. With single-threaded programs, most of these cores are left unused. This can become especially noticeable if _blocking_ requests are involved, where the execution of the entire program is halted until a task finishes.

A common solution to this program is to make the program _multi-threaded_. Multi-threaded programs run tasks concurrently, or in parallel. Each thread executes its own execution path of the program, allowing the program to execute multiple tasks at a time. Now, a blocking request could be executed on a different thread, allowing to program to continue execution without having to wait for the request to complete.

With many cores being available on modern operating systems, this paradigm becomes increasingly common. The increased efficiency of the program's execution seems like an obvious reason to take advantage of it. However, when making this change, energy consumption is often left out of the equation. In this report, we will investigate how single-threaded and multi-threaded programs compare in energy consumption, and what considerations a developer should take in mind when choosing between the two paradigms.

More specifically, we will investigate how the memory usage of the same program differs given a single-threaded and multi-threaded implementation. For this, we will take into account the overhead of creating a thread, the number of threads used and the effect of reusing threads.

# Methodology
We will use Java as testing language. Java has APIs available that allows us to easily configure the number of threads and whether threads are reused. Furthermore, in Java threads are OS threads, which is what we want to measure. Languages like Go have coroutines that are lightweight versions of threads, which are managed by the Go runtime and not the OS. Because these threads barely have any overhead, they are less interesting to study.

We will measure the energy consumption using EnergiBridge[^1]<sup>,</sup>[^2]. EnergiBridge is a cross-platform energy measurement utility which internally uses LibreHardwareMonitor[^3] to measure the energy consumption of a program. EnergiBridge is designed to support multiple operating systems and processor brands, which makes it not only easy to use, but also easy to compare different hardware setups. EnergiBridge can be used from the command line. For example, to measure the energy usage of visiting `google.com` using Google Chrome for ten seconds, one can use the following command:

```shell
energibridge -m 10 -- google-chrome google.com
```

For a more detailed usage guide, see the GitHub page.

To aid the reproducibility of our results, we will abstract away the usage of EnergiBridge in PowerShell scripts. Because EnergiBridge requires elevated permissions, the scripts will automatically trigger a User Account Control (UAC) prompt that asks for the required permissions. Because running a PowerShell script with elevated permissions carries some risk, the reader is invited to audit the scripts first.

Because multi-threaded programs draw more power simultaneously, one should measure the _total_ energy consumption across all processors. Luckily, this is what LibreHardwareMonitor does; it measures the energy/power sensors at the package level. Here package level refers to the entire physical CPU chip. Thus, because the energy measurements are tied to hardware sensors, they automatically include all active threads running on all cores.

However, because all cores are always measured, there will be a significant amount of background noise that will be captured in the measurements. Therefore, to make our measurements as accurate as possible, one must eliminate as many sources of background memory consumption as possible, and only measure the memory consumption as a consequence of executing the program. For this, we will first perform a null-measurement, which will measure the energy consumption of the system when nothing is being done. On Windows, the `timeout` command sleeps (in contrast to busy waiting) for an amount of time. The `null_measurement.ps1` script measuresures sleeping for ten seconds for a total of thirty iterations.

```shell
./null_measurement.ps1
```

Moreover, one should ensure that the measurements are consistent and reproducible. For this, we will adhere to the following criteria and configuration settings when performing the measurements:

- all applications should be closed;
- notifications should be turned off;
- only the required hardware should be connected (no USB drives, external disks, external displays, etc.);
- unnecessary services running in the background should be stopped (e.g., web server, file sharing, etc.);
- network connections should be switched off;
- brightness is fixed to the lowest possible;
- volume is turned off.

In our case, the device that was used to perform the measurements has the following specifications:

- the operating system is Windows 11;
- the CPU is TODO;
- the installed physical memory (RAM) is TODO;
- the resolution is 1920 x 1080, with a refresh rate of 60 hertz;

To reduce variance, each specific measurement will be performed thirty times. Additionally, between each measurement, there is a configurable pause that allows the processor to cool down.

In the next section we will discuss in more detail what particular program we used for measuring energy consumption.

# Implementation
To measure the differences in energy consumption, we will use the X/Y/Z as test program. This program lends itself well for this experiment because it is not easily optimised by the compiler/CPU, ...

# Hardware setup
To be able to ensure that the measurements are consistent and reproducible some precautions had to be taken. Most importantly all the collected measurements were made on the same device, as using only one device makes it easier to have a consistent setup. 
In our case, the device that was used to perform the measurements has the following specifications:

- the operating system is Windows 11;
- the CPU is an Intel Core i7-12700H;
- the installed physical memory (RAM) is 16 GB;
- the resolution is 1920 x 1080, with a refresh rate of 60 hertz;

Additionally the following criteria and configuration settings were used when performing the measurements:

- the device is disconnected from the internet;
- bluetooth is turned off;
- no external devices are connected (eg., USB-drives, computer mouse, external dispalys, etc.);
- the device is connected to a power supply;
- the brightness of the device is set to the maximum and is not dynamic;
- screen timeouts are turned off (the device should not enter sleep mode while collecting measurements);
- all applications are closed such that they do not keep on running in the background;
- unnecessary services running in the background are stopped (e.g., web server, file sharing, etc.);
- only a powershell is opened that is used to run the scripts for the measurements;

Besides the setting of the device itself the environment can also have an impact on the performance. Therefore some addition thing had to be ensured like:

- The temperature of the room is consistent somewhere around 20 degrees Celsius;
- Make sure the room is big, such that the device will not raise the room temperature;
- The laptop is placed in the shadows, such that the sun will not heat it up;
- There are no external heating or cooling devices close enough to the device to have an influence;

After ensuring that all the above mentioned conditions were met, the scripts to make the measurements were ready to be run.

# Results
After running all the tests the following plots can be made:

The first plot shows the average power consumption for the null measurements. The mean power over 28 runs (2 were left out as outliers) shows that the device uses around 2.2 W when in an idle state.

![null](img/g12_comparing_threading/null.png "Null Measurements")

This second plot shows the programs total energie consumption in Joules, for each experiment with different amounts of threads. For each experiment around 0 to 3 measurements were labeled as outliers and were left out from this plot. As already mentioned using more threads for computations also speeds up the process. To still be able to compare the experiments, we want to isolate the energy consumption of the program itself. To do this we subtract the found background power consuption (2.2 W) multiplied by the time it took each measurement to run:
$J_{program} = J_{total} - P_{null} * \Delta t$

![energy](img/g12_comparing_threading/energy_plot.png "Total energy consumption")

Interestingly using more threads clearly reduces the total energy consumption. This means that parallelizing a program will not only speed up the run time, but can also reduce the total energy it will consume. We however have to keep in mind that this does not mean that the program draws less power. On the contrary, the third plot shows that using more threads increases the power usage of the program:

![power](img/g12_comparing_threading/power_plot.png "Average power consumption")

This indicates that when continuously running a multi-threaded program as opposed a single threaded program, will use a lot more energy. Only when running the program a (small) finite amount of times it will be beneficial for the energy consumption to use multiple threads compared to a single one.


# Statistical analysis of the results
We will use X/Y/Z to draw conclusions, ...

# Conclusion and future work
A.

# References

[^1]: Sallou, J., Cruz, L., & Durieux, T. (2023). _EnergiBridge: Empowering software sustainability through cross-platform energy measurement_. arXiv. https://doi.org/10.48550/arXiv.2312.13897

[^2]: Durieux, T. (n.d.). _EnergiBridge_. GitHub. https://github.com/tdurieux/EnergiBridge

[^3]: LibreHardwareMonitor. (n.d.). _LibreHardwareMonitor_. GitHub. https://github.com/LibreHardwareMonitor/LibreHardwareMonitor
