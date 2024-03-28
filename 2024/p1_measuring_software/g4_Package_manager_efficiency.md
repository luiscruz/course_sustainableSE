---
author: Lucian Negru, Eleni Papadopoulou, Yang Li
title: "Npm vs Yarn: Energy Efficiency"
image: "../img/p1_measuring_software/g4_Package_manager_efficiency/Time.PNG
../img/p1_measuring_software/g4_Package_manager_efficiency/Energy.PNG
../img/p1_measuring_software/g4_Package_manager_efficiency/Power.PNG
"
date: 28/02/2024
summary: |-
  This project aimed to test which of the two most popular JavaScript package managers, npm or yarn, is more energy efficient. We have run automated experiments which install a large list of packages in isolated environments using both tools. The installation process was run under the Energi Bridge utility tool to measure the average power draw of the process for each package manager. The results showed that yarn was more consistent in its power draws throughout the 30 runs of the experiment and achieved a 4.7% lower power usage than npm. We believe these results to be practically significant, as package installation is one of the most frequent functions in software development. In our strive for a more environmentally sustainable IT sector, we ought to implement and innovate more energy-efficient systems, applications, and functionalities, and we believe yarn manages to improve upon npm and do exactly that.
---
# Npm vs Yarn: Energy Efficiency
## **Introduction**

Software systems are becoming larger and more complex as time passes, however, so does the energy consumption of these ever-growing systems. Software development accounted for 150 TWh of energy use in 2023 ([Sharma, 2023]), representing an increase of approximately 23% each year. In our endeavour to have a more environmentally sustainable IT sector, we must also take a look at its energy consumption through development computation.

In this project, we tackled what is some of the most used functionalities in software development, package installation, and compared two different tools which handle that on their energy efficiency. When it comes to software development, no language is more used than JavaScript ([Vailshery, 2024]). The most popular package managers for JavaScript are [`npm`] and [`yarn`]; therefore our project aims to answer: **Which JavaScript package manager is more energy efficient, npm or yarn?** We ran package installation experiments and analysed the results based on time, energy consumption and efficiency distributions to answer the question. The setup for the automated experiment can be found in the following [repository].

## **What are package managers**

Package managers are tools that help developers manage the libraries and dependencies used in their projects. These tools allow automating the process of installing, upgrading, configuring and removing computer software packages. They play an important role in modern software development, especially in handling complex dependencies, ensuring software version consistency and identifying vulnerabilities. 

Package installations are typically included in most stages of deployment within pipelines. This means they run with every push a developer makes. Having faster package installation is a great benefit to developers and we are interested in how the difference in speed may affect a difference in energy efficiency.

### What is `npm`?

Npm (Node Package Manager), released in 2010, is a package manager for JavaScript and is the default package management tool for Node.js. It allows developers to install, share, and distribute code from the npm repository. Npm is not only a command-line tool, but also a package database that allows developers to publish new packages, update packages, or manage package dependencies. With npm, developers can easily add, update or remove project dependencies, manage project versions and scripts, and publish and share their open-source libraries.

### What is `yarn`?

Yarn is a new JavaScript package manager developed by Facebook (now Meta) to improve on some of npm's shortcomings. Launched in 2016, yarn offers faster dependency installation, tighter package versioning, and better security. Yarn caches each package download, so installing the same package again doesn't require an internet connection, which greatly speeds up installation speed and hypothetically also energy efficiency. Although npm and yarn have a lot of overlap in functionality, they each have their specialities in terms of performance, user interface and security.

## **Methodology**

This section will go over the setup of our experiments, including the energy measurement utility we used, the environment setup and the automation process.

## Energi Bridge utility for energy measurement

[Energi Bridge] is a software utility tool for measuring the energy usage of a system (process). When running the package installation, Energi Bridge gives us a precise energy measurement for the process of that specific task. This ensures a one-to-one comparison between npm and yarn.

### Docker containers for isolated experimentation

In the context of comparing power consumption during package installation with different package managers, the use of an isolated environment is crucial. The isolated environment provides reliability since it ensures that the environment is consistent across runs. Additionally, since different package managers can rely on different versions of dependencies, an isolated environment helps to avoid conflicts between the different requirements and dependencies.

