---
author: Mitali P, Pia A, David Vos
title: Is Notion "Greener" on Web browser or Desktop?
date: 27/02/2024
summary: |-
Ever wondered how much energy is consumed by some of the softwares that we use often ? We explore the energy consumption of one such software - Notion , something one might find using quite often for organising notes. 
Primarily we see if its energy-efficient to use Notion on desktop or on Web Browser. 
---
Note-taking softwares are becoming increasingly feature-packed.We use various note taking softwares often, but are we saving more energy by using it on desktop or running it on the web ? Even though Notion provides similar features to the end user, using their native version or Web counterpart might lead to different levels of energy consumption and performance. 
In this blogpost we asses the energy consumption between the desktop version and the web version of Notion.

At TU Delft many students create, collaborate and organise their notes on Notion. This can be attributed to the fact that Notion allows for creating databases, integration with google drive, github and its use of KaTeX library to render math equations.

While sustainiabilty might not be the integral aspect of the Notion software we can make it an afterthought and use it in a manner where we reduce overall energy consumption or save our laptops energy.

Methodology :
We conducted the same experiment (login to logout) on two different modes of operation of notion, one mode being desktop and the other mode being notions web application on chrome web browser. We are using the cornell note system template as a use case for both the modes. We have tried to include all the basic features that we think users usually use on notion in the workflow pipeline.
The experiment flow for interaction with Notion is as follows:
open Desktop app on fullscreen -> login using google sign in option(we created a dummy account for this experiment) -> create a new page using the cornell system template -> write a page title with some basic text -> make a todo list -> write some notes-> write a math equation -> write a piece of code -> check a todo -> logout
Similar flow was followed for the web appliation too.
Each iteration of the experiment is around 3 minutes. 
So the total time for the whole experiment is about 3 hours. 

We ran an automated script to open notion on desktop and the web version on chrome.
Each of it was run 30 times and to prevent the order of experiments influencing the resulting measurements, the experiments were randomly shuffled.
For each experiment, we took the following measurements: 
elapsed measurement time(ms) and System_Power(Watts) which we convereted to Joules. 

Experimental set up :
We conducted the experiments on MacBook Air M1 Laptop with 8GB RAM running macOS Sanoma 14.2.1 (23C71). The specific software used for the experiment is:
| Software      | Vesrion |
|---------------|---------|
| Notion Desktop| 3.2.1     |
| Google Chrome Browser| 122.0.6261.69     |

The energy consumption was measured using [EnergiBridge](https://github.com/tdurieux/EnergiBridge)

Before executing the experiments it is important to record the state of the system under test so that the state can be kept as consistent as possible between experiments. In addition to the hardware and software specifications above, we made sure that the laptop was in the following state to minimize confounding factors:

* Stable Wifi6 Connection with average throughput of 250mbps.
* Notifications turned off 
* Power cable plugged in 
* Screen brightness set to 100 %
* No applications/programs/services running in the background. 

Since hardware temperature affects the energy consumption among the experiment runs which impacts the results, we set up a warm up routine with a dummy task of calculating fibonnaci sequence for 30 seconds to minimise the temperature difference. 
The experiment structure was as follows :

1. warm up CPU
2. Shuffle and run 60 iterations(30 for desktop experiment and 30 for chrome broswer experiment each)
    1. Start measuring 
    2. Start Notion Workflow (mentioned above) using an automated script 
    3. Stop Notion Workflow and Logout(also automated)
    4. Stop Measuring
    5. Wait for 30 seconds
    6. Delete the current created note page
    7. Wait for 30 seconds


Replication:
The code to replicate the experiments can be setup using [GithubNotionSSE] (https://github.com/mitalipatil99/SSE_notion)
For the setup we have created a dummy google account for Notion login , the details of which are in the GitHub repository.
To get the set up running on a Mac: 
1. Install Notion on Desktop
2. Set up the dummy google account on chrome , each experiment will login and logout using that ID. 
3. Set up [EnergiBridge](https://github.com/tdurieux/EnergiBridge)
4. Run the main python file 



Results :
From the Results we see that the energy consumption on desktop is far higher than on the web browser. This is surprising as Native applications are seen to use less energy. 


Graphs:



discussion:
practical implications.

Limitation:
worth noting the response time on web vs desktop ,
accesibililty to online vs offline features

Conclusion: