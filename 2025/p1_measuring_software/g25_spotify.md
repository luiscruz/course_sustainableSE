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

# Introduction
The last few decades have seen a dramatic shift in the way music is distributed and consumed. The rise of digital streaming platforms such as Spotify have transformed music into an on-demand service, replacing the need to purchase physical formats such as CDs or vinyl. [^music_industry_shift] 

Today, streaming generates over 67% of global music revenues [^global_music_report], consolidating its dominance in the industry. With 675 million monthly active users [^spotify_report] and a market share of over 30% [^streaming_stats], Spotify is the undisputed leader in the music streaming market. While this shift has made music more accessible than ever, it also poses questions about its environmental impact, since streaming requires a service provider, constant network data transmission, and device power.

In recent years, web-based streaming has become increasingly popular as it eliminates the need for users to install additional applications on their devices. While web applications are often favoured for their accessibility and convenience, they can come with trade-offs in terms of energy efficiency. In this article, we compare the energy consumption of Spotify's web and desktop applications. By analysing these differences, we aim to provide valuable insights to help users make more informed choices about their streaming habits.


TODO: outline
TODO: At link to our github
# Hardware setup

# Methodology

# Results 
(We could add plots of the timeline)
### Violin Plots and Outliers Removal
We have plotted the data<!--[^github]--> collected from the experiment into two violin plots, as can be seen in Figure 1. It is clear from the plots that both the result for the web and native version contain outliers. We used Shapiro-Wilk test to check if our results are normal, the results from this test can be seen in Table 1 The p-value for the web version (2.1 × 10<sup>-8</sup>) and for the native version (5.0 × 10<sup>-4</sup>) reported by the Shapiro-Wilk are smaller than 0.05 and thus the data is not normally distrubted. We therefore used z-score outlier removal to remove outliers, we had to apply this twice before the p-value of the Shapiro-Wilk test was larger than 0.05, as can be seen in Table 2 The violin plot for the data without outliners can be seen in Figure 2. We removed three data points, two from the web version (129.5J and 788.4J) and one from the native version (814.3J).

![Violin Plot](box_outliers.png)
*Figure 1: Violin plot of energy consumption (J) with outliers.*

| Shapiro-Wilk            	| W      	| p-value     	|
|-------------------------	|--------	|-------------	|
| With outliers web       	| 0.5549 	| 2.1 * 10<sup>-8</sup> 	|
| With outliers native    	| 0.8456 	| 5.0 * 10<sup>-4</sup> 	|
| Without outliers web    	| 0.9573 	| 0.3002      	|
| Without outliers native 	| 0.9882 	| 0.9809      	|
*Table 1: Values reported by Shapiro-Wilk with and without outliers.*

![Violin Plot](box_no_outliers.png)
*Figure 2: Violin plot of energy consumption (J) without outliers.*

### Welch's t_test and Significance
To determine the significance of our results we used Welch’s t-test, which reported a t-statistic of -9.3 and a p-value of 3.21 × 10<sup>-12</sup>. Since p < 0.05 we conlcude that there is a statistically significant difference. From the t-statistic we conclude that the native version consumes significantly more energy.

### Effect Size
To get an insight into the effect size of our experiments we computed multiple values, including the average difference, percent change and cohan's d, these can be seen in Table 2

|                	| Web   	| Native 	| Difference 	|
|----------------	|-------	|--------	|------------	|
| Minimum value  	| 572.4 	| 653.2  	| 80.8       	|
| Maximum value  	| 711.4 	| 741.2  	| 29.8       	|
| Average        	| 625.3 	| 692.7  	| 67.4       	|
| Percent change 	|       	|        	| 10.78%     	|
| Cohan's d      	|       	|        	| 2.4        	|
*Table 2: Effect size analysis.*

# Discussion

# limations and Issues

# Conclusion

# Future Work

---

[^music_industry_shift]: [An Economic Analysis of the Effects of Streaming on the Music Industry in Response to Criticism from Taylor Swift](https://scholarworks.uni.edu/cgi/viewcontent.cgi?params=/context/mtie/article/1154/&path_info=05_Zehr_music_streaming.pdf)
[^global_music_report]: [IFPI - Global Music Report](https://www.ifpi.org/wp-content/uploads/2024/04/GMR_2024_State_of_the_Industry.pdf)
[^spotify_report]: [2024 Earnings](https://newsroom.spotify.com/2025-02-04/spotify-reports-fourth-quarter-2024-earnings/?utm_source=chatgpt.com)
[^streaming_stats]: [Music Streaming Services Stats (2025)](https://explodingtopics.com/blog/music-streaming-stats)