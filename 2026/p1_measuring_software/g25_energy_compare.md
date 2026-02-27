---
author: Arnas Venskūnas, Dibyendu Gupta, Nick van Luijk, Sophie Schaaf
group_number: 25
title: "Energy Compare Project - Doomscrolling Reels vs. Shorts"
image: "img/g25_energy_compare/proposal_cover.png"
date: 12/02/2026
summary: |-
    Screen time is often discussed in terms of productivity and mental health, but what about energy usage? In this post, we compare the system energy usage for different frequency of scrolling while doomscrolling Tiktok versus YouTube Shorts.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Introduction

In 2025, people spent on average 141 minutes per day on social media[^time-spent]. That adds up to over 850 hours per person per year, much of it spent watching short-form content. A short break can easily turn into an endless session of watching a stream of recommended videos. This continuous video scrolling is also colloquially dubbed "Doomscrolling".

Every swipe has a cost beyond attention. The energy consumed by our devices to load, decode and play these videos is not something you might think about. In this project, we measure the total system power consumption while doomscrolling Instagram Reels and YouTube Shorts to understand the energy usage of our social media habits.

This research aims to provide insights on which platform to use in order to decrease your energy usage during a doomscrolling session.

Of course, using less energy during doomscrolling will be positive for the environment. However, there are more direct advantages to the community of doomscrollers.

Access to a charger is not always a given while in the midst of our doomscrolling sessions. When your device is low on battery, choosing the more energy-efficient platform might add extra time to keep scrolling. 

However, even if an energy source is available, the cost of energy has only been increasing over the last 5 years [^energy-prices]. Therefore, the findings in this research may allow you to reduce the price of your energy bill as well.

If you're going to doomscroll, you might as well do it in an energy-efficient way.

## Motivation

## Methodology

The aim is to quantify and compare the power consumption associated with doomscrolling. Therefore, we designed a comparative experiment analyzing the energy consumed by both TikTok as well as YouTube.

### Design Choices of the Experiments

The design of the experiment was one of the most important steps of the experimental setup. During the design phase, we contemplated and debated between various approaches to perform the experiment. The choice of approach affects the implementation and results of the experiment, hence they needed to be critically discussed and justified. 

#### <u>Frequency of Scrolling</u>

The design of the experiment also tries to mimic the actions of users, while keeping it consistent so that it's scientifically measurable and reproducible. An example of this choice was the frequency of scrolling - non-randomized (scrolling consistently after every 2, 5, and 10 seconds). In reality, the frequency of scrolling depends on different factors (attention capture of the video, user preference, network constraints, etc.) and is hence naturally random. However, to attain scientific basis for our experiments, we chose to make scrolling consistent.

#### <u>Moment of Energy Consumption Measurement</u>

Another key design choice was when we start measuring the energy used by the system. We know energy tests are flaky, and energy measurement had to be malleable to ensure room for error (network issues or delay, start-up time for the browser, warm up time, killing background processes of the system, etc.). Energy measurement began after:
- closing all popups (INSERT SCREENSHOT FOR CLOSING DIFFERENT POPUPS)
- "rejecting optional cookies"
- closing random popups while scrolling (since we are not logged into any of the social media apps)
- warm up time of 5 seconds (for any other browser processes to be completed)

Other factors such as brightness, sound of the system, size of the browser window, stable wired WiFi connection, room temperature remained constant during in experiments to not skew the energy consumption of the system.

#### <u>Warm-up Time</u>



### Experimental Setup


### Hardware/Software Details

## Test Environment
All tests were conducted within a standard Linux-based Operating System, using the Google Chrome browser. 

Capturing the energy spent for each experiment was done using EnergiBridge. EnergiBridge is a cross-platform command-line utility that can analyze the performance directly from our machine's low-level hardware sensors.

The experiments consisted of standardized scrolling sessions with a length of 30 seconds. For both platforms, the experiments were repeated 30 times to ensure generalizability.

For these experiments, the scrolling process was automated. Scrolling frequency was varied between the options of two, five or 10 seconds. This allows us to evaluate the impact of the pace of the content consumption as well.

## Tests
**TODO: Finalized code blocks for the test cases.**

## Experimental Controls
Desktop computers often run numerous background processes that could skew our energy measurements. Therefore, we aimed to create a strictly controlled testing environment. 

To achieve this, we disabled wireless networks in favour of an Ethernet connection. Additionally, we unplugged all non-essential USB peripherals and terminated all background applications, including cloud syncing tools. Lastly, we locked the monitor to a fixed, medium brightness level. 