[Docker] Containers provide a lightweight and isolated environment for running the experiments. Each package manager (npm and yarn) installs the same `package.json` within separate Docker containers to ensure independence and avoid interference. This process involves specifying a list of packages, initiating the installation process, and recording relevant metrics such as the time taken for installation and uninstallation, the energy and the power consumption for the procedure. The experiments are run 30 times for each package manager. Running the experiment 30 times provides more robust results and helps account for variability. The process repetitions result in reliability by encompassing average performance and revealing potential patterns or trends.


### Shell script for automated experimentation

The experiment runs using the `build.sh` file (or `windows-build.bat` for Windows). This script has been created to automate the experimentation by building the Docker images and running the installations/uninstallations for both package managers under the Energi Bridge measurement process. Automating experiments using scripts ensures consistency since all the experiments are guaranteed to be conducted with the same set of instructions and parameters. Additionally, it is efficient because it allows us to run a large number of trials without manual intervention. Finally, the script writes a `.csv` file for each of the two experiment outputs (one for npm and one for yarn), which reduces the probability of human error if this procedure were to be executed manually.

### Additional setup procedures

Additional procedures are needed to ensure a fair experiment:
1. The shell script alternates between the use of npm and yarn such that the order in which the two were used does not influence the outcome. 

2. System settings – such as screen brightness, internet connection, and background processes – were controlled throughout the experiments. 

3. The installation cache is removed after every run. Although this impedes one of yarn's advantages over npm, we want the different runs of the experiment to be in isolation from each other.

4. A CPU stress test was run before the experimentation using [Cinebench] to ensure that the first runs did not have a temperature advantage.

The experiment was conducted on an Apple M1 processor with the laptop plugged in.


## **Results**

### Time distribution for npm and yarn
The violin plot of the time distribution shows that npm's processing time distribution is relatively wide, which means that its processing time exhibits greater variability across runs. This width suggests that run times can fluctuate over a wide range in the use of npm. In contrast, yarn's time distribution looks more compact and consistent, suggesting that yarn's processing times are more stable and less variable across runs.

Additionally, in this graph, the median for yarn looks lower than the median for npm, this would indicate that yarn typically has faster processing times.

The violin plot for npm shows longer tails, which could indicate the presence of some extremely long processing time runs. In contrast, yarn's distribution may be more centred with shorter tails, indicating fewer extremes or less fluctuation in processing times.

![Time Distribution](../img/p1_measuring_software/g4_Package_manager_efficiency/Time.PNG)

### Energy distribution for npm and yarn

The violin plots of energy consumption show that the energy consumption distributions of npm and yarn show different patterns. npm's energy consumption distribution is likely to be wider, suggesting that its energy consumption is more variable across runs. In contrast, yarn's energy consumption distribution is likely to be relatively narrow, indicating that its energy consumption is more consistent across runs. If one looks at the white dots and thick black lines inside each violin plot, one can see the difference between the median (white dots) and interquartile range (thick black lines) of energy consumption for npm and yarn.

![Energy Distribution](../img/p1_measuring_software/g4_Package_manager_efficiency/Energy.PNG)

### Power distribution for npm and yarn

The violin plot of power usage shows the distributional characteristics of npm and yarn in terms of power usage. Similar to energy consumption, npm's power usage distribution may exhibit greater variability, while yarn shows a more consistent pattern of power usage. Yarn displays a 4.8% lower power usage than npm.

This difference may indicate that yarn is more efficient in power management compared to npm, possibly because yarn better optimises the task execution process and reduces the need for high power consumption.

![Power Distribution](../img/p1_measuring_software/g4_Package_manager_efficiency/Power.PNG)

In summary, yarn exhibits high efficiency and consistency in time, energy and power distribution, making it a preferred tool when performing dependency management tasks, especially in scenarios where fast response and efficient energy use are sought. However, in the actual selection and use process, the most appropriate decision should be made based on the project requirements and environmental characteristics, taking into account various factors.


## **Analysis**
### Are the results statistically significant?

To determine whether the experimental data meets the statistical significance of normal distribution, firstly we use the [Shapiro-Wilk] normality test. Based on the analysis we can see:

