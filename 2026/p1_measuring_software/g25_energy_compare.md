---
author: Arnas Venskūnas, Dibyendu Gupta, Nick van Luijk, Sophie Schaaf
group_number: 25
title: "Energy Compare Project - Doomscrolling Reels vs. Shorts"
image: "img/g25_energy_compare/proposal_cover.png"
date: 12/02/2026
summary: |-
    Screen time is often discussed in terms of productivity and mental health, but what about energy usage? In this post, we compare the total system power while doomscrolling Instagram Reels versus YouTube Shorts.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Introduction

In 2025, people spent on average 141 minutes per day on social media[^time-spent]. That adds up to over 850 hours per person per year, much of it spent watching short-form content. A short break can easily turn into an endless session of watching a stream of recommended videos, a phenomenon known as "doomscrolling."

Every swipe has a cost beyond attention. The energy consumed by our devices to load, decode and play these videos is not something you might think about. In this project, we measure the total system power consumption while doomscrolling Instagram Reels and YouTube Shorts to understand the energy usage of our social media habits.

If you're going to doomscroll, you might as well do it in an energy-efficient way.

## Methodology
### Analysis
#### Exploratory Analysis
Violin + Box plots, expect the shape and outliers of the data.
#### Normality
After the measurements are taken, it is important to ensure that data is normal. To measure normality, Shapiro-Wilk's test was performed. If the results do not assume normality, the points of data, deviating by more than 3 standard deviations from the mean were excluded and the Shapiro-Wilk's test was conducted again. If the results still did not indicate normality, the experiment was repeated.
#### Statistical Significance
Group differences were evaluated using the Welch’s t-test, which does not assume equal variances between groups. Statistical significance was determined using a α = 0.05.
#### Effect Size

To evaluate the practical implication of the observed results, mean difference and percent change were calculated.
Cohen’s d was computed to measure statistical effect size. Effect sizes were interpreted according to conventional benchmarks:

Small effect: d ≈ 0.2

Medium effect: d ≈ 0.5

Large effect: d ≈ 0.8

While statistical difference is unlikely to arise by chance, the practical importance will be further evaluated in the discussion section.

## Results

### Analysis
#### Exploratory Analysis
#### Normality
#### Statistical Significance
#### Effect Size

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

## Conclusion

## Future work

## References

[^time-spent]: B. Elad, "Average Time Spent On Social Media By App, Country, Region And Trend (2025)," *ElectroIQ*, Jun. 30, 2025. [Online]. Available: [https://electroiq.com/stats/average-time-spent-on-social-media/](https://electroiq.com/stats/average-time-spent-on-social-media/). [Accessed: Feb. 24, 2026].

[^storage-for-the-web]: P. LePage, "Storage for the web," *web.dev*, Sep. 23, 2024. [Online]. Available: [https://web.dev/articles/storage-for-the-web](https://web.dev/articles/storage-for-the-web). [Accessed: Feb. 26, 2026].

[^youtube-ab-testing]: "YouTube feature experiments & rollouts, *YouTube Help*. [Online]. Available: [https://support.google.com/youtube/answer/7367023?hl=en](https://support.google.com/youtube/answer/7367023?hl=en). [Accessed: Feb. 26, 2026].