With these mitigations, external influences on the stability of the to-be-measured energy consumption of solely the Doomscrolling. Therefore, solely the power consumption of video rendering and network requests is measured. Becasue of this, the expectation is that the measurements will not differ significantly across platforms.


## Analysis
### Exploratory Analysis
Violin + Box plots, expect the shape and outliers of the data.

### Normality
After the measurements are taken, it is important to ensure that data is normal. To measure normality, Shapiro-Wilk's test was performed. If the results do not assume normality, the points of data, deviating by more than 3 standard deviations from the mean were excluded and the Shapiro-Wilk's test was conducted again. If the results still did not indicate normality, the experiment was repeated.

### Statistical Significance
Group differences were evaluated using the Welch’s t-test, which does not assume equal variances between groups. Statistical significance was determined using a α = 0.05.

### Effect Size
To evaluate the practical implication of the observed results, mean difference and percent change were calculated.
Cohen’s d was computed to measure statistical effect size. Effect sizes were interpreted according to conventional benchmarks:

Small effect: d ≈ 0.2

Medium effect: d ≈ 0.5

Large effect: d ≈ 0.8

While statistical difference is unlikely to arise by chance, the practical importance will be further evaluated in the discussion section.

# Results

## Analysis
### Exploratory Analysis

This section presents violin and box plots based on the averages of 30 measurements for each platform on 2, 5 and 10 second intervals of scrolling.

“Raw” plots include all observations, while “clean” plots exclude outliers using the 1.5xIQR rule. We found that for some runs on TikTok, the reels were stuck, and the bot script was unable to scroll. We assume that these occurences represent the outliers on the lower end, providing a justification to remove them.

#### 2 second intervals

![2_raw](img/g25_energy_compare/measurements_2_violin_box_raw.png)

##### Chrome_TikTok
The distribution is hourglass-shaped, with observations concentrated at the lower and upper ends. It is skewed toward higher values, as the mean is lower than the median. Variability is relatively high.

##### Chrome_YouTube
The distribution is approximately symmetric and resembles a normal shape. The mean and median are nearly identical, and variability is noticeably lower than TikTok.

##### Comparison
On average, energy consumption is similar across platforms. However, TikTok shows greater dispersion, indicating a higher probability of elevated energy consumption in individual runs.

![2_clean](img/g25_energy_compare/measurements_2_violin_box_clean.png)

No noticeable difference after outlier removal.

#### 5 second intervals

![5_raw](img/g25_energy_compare/measurements_5_violin_box_raw.png)

##### Chrome_TikTok

As in the 2-second case, variability is higher than YouTube. The distribution is more strongly skewed toward higher values, suggesting a greater likelihood of increased energy consumption.

##### Chrome_YouTube

Variability increases compared to the 2-second interval. The distribution shows slight lower-tail skewness, with the median below the mean.

##### Comparison

Both the mean and median are higher for TikTok, indicating greater overall energy consumption relative to YouTube.

![5_clean](img/g25_energy_compare/measurements_5_violin_box_clean.png)

After removing the outliers, Chrome_tiktok graph appears to attain a normal distribution. Since outliers were on the lower end, both mean and median are higher.

![10_raw](img/g25_energy_compare/measurements_10_violin_box_raw.png)

##### Chrome_TikTok

Variability remains higher than YouTube but the distribution is more evenly spread and appears approximately symmetric. No clear outliers are observed.

##### Chrome_YouTube

Variability increases relative to earlier intervals. The mean and median converge, and the distribution appears approximately normal.

##### Comparison

Unlike previous intervals, the minimum energy consumption is roughly the same across platforms. However, TikTok consistently shows higher average consumption across runs.

![10_clean](img/g25_energy_compare/measurements_10_violin_box_clean.png)

##### Conclusion

Accross the runs, TikTok showed more unstable or inconsistent energy consumption across runs with similar or higher mean and average. It can be inferred, that TikTok is less energy efficient in the long run.

### Statistical Significance

The tests were conducted after removing outliers.

| Interval (s) | TikTok Normal |  YouTube Normal | Test Type      | Test Score | Significant  |
|--------------|---------------|-----------------|----------------|------------|--------------|
| 2s           | False         | True            | Mann-Whitney U | 0.2719     | No           |
| 5s           | True          | True            | Welsch's t-test| 1.471e-19  | Yes          |
| 10s          | True          | True            | Welsch's t-test| 0.0002     | Yes          |

### Effect Size

