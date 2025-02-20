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
### Further research & limitations
