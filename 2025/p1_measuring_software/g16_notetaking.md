---
author: Mirko Boon, Reeve Lorena, Gopal-Raj Panchu, Sotiris Vacanas
title: "Comparing Energy Consumption of Note-Taking Applications"
image: 
date: 28/02/2024
summary: |-
 TODO SUMMARY
---

# Comparing Energy Consumption of Note-Taking Applications
## Introduction
Everyone has to take notes sometime; university classes, business meetings, grocery lists, etc. Many people will start up their favorite text editor and start typing. Considering that just about everyone takes notes at least once a day, minor improvements in energy consumption can be cumulatively massive. Therefore, this report researches the energy consumption of several text editors which may be used to quickly take notes on windows machines. We hope this will result in recommendations regarding software which may be used to take quick notes in an energy efficient manner.
### Problem statement


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
### Analysis

## Discussion
### Implication
### Further research & limitations

## References
## Replication
