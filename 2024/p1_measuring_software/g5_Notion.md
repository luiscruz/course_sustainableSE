---
author: Mitali P, Pia A, David V
title: Is Notion "Greener" on Web browser or Desktop?
date: 27/02/2024
summary: |-
Ever wondered how much energy is consumed by some of the softwares that we use often ? We explore the energy consumption of one such software - Notion , something one might find using quite often for organising notes. 
Primarily we see if its energy-efficient to use Notion on desktop or on Web Browser. 
---
Note-taking software is becoming increasingly feature-packed. We use various note-taking software often, but are we saving more energy by using it on the desktop version or running it on the web? Even though Notion provides similar features to the end user, using their native version or Web counterpart might lead to different levels of energy consumption and performance. 
In this blog post, we asses the energy consumption between the desktop version and the web version of Notion.

At TU Delft many students create, collaborate and organise their notes on Notion. This can be attributed to the fact that Notion allows for creating databases, integration with Google Drive, GitHub and its use of LaTeX library to render math equations.

While sustainability might not be the integral aspect of the Notion software we can make it an afterthought and use it in a manner where we reduce overall energy consumption or save our laptops energy.

## Methodology 
We conducted the same experiment (login to logout) on two different modes of operation of notion, one mode being desktop and the other mode being notions web application on Chrome web browser. We are using the Cornell note system template as a use case for both modes. We have tried to include all the basic features that we think users usually use on Notion in the workflow pipeline.
The experiment flow for interaction with Notion is as follows:
open Desktop app on fullscreen -> login using google sign in option(we created a dummy account for this experiment) -> create a new page using the Cornell system template -> write a page title with some basic text -> make a todo list -> write some notes-> write a math equation -> write a piece of code -> check a todo -> logout
A similar flow was followed for the web application too.
Each iteration of the experiment is around 3 minutes. 
So the total time for the whole experiment is about 3 hours. 

We ran an automated script to open Notion on the desktop and the web version on Chrome.
Each of them was run 30 times and to prevent the order of experiments influencing the resulting measurements, the experiments were randomly shuffled.
For each experiment, we took the following measurements: 
elapsed measurement time(ms) and System_Power(Watts) which we convereted to Joules. 

## Hardware set up 
We conducted the experiments on a MacBook Air M1 Laptop with 8GB RAM running macOS Sanoma 14.2.1 (23C71). The specific software used for the experiment is:
| Software      | Vesrion |
|---------------|---------|
| Notion Desktop| 3.2.1     |
| Google Chrome Browser| 122.0.6261.69     |

