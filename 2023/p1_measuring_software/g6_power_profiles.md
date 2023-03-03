---
author: Rover van der Noort, Martijn Smits, Remy Duijsens, Dajt Mullaj
title: "The Effect of Different Power Profiles on Energy Consumption and Runtime Performance in Machine Learning Applications"
date: 03/03/2023
summary: "Training neural networks is a daily task for AI engineers. In this study, we evaluate the effects of different power profiles on the performance and energy consumption of a neural network training benchmark. Our results show that the power-save profile causes the benchmark to use significantly less energy than the other power profiles. The difference in runtime is statistically significant but in absolute measure not practically relevant for this use case."
---


## Introduction

Climate change is an important research topic and specifically in the field of computer science the problem of massive power consumption persists [1, 2]. Recently many new solutions have appeared, which try to tackle this problem in a variety of ways [1, 2, 6]. Popular operating systems (OS) have introduced power-saving settings as built-in features, which enable any user to activate them. It is however not directly clear how much energy these profiles save or how it affects the performance of a system.

The popularity of Machine Learning (ML) models has increased parallel to the interest in sustainability [3]. However, generally, these models require large quantities of energy to train and deploy [3, 5]. TensorFlow is a widely used open-source library to create and deploy ML models. Perfzero offers a benchmark framework to test a system's performance for machine learning computations.

This study investigates the impact of the Ubuntu Power Profiles on the benchmark framework for TensorFlow and could show ML developers the impact of power saving methods. This study elaborates on the studied libraries and how they will be tested, followed by the results of the experiment. This is concluded with a discussion of the findings and some further work recommendations. 


## Related Work

Ubuntu Power Profiles are built into Gnome as the power-tools-daemon, which offers three different power modes: balanced, power-saver, and performance. It performs a set of actions depending on the profile and the system's highly customizable hardware. For Intel-based machines, it uses P-state scaling, which can utilise hardware-specific optimizations for energy consumption or performance. 

There are similar applications like power-tools-daemon, such as the open-source applications TuneD by RedHat and TLP by linrunner. They differ only in some specific implementation details but do not work concurrently.

Many Energy Profiler applications vary in their method of measurement [4].  ...


## Methodology
Multiple factors play a role in the power consumption rate of a computer. To increase the accuracy of the results, we need to minimise the effect of these factors. Therefore we will prepare the environment (both internal and external) before running the tests, we will do that as follows:  

- **Background processes** use power and can also cause spikes in energy consumption. This will lead to inaccurate measurements of the actual power consumption of the benchmarking software. Therefore we will kill all non-essential background tasks during the test, this will also include disabling notifications. On top of that, we will randomise the order in which the tests are run. This is to decrease the chance of unforeseen background tasks running only during one specific scenario.  
- **Battery health** can affect power consumption and therefore we will not run the test on battery mode.  
- **External devices** can also impact battery life, therefore we will run the tests with no external devices plugged in.  
- **Temperature** also plays a role in the energy consumption of a computer. Therefore we will run all the tests at room temperature. We will also take thirty-second breaks in between runs of the benchmark to give the components in the computer time to cool down. Before running any of the tests we will run a Fibonacci sequence for one minute to warm up the CPU and a benchmark for roughly 40 seconds to warm up the GPU, this is because we cannot fully cool down the components for each of the tests.  
- **Other external factors**, such as the surface on which the computer stands, may also affect power consumption. Therefore we will gather all the results in the same environment on the same device.

After preparing the environment we will run the tests. The tests consist of three different scenarios. There are three different power modes for which we test the power consumption of an idle system and the consumption of running the benchmark. The power profiles are as follows:  

- **Power saver:** This profile is designed to minimise power consumption by reducing the CPU speed, disabling some hardware features, and other optimisations.  

- **Balanced:** This is the default profile that provides a good balance between performance and power consumption.  

