---
author: Julian Hirschler, Patrick Krumpl, Shantanu Jare, Sven Butzelaar, Thomas Verwaal
title: "Native vs. Web: Analyzing the Energy Consumption of Spotify Apps"
image: "https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg"
date: 28/02/2025
summary: |-
  abstract Lorem ipsum dolor sit amet, consectetur adipisicing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
  reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
  pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
  culpa qui officia deserunt mollit anim id est laborum.
---
<!-- TODO: write abstract -->

# Introduction
The way music is consumed and distributed has changed dramatically over the past few decades. The rise of digital streaming platforms such as Spotify has transformed music into an on-demand service, replacing the need to purchase physical products such as CDs or vinyl. [^music_industry_shift] 

Today, streaming generates over 67% of global music revenues [^global_music_report], confirming its dominance in the industry. With 675 million monthly active users [^spotify_report] and a market share of over 30% [^streaming_stats], Spotify is the clear leader in the music streaming market. While this shift has made music more accessible than ever, it also poses questions about its environmental impact, since streaming requires a service provider, constant network data transmission, and device power.

In recent years, web-based streaming has become more and more popular as it eliminates the need for users to install additional applications on their devices. While web applications are often favoured for their accessibility and convenience, desktop applications often offer more features to the user. In this article, we compare the energy consumption of Spotify's web and desktop applications. By analysing these differences, we aim to provide valuable insights to help users make better decisions about their streaming habits.


<!-- TODO: We could add plots of the timeline -->
# Methodology
This chapter describes the methodology used to compare the energy consumption of Spotify's web and desktop applications. It covers the design of the experiment and how the experiment itself was conducted, including the automation and setup of the experiment.

## Design of the experiment
<!-- TODO: write about how it was designed -->
<!-- TODO: also talk about our first setup without closing and opening the app. You can refer to  "Results initial setup without closing and opening (web)app"-->
The first thing to do when before conducting the experiment is designing it. Therefore, a specific use case of the application, in our case Spotify's web and desktop application, has to be determined. It is also important to design the experiment in such a way, that it mimics actual user behaviour and is realistic.

First, we designed and conducted an experiment with both applications (desktop and web) opened at the same time. We switched between the windows and played exactly one song randomly in each test run. However, the disadvantages of this kind of experiment were that the other window that was opened in the background influences the accuracy of the measurement. Moreover, playing a random song also has an influence on the energy consumption. Thus, the data was not really normally distributed.

The goal for designing the revised experiment was to minimize any biases by other applications and only focus on the application that is being executed. Moreover, we still wanted to play more than one song to mimic realistic user behaviour, but also wanted the data to be normally distributed amongst the experiment. Thus, we hab to design the single runs similarily, while also integrating some randomness.

For the final experiment, we have decided to have 30 runs per application. The runs itself are randomly shuffeled. For one single run, we first open the respective application (i.e. web or desktop). Next, we wait for a few seconds such that the application is fully loaded and the opening does not have an influence on the energy measurement. We did not want to include the starting of the application in this measurement, because we wanted to solely focus on the use case of playing music. Next, the energy measurement is started and four songs are played in a random order. Each song is played for 20 seconds. Including the delays for starting and searching for the songs, one run takes approximately 2 minutes. After the run, the application is closed and we do a pause of 1 minute. Thus, the whole experiment takes about 3 hours.

## Experiment setup
<!-- TODO: describe what we did as setup -->
<!-- TODO: also describe why energy measurements are so difficult and what the ZEN mode is-->
<!-- TODO: how to set up energy measurements with minimum bias -->
<!-- TODO: also write about the warm up and initialization somewhere. Either here or in the experiment design-->

## Experiment execution
<!-- TODO: write about how we automated the tests and why this is important-->
<!-- TODO: Also write about how we do the energy measuremt somewhere. Explain and link EnergiBridge-->

