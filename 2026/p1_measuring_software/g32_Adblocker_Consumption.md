---
author: Cem Gungor, Rodrigo Montero Gonzalez, Sahana Ganesh, Poyraz Temiz
group_number: 32
title: "Adblocker Consumption: Measuring the Energy Usage of Adblockers"
image: "img/gX_template/project_cover.png"
date: 12/02/2026
summary: |-
  This study compares the energy consumption between two profiles, where one profile has an ad blocker extension and the other one does not. In both profiles we simulate a user reading and browsing content on different newsletters, through an automated script. Our findings aim to highlight the significant energy difference when one uses an adblocker as compared to when one does not.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Introduction

Energy efficiency has become an increasingly important concern in software systems. Even small differences in energy consumption can accumulate significantly when multiplied across millions of users and daily interactions. Web browsing is one of the most common computing activities, yet its energy implications are often overlooked. Ad blockers are widely used tools designed to improve user experience by preventing the display of advertisements and tracking scripts. While their primary purpose is privacy protection and usability, their impact on energy consumption is less well understood.

On the one hand, an ad blocker introduces additional processing inside the browser, which could increase computational overhead. On the other hand, blocking advertisements and third-party scripts may reduce the amount of content loaded and executed, potentially decreasing CPU workload and energy usage. This raises an interesting question: does enabling an ad blocker increase or decrease energy consumption during web browsing?

---

## Motivation

Ad blockers might affect energy efficiency on a larger scale in addition to individual user experience. Millions of people use the internet every day, so even small energy savings per session could add up to significant drops in total energy consumption. Since software-level design decisions can have system-wide energy and environmental effects, it is crucial to comprehend whether widely used technologies like ad blockers increase or decrease energy usage from the standpoint of sustainable software engineering.

In this study, we experimentally evaluate the impact of using an ad blocker on CPU package energy consumption during a simulated news browsing session. By comparing browsing sessions with and without an ad blocker under controlled conditions, we aim to determine whether such a commonly used tool has measurable energy implications.

---

## Methodology

This study investigates the impact of an ad blocker on CPU energy consumption during web browsing. We compare two browser configurations:

* **Profile 1 – Without Ad Blocker**
* **Profile 2 – With Ad Blocker**

Throughout the remainder of this report, these two configurations will be referred to as *Profile 1* (without ad blocker) and *Profile 2* (with ad blocker).

Both configurations were tested under identical conditions using a controlled browsing script.

### Research Question

Does enabling an ad blocker reduce CPU package energy consumption during a simulated news browsing session?

### Hypothesis

We hypothesize that enabling an ad blocker reduces energy consumption by preventing the loading and execution of advertisements.

---

### System Setup

* **Device:** HP ZBook X G1i
* **CPU:** 16 cores
* **Processor:** Intel(R) Core Ultra 7 255H (2.00 GHz)
* **RAM:** 32GB
* **Operating System:** Ubuntu Linux 24.04.3 LTS

---

### Software Setup

Google Chrome was used as the browser in both configurations. Both browser profiles were newly created and used exclusively for this experiment.

* **Profile 1:** No ad blocker installed
* **Profile 2:** Stands AdBlocker installed and enabled with default filter settings

The following python and library versions were used for this experiment:
* **Python:** 3.12.3
* **Python Libraries:**
  * **websocket-client:** 1.9.0
  * **requests:** 2.32.5

Energy measurements were collected using Energibridge. The energy of the CPU package was obtained from the `PACKAGE_ENERGY (J)` counter. This metric represents cumulative CPU energy consumption and is appropriate for bounded, one-off workloads.

---

### Browsing Workload

To simulate realistic browsing behavior, we developed an automated script that navigates to a predefined set of news websites:

