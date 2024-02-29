---
author: Thijs Nulle, Harmen Kroon, Petter Reijalt 
title: "Comparing Energy Consumption of React Framework Versions"
image: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/2300px-React-icon.svg.png"
date: 29/02/2024
summary: |-
 Javascript Frameworks play a fundamental in current-day website development. Major releases are rolled out yearly and add new improvements over previous versions. This research shows significant developments in terms of power consumption related to loading large datasets between different versions of the React Framework 
---

# Comparing Energy Consumption of React Framework Versions
![](https://crowdbotics.ghost.io/content/images/2019/06/React-Event-Listeners.png)

## Introduction
The ICT sector currently accounts for 1.8 to 2.0% of all global emissions. It is predicted that the output of the ICT sector will increase to 830 MT of CO2 emissions in 2030. Because of the ever-expanding ICT sector, it will become more and more important to write code that keeps power consumption to a minimum, to keep in line with the 1.5°C decarbonisation pathway and net-zero targets set by companies and countries worldwide. 
[^1]

One of these factors in the CO2 output of the sector is the output of websites. A website with 10.000 page visits per month results on average in an annual CO2 emission of 211kg (a single page visit produces 1.76 grams of CO2).[^2]

Most websites nowadays use some kind of Javascript framework. Providing developers with pre-written and pre-tested code to write easily scalable web applications.[^3] Currently, only 18.3% of websites do not use any kind of Javascript framework. While these Javascript frameworks make it easier to produce and scale websites, they also introduce a certain kind of extra overhead, which results in extra energy consumption.[^4] 

One of the biggest frameworks is React, which is built by Meta and used by 7 per cent of all websites worldwide. These include one of the most-visited websites worldwide. Namely, Apple.com, Linkedin.com, and Amazon.com are some of the most notable names that use React in one way or another on their websites.[^5]

Changes in React can cause huge changes downstream, with millions of websites being affected. One of these changes is power consumption. More efficient code in the React framework can result in drastic cuts in carbon emissions. Research, however, shows that a significant amount of websites run outdated versions of the React Framework. [^6] This could be because of a myriad of issues that could arise from upgrading to a newer version. Most notably breaking changes that break backwards compatibility, in which case the developer has to go in and manually change the code. 
 
We researched whether or not over time changes in the React framework have led to more efficient code and thereby less power consumption. We looked at the fact whether or not upgrading to the newest React version can benefit companies, from an environmental point of view. 


[^1]:[Allianz Research](https://www.allianz.com/en/economic_research/insights/publications/specials_fmo/decarbonizing-information-technologies.html#:~:text=The%20information%20and%20communications%20technologies,1.8%20to%202.8%25%20in%202020)
[^2]:[Zifera](https://zifera.io/blog/why-you-should-care-about-the-co2-emissions-of-your-website=)
[^3]:[Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks#introductory_guides) 
[^4]: [Green and Sustainable JavaScript a study into the impact of framework usage](https://www.diva-portal.org/smash/get/diva2:1768632/FULLTEXT01.pdf)
[^5]: [w3techs](https://w3techs.com/technologies/details/js-react)
[^6]: [w3techs](https://w3techs.com/technologies/details/js-react/15)

## Methodology

### Experiment
To compare the evolution of energy consumption within the React framework, we propose two implementations of the same website, using both a legacy version and a modern version. The website contains a simple, CPU-intensive task in loading a large dataset, rendering the dataset inside a table and performing several operations on the dataset, which we will highlight later. In essence, we compare the energy usage of the framework’s state management and rendering process.

For this article, we used React version 0.18.2 (modern version) versus the last beta release 0.14 (legacy version). The main difference between the legacy version and the modern version of React is the style in which one writes components to use within a website; legacy React uses class components, whereas modern React uses functional components. Inherently, these can perform the same operations, but under the hood, they are functionally different and their performance might differ. The largest difference between class- and functional components is regarding the state management, where the legacy version utilises the class-based `this.setState` functionality, and the modern version utilises the `useState` hook. Essentially, these two functions have the same outcome but are implemented differently under the hood, and thus also perform differently on energy usage.

As loading a large dataset, and subsequently rendering the data inside a table, is not necessarily an interesting benchmark, we opted to add CPU-intensive tasks to perform on the dataset. The dataset consists of 10k rows consisting of an identifier (integer between 1 and 100), name (random string of 50 characters), age (integer between 1 and 100) and a comma-separated list of hobbies (random selection of 30 hobbies). After each operation we perform, we take the resulting data and store it as a local variable inside the component using the method as advised by the version of the framework. The operations we perform in order are:

1. Filter all rows that have an identifier greater than 90
2. Filter all rows that do not contain the letter K inside the name
3. Filter all rows that have an age less than 21
4. Filter all rows that do not contain swimming as a hobby
5. Reverse all rows
6. Randomise the order of all rows
7. Increase the age by 1 for all rows
   
Each CPU-intensive task is linked to a dedicated button for direct invocation. This minimalist user interface ensures simplicity and isolates table rendering, minimising potential overhead. This approach prioritises accurate energy consumption measurements and enables a focused comparison between the legacy and modern versions of React.



### Tools
Our experiment is automated using Python and can be found [here](https://github.com/thijsnulle/sse-project1/tree/script). Tasks are double shuffled - both react version as well as browser - and alternated with 50 seconds of sleep to mitigate tail energy consumption. Before energibridge measurements, the React server is initialised and once the server is up and running the browser-specific webdriver is opened with [Selenium](https://www.selenium.dev/). During a task, the exact same order of button presses is performed and the energibridge measurement will end once the browser window is terminated automatically.


### Hardware set-up
The experiment is performed on an Intel Core i7-6700HQ CPU running no non-windows services and incorporating extra tasks up front for warm-up. External factors are accounted for by connecting to the internet via ethernet and having the room controlled at room temperature.



## Results 

The results of our experiment can be found on our [Github repository](https://github.com/thijsnulle/sse-project1/tree/script/experiment/win32). Here 2 different experiments, can be found. For this section we used the last experiment we ran. Here 2 folders can be found with 32 iterations of the experiment for both the modern version and the legacy version. 

### Energy & Power
To determine the difference in energy consumption between both versions, we calculated the energy consumption for different components of the computer system. We computed the following violin graph, to show the distribution of 30 data points over the 2 versions across 4 categories. This shows us that distributions of the dram_energy, package_energy and pp0_energy significantly differ from one another. The latest version of React in this case requires significantly less energy across these 4 categories. In most graphs, we have a few upward outliers that can be attributed to external processes simultaneously running on the computer. 

| ![python CPU/GPU boxplot](./../img/p1_measuring_software/g2_react/violin_react.jpeg) | 
|:--:|
|Figure 1: CPU/GPU comparison for Python code|

| ![python DRAM boxplot](./../img/p1_measuring_software/g8_energy_IDE/python%20DRAM.png) | 
|:--:|
|Figure 2: DRAM comparison for Python code|






### Python

| ![python CPU/GPU boxplot](./../img/p1_measuring_software/g8_energy_IDE/python%20usage.png) | 
|:--:|
|Figure 1: CPU/GPU comparison for Python code|

| ![python DRAM boxplot](./../img/p1_measuring_software/g8_energy_IDE/python%20DRAM.png) | 
|:--:|
|Figure 2: DRAM comparison for Python code|

#### Visual Studio Code

The boxplot of running a Python application in Visual Studio Code shows no outliers and exhibits a pattern that indicates a normal distribution as well. If we perform a Shapiro-Wilk test, we get a p-value of 0.875, which confirms our theory that the data is normally distributed. That means we can expect a program to use 239 J of energy for a run on average. Energy usage typically ranges from 230 to 245.

With the GPU energy consumption, we see a similar pattern. The boxplot shows a similar distribution of values, although the scale is different on the y-axis. This indicates that the data that we have collected matches a normal distribution. This is confirmed by our Shapiro-Wilk test, which returns a p-value of 0.840. While this does not guarantee that the data is a normal distribution, all the signs we look for are pointing in this direction. The average energy usage is roughly 212 Joules.

Lastly, we can observe the RAM energy usage over the different runs. Here, the average is more centered within the box plot. This still seems like valid distribution and could be considered normal. Upon running the Shapiro-Wilk test, we get a p-value of 0.430, which does not disprove our hypothesis. So we consider this to be a normal distribution, which averages our energy consumption at 25.5 J.

#### IntelliJ

Upon examining the IntelliJ CPU energy usage for the Python application, we see that the distribution shape is a bit different. The boxplot contains an outlier. If we look at the data, there is one outlier that is significantly higher than the others. This run has a value of over 500 J. Since this only happens in the first run, it could be that some other process happened to interfere at the first run of the distribution. Upon further inspection of the data, the application seems to run longer on the first run than on other runs. It took 48 seconds for its first run, where other runs average around 42 seconds. The stalling of this run seems to explain its higher energy consumption quite well, so it is best excluded from our estimation. However, running the statistical analysis shows us that the p-value still reaches 0.083, which means the statistical test still does not reject the hypothesis that this is a normal distribution, even with the outlier. So while the outlier could be removed, we still include it in our average, which would result in an expected energy consumption of 422 J per run for the CPU.

For the GPU, we can see it is also influenced by the first run as an outlier. Here, the difference is more apparent. This, the Shapiro-Wilk test does not reject the hypothesis at a value of 0.107. We can still assume this data to be normal. The shape does however still match a normal distribution, even though we can only see one tail. This graph shows us the average consumption would be around 370 Joules per run done for the GPU.

For its DRAM energy consumption, we see something different happening. The first run again seems to influence the results strongly. Once we remove this run from the data, we get an even lower p-value of 0.02 versus 0.04 with the outlier. It seems that the DRAM behaviour is not centered around a normal distribution.

### Java

| ![Java CPU/GPU boxplot](./../img/p1_measuring_software/g8_energy_IDE/java%20usage.png) | 
|:--:|
|Figure 3: CPU/GPU comparison for Java code|

| ![Java DRAM boxplot](./../img/p1_measuring_software/g8_energy_IDE/java%20DRAM.png) | 
|:--:|
|Figure 4: DRAM comparison for Java code|

#### Visual Studio Code

For the Java experiment in Visual Studio Code, we can again see an outlier in the boxplot. If we take a look at the runs, we can see that there are two values that are significantly higher than the others, which are 273 and 241. These do not happen at the start of the run, but seems to happen in runs that are neither close to the first or last experiment. What these do have in common is that they run for a lot longer than other runs, both upwards of 20 seconds compared to 15 seconds for other executions. If we exclude these runs, the data does seems to behave according to a normal distribution. The average however with these is 160 J for the CPU.

If we evaluate the GPU data for Visual Studio Code for the Java experiment, it matches the pattern we observe in the CPU data. The Shapiro-Wilk test reject the hypothesis as well, with a p-value of 0.02. The same data points that heavily influence the CPU data are also different in the GPU data. In these runs the GPU consumes upwards of 200 J of energy, versus around 130 J for the runs that finish earlier than 20 seconds. On average however, they consume 133 J of energy.

This again holds for the DRAM data. Here the outliers are distinctly present on the boxplot, with values at 48 J and 44 J. The Shapiro-Wilk also reject the normal distribution with a p-value of 0.01. The average ends up with the outliers at around 26 J.

#### IntelliJ

In IntelliJ, the data is not indicative of anything other than a normal distribution. This is also seen in the p-value, which is returned to be 0.39. This means that an expected energy consumption of 322 J on average is a consistent measurement over our runs, with little variation to be seen in both distributions.

### JavaScript

| ![JavaScript CPU/GPU boxplot](./../img/p1_measuring_software/g8_energy_IDE/javascript%20usgae.png) | 
|:--:|
|Figure 5: CPU/GPU comparison for JavaScript code|

| ![JavaScript DRAM boxplot](./../img/p1_measuring_software/g8_energy_IDE/javascript%20DRAM.png) | 
|:--:|
|Figure 6: DRAM comparison for JavaScript code|

#### Visual Studio Code

Based on the boxplot, which shows no outliers and has its mean in the center of the distribution, we assume that the data is distributed normally. This is confirmed by the p-value from the Shapiro-Wilk test, which returns a value of 0.74. These factors indicate that the program has a predictable average energy consumption, which hovers around 168 J for the CPU.

For the GPU, the p-value of the Shapiro-Wilk test does not reject the hypothesis. This would make it acceptable for us to assume the data is distributed normally, which would in turn indicate that the experiment has run successfully. The average value we would get is around 149 J.

Lastly, for the DRAM, we get a p-value of 0.97, which would indicate that the distribution is normal. This on average takes about 20 J of energy. The boxplot confirms together with the test that it is okay to assume a normal distribution on the data.

#### IntelliJ

For the CPU, we can see a clear outlier in the data. This also results in a rejection of the hypothesis, since we get a value of 0.0004. Without this outlier, the data gets a p-value of 0.46 on the Shapiro-Wilk test. If we remove the outlier, this results in an average energy consumption of 360 J.

A similar situation can be detected in the GPU, where we can see that the hypothesis of a normal distribution is rejected as well, because of this outlier. It also returns a p-value lower than our alpha threshold, with a p-value of 0.0007. The average ends up at around 320 J.

Finally, for the DRAM, we can see that the outlier has a reduced impact on our hypothesis. There is a smaller difference when we compare this outlier to the outliers of the CPU and GPU. This also allows for the hypothesis to not be rejected, since p = 0.057. However, this value still increases the average significantly to 51 J.

## Discussion

In all plots shown above, it can be seen that the average energy consumption of Visual Studio Code is lower than IntelliJ. This is seen very clearly for the CPU and GPU energy consumption, where the difference is typically over 100 J over this time span. In order to validate that these results are statistically significant, we decided to run a Student's t-test in order to ensure that the results are valid. 

The results of these tests are all clear of the alpha threshold, ranging from 5.0e-6 to 1.1e-20, which show that the distributions are different Its practical significance is clear. Even in terms of DRAM, the result show that the relative consumption of IntelliJ is higher than its Visual Studio Code usage. While 100 J does not seems large, these experiments are run over short time spans, typically less than 30 seconds. If we extrapolate the 100 J difference, which is multiplied by 2 since both the CPU and GPU usage exhibit this difference, it would equate to 200 J / 0.5 m = 6 W. With this particular laptop, which has a battery of 45 Whr, this means that a 6 W difference has great benefits for the developer, as it contributes to less battery usage. Thus, we can conclude that the energy consumption of Visual Studio Code is lower, which is what we hypothesised in our original proposal for the experiment.

### Limitations and future research

Our research had a few limitations, which we will briefly discuss in this section.

One possible limitation of our research is the fact that the tests were only performed on one system, as specified in the [hardware set-up section](#hardware-set-up) above. While this ensures that the results of the different tests are easily comparable, it also makes it harder to generalize our results. 

This project had a time span of a week. Therefore, the software may not be perfectly optimised. For example, it is possible that the code that closes Intellij and Visual Studio Code only closes the window, but not the background processes of the software. This could have influenced the speed of the next start up.

For each program/software combination, we executed the experiment 10 times. However, these 10 similar experiments were executed in a row. This could result in e.g. IntelliJ closing down and immediately starting back up. This could have influenced the results since data from the software could still be active in the RAM.

Furthermore, we tried to execute the experiments as humanlike as possible. This means that the experiments were run in a normal Microsoft Windows environment with background processes on. These background processes could have influenced the final outcomes. 

Lastly, one could argue that running code is not the only thing a developer does with an IDE. A substantial amount of time is spent writing, reading and debugging. In future research, one could expand on this knowledge by testing an idle mode or simulating a developer that writes code.

## Conclusion

In this blog, we analysed and compared the energy consumption of two of the most popular IDEs, Visual Studio Code and IntelliJ. We tested the energy consumption by running a Python application a Java application, and a Node.js server. These tests simulated real life user behaviour using an automated script that mimics user clicks and keyboard usage. Based on the results of our tests, we found that Visual Studio Code uses significantly less energy than IntelliJ. Therefore, the recommendation is to use Visual Studio Code for reduced battery usage and a reduced carbon footprint.