- **High performance:** This profile maximises performance by increasing the CPU speed, disabling some power-saving features, and other optimisations.  
We will measure the *total power consumption* to run the benchmark. To further decrease the potential effect of undesired factors, we take a couple of extra measures. First, we will run each scenario 30 different times and average the results. Secondly, we automate the full test, so that manual mistakes are eliminated.

The measurement tool that is created to automatically execute the experiments according to the decribed methodology is available at https://github.com/remyd95/SSE_Project1.

## Results
The experiments were executed on an HP ZBook Studio G4 with an Intel i7-7700HQ processor and an NVIDIA Quadro M1200 Mobile with 8GB RAM. The operating system used was Ubuntu 22.04.2. In total 90 experiments, 30 for each power mode, were conducted in a randomly shuffled order. The benchmark workload that was used is a synthetic neural network training job on the Cifar-10 dataset on a Resnet model. This workload was controlled by the Perfzero benchmark tool, which is designed for Tensorflow performance benchmarks. Tensorflow has been configured to use the available GPU in the system to resemble the setup that is most common for AI engineers. The energy consumption was measured using the Powerstat tool which is based on the Intel RAPL measurement feature. 

 
The results obtained for each profile are presented in the following table.


TABLE OF RESULTS
 

### Exploratory Analysis

We visualized the data to gain some insights into its structure. As can be seen in Figure (ADD FIGURES ERRORBARS), it seems that the data is structured as expected, with the Powersaver profile being the most energy efficient and costly in terms of time and the Performance profile being the fastest but least energy efficient. However to draw any conclusive interpretation we need to understand the statistical significance of the results. To do that we explored the data distribution using a box plot and a violin plot. To run the necessary test for statistical significance we needed to confirm that the data is normal. As seen in the distribution plots this is hard to conclude just from the visualizations. We therefore run a Shapiro-Wilk test to confirm normality. The p-values obtained from the test are displayed in the following table.

 

TABLE TO BE INSERTED

 

As can be seen not all data is normally distributed. We therefore tried to remove the outliers using z-scores, and removing points with a score higher than three standard deviations. However, only the time data for the Balanced profile became normal after outlier removal. We therefore performed a sanity check by rerunning the whole experiment, however, we got similar results regarding the data normality distributions as shown in Table X.

 

TABLE WITH SHAPIRO TEST FOR FIRST EXPERIMENT

 

Therefore we moved forward concluding that not all data distributions are normal. 

 

### Statistical Significance and Effect Size 

 

We checked the statistical significance of the differences between the three profiles by using a two-sided Welsch t-test or Manney-Wittney U-test depending on the normality of the data. 

 

ADD TABLE OF RESULTS 

 

Of these results, only the difference in energy consumption between the Balanced and Performance profile is not significant. We therefore moved to check first the difference in medians between the energy consumption of the Performance and Powersaver profile, which is 387 J, and between the Balanced and Powersaver profile, which is 386 J. In both cases, the difference is of three orders of magnitude. The difference in time, instead, is always below 1 second. 

 

ADD A TABLE WITH DIFFERENCES 

 

We also computed the pair percentages as reported in the following table. 

 

ADD TABLE PAIR PERCENTAGES

 

Finally, we computed the Choen's or Cliff's delta, again depending on the normality of the data. Each delta result indicates that the difference of the distributions is large, in the case of the times of the Balanced and Performance profile, for example, Choen's data indicates that the results are generally separated by almost an entire standard deviation.

<!-- argue about practical signifiance (This is in the discussion or as a new section in results not sure)-->

The complete data analysis on which this section is based is available as notebook in our code repository at https://github.com/remyd95/SSE_Project1/blob/main/data_analysis.ipynb.

## Discussion