| Interval (s) | Mean difference | Percent difference | Cohen's d |
|--------------|-----------------|--------------------|-----------|
| 2s           | 3.1293          | 1.31%              | 1.174     |
| 5s           | 14.7714         | 6.68%              | 4.5612    |
| 10s          | 3.81185         | 1.81%              | 1.0327    |

## Discussion

### Test isolation

To isolate the tests from each other, we're creating a new browser instance and profile for each run. This ensures that the browser's cache and other stateful data do not influence the results. Static assets such as the JavaScript bundle and CSS files are not cached across runs, which means that each run will have to download and process these assets from scratch.

Wether this is realistic depends on the user behavior and device. For example, Chromium allows an origin to use up to 60% of the total disk space for caching, and when disk space is low, evict the least recently visited origins[^storage-for-the-web]. A user could visit the homepage of YouTube, download the static assets once, and then watch Shorts without re-downloading the assets. However, modern web applications, including YouTube[^youtube-ab-testing], often use A/B testing to serve different versions of the site to different users, which can lead to variations in energy consumption. Additionally, updates to the application can cause different versions of the static assets to be served, which can also invalidate the cached assets. Therefore, we believe that our approach of creating a new browser instance and profile for each run is a reasonable way to isolate the tests and ensure that the results are not influenced by caching or other stateful data.

### Recommendation algorithms

While developing the scripts to automate the Chromium browser, we encountered several challenges. Althrough we start with the same video uploaded to both platforms, the recommendation algorithms of YouTube and Instagram may serve different videos to the user, which can lead to variations in energy consumption. To attempt to reduce the influence of the recommendation algorithms, all tests are run without a logged in user. Therefore, a scrolling session of one test should not influence the next test, as the recommendation algorithms will not have any user data to personalize the content. However, it is still possible that the platforms use browser fingerprinting techniques to attempt to identify the user and serve personalized content, which could influence the results.

### Automation mitigations

Initially, we attempted to measure the energy consumption of scrolling Instagram Reels. However, we found that the Instagram web application does now allow an anonymous user to scroll more than 4 videos, which is not enough to get a reliable measurement. As we did not want to log in to an account, we decided to drop the Instagram Reels tests.

<div style="display: flex; align-items: center; justify-content: center; gap: 2rem; margin-block: 1rem;">
    <img src="./img/g25_energy_compare/youtube_cookies.png" alt="YouTube cookie prompt" style="width: calc(50% - 1rem);"/>
    <img src="./img/g25_energy_compare/tiktok_cookies.png" alt="TikTok cookie prompt" style="width: calc(50% - 1rem);"/>
</div>

Instead, we focused on YouTube Shorts and TikTok. YouTube allows an anonymous user to scroll through Shorts without any limitations, but it does show a cookie consent prompt that pops up before the first video is loaded. Before the measurements are taken, the script clicks the "Reject all" button to ensure that the cookie consent prompt does not influence the results.

Simmilarly, TikTok also shows a cookie consent prompt, where we again click the "Decline optional cookies" button before the first video is played. TikTok also shows a pop-up asking the user to log in when the page is loaded, but can be dismissed by clicking the X button. Because we do not want to log in to an account, we click the X button whenever the pop-up appears during the measurements.

While analyzing the results, we noticed that the energy consumption of TikTok of some test runs was significantly lower than the other runs. After investigating the issue, we found that TikTok was disallowing the automated browser to scroll through the videos, and loaded only the first video. These outlier runs were excluded from the analysis to ensure that the results are not influenced by this issue.

### Practical importance

# Conclusion

# Future work

# References

[^energy-prices]: CBS, "Average energy prices for consumers", Accessed Feb. 26, 2026, https://opendata.cbs.nl/#/CBS/en/dataset/85592ENG/table
[^time-spent]: B. Elad, "Average Time Spent On Social Media By App, Country, Region And Trend (2025)," *ElectroIQ*, Jun. 30, 2025. [Online]. Available: [https://electroiq.com/stats/average-time-spent-on-social-media/](https://electroiq.com/stats/average-time-spent-on-social-media/). [Accessed: Feb. 24, 2026].

[^storage-for-the-web]: P. LePage, "Storage for the web," *web.dev*, Sep. 23, 2024. [Online]. Available: [https://web.dev/articles/storage-for-the-web](https://web.dev/articles/storage-for-the-web). [Accessed: Feb. 26, 2026].

[^youtube-ab-testing]: "YouTube feature experiments & rollouts, *YouTube Help*. [Online]. Available: [https://support.google.com/youtube/answer/7367023?hl=en](https://support.google.com/youtube/answer/7367023?hl=en). [Accessed: Feb. 26, 2026].
