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
To perform this experiment we set up an automated test script which starts up a text editor, types 200 characters while simulating human behavior, saves the file, and then proceeds to close the text editor. 
The energy consumption is measured through the entirety of this script.

### Tooling
We use EnergiBridge to monitor the energy consumption during this experiment.
Additionally, AutoHotkey is used to simulate typing behavior.

### Text editors
We decided to test the following text editors as they are popular options when a quick document is needed.
Vim
Notepad
Notepad++
Word

### Controlled Variables
We warm up the CPU by running a fibonacci sequence for 5 minutes. 
After every measurement we wait 1 minute to allow the CPU to cool down.
We ran the experiment 30 times per text editor to account for variability.
The order of measurements was shuffled to reduce systematic impact between measurements.

## Results
### Analysis

## Discussion
### Implication
### Further research & limitations

## References
## Replication
