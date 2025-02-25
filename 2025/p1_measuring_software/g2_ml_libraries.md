---
author: Reinier Schep, Maosheng Jiang, Razvan Loghin, Alex Zheng
title: "Tensorflow, Torch and JAX energy consumption comparison for convolutional neural networks on MNIST"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
    Tensorflow, Torch and JAX energy 
    consumption comparison for convolutional neural networks on MNIST dataset.
---

## Introduction
As machine learning (ML) models become complexer and operate on a larger scale, 
their computational demands have increased, leading to increased 
energy consumption. Training large-scale deep learning models 
can require as much energy as powering multiple households for
weeks, with some studies estimating that training a single deep
learning model can emit as much carbon as five cars over their 
lifetime [Strubell et al., 2019](https://aclanthology.org/P19-1355/). Given the rapid expansion of AI applications across industries, optimizing the energy efficiency of ML frameworks is critical for reducing both operational costs and environmental impact.

This paper investigates the energy efficiency of three widely 
used ML frameworks: Keras, PyTorch, and JAX. Each of these 
frameworks offers distinct design philosophies and computational 
optimizations which may significantly impact their 
energy consumption. While extensive research has been done to compare these frameworks in terms 
of training speed and model accuracy, fewer studies have focused on their power
consumption and energy efficiency. Given the scale at which these ML libraries can be deployed in the real world, 
small differences could quickly lead to significant practical differences in energy consumption.

By systematically measuring energy usage for the same exact workload across 
different frameworks for multiple iterations, 
this study aims to provide insights into how ML engineers can make more 
sustainable choices when selecting a ML framework. The results will be valuable 
for researchers, developers, and organizations seeking to balance model 
performance with environmental responsibility and associated costs.

For this experiment we aim to compare the energy consumption of Keras (using TensorFlow), PyTorch and JAX when training a Convolutional Neural Network (CNN).
We have implemented the same exact CNN architecture for each framework and then we measure energy usage of each.


## Methodology
### CNN architecture used

The CNN architecture used is shown in the figure below *insert figure*

- **Convolutional Layer (64 filters, 3x3, ReLU, same padding)** – Extracts local features while maintaining spatial dimensions.
- **Pooling Layer (2x2, stride 2)** – Reduces spatial size to retain essential features efficiently.
- **Convolutional Layer (128 filters, 5x5, ReLU, same padding)** – Captures more complex patterns with a larger receptive field.
- **Pooling Layer (2x2, stride 2)** – Further reduces spatial dimensions to improve computational efficiency.
- **Flatten Layer** – Converts multi-dimensional feature maps into a 1D vector for classification.
- **Fully Connected Layer (10 units, softmax activation)** – Produces class probabilities for final classification.



### Hardware and software setup

The experiment was conducted on a computer with the following hardware/software:
- OS: Microsoft Windows 11 Pro (10.0.26100 Build 26100)
- CPU: AMD Ryzen 5 3600 6 cores@3593Mhz, 12 logical cores
- RAM: 16GB
- GPU: NVIDIA RTX 2060 Super
- Python 3.11.8
- Poetry 1.8.3 (dependency management)
- Tensorflow (keras) 2.18.0
- Torch 2.6.0
- Jax  0.5.0
- Other dependencies can be found in the Github repository used to carry out the [experiment](https://github.com/flazedd/cs4575-project1) 
- [EnergiBridge 0.0.7](https://github.com/tdurieux/EnergiBridge/releases/tag/v0.0.7) is used and the necessary files are already included in the repository

Other important settings which have been changed on the machine under which the experiment runs (we call this Zen mode):
- All applications are closed in task manager, except an Administrator Powershell which executes the experiment
- Notifications are turned off
- A single monitor is connected
- Internet connection is disabled

### Energy measurement
Energy measurement was done by using the tool [EnergiBridge](https://github.com/tdurieux/EnergiBridge), which is able to measure the CPU energy used in joules at a specific timestamp. Using the timestamps and the CPU energy, we can calculate the average power used during an experiment, we use the following formula: $P_{avg} = \frac{E}{\Delta t}$, where $E$ is the CPU energy (in Joules) used in the timespan $\Delta t$, which is the difference between the begin and end time of the experiment in seconds.


### Dataset
The [MNIST dataset](https://www.kaggle.com/datasets/hojjatk/mnist-dataset) was used for training and evaluating the CNN described earlier. It has to be mentioned that the datatype transformation pipeline differs per framework, in our implementations the execution flow is as follows:

- Keras: PyTorch tensor -> NumPy array
- JAX: PyTorch tensor -> NumPy array -> JAX array
- PyTorch: PyTorch tensor

We assume that the energy usage in the actual training of the CNN is far more significant than the energy usage in the datatype transformation, and thus consider this a neglectable difference for the energy measurement results. However, for larger datasets a similar datatype transformation pipeline has to be used to ensure the reliability of the experiments.


### Evaluation
The task of each framework consists of training the CNN for 3 epochs and then evaluating the accuracy.
Before starting the energy measurement of this task, the CPU is warmed up for 5 minutes by doing calculations to prevent cold starts which affect energy consumption.
Then, a sequence of timestamped power measurements are taken for each framework during their execution, in which they complete 3 epochs of training and evaluation of their accuracy.
After the execution of a framework, an idle time of 1 minute is introduced instead of 
directly measuring the next framework to prevent tail energy usage from influencing the energy usage of the next framework to be evaluated. 
This will be done for a total of 35 iterations, each iteration the order of frameworks evaluated 
is shuffled randomly to mitigate any potential order bias.
This results in 35 .csv files generated by EnergiBridge which contain
the energy measurements for each framework which will be used for further analysis.


## Results
### Time
The violin plot below shows for each framework the distribution of the obtained execution times in seconds. We see that Tensorflow (Keras) has the fastest execution time on average followed by PyTorch and JAX since the distributions do not overlap. We can also observe that Keras and JAX have similar widths of their distribution, while PyTorch has a wider distribution indicating more variability in its runtimes.

![Violin plot of time used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/time_plot.png)

### Energy
The violin plot below shows the distribution of the energy consumed by the different frameworks. We observe that Keras has the lowest energy consumption and the smallest width in distribution compared to PyTorch and and JAX. This indicates that Keras is the most efficient framework and has the least variability in the energy consumed.

![Violin plot of energy used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/energy_plot.png)

### Power 
The violin plot below shows the distribution of the average power used by each framework over the span of its execution time. It should come as no surprise that Keras performs best here as well since we previously saw it performed the fastest and using the least energy. Here, it also has the narrowest distribution followed by Pytorch and then JAX. 

![Violin plot of power used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/power_plot.png)


To summarize, Tensorflow (Keras) has the overall lowest execution time and least amount of energy consumed. Then Pytorch follows on both metrics and JAX comes in last place on both metrics.

<!-- Show some violin box plots for each framework here...
Some p-values etc.
Is the data observed normal? shapiro wilk test
Effect size analysis -->

## Analysis
### Statistical significance
This section answers the question if the differences in performance are statistically significant. First we need to determine if the distributions follow a normal distribution before we can compare them. 
- For the time data a p-value far less than 0.05 is observed for each framework, indicating that execution times are not normally distributed.
- For the energy data a p-value far less than 0.05 is observed for each framework, indicating that energy consumption is not normally distributed.
- For the power data a p-value significantly above 0.05 (0.35, 0.88 and ? respectively for Keras, PyTorch and JAX) is observed for each framework. This  indicates that we cannot statistically reject the hypothesis that power data is normally distributed. 

Considering that not all data can be assumed to be normally distributed, we resort to the non-parametrical Mann-Whitney U test for which normality of data is not a requirement. 

The table below contains the p-value for the Mann-Whitney U which compares the distribution of 2 frameworks across some metric (time, energy and power). 


| Metric  | Keras vs Torch | Keras vs JAX | Torch vs JAX |
|---------|--------------|--------------|--------------|
| Time    | 3.11e-13    | 3.11e-13    | 1.42e-13    |
| Energy  | 3.11e-13    | 3.11e-13    | 1.54e-13    |
| Power   | 8.09e-21    | 5.38e-12    | 1.68e-04    |

As can be observed, each p-value is far less than 0.05 which tells us that the distributions of the frameworks across all metrics is indeed statistically signficant.



### Practical significance
Machine learning applications benefit from a vast amount of data processing and many training iterations, this process is notorious for consuming large amounts of energy. For example, it is estimated that it took about 10 gigawatt-hour (GWh) of energy consumption to train ChatGPT-3, which is equivalent to the yearly electricity consumption of a 1000 U.S. households according to the [University of Washington](https://www.washington.edu/news/2023/07/27/how-much-energy-does-chatgpt-use/). ChatGPT-3 received hundreds of millions of queries per day which used up around 1 GWh which equals the daily energy consumption of about 33,000 US households. Therefore, any slight difference in energy consumption of ML frameworks can already have a huge impact. 

The tables below show the percentage increase for the different metrics time, energy and power. This highlights the significant relative differences between frameworks. For example, in table 1 it can be seen that PyTorch needs about 20% more time to complete the same task and consumes 22.34% more energy. If we apply  this to the ChatGPT-3 example it would mean that you could either choose to use PyTorch or you could choose to use Keras and give 223 US households a year of free electricity. This highlights how big of a difference the choice in ML framework can make.


### Table 1:  Keras vs. Torch

| Metric       | Keras (Median) | Torch (Median) | Percentage Increase/Decrease |
|--------------|----------------|----------------|------------------------------|
| **Time**     | 122.4320 s      | 146.8430 s      | **+20.00%**                   |
| **Energy**   | 6835.5719 J     | 8372.7679 J     | **+22.34%**                   |
| **Power**    | 55.6824 W       | 57.0860 W       | **+2.54%**                    |

---

### Table 2: Torch vs. JAX

| Metric       | Torch (Median) | JAX (Median)  | Percentage Increase/Decrease |
|--------------|----------------|----------------|------------------------------|
| **Time**     | 146.8430 s      | 169.0740 s      | **+15.14%**                   |
| **Energy**   | 8372.7679 J     | 9733.5067 J     | **+16.26%**                   |
| **Power**    | 57.0860 W       | 57.6347 W       | **+0.96%**                    |

---

### Table 3: Keras vs. JAX

| Metric       | Keras (Median) | JAX (Median)  | Percentage Increase/Decrease |
|--------------|----------------|----------------|------------------------------|
| **Time**     | 122.4320 s      | 169.0740 s      | **+38.06%**                   |
| **Energy**   | 6835.5719 J     | 9733.5067 J     | **+42.37%**                   |
| **Power**    | 55.6824 W       | 57.6347 W       | **+3.51%**                    |


## Discussion
It should come as no surprise that Tensorflow (keras) is the most efficient framework, since its design philosophy
is to prioritize performance and scalability for large-scale models. PyTorch is more geared towards small-scale models
and prioritizes simplicity and adaptability [^1]. The JAX framework coming in last might be because experiments were executed
on the CPU, and a key feature of JAX is that it uses Accelerated Linear Algebra (XLA) and just-in-time (JIT) compilation
to achieve better performance on GPUs and TPUs [^2]. However, the JAX framework might not have come to full fruition in
this experiment since only CPU performance is considered here.

[^1]: https://www.simplilearn.com/keras-vs-tensorflow-vs-pytorch-article
[^2]: https://github.com/jax-ml/jax


## Limitations & future work
We set a seed for each ML framework so that it performs the same 
computations across iterations which reduces variability. 
A limitation is that we couldn't get the frameworks to all start at the same point 
so that they would produce the same exact weights and accuracy and so on.
Still, this should not affect the energy measurements since all frameworks 
have gone through the same amount of epochs of training. 
For future work, different versions of the same framework could be 
used to examine energy efficiency differences between versions. This is relevant
because when you select a ML framework to work with, you also have to select some
version to use. For a future experiment, it would be interesting to see if the same results can be achieved
if all frameworks are forced to run on a GPU instead of a CPU since this would put the GPU optimizations of the frameworks
to the test.



## Conclusion
In this report, we conducted an experiment to assess the energy efficiency of the popular ML 
frameworks Tensorflow (keras), PyTorch and JAX. We found that Tensorflow (keras) had the fastest execution time
and consumed the least amount of energy when tasked with training a convolutional neural network 
for 3 epochs and evaluating its accuracy. The next fastest and most energy efficient framework was PyTorch, but it already
took 20% more time and consumed 22.34% more energy compared to Tensorflow (keras). The JAX framework performed worst, 
it took 15.14% more time and consumed 16.26% more energy compared to the PyTorch framework (which already came in second).
Given the large scale at which ML frameworks are usually deployed, these relative differences in energy consumption can 
lead to monumental differences in practice.


