---
author: Mirko Boon, Reeve Lorena, Gopal-Raj Panchu, Sotiris Vacanas
title: "Comparing Energy Consumption of Note-Taking Applications"
image: 
date: 28/02/2024
summary: |-
    In this experiment we compared the energy efficiency of different text-editing applications to evaluate which common text-editor is most efficient. We have found that notepad++ is significantly more efficient than alternatives like word and vs-code and recommend taking short notes in notepad++ when possible to reduce energy consumption.
---

# Comparing Energy Consumption of Note-Taking Applications
## Introduction
Everyone has to take notes sometime; university classes, business meetings, grocery lists, etc. Many people will start up their favorite text editor and start typing without giving it much further thought. Considering that just about everyone takes notes at least once a day, minor improvements in energy consumption can be cumulatively massive, which justifies looking into the energy consumption of different text editors. Therefore, this report researches the energy consumption of several text editors which may be used to quickly take notes on windows machines. The energy consumption of each text editor was measured in Joules using Energibridge while given the task of taking a short 50 character note in the editor. We hope this will result in recommendations regarding software which may be used to take quick notes in an energy efficient manner.

For this study, we selected text editors commonly used by EEMCS students. The selected text editors are:
- Notepad: A minimalist text editor that comes pre-installed on Windows. Its simplicity and lack of advanced features makes it a likely candidate for low energy consumption.
- Notepad++: An open-source text editor that offers more functionality than Notepad, such as syntax highlighting and plugin support. While still relatively lightweight, it may have a higher energy footprint compared to Notepad.
- Microsoft Word: A well known text editor that offers a wide range of advanced features for document creation, formatting, and collaboration. Its extensive feature set should cause it to be more energy-intensive than simpler editors.
- Visual Studio Code: A highly customizable code editor that is popular among developers. It is packed with features such as plugins, debugging tools, and interface customized to write software, making it likely to consume significantly more energy than simpler editors.


### Problem statement
This report aims to evaluate the energy consumption of several widely-used text editors on Windows machines, with the goal of identifying which software options are most energy-efficient for everyday note-taking. By understanding the energy demands of different text editors, we hope to provide recommendations that will help users, particularly students and professionals, make informed choices about which software to use based on its energy efficiency.

## Methodology
In this experiment we test the energy consumptions of various text editors while simulating natural typing behavior. 
To perform this experiment we set up an automated test script which starts up a text editor, types 50 characters while simulating human behavior, saves the file, and then proceeds to close the text editor. 
The energy consumption measurment begins after we launch the text editor and ends after we close it.

### Hardware
We run the experiment on a single computer witht he following specifications:

1. Processor: AMD Ryzen 7 5800H 
2. Graphics Card: Nvidia RTX 3070
3. RAM: 16GB
4. Storage: 1TB SSD
5. Operating System: Windows 11

### Tooling
We use EnergiBridge to monitor the energy consumption during this experiment.
Additionally, AutoHotkey is used to simulate typing behavior.

### Text editors
We decided to test the following text editors as they are popular options when a quick document is needed.
VS Code
Notepad
Notepad++
Word

### Controlled Variables
We warm up the CPU by running a fibonacci sequence for 5 minutes. 
After every measurement we wait 1 minute to allow the CPU to cool down.
We ran the experiment 30 times per text editor to account for variability.
The order of measurements was shuffled to reduce systematic impact between measurements.

### Setup
Before running the experiment we needed to ensure that the computer was in "Zen mode". This means that the only software that is running on our computer is the software whose energy consumption we want to measure.
In practice this is impossible, but we can limit the effect of background processes by ensuring the following:

- all applications are closed;
- all peripherals and other hardware are disconnected, for our experiment these included:
    - External monitor
    - Bluetooth keyboard
    - Bluetooth mouse
- turn off notifications;
- remove any unnecessary services running in the background (e.g., web server, file sharing, etc.);
- disconnect the computer from the internet since it's not required for our experiment

## Results