## Replication
To replicate this experiment, check out our public [GitHub repository](https://github.com/famulenz-pkrumpl/SSE_Spotify). It contains all the necessary scripts as well as instructions on how to set up the experiment.[^sse_github_repo]


# Hardware setup
<!-- TODO: write hardware setup-->

# Results 

## Results initial setup without closing and opening (web)app
As discussed in the methodology, our initial approach was to keep the app and the web browser open during all experiments. The results, as can be seen in Figure 1 show a plot without a normal distribution. We assume that the results with a lower energy consumption might have benefitted from internal cashing. This lead us to change our setup to open and close the (web)app for every run.

![Violin Plot](../img/p1_measuring_software/g25_spotify/box_without_closing_setup.png)
*Figure 1: Violin and Box plots of energy consumption (J) without outliers.*

## Results improved setup
### Violin and Box Plots and Outliers Removal
We have plotted the data[^github] collected from the experiment into two violin and box plots, as can be seen in Figure 2. It is clear from the plots that both the result for the web and native version contain outliers. We used Shapiro-Wilk test to check if our results are normal, the results from this test can be seen in Table 1. The p-value for the web version (2.1 × 10<sup>-8</sup>) and for the native version (5.0 × 10<sup>-4</sup>) reported by the Shapiro-Wilk are smaller than 0.05 and thus the data is not normally distributed. We therefore used z-score outlier removal to remove outliers, we had to apply this twice before the p-value of the Shapiro-Wilk test was larger than 0.05, as can be seen in Table 2. The violin and box plots for the data without outliers can be seen in Figure 3. We removed three data points, two from the web version (129.5J and 788.4J) and one from the native version (814.3J).

![Violin Plot](../img/p1_measuring_software/g25_spotify/box_outliers.png)
*Figure 2: Violin and Box plots of energy consumption (J) with outliers.*

| Shapiro-Wilk            	| W      	| p-value     	|
|-------------------------	|--------	|-------------	|
| With outliers web       	| 0.5549 	| 2.1 * 10<sup>-8</sup> 	|
| With outliers native    	| 0.8456 	| 5.0 * 10<sup>-4</sup> 	|
| Without outliers web    	| 0.9573 	| 0.3002      	|
| Without outliers native 	| 0.9882 	| 0.9809      	|

*Table 1: Values reported by Shapiro-Wilk with and without outliers.*

![Violin Plot](../img/p1_measuring_software/g25_spotify/box_no_outliers.png)
*Figure 3: Violin and Box plots of energy consumption (J) without outliers.*

### Welch's t_test and Significance
To determine the significance of our results we used Welch’s t-test, which reported a t-statistic of -9.3 and a p-value of 3.21 × 10<sup>-12</sup>. Since p < 0.05 we conclude that there is a statistically significant difference. From the t-statistic we conclude that the native version consumes significantly more energy.

### Effect Size
To get an insight into the effect size of our experiments we computed multiple values, including the average difference, percent change and cohan's d, these can be seen in Table 2.

|                	| Web   	| Native 	| Difference 	|
|----------------	|-------	|--------	|------------	|
| Minimum value  	| 572.4 	| 653.2  	| 80.8       	|
| Maximum value  	| 711.4 	| 741.2  	| 29.8       	|
| Average        	| 625.3 	| 692.7  	| 67.4       	|
| Percent change 	|       	|        	| 10.78%     	|
| Cohan's d      	|       	|        	| 2.4        	|

*Table 2: Effect size analysis.*

# Discussion
<!-- TODO: Mention that the desktop version has more features than the web verions, that might consume more energy. But the desktop version has caching, which does not improve it -->
<!-- TODO: also mention the paper https://www.ivanomalavolta.com/files/papers/MOBILESoft_2023.pdf and mention that on Android, it is opposite -->

# Limations and Issues
<!-- TODO: mention that the experiment does not cover all use cases-->
<!-- TODO: mention that the app have different settings (e.g. audio quality, video playback, caching ...) that also influences the energy consumption and that the desktop app has in general more setting-->

# Conclusion

# Future Work
<!-- TODO: what could maybe be added here: compare more use cases, compare different browsers, compare different settings for audio quality, disable video, ...-->


---

[^music_industry_shift]: [An Economic Analysis of the Effects of Streaming on the Music Industry in Response to Criticism from Taylor Swift](https://scholarworks.uni.edu/cgi/viewcontent.cgi?params=/context/mtie/article/1154/&path_info=05_Zehr_music_streaming.pdf)
[^global_music_report]: [IFPI - Global Music Report](https://www.ifpi.org/wp-content/uploads/2024/04/GMR_2024_State_of_the_Industry.pdf)
[^spotify_report]: [2024 Earnings](https://newsroom.spotify.com/2025-02-04/spotify-reports-fourth-quarter-2024-earnings/?utm_source=chatgpt.com)
[^streaming_stats]: [Music Streaming Services Stats (2025)](https://explodingtopics.com/blog/music-streaming-stats)
[^sse_github_repo]: [GitHub repository with source code of experiment](https://github.com/famulenz-pkrumpl/SSE_Spotify)