* [https://www.dailymail.co.uk](https://www.dailymail.co.uk)
* [https://www.bbc.com/news](https://www.bbc.com/news)
* [https://www.theguardian.com](https://www.theguardian.com)

The script uses Chrome DevTools Protocol via a WebSocket connection to navigate to each website, wait for page loading, and scroll the page at fixed intervals. For each website, the script scrolls continuously for 30 seconds, simulating a user reading and browsing content. This results in a fixed browsing session consisting of three sequential news pages.

**Disclaimer**: Most news websites use cookies. Before running the scripts cookies pop-up should be closed in both profiles in all websites.

---

### Experimental Procedure

To reduce external interference and improve measurement reliability, a “zen mode” setup was applied. All unnecessary applications were closed, notifications were disabled, screen brightness was fixed, external monitors were disconnected, and the system was connected to power throughout the experiments.

Before collecting experimental data, a warm-up phase consisting of three complete browsing executions was performed and discarded. This allowed the CPU to reach a stable thermal and frequency state, reducing bias caused by cold starts, initial boost behavior, and cache warming effects.

Each browser configuration was executed 30 times, resulting in 60 total runs. The order of executions was randomized to reduce systematic bias. Randomization was applied independently for each run, ensuring that neither profile consistently benefited from execution order or temporal effects such as gradual temperature changes.

To further reduce interference between executions, a fixed cooldown period was applied. A 15-second rest period was enforced between the two profiles within a run, and an additional 30-second rest period was applied after completing both profiles before starting the next run. These pauses helped mitigate tail energy effects and thermal carry-over between measurements.

For each execution, total CPU package energy was computed as the difference between the final and initial cumulative `PACKAGE_ENERGY (J)` values. This produced one energy value per run. The `PACKAGE_ENERGY (J)` counter was selected as the primary metric because it directly represents cumulative CPU energy consumption. Since the browsing session is a bounded workload with a clear start and end, total energy consumption is more appropriate than instantaneous power measurements. 

---

## Results

We collected 30 independent executions for each profile, resulting in two samples of equal size. For each execution, total `PACKAGE_ENERGY (J)` was computed as the difference between final and initial cumulative energy values. This produced one energy value per run, which served as the unit of analysis.

---

### Exploratory Data Analysis

The histogram, boxplot and violin plots obtained from the results are shown below. The two distributions are clearly separated, with Profile 2 exhibiting consistently lower energy values.

![Histogram of Energy Distribution](img/g32_Histogram_Energy_Distribution.png)

**Figure 1.** Histogram - The left distribution indicates the energy consumption of Profile 2, and the right distribution indicates the energy consumption for Profile 1.

![Box Plot of Energy Consumption](img/g32_Box_Plot_Energy_Consumption.png)

**Figure 2.** Box Plot - Comparison of total energy consumption for Profile 1 and Profile 2

![Violin Plot of Energy Consumption](img/g32_Violin_Plot_Energy_Consumption.png)

**Figure 3.** Violin Plot - Comparison of total energy consumption for Profile 1 and Profile 2.

---

### Normality Assessment

Following the procedure described in the course slides, we tested normality using the Shapiro–Wilk test.

* Profile 1: The test did not reject normality (p = 0.27172).
* Profile 2: The test did not reject normality (p = 0.61508).

Since both distributions were assumed normal, we proceeded with a parametric statistical test.

---

### Statistical Significance

Given that both samples satisfied the normality assumption, we applied Welch’s t-test to compare the two independent samples. The test indicated a statistically significant difference between the profiles (p < 0.001).

The mean energy consumption was:

* **Profile 1:** 1050.959 J
* **Profile 2:** 644.179 J

The mean difference was **406.780 J**, corresponding to a **38.71% reduction** in energy consumption for Profile 2 relative to Profile 1.

The magnitude of this reduction exceeded initial expectations, indicating that the effect of blocking advertisement-related content on energy consumption is not only statistically detectable but also substantial in practice.

---

### Practical Significance

In addition to statistical significance, the magnitude of the observed difference suggests a practically meaningful improvement under the tested workload. Since both samples followed an approximately normal distribution and no extreme outliers were observed, the assumptions for the parametric test were satisfied. Overall, the results provide consistent evidence that Profile 2 consumes less energy than Profile 1 under the experimental conditions.

---

### Practical Effect

According to our analysis, profile without the adblocker has an average CPU package power around 10.0 whereas the profile with the adblocker is 6.1. According to [eyeo's 2023 ad-filtering report](https://info.eyeo.com/adfiltering-report) around 900 million people are using adblockers, of which around 400 million is desktop users. Additionally, according to [Global Web Index's 2018 report](https://www.gwi.com/hubfs/Downloads/Ad-Blocking-trends-report.pdf) around 43% of internet users reported to have used ad-blockers in the past month of report date. On the news side, survey data from [GWI reports](https://www.gwi.com/hubfs/Digital_vs_Traditional_Media_Consumption.pdf?utm_source=chatgpt.com) that internet users (16–64) spent about 50 minutes per day on 'online press' globally (2016). Even if we conservatively assume 50 million adblocker users spending about 30 minutes per day on online press, the estimated annual energy savings would be approximately 35 GWh.

Under our conservative assumptions, the estimated 35 million kWh in annual savings is equivalent to the yearly electricity use of roughly 10,000-13,000 Dutch households, depending on the household consumption data of [CBS](https://www.cbs.nl/en-gb/figures/detail/81528ENG).


---

## Discussion

The results show that the browsing profile with the ad blocker enabled consumed considerably less energy than the profile without the ad blocker. On average, the ad blocker reduced total CPU package energy consumption by approximately 30% per browsing session.

This difference is likely related to the amount of content loaded by modern websites. News pages often include advertisements, tracking scripts, animations, and additional network requests. These elements require extra CPU processing and script execution. When the ad blocker is enabled, part of this content is prevented from loading, which reduces computational work and therefore energy consumption.

The energy values for the ad blocker profile were also more tightly clustered, suggesting reduced variability across executions. Advertising systems frequently load dynamic and asynchronous content, which can introduce fluctuations in CPU activity. Removing part of this behavior may lead to more stable runs.

Part of the energy reduction may also be explained by differences in runtime. If pages load faster when advertisements are blocked, total execution time decreases, which directly reduces total energy consumption. In this sense, the lower energy usage reflects both reduced computational load and potentially shorter browsing sessions.

While the measurements focus on a single browsing session, the observed energy savings become significant when considered at scale. Web browsing is one of the most frequent daily computing activities, and ad blockers are used by millions of users. A consistent reduction in CPU energy consumption per session suggests that content blocking mechanisms can contribute meaningfully to reducing overall energy demand on end-user devices.

From a sustainable perspective, this raises questions about responsibility and design incentives. While website operators prioritize revenue generation, the resulting energy costs can have an effect on end users and their devices. Tools such as ad blockers can therefore be seen as more energy-efficient behavior. On the other hand, from an economic point of view, news websites rely on ads to generate the revenue needed to stay alive. If we promote the idea of using adblockers, we may consequently be limiting these websites’ ability to produce content. This concern is especially important given that a significant share of news audiences now blocks ads, highlighting the scale of the challenge facing the industry. At the same time, the business model of news media has shifted away from ad dependence toward subscription based access. This raises the question of how news articles can generate revenue in a different, more energy-efficient manner and whether subscription based access is in fact more energy efficient. This problem links to the trade-off in sustainable software engineering that pushing for more sustainable practices can have an economic, time, or effort cost.

---

## Threats to Validity

Despite efforts to control experimental conditions, several threats to validity remain.

**Internal Validity:** Although background applications were closed and a zen-mode setup was applied, complete isolation of the system cannot be guaranteed. Operating system processes and hardware-level power management mechanisms may introduce minor variability. Additionally, while warm-up and cooldown phases reduce thermal bias, small temperature differences between runs may still influence CPU energy measurements.

**Construct Validity:** The study measures CPU package energy rather than full system energy. Other components such as DRAM, storage, and network interfaces also contribute to total device energy consumption. Therefore, the results specifically reflect CPU-related energy effects and may not fully represent overall device-level energy savings.

**External Validity:** The browsing workload was limited to three selected news websites and a fixed interaction pattern. Different types of websites, such as video streaming platforms, social media applications, or static content pages, may exhibit different energy characteristics. All the aforementioned websites are used on a daily basis by many users worldwide so measuring the impact of using and ad blocker would provide a clearer idea on its effect. Furthermore, only one ad blocker and one hardware platform were tested. There are many ad blockers available for download that may contain different strategies on preventing ads, with some perhaps being more or less efficient. Even though there is evidence to suggest that using the ad blocker mentioned above may reduce the energy consumption, other adblockers can have the opposite effect. It should also be mentioned that results may vary across different browsers, filter configurations, operating systems, or processor architectures.

**Ecological Validity:** Although the automated scrolling script simulates reading behavior, it does not capture the full variability of real user interaction patterns. Human browsing behavior includes pauses, clicks, tab switching, and multitasking, which may influence energy consumption differently.

These limitations should be considered when interpreting the results and generalizing the findings beyond the experimental setup.

---

## Conclusion

In this study, we investigated the impact of enabling an ad blocker on CPU package energy consumption during a simulated news browsing session. Using 30 independent executions per configuration and following the statistical analysis procedure, we compared browsing sessions with and without an ad blocker.

Answering our research question, enabling an ad blocker does reduce CPU package energy consumption during a simulated news browsing session, resulting in a statistically significant reduction compared to browsing without an ad blocker.

Our results indicate that enabling the ad blocker reduced total CPU energy consumption per session. The difference was statistically significant under the tested workload.

These findings suggest that, in the evaluated scenario, blocking advertisements and third-party scripts reduces computational work and therefore lowers energy consumption. While the results are specific to the selected websites and experimental setup, they indicate that ad blockers may have energy efficiency implications beyond usability and privacy considerations.

Future work could extend this study by evaluating different categories of websites, such as video streaming platforms or social media applications, where advertising behavior differs substantially. Additionally, testing multiple ad blockers with varying filter lists, as well as measuring the full system energy consumption including memory and network interfaces, would provide a more comprehensive view of the energy implications. Repeating the experiment on different hardware architectures could further improve generalizability.

---

All of our scripts and outputs are available in our [GitHub](https://github.com/sg003/sustainable_p1)

### Relevant Links:

AdBlocker Used: https://chromewebstore.google.com/detail/ad-blocker-stands-adblock/lgblnfidahcdcjddiepkckcfdhpknnjh?utm_source=ext_app_menu

EnergiBridge GitHub Repo: https://github.com/tdurieux/energibridge