The energy consumption was measured using [EnergiBridge](https://github.com/tdurieux/EnergiBridge)

Before executing the experiments it is important to record the state of the system under test so that the state can be kept as consistent as possible between experiments. In addition to the hardware and software specifications above, we made sure that the laptop was in the following state to minimize confounding factors:

* Stable Wifi6 Connection with an average throughput of 250mbps.
* Notifications turned off 
* Power cable plugged in 
* Screen brightness set to 100 %
* No applications/programs/services running in the background. 

Since hardware temperature affects the energy consumption among the experiment runs which impacts the results, we set up a warm-up routine with a dummy task of calculating the Fibonacci sequence for 30 seconds to minimise the temperature difference. 
The experiment structure was as follows :

1. Warm up CPU
2. Shuffle and run 60 iterations(30 for desktop experiment and 30 for chrome browser experiment each)
    1. Start measuring 
    2. Start Notion Workflow (mentioned above) using an automated script 
    3. Stop Notion Workflow and Logout(also automated)
    4. Stop Measuring
    5. Wait for 30 seconds
    6. Delete the current created note page
    7. Wait for 30 seconds


## Replication
The code to replicate the experiments can be set up using [GithubNotionSSE] (https://github.com/mitalipatil99/SSE_notion)
For the setup, we have created a dummy Google account for Notion login, the details of which are in the GitHub repository.
To get the set up running on a Mac: 
1. Install Notion on Desktop
2. Set up the dummy Google account on chrome, each experiment will log in and logout using that ID. 
3. Set up [EnergiBridge](https://github.com/tdurieux/EnergiBridge)
4. Run the main Python file 


## Results 

The data produced from the experiments was analyzed by plotting the energy consumption for each experiment. The data was plotted using a violin plot to show the distribution of the data and a time series plot to show the energy consumption over time.
After producing the violin plot, it was observed that there were some outliers in the data for the web experiment (seen in Figure 1). 

![violin_plot_with_outliers.png](..%2Fimg%2Fp1_measuring_software%2Fg5_Notion%2Fviolin_plot_with_outliers.png)

*Figure 1: Violin plot of energy consumption (J) with outlier data.*

The time series plot (seen in Figure 2) also showed the presence of outliers in the data.

![time_series_with_outliers.png](..%2Fimg%2Fp1_measuring_software%2Fg5_Notion%2Ftime_series_with_outliers.png)

*Figure 2: Time series plot of power consumption(W) with outlier data sets*

The outlier data sets appear to have a near-constant energy consumption over time, which is not consistent with the rest of the data. 
Furthermore, the energy consumption of the outlier data sets is significantly higher than the rest of the data for one of the outliers and lower for the other one.
Why these outliers are present in the data is not clear, especially as the power usage reported by the outliers has a very low variance.

### Without Outliers
After removing the outliers from the data, the violin plot (seen in Figure 3) and time series plot (seen in Figure 4) were produced again.
Furthermore, the min, max, average and variance were calculated for both experiments. The results are shown in Figure 5.

![violin_plot.png](..%2Fimg%2Fp1_measuring_software%2Fg5_Notion%2Fviolin_plot.png)

*Figure 3: Violin plot of energy consumption (J) without outlier data.*

The violin plot for the web experiment shows a normal distribution, albeit with a very low variance.
The violin plot for the desktop experiment appears to show a corrupted distribution, with a very high variance.
We observe that from a first glance, it is very clear that the desktop version of Notion consumes more energy than the web version.

![time_series.png](..%2Fimg%2Fp1_measuring_software%2Fg5_Notion%2Ftime_series.png)

*Figure 4: Time series plot of power consumption(W) without outlier data.*

The time series plots for both experiments show a correlated pattern, where the first 50 seconds experience a large oscillation in power consumption.
We also observe a peak around the 105 sec mark for both experiments. Lastly, there also appears to be a peak at the end of every experiment run.

![notion_metrics.png](..%2Fimg%2Fp1_measuring_software%2Fg5_Notion%2Fnotion_metrics.png)

*Figure 5: Metrics for the Notion experiments without outliers.*
discussion:

Our metrics confirm what was already clear from the plots. The desktop application has a higher energy consumption, while at the same time having a vastly larger variance.

Moreover, after comparing the calculations with a Welch t-test with a p-value < 0.05, we get the following results:
t= 43.1496, standard error of difference = 3.716 with p-value < 0.0001 which means that the difference is not by chance and is extremely statistically significant. 
Thus we can reject our null hypothesis and conclude that the desktop is way less energy-efficient than the web version. 


## Discussion 

The differences are pretty overwhelming for the same use case. Because our distribution is not normal we cannot confidently say that the errors that affected the desktop measurements were equally affecting the web measurements. Some of the potential reasons could be:
1. Error in automated experimental  execution
2. Unusual task being run by the system despite all background processes and notifications being turned off 
3. Since we are relying on third-party software(Energibridge) to collect the data, we cannot ensure its accuracy.

After we remove the outliers we can see a large interquartile range for the desktop box plot which implies a significant variability in the energy consumption and less consistency in energy usage across different runs.
This could stem from syncing and background processes such as syncing data across devices (Note: Notion run on desktop was Online). It can also be attributed to the software code, performance optimisation can lead to fluctuations in energy usage. 


## Limitations and Issues

Limitations present themselves in these experiments in various forms.

1. The Notion software interacts with a remote system, making the power measurements non-deterministic.
2. Outliers present themselves in the data in the form of two data sets with very consistent power consumption, albeit with a higher and lower consumption than the other experiments. How these outliers came to be is not clear, as it could be due to a variety of reasons (e.g. powerBridge software).
3. As the application has to interact via the internet it is subject to network latency and throughput. Creating variations in the energy consumption.


## Conclusion:
could be better to use web , only works when online , data is synched and stored automatically. 