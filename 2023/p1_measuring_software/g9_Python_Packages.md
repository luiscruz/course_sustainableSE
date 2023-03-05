---
author: Ivor Zagorac, Philippe de Bekker, Merel Steenbergen, Sebastien van Tiggele
title: "Energy consumption analysis of your favourite python data analysis packages"
date: 05/03/2023
summary: "A comparison of the energy efficieny of often-used python packages"
bibtex: |-
  @misc{p1_python_packages,
    title = {Energy consumption analysis of your favourite python data analysis packages},
    author = {Ivor Zagorac, Philippe de Bekker, Merel Steenbergen, Sebastien van Tiggele},
    year = {2023},
    howpublished={link-tbd},
    note = {Blog post.}
  }
---


## Introduction

Python is often used for data analysis, as it is easy to use and has lots of accessible packages. Of course, some of these packages have distinct features which makes chosing which one to use relatively easy. However, often the same result could be accomplished with multiple packages and the choice is made based on personal preference, common practices online or previous experience of the developer. Usually, environmental sustainability and energy consumption are not taken into account when making this choice. 

In this report, we aim to compare the energy consumption of four popular data science libraries for Python: `pandas`, `polars`, `vaex`, and `dask`.

<img src="https://i.imgur.com/tgeU7TK.png" width="100px" style="margin: 10px">
<img src="https://i.imgur.com/J4AGQ4o.png" width="100px" style="margin: 10px">
<img src="https://i.imgur.com/LWtCLlR.png" width="100px" style="margin: 10px">
<img src="https://i.imgur.com/LUwLYBg.png" width="100px" style="margin: 10px">

[**TODO**: Any image (also in results section), download the source image and upload it in the /img folder on the GitHub repository (and change the link from imgur to the location path)]

To ensure a fair comparison, we will focus on overlapping features of these packages, specifically the following operations:
* Group by
* Merge (join)
* Read and write

We will test these features on a large dataset, as these are common operations in data analysis and can be computationally intensive tasks. [The motivation behind this comparison is to identify the most energy-efficient library to use for data analysis, with the ultimate goal of reducing carbon emissions.]

We will begin by introducing each library and discussing their strengths and weaknesses [**TODO**]. Then, we will describe the methodology used to compare the energy consumption of each library. Finally, we will present the results of our comparison and draw conclusions about the energy efficiency of each library. Overall, this report aims to provide valuable insights into the energy consumption of popular data science libraries and how they can be used in a more sustainable way.

The most widely used library is Pandas, and earlier research [1] has been comparing this package against alternatives that might perform better on operations used on very large datasets. The focus here has been on speed and memory usage, but not on energy consumption. Using the
* introduction is nogal oncoherent maar denk dat wel duidelijk is wat het idee is
* elaborate on the experiments themselves and the packages themselves


## Methodology
To run and analyse the three data operations using the four packages, we follow a systematic approach:

1) **Zen mode 🧘🏾‍♀️**- Disabling all background tasks and redundant applications, bluetooth, WiFi, and more, to get as stable measurements as possible. This also means having a consistent room temperature throughout the measuring, in our case 21 degrees Celcius.
2) **Start PowerGadget log ▶️** - Creates a `.csv` log of power consumption.
3) **Run experiments** (automated 🤖)
    - 🔥 Warming up machine - running 5 minutes of CPU intensive tasks for adequate hardware temperature.
    - 🔀 Shuffled order - this increases measurement precision over sample set (could be hidden errors).
    - 🔁 Repeated 5 times - this forms a distribion of samples.
    - ⏯️ Wait 30 seconds in between - reduces effect of tail energy.
    - ⌛ Measure start and stop time of each inner execution in `.csv`
4) **Stop PowerGadget log ⏹️** - Saves the `.csv` log of power consumption.
5) **Calculate energy consumption 🧮** - by matching the timestamps of the `.csv` files, we can calculate the energy consumption for each iteration per package of an experiment.

The documentation and code used to run, parse and visualize the experiments can be found [here](https://github.com/philippedeb/CS4415-SSE). The setup on which we run the experiments is a (plugged in) HP ZBook Studio G5 with the following specs:
* Processor: Intel Core i7-8750H, Intel64, 2.2 GHz, 6 cores
* RAM: 16GB, DDR4
* Display: 15,6" size, 1920x1080 resolution, 100% brightness, IPS
* GPU: NVIDIA Quadro P1000, 4GB, Driver version 31.0.15.1669
 

## Results

[**TODO**: Elaborate on each result]

### Groupby experiment
![](https://i.imgur.com/QFOeta9.png)
![](https://i.imgur.com/JFhZZkX.png)

### Merge experiment
![](https://i.imgur.com/H4dFqqK.png)
![](https://i.imgur.com/OoYN6up.png)


### Read and write experiment
![](https://i.imgur.com/bq1aOpr.png)
![](https://i.imgur.com/HbJsRTB.png)


## discussion
* stukje vertellen over hoe veel verschil deze waardes nou echt uitmaken (create **Practical Significance** section)
* pandas is opzich ook wel makkelijk te gebruiken, voor kleinere datasets boeit het dan misschien niet


## Limitations (<- just mention this in the discussion)
* test setup could have been ran more times if there were less time constraints
* More operations could have been measured if there were less time constraints
* Checking distribution of sample set according to p (or t?)-test (see lecture slides)
* The experiments were only run on 1 computer, but using more different setups could have given us more data to work with. However, among the four of us only 1 had a computer running intel on windows.


## conclusion





https://towardsdatascience.com/8-alternatives-to-pandas-for-processing-large-datasets-928fc927b08c
1. https://h2oai.github.io/db-benchmark/
2. https://ponder.io/pandas-is-now-as-popular-as-python-was-in-2016/
