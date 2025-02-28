---
author: Reinier Schep, Maosheng Jiang, Razvan Loghin and Alex Zheng
title: "TensorFlow, Torch and JAX energy consumption comparison for convolutional neural networks on MNIST"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
  TensorFlow, Torch and JAX energy 
  consumption comparison for convolutional neural networks on MNIST dataset.
---

## Introduction

As machine learning (ML) models become more complex and operate on a larger scale,
their computational demands have increased, leading to increased
energy consumption. Training large-scale deep learning models
can require as much energy as powering multiple households for
weeks, with some studies estimating that training a single deep
learning model can emit as much carbon as five cars over their
lifetime [Strubell et al., 2019](https://aclanthology.org/P19-1355/). Given the rapid expansion of AI applications across industries, optimizing the energy efficiency of ML frameworks is critical for reducing both operational costs and environmental impact.

This report investigates the energy efficiency of three widely
used ML frameworks: Keras, PyTorch, and JAX. Each of these
frameworks offers distinct design philosophies and computational
optimizations which may significantly impact their
energy consumption. While extensive research has been done to compare these frameworks in terms
of training speed and model accuracy, fewer studies have focused on their power
consumption and energy efficiency. Moreover, research has also highlighted inconsistencies in ML implementations
across libraries, showing that even the same conceptually identical ML method can yield different results depending on the library used [Liem & Panichella, 2020](https://arxiv.org/abs/2012.08387).
While such discrepancies affect correctness and reproducibility, another critical but often overlooked aspect is the sustainability of these ML frameworks.
Given the scale at which these ML libraries can be deployed in the real world,
small differences could quickly lead to significant practical differences in energy consumption.

By systematically measuring energy usage for the exact same workload across
different frameworks for multiple iterations,
this study aims to provide insights into how ML engineers can make more
sustainable choices when selecting a ML framework. The results will be valuable
for researchers, developers, and organizations seeking to balance model
performance with environmental responsibility and associated costs.

For this experiment, we aim to compare the energy consumption of Keras (using TensorFlow), PyTorch and JAX when training a Convolutional Neural Network (CNN) for the popular and widely used MNIST dataset of handwritten digits.
We have implemented the exact same CNN architecture for each framework, and then measured the energy usage of each.

## Methodology

### CNN architecture used

The CNN architecture used is shown in the figure below
![Convolutional Neural Network](../img/p1_measuring_software/g2_ml_libraries/net.png)

- **Convolutional Layer (64 filters, 3x3, ReLU, same padding)** – Extracts local features while maintaining spatial dimensions.
- **Pooling Layer (2x2, stride 2)** – Reduces spatial size to retain essential features efficiently.
- **Convolutional Layer (128 filters, 5x5, ReLU, same padding)** – Captures more complex patterns with a larger receptive field.
- **Pooling Layer (2x2, stride 2)** – Further reduces spatial dimensions to improve computational efficiency.
- **Flatten Layer** – Converts multi-dimensional feature maps into a 1D vector for classification.
- **Fully Connected Layer (10 units, softmax activation)** – Produces class probabilities for final classification.

### Hardware and software setup

The experiment was conducted on a computer with the following hardware/software:

- OS: Microsoft Windows 11 Home (Build 22631.4890)
- CPU: AMD Ryzen 5 5600H 6 cores@3300Mhz, 12 logical cores
- RAM: 16GB
- GPU: NVIDIA RTX 3060 Laptop
- Python 3.11.8
- Poetry 1.8.3 (dependency management)
- TensorFlow (keras) 2.18.0
- Torch 2.6.0
- Jax 0.5.0
- Other dependencies can be found in the GitHub repository used to carry out the [experiment](https://github.com/flazedd/cs4575-project1)
- [EnergiBridge 0.0.7](https://github.com/tdurieux/EnergiBridge/releases/tag/v0.0.7) is used and the necessary files are already included in the repository

Other important settings which have been changed on the machine under which the experiment runs (Zen mode):

- All applications are closed in task manager, except an Administrator Powershell which executes the experiment
- Notifications are turned off
- A single monitor is connected
- Internet connection is disabled

### Energy Measurement

Energy measurement was performed using the [EnergiBridge](https://github.com/tdurieux/EnergiBridge) tool, which measures CPU energy consumption in joules at specific timestamps. By recording these timestamps alongside the CPU energy values, we can compute the average power used during an experiment with the formula:

$$P_{avg} = \frac{E}{\Delta t}$$

Here, $E$ denotes the CPU energy consumed (in joules) over the time span $\Delta t$, which is the difference between the experiment's start and end times (in seconds). Additionally, we use the Energy Delay Product (EDP) metric to penalize slower executions by emphasizing runtime. In our case, the EDP is defined as:

$$EDP = E \times \Delta t$$

The unit for EDP is $J\cdot s$.

### Dataset

The [MNIST dataset](https://www.kaggle.com/datasets/hojjatk/mnist-dataset) was used for training and
evaluating the CNN described earlier.

 <!-- It has to be mentioned that the datatype transformation 
 pipeline differs per framework, in our implementations the execution flow is as follows:

- Keras: PyTorch tensor -> NumPy array
- JAX: PyTorch tensor -> NumPy array -> JAX array
- PyTorch: PyTorch tensor -->

<!-- We assume that the energy usage in the actual training of the CNN is far more significant than the energy usage in the datatype transformation, and thus consider this a negligible difference for the energy measurement results. However, for larger datasets a similar datatype transformation pipeline has to be used to ensure the reliability of the experiments. -->

### Evaluation

The task of each framework consists of training the CNN for 3 epochs and then evaluating the accuracy.
Before starting the energy measurement of this task, the CPU is warmed up for 5 minutes by doing calculations to prevent cold starts which affect energy consumption.
Then, a sequence of timestamped power measurements are taken for each framework during their execution, in which they complete 3 epochs of training and evaluation of their accuracy.
After the execution of a framework, an idle time of 1 minute is introduced instead of
directly measuring the next framework to prevent tail energy usage from influencing the energy usage of the next framework to be evaluated.
This will be done for a total of 30 iterations, each iteration the order of frameworks evaluated
is shuffled randomly to mitigate any potential order bias.
This results in 30 .csv files generated by EnergiBridge which contain
the energy measurements for each framework which will be used for further analysis.

### Data Cleaning

It is possible that the EnergiBridge application produces wrong information in the output CSV files.
EnergiBridge could produce a measurement where the accumulative CPU energy measurement is lower than the previous measurement,
which is not possible. Furthermore, if the total energy usage measurement of a single task is negative due to incorrect output of EnergiBridge,
then we discard the measurement. Finally, to remove outliers which may be caused by external factors, we remove data points
that deviate from the mean by 3 standard deviations.

## Results

### Time

The violin plot below shows for each framework the distribution of the obtained execution times in seconds.
We see that TensorFlow (Keras) has the fastest execution time on average followed by PyTorch and JAX since
the distributions do not overlap. We can also observe that Keras and PyTorch have similar distribution shapes,
while JAX has a wider distribution indicating more variability in its runtimes. Also, JAX is roughly 3 times as slow on average than PyTorch.

![Violin plot of time used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/time_plot.png)

### Energy

The violin plot below shows the distribution of the energy consumed by the different frameworks.
We observe that Keras has the lowest energy consumption and the smallest width in distribution, closely followed by PyTorch and then JAX.
This indicates that Keras is the most efficient framework and has the least variability
in the energy consumed which makes it the most consistent of these three.

![Violin plot of energy used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/energy_plot.png)

### Power

The violin plot below shows the distribution of the average power used by each framework over the span of its
execution time. On average, Keras has the highest power consumption, followed by PyTorch and then JAX.
Also, Keras has to largest distribution width, followed by PyTorch and then JAX.

![Violin plot of power used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/power_plot.png)

### Energy-Delay Product

The EDP punishes implementations which have low average power, but which take long to complete by squaring the time taken to complete.
JAX has both of these properties as seen in previous plots. Therfore it should be no surprise that JAX scores
worst on the EDP metric. Keras performs best, followed by PyTorch.

![Violin plot of power used by ML libraries](../img/p1_measuring_software/g2_ml_libraries/edp_plot.png)

To summarize, TensorFlow (Keras) has the overall lowest execution time and least amount of energy consumed.
Then PyTorch follows on both metrics and JAX comes in last place on both metrics.
For average power, JAX performed best, followed by PyTorch and then Keras.
Keras scored best on the EDP metrics, followed by PyTorch and then JAX.

<!-- Show some violin box plots for each framework here...
Some p-values etc.
Is the data observed normal? shapiro wilk test
Effect size analysis -->

## Analysis

### Statistical significance

This section answers the question if the differences in performance are statistically significant.
First, we assess the distribution of the data using the Shapiro-Wilk test, which tests for normality:

### Table 1: Shapiro Wilk test

| Metric     | Keras  | PyTorch | JAX      |
| ---------- | ------ | ------- | -------- |
| **Time**   | 0.7846 | 0.2476  | 1.01e-07 |
| **Energy** | 0.0006 | 0.3966  | 1.65e-08 |
| **Power**  | 0.5148 | 0.0261  | 4.02e-08 |
| **EDP**    | 0.3276 | 0.8744  | 1.72e-08 |

Each cell in [Table 1](#table-1-shapiro-wilk-test) is the p-value of the Shapiro-Wilk test for certain combination of metric and framework.
For the p-values which are significantly below 0.05, we need to reject the hypothesis
that this data follows a normal distribution.
Therefore, the Mann-Whitney U test will be used to compare those distributions.
The only pairs of distributions which both have a p-value above 0.05 are Keras and PyTorch
on the time and EDP metric, for that comparison the independent t-test
will be used since we cannot reject normality of those distributions.

[Table 2](#table-2-distribution-comparison) below presents the p-values for the respective statistical tests comparing
the distributions of each framework across time, energy, power and EDP metrics.

### Table 2: Distribution comparison

| Metric | Keras vs PyTorch  | Keras vs JAX   | PyTorch vs JAX |
| ------ | ----------------- | -------------- | -------------- |
| Time   | 8.58e-82 (t-test) | 2.01e-12 (MWU) | 2.72e-12 (MWU) |
| Energy | 2.09e-13 (MWU)    | 2.72e-12 (MWU) | 3.72e-12 (MWU) |
| Power  | 1.06e-04 (MWU)    | 2.01e-12 (MWU) | 3.72e-12 (MWU) |
| EDP    | 1.03e-63 (t-test) | 2.01e-12 (MWU) | 2.72e-12 (MWU) |

As can be observed, each p-value is significantly below 0.05,
confirming that the observed differences between frameworks in time, energy, power consumption
and EPD are statistically significant.

### Practical significance

Machine learning applications benefit from a vast amount of data processing and many training iterations, this process is notorious for consuming large amounts of energy.
For example, it is estimated that it took about 10 gigawatt-hour (GWh) of energy consumption to train ChatGPT-3,
which is equivalent to the yearly electricity consumption of a 1000 U.S. households according to the
[University of Washington](https://www.washington.edu/news/2023/07/27/how-much-energy-does-chatgpt-use/).
ChatGPT-3 received hundreds of millions of queries per day which used up around 1 GWh which equals the daily energy consumption of
about 33,000 US households. Therefore, any slight difference in energy consumption of ML frameworks can already have a huge impact.

The tables below show the percentage increase for the different metrics time,
energy, power and EPD. This highlights the significant relative differences between
frameworks. For example, in [Table 3](#table-3-keras-vs-torch) it can be seen that PyTorch needs about 61.71% more
time to complete the same task and consumes 62.71% more energy. If we apply this to
a large machine learing task like the ChatGPT-3 example, it would mean that you
could either choose to use PyTorch
or you could choose to use Keras and give about 627 US households free
electricity for a year. This highlights how big of a difference the choice in ML framework
can make.

### Table 3: Keras vs. Torch

| Metric     | Keras (Median)  | Torch (Median)   | Percentage Increase/Decrease |
| ---------- | --------------- | ---------------- | ---------------------------- |
| **Time**   | 121.512 s       | 196.501 s        | **+61.71%**                  |
| **Energy** | 4910.2352 J     | 7989.4385 J      | **+62.71%**                  |
| **Power**  | 40.4442 W       | 40.5893 W        | **+0.36%**                   |
| **EDP**    | 597288.5663 J⋅s | 1569504.3747 J⋅s | **+162.77%**                 |

---

### Table 4: Torch vs. JAX

| Metric     | Torch (Median)   | JAX (Median)     | Percentage Increase/Decrease |
| ---------- | ---------------- | ---------------- | ---------------------------- |
| **Time**   | 196.501 s        | 521.436 s        | **+165.36%**                 |
| **Energy** | 7989.4385 J      | 15461.0326 J     | **+93.52%**                  |
| **Power**  | 40.5893 W        | 29.6987 W        | **-26.83%**                  |
| **EDP**    | 1569504.3747 J⋅s | 8055534.4505 J⋅s | **+413.25%**                 |

---

### Table 5: Keras vs. JAX

| Metric     | Keras (Median)  | JAX (Median)     | Percentage Increase/Decrease |
| ---------- | --------------- | ---------------- | ---------------------------- |
| **Time**   | 121.512 s       | 521.436 s        | **+329.12%**                 |
| **Energy** | 4910.2352 J     | 15461.0326 J     | **+214.87%**                 |
| **Power**  | 40.4442 W       | 29.6987 W        | **-26.57%**                  |
| **EDP**    | 597288.5663 J⋅s | 8055534.4505 J⋅s | **+1248.68%**                |

## Discussion

It should come as no surprise that TensorFlow (Keras) is the most efficient framework, since its design philosophy is to prioritize performance
and scalability for large-scale models according to [Simplilearn]. As shown in [Table 3](#table-3-keras-vs-torch),
Keras completes the task in **121.512 seconds**, whereas PyTorch takes **196.501 seconds**, a **61.71% increase** in execution time.
Similarly, energy consumption for PyTorch is **7989.4385 J**, which is **62.71% higher** than Keras. The power consumption
difference is marginal at **+0.36%**, indicating that the increased energy usage is primarily due to the longer execution time rather than significantly higher power draw.

PyTorch is more geared towards small-scale models and prioritizes simplicity and adaptability according to [Simplilearn].
This aligns with the results in [Table 4](#table-4-torch-vs-jax), where PyTorch outperforms JAX in both time and energy consumption.
PyTorch completes the task in **196.501 seconds**, while JAX takes **521.436 seconds**, marking a **165.36% increase**.
The energy consumption follows a similar pattern, with JAX consuming **15461.0326 J**, a **93.52% increase** compared to PyTorch.

The JAX framework coming in last might be because experiments were executed on the CPU, and a key feature of JAX is that it uses
Accelerated Linear Algebra (XLA) and just-in-time (JIT) compilation to achieve better performance on GPUs and TPUs according to
their [Github]. This is further emphasized in [Table 5](#table-5-keras-vs-jax), where JAX performs significantly worse than Keras.  
JAX takes **521.436 seconds**, which is **329.12% longer** than Keras, and consumes **15461.0326 J**, a **214.87% increase** in
energy consumption. However, the JAX framework might not have come to full fruition in this experiment since only CPU performance is considered here.

[Simplilearn]: https://www.simplilearn.com/keras-vs-tensorflow-vs-pytorch-article
[Github]: https://github.com/jax-ml/

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

In this report, we conducted an experiment to assess the energy efficiency of the popular ML frameworks TensorFlow (Keras), PyTorch, and JAX.
We found that TensorFlow (Keras) had the fastest execution time and consumed the least amount of energy when tasked with training a convolutional
neural network for 3 epochs and evaluating its accuracy.

The second fastest and most energy-efficient framework was PyTorch,
but it already took **61.71% more time** and consumed **62.71% more energy** compared to TensorFlow (Keras).
The JAX framework performed worst, taking **165.36% more time** and consuming **93.52% more energy**
compared to the PyTorch framework (which already came in second).

Given the large scale at which ML frameworks are usually deployed, these relative differences in
energy consumption can lead to monumental differences in practice.

## Appendix - Raw data

```
 Results for keras

Computed Metrics:
Time metrics:
   - Shapiro Wilk P-Value: 0.784629398229877
   - Mean: 121.5040263157895
   - Median: 121.512
   - Variance: 0.5608752155049792
   - Standard Deviation: 0.7489160270050169
   - Minimum Value: 119.624
   - Maximum Value: 123.051
Energy metrics:
   - Shapiro Wilk P-Value: 0.0006012061237948319
   - Mean: 4914.063748333906
   - Median: 4910.235214233398
   - Variance: 487.3819500303882
   - Standard Deviation: 22.076728698572808
   - Minimum Value: 4835.301055908203
   - Maximum Value: 4979.832672119148
Power metrics:
   - Shapiro Wilk P-Value: 0.5147560930456103
   - Mean: 40.4255172687251
   - Median: 40.44419116557411
   - Variance: 0.055736331161044025
   - Standard Deviation: 0.23608543191193315
   - Minimum Value: 39.85268407788251
   - Maximum Value: 41.00262791083769
EDP metrics:
   - Shapiro Wilk P-Value: 0.32756376070069343
   - Mean: 596807.706670142
   - Median: 597288.5662610319
   - Variance: 35058202.95752139
   - Standard Deviation: 5920.996787494601
   - Minimum Value: 584515.5492591705
   - Maximum Value: 612773.3901369333

 Results for torch

Computed Metrics:
Time metrics:
   - Shapiro Wilk P-Value: 0.24755001126554754
   - Mean: 196.52997297297296
   - Median: 196.501
   - Variance: 2.4769596381381374
   - Standard Deviation: 1.5738359629065977
   - Minimum Value: 193.319
   - Maximum Value: 200.946
Energy metrics:
   - Shapiro Wilk P-Value: 0.396570910070075
   - Mean: 7991.3989817301435
   - Median: 7989.438499450684
   - Variance: 4535.631853475217
   - Standard Deviation: 67.34709981487858
   - Minimum Value: 7826.786437988281
   - Maximum Value: 8146.329483032227
Power metrics:
   - Shapiro Wilk P-Value: 0.02612627535645499
   - Mean: 40.664206438889124
   - Median: 40.58930408356134
   - Variance: 0.050818068304687956
   - Standard Deviation: 0.22542863239767916
   - Minimum Value: 40.345931622927964
   - Maximum Value: 41.13800846814706
EDP metrics:
   - Shapiro Wilk P-Value: 0.8743526806131524
   - Mean: 1569373.9417718607
   - Median: 1569504.3747069703
   - Variance: 638183528.5823413
   - Standard Deviation: 25262.294602477054
   - Minimum Value: 1513066.5274054564
   - Maximum Value: 1636972.3242973937

 Results for jax_jit

Computed Metrics:
Time metrics:
   - Shapiro Wilk P-Value: 1.0084512871825459e-07
   - Mean: 524.5563333333333
   - Median: 521.4359999999999
   - Variance: 82.45656043678174
   - Standard Deviation: 9.080559478180943
   - Minimum Value: 517.677
   - Maximum Value: 556.239
Energy metrics:
   - Shapiro Wilk P-Value: 1.650650289756625e-08
   - Mean: 15717.139767456054
   - Median: 15461.032592773438
   - Variance: 516979.5139220439
   - Standard Deviation: 719.012874656667
   - Minimum Value: 15258.066589355469
   - Maximum Value: 18551.803604125973
Power metrics:
   - Shapiro Wilk P-Value: 4.0211652370473554e-08
   - Mean: 29.950003883374333
   - Median: 29.698660823907385
   - Variance: 0.7198420102711628
   - Standard Deviation: 0.8484350359757444
   - Minimum Value: 29.318078058090865
   - Maximum Value: 33.35221659057702
EDP metrics:
   - Shapiro Wilk P-Value: 1.7224945725995178e-08
   - Mean: 8250571.834062944
   - Median: 8055534.450497742
   - Variance: 283266130314.75055
   - Standard Deviation: 532227.5174347438
   - Minimum Value: 7898750.137777771
   - Maximum Value: 10319236.684955427
Comparison between libraries keras and torch
Statistical comparsion for Time
    Test Used: Independent T-test
    t-test p-value: 8.579590415196178e-82
    Mean difference: -75.02594665718345
    Median difference: -74.989
Statistical comparsion for Power
    Test Used: Mann-Whitney U Test
    t-test p-value: 0.00010571240818944696
    Mean difference: -0.23868917016402236
    Median difference: -0.1451129179872268
Statistical comparsion for Energy
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.0893291320261987e-13
    Mean difference: -3077.3352333962375
    Median difference: -3079.203285217285
Statistical comparsion for EDP
    Test Used: Independent T-test
    t-test p-value: 1.0341264441118311e-63
    Mean difference: -972566.2351017187
    Median difference: -972215.8084459384
---
Comparison between libraries keras and jax_jit
Statistical comparsion for Time
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.0057822661250468e-12
    Mean difference: -403.05230701754385
    Median difference: -399.9239999999999
Statistical comparsion for Power
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.0057822661250468e-12
    Mean difference: 10.47551338535077
    Median difference: 10.745530341666726
Statistical comparsion for Energy
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.7177959763559135e-12
    Mean difference: -10803.076019122149
    Median difference: -10550.797378540039
Statistical comparsion for EDP
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.0057822661250468e-12
    Mean difference: -7653764.127392802
    Median difference: -7458245.88423671
---
Comparison between libraries torch and jax_jit
Statistical comparsion for Time
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.7164447323182373e-12
    Mean difference: -328.0263603603604
    Median difference: -324.93499999999995
Statistical comparsion for Power
    Test Used: Mann-Whitney U Test
    t-test p-value: 3.716375056049142e-12
    Mean difference: 10.714202555514792
    Median difference: 10.890643259653952
Statistical comparsion for Energy
    Test Used: Mann-Whitney U Test
    t-test p-value: 3.716375056049142e-12
    Mean difference: -7725.74078572591
    Median difference: -7471.594093322754
Statistical comparsion for EDP
    Test Used: Mann-Whitney U Test
    t-test p-value: 2.7177959763559135e-12
    Mean difference: -6681197.892291084
    Median difference: -6486030.075790771
---
```