The presented work comes with a couple of limitations. The Perfzero TensorFlow benchmark tool requires an internet connection to be able to run. An Internet connection can cause serious distortions in the measurement, for instance, due to background processes that need to sync. Another limitation related to the benchmark tool is that we had to use a synthetic benchmark tool to be able to keep the experiments short. Real-world machine learning training jobs in common scenarios can take several hours to complete. In an ideal experiment, such a real-world training job would be the best choice. Another limitation is that ultimately, the effects of the unwanted side factors cannot be removed. These factors, especially in our setup, can only be minimised. Lastly, the gathered data does not follow a normal distribution for all power mode results. However, it is known that when working with AI applications, the outcome is rarely deterministic and a normal distribution is therefore not feasible.


<!--

- energy: power-saver not normal

- time: power-saver and performance not normal -->


In the context of our research, the power save mode is the most energy-efficient. However, in a real scenario, a user might not do the same preparation as we did. They might have their screen turned on, or unnecessary background processes running. Since the power-save mode has an overall longer runtime, it could be possible that with additional energy-consuming processes running for an overall longer time, that power-save mode might be more energy-consuming than the other energy profiles. Extra research needs to be conducted to prove or disprove this hypothesis.

<!-- 
- Limitation -> wifi
- Limitation -> synth benchmark, real benchmark
- Limitation -> unwanted factors cannot be removed, only minimised
- Hard to get normal distr. when working with ML applications 
- energy: power-saver not normal
- time: power-saver and performance not normal
- Discussion point: In the context of our research the powersave mode is the most beneficial, however in a real scenario the user might have their display on and background processes running, therefore the longer runtime of the task might actually consume more energy overall 
-->


## Conclusion

In this work, we have motivated the need for energy-efficient solutions, especially in energy-intensive domains like Artificial Intelligence. One easy way to adjust the power usage on laptops is by applying different power profiles. Three different power profiles for the Ubuntu Linux operating system have been benchmarked on a machine learning training job. The experiments measured both energy consumption and the runtime of the training job. The results of the experiments show that the power-save profile consumes significantly less energy than the balanced and performance profiles. While the runtime shows the same significant difference, the practical significance is less applicable. The small increase in runtime compared to the large decrease in energy consumption makes the power-save profile the best energy-aware choice for AI engineers. The experiments were also repeated with Tensorflow without GPU support. A similar energy pattern emerged with again little practical significance in the difference in runtime across all power modes. Further research can extend this work by repeating the experiments in a more controlled setting. Furthermore, instead of short synthetic benchmarks, real benchmarks can be used to simulate real-world machine learning mode training scenarios. At last, different systems can be evaluated including operating systems, different models and datasets, and different types of hardware including hardware that is more commonly by AI engineers.


## References
[1] Hayri Acar, G ̈ulfem I Alptekin, Jean-Patrick Gelas, and Parisa Ghodous.
The Impact of Source Code in Software on Power Consumption. Interna-
tional Journal of Electronic Business Management, 14:42–52, 2016.


[2] Coral Calero and Mario Piattini. Introduction to Green in Software Engi-
neering, pages 3–27. Springer International Publishing, Cham, 2015.


[3] Eva Garc ́ıa-Mart ́ın, Crefeda Faviola Rodrigues, Graham Riley, and H ̊akan
Grahn. Estimation of energy consumption in machine learning. Journal of
Parallel and Distributed Computing, 134:75–88, 2019.


[4] Erik Jagroep, Jan Martijn E. M. van der Werf, Slinger Jansen, Miguel Fer-
reira, and Joost Visser. Profiling energy profilers. In Proceedings of the 30th
Annual ACM Symposium on Applied Computing, SAC ’15, page 2198–2203,
New York, NY, USA, 2015. Association for Computing Machinery.


[5] Mohit Kumar, Xingzhou Zhang, Liangkai Liu, Yifan Wang, and Weisong
Shi. Energy-efficient machine learning on the edges. In 2020 IEEE
International Parallel and Distributed Processing Symposium Workshops
(IPDPSW), pages 912–921, 2020.3


[6] Stefan Naumann, Markus Dick, Eva Kern, and Timo Johann. The greensoft
model: A reference model for green and sustainable software and its engi-
neering. Sustainable Computing: Informatics and Systems, 1(4):294–304,
2011.