The results from our experiments are illustrated in the violin plot below:

![image](violinplotfinal.png)

The violin plot shows the total energy consumption for NotePad++, NotePad, MS Word and Visual Studio Code.

This violin plot was created after the rejecting outliers using the z-score. After performing the outlier rejection, we kept all the runs except for one run of the Visual Studio Code. Thus we kept 29 runs for Visual Studio Code and 30  runs for the rest of the editors.

After conducting the Shapiro-Wilks test to test for data normality, we get the following results: 

| Editor             | Is Data Normal? | P-Value |
|--------------------|-----------------|---------|
| NotePad            | False           | 0.00085 |
| NotePad++          | False           | 0.00012 |
| Microsoft Word     | False           | 0.012   |
| Visual Studio Code | True            | 0.067   |


Finally, we conducted the Welch's t-test to test for significance. The results of the Welch's t-test that we conducted are illustrated in the table below:

| Test                            | Is it Significant? | P-Value |
|---------------------------------|--------------------|---------|
| NotePad vs NotePad++            | ✅                  | 0.0003  |
| NotePad vs Visual Studio Code   | ✅                  | 0.0000  |
| NotePad vs MS Word              | ✅                  | 0.0000  |
| NotePad++ vs Visual Studio Code | ✅                  | 0.0000  |
| Visual Studio Code vs MS Word   | ✅                  | 0.0000  |

### Analysis
## Discussion
### Implication
From our experiments we can see a clear difference in the energy consumption of the more lightweight text editors (Notepad, Notepad++) compared to the heavier text editors. 
We do have to note the fact that data was not normally distributed. This could potentially be caused by processes running in the background with a variable amount of energy consumption.
Ofcourse heavier text editors include functionalities that the more lightweight editors do not posess, such as spelling and grammar checking, syntax highlighting for programming and more.
Our hypothesis was that these extended features could lead to a higher energy consumption. Our results prove this, with a p value < 0.005 for all comparisons when executing the Welch's t-test.
It is interesting that the energy consumption of Notepad++ is lower than Notepad. Notepad++ has a more extensive feature set than Notepad, but consumes less energy. 
This does indicate that more features does not necessiraly indicate a higher energy consumption.
Furthermore, there is a small caveat. While additonal features might lead to a higher power consumption, it might also allow the user to more quickly write their notes.
Features such as grammar and spelling checkers, table creation or even image insertion could cause a student to be able to save a lot of time writing their notes, leading to a smaller total energy consumption.

### Further research & limitations
While our study investigated the energy consumption of 4 text editors that are commonly used at EEMCS, there are many more text editors used. 
Further studies could investigate the energy consumption of other text editors, potentially also including web based editors.

Our experiment does not cover an entire workflow, which would also include opening the application and saving the file. 
The reason for the exclusion of these actions were the high variability of opening applications and difficulty with saving files using autohotkeys.
It could be the case that a much larger amount of energy is used when performing one of these actions compared to the typing part. 
Further research could take into accounts these additional actions.

While our experimental setup aimed to reduce external influences, the non-normal distributed data suggests this might not have been entirely effective.
Future research might be able to isolate the experiment even further, leading to more accurate results.
## Conclusion
We aimed to determine which text editor is most energy efficient for note taking on windows computers. This was done by comparing the four popular text editors Word, Notepad, Notepad++ and Visual studio code.
Our results indicate that Notepad++ has the lowest energy consumption, with Notepad following closely behind. Both of these text editors are considerably more lightweight, with a much smaller feature set.
Both Word and Visual Studio Code used a lot more energy, with Visual Studio Code using the most of all text editors investigated.

While the more heavy weight editors consume more energy, their additional functionallity might be worth their increased energy consumption. 
Selecting the best editor to use is thus highly dependent on if a user needs these exteded capabilities. 
Thus our reccommendation is that if the additonal features of the more heavy text editors are unneccesary, to use one of the more lightweight editors, preferably Notepad++.
## References
## Replication