- The p-values for the time data (npm and yarn) are much less than 0.05, indicating that these data sets do not follow a normal distribution.
- The p-value for energy data (npm and yarn) is also much less than 0.05, again indicating that these data sets do not follow a normal distribution.
- The power data has p-values of 0.67 and 0.29 for npm and yarn respectively, indicating that the assumption of a normal distribution cannot be statistically rejected, and this is especially true for the power data for npm, but given the results of the other tests, we may need to use non-parametric tests for all variables to assess the statistical significance of the differences, and these tests do not rely on distributional assumptions about the data.

The Mann-Whitney U test is a non-parametric statistical test used to compare whether the medians of two independent samples differ. The test does not require the data to follow a normal distribution and is therefore suitable for analysing data sets that do not satisfy the assumption of a normal distribution for parametric tests. By comparing the ranks of two samples rather than comparing their values directly, the Mann-Whitney U test can assess the difference between two sample distributions independent of outliers. Based on the analysis we can see:

- Time data: p-value of 2.39 x 10<sup>-10</sup>, which is much less than 0.05, indicating that the difference between npm and yarn in time performance is statistically significant.
- Energy data: p-value of 4.20 x 10<sup>-10</sup>, again much less than 0.05, indicating that the difference between npm and yarn in energy consumption is statistically significant.
- Power data: p-value is 0.3478, which is higher than 0.05, indicating that the difference in power usage between npm and yarn is not statistically significant.

The results of the test show that there is a statistically significant difference between npm and yarn in terms of time and energy consumption, implying that the two perform differently in these areas and that this difference is statistically significant. However, in terms of power usage, the difference between the two is not statistically significant, indicating that as far as power consumption is concerned, they perform similarly and there is no significant difference.

### Are the differences practically significant?

Analysing statistical significance can lack insight into the context behind the investigation. While the results may not be statistically significant, the 4.7% higher energy efficiency of yarn over npm may provide practical significance. 

As stated previously, package installation is a frequently occurring process in software development. A 4.7% improvement can accumulate a high amount of energy saved over a larger period of time. Bringing back the energy usage of software development computation figure of 150 TWh, a 4.7% improvement would equate to 7 TWh of energy usage saved per year. This number represents the annual energy usage of over half a million average households. While software development computation does not account only for package installations, the comparison is made to show that even a small change can make a huge difference in the context of the ever-growing IT sector.


## Limitations and future work

One limitation was the network connection being over WiFi and not cable, possibly resulting in a less stable connection throughout the experiments. Given the current hardware setup, it was not possible to address this issue. 

Another limitation was that stress-testing the CPU increased the temperature above the desired level. During package installation, the CPU kept a constant 48 degrees Celsius, while the stress-testing brought it to 57 degrees. This means that the first few runs of the experiment were conducted with a hotter CPU than the rest, possibly affecting the final results. 

For future work, we would like to experiment with more package managers. One promising contender would be [Bun], a new JavaScript runtime which includes its own package manager, which has been shown to have up to 10x faster installation times than yarn. Another improvement for future work would be to increase the number of packages and the inter-package dependency, perhaps also testing yarn's ability to cache dependencies. Lastly, using an existing package benchmark may offer better comparisons with other package managers.

## **Conclusion**

In this report, we have investigated the energy efficiency of the two most popular JavaScript package managers, npm and yarn, in their package installation functionalities. We have run automated experiments in isolated environments to determine how much energy both tools use and determined that yarn is 4.7% more energy efficient than npm. 

This energy efficiency can be attributed to yarn's ability to install packages in parallel and – although not relevant in our experiment setup – its ability to cache installed packages. 

While the difference may not be statistically significant, we have argued as to why we consider it practically significant in the context of achieving a more environmentally sustainable IT sector. We have published the experiment in the following [repository], and encourage future work to be done on more package managers, more complex package dependencies, and more benchmarks.


[Vailshery, 2024]: <https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/>

[Sharma, 2023]: <https://www.i-scoop.eu/sustainability-sustainable-development/it-sector-electricity-demand/>

[`npm`]: <https://www.npmjs.com/>

[`yarn`]: <https://yarnpkg.com/>

[Shapiro-Wilk]: <10.1093/biomet/52.3-4.591>

[repository]: <https://github.com/MissingCurlyBracket/npm-VS-yarn-Energy-Efficiency-Experiment>

[Energi Bridge]: <https://github.com/tdurieux/energibridge>

[Docker]: <https://www.docker.com/>

[Cinebench]: <https://www.maxon.net/en/cinebench>

[Bun]: <https://bun.sh/package-manager>