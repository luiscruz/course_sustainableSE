---
author: Lucian Negru, Eleni Papadopoulou, Yang Li
title: "Npm vs Yarn: Energy Efficiency"
image: "../img/p1_measuring_software/g4_Package_manager_efficiency/Time.PNG
../img/p1_measuring_software/g4_Package_manager_efficiency/Energy.PNG
../img/p1_measuring_software/g4_Package_manager_efficiency/Power.PNG
"
date: 28/02/2024
summary: |-
  
---
# Npm vs Yarn: Energy Efficiency
## **Introduction**
## **What are package managers**

Package managers are tools that help developers manage the libraries and dependencies used in their projects. These tools allow automating the process of installing, upgrading, configuring and removing computer software packages. They play an important role in modern software development, especially in handling complex dependencies and ensuring software version consistency.

### What is npm?

npm (Node Package Manager) is a package manager for JavaScript and is the default package management tool for Node.js. It allows developers to install, share, and distribute code from the npm repository. npm is not only a command-line tool, but also a package database that allows developers to publish new packages, update packages, or manage package dependencies. With npm, developers can easily add, update or remove project dependencies, manage project versions and scripts, and publish and share their own open source libraries.

### What is yarn?

Yarn is a new JavaScript package manager developed by Facebook to improve on some of npm's shortcomings.Launched in 2016, Yarn offers faster dependency installation, tighter package versioning, and better security.Yarn caches each package download, so installing the same package again doesn't require an internet connection, which greatly speeds up installation speed.

Although npm and yarn have a lot of overlap in functionality, they each have their own specialities in terms of performance, user interface and security. Developers can choose which tool to use based on their personal or team preferences. Over time, both npm and yarn have been updated and improved to better serve the JavaScript community.

## **Methodology**

### Docker containers for isolated experimentation

### Shell script for automated experimentation

## **Results**

### Time distribution for npm and yarn
The violin plot of the time distribution shows that npm's processing time distribution is relatively wide, which means that its processing time exhibits greater variability across runs. This width suggests that run times can fluctuate over a wide range in the use of npm. In contrast, yarn's time distribution looks more compact and consistent, suggesting that yarn's processing times are more stable and less variable across runs.

Also, in this graph, if the median for yarn looks lower than the median for npm, this would indicate that yarn typically has faster processing times.

The violin plot for npm shows longer tails, which could indicate the presence of some extreme long processing time runs. In contrast, yarn's distribution may be more centred with shorter tails, indicating fewer extremes or less fluctuation in processing times.

![Time Distribution](../img/p1_measuring_software/g4_Package_manager_efficiency/Time.PNG)

### Energy distribution for npm and yarn

The violin plots of energy consumption show that the energy consumption distributions of npm and yarn show different patterns. npm's energy consumption distribution is likely to be wider, suggesting that its energy consumption is more variable across runs. In contrast, yarn's energy consumption distribution is likely to be relatively narrow, indicating that its energy consumption is more consistent across runs. If one looks at the white dots and thick black lines inside each violin plot, one can see the difference between the median (white dots) and interquartile range (thick black lines) of energy consumption for npm and yarn.

![Energy Distribution](../img/p1_measuring_software/g4_Package_manager_efficiency/Energy.PNG)

### Power distribution for npm and yarn

The violin plot of power usage shows the distributional characteristics of npm and yarn in terms of power usage. Similar to energy consumption, npm's power usage distribution may exhibit greater variability, while yarn shows a more consistent pattern of power usage.

This difference may indicate that yarn is more efficient in power management compared to npm, possibly because yarn better optimises the task execution process and reduces the need for high power consumption.

![Power Distribution](../img/p1_measuring_software/g4_Package_manager_efficiency/Power.PNG)

In summary, yarn exhibits high efficiency and consistency in time, energy and power distribution, making it a preferred tool when performing dependency management tasks, especially in scenarios where fast response and efficient energy use are sought. However, in the actual selection and use process, the most appropriate decision should be made based on the project requirements and environment characteristics, taking into account various factors.


## **Analysis**
### Are the results statistically significant?

In order to determine whether the experimental data meets the statistical significance of normal distribution, firstly we use the Shapiro-Wilk normality test. Based on the analysis we can see:
- The p-values for the time data (npm and yarn) are much less than 0.05, indicating that these data sets do not follow a normal distribution.
- The p-value for energy data (npm and yarn) is also much less than 0.05, again indicating that these data sets do not follow a normal distribution.
- The power data has p-values of 0.6659900546073914 and 0.2947884202003479 for npm and yarn respectively, indicating that the assumption of a normal distribution cannot be statistically rejected, and this is especially true for the power data for npm, but given the results of the other tests, we may need to use non-parametric tests for all variables to assess the statistical significance of the differences, and these tests do not rely on distributional assumptions about the data.

The Mann-Whitney U test is a non-parametric statistical test used to compare whether the medians of two independent samples differ. The test does not require the data to follow a normal distribution and is therefore suitable for analysing data sets that do not satisfy the assumption of a normal distribution for parametric tests. By comparing the ranks of two samples rather than comparing their values directly, the Mann-Whitney U test is able to assess the difference between two sample distributions independent of outliers.

In this experiment, the normal distribution test showed that the time and energy data did not follow a normal distribution, while the power data had inconsistent normality, so the Mann-Whitney U test was chosen to assess the difference in performance between npm and yarn in terms of time, energy and power. Based on the analysis we can see:

- Time data: p-value of 2.39 x 10<sup>-10</sup>, which is much less than 0.05, indicating that the difference between npm and yarn in time performance is statistically significant.
- Energy data: p-value of 4.20 x 10<sup>-10</sup> , again much less than 0.05, indicating that the difference between npm and yarn in energy consumption is statistically significant.
- Power data: p-value is 0.3478, which is higher than 0.05, indicating that the difference in power usage between npm and yarn is not statistically significant.

The results of the test show that there is a statistically significant difference between npm and yarn in terms of time and energy consumption, implying that the two perform differently in these areas and that this difference is statistically significant. However, in terms of power usage, the difference between the two is not statistically significant, indicating that as far as power consumption is concerned, they perform similarly and there is no significant difference.

### Are teh differences practically significant?

## **Conclusion**
