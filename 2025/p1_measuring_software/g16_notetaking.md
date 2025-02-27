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

### Setup

#### Hardware
We run the experiment on a single computer witht he following specifications:

1. Processor: AMD Ryzen 7 5800H 
2. Graphics Card: Nvidia RTX 3070
3. RAM: 16GB
4. Storage: 1TB SSD

#### Software
The following text editors will be tested:
1. VS Code
2. Notepad
3. Notepad++
4. Word

We have chosen these editors as they are widely available and very commonly used by students.
Each editor is installed with default settings and are running on Windows 11.

### Tooling
EnergiBridge will be used to measure the energy consumption of the computer during the experiment. In addition, we will use Autohotkey scripts to simulate launch and close the editors as well as to simulate keystrokes.

### Controlled Variables

CPU temperature must be similar for all measurments to avoid skewing the results. This is ensured by letting the CPU cool down for 1 minute between measurments.
The experiment will be run 30 times per editor to account for variability in measurments.
The order of measurements will be random to reduce systematic impact between measurmenets.
There will be no interaction with the computer while running the computer to ensure

### Experiment

#### Setup
Before running the experiment we need to ensure that the computer is in "Zen mode". This means that the only software that is running on our computer is the software whose energy consumption we want to measure.
In practice this is impossible, but we can limit the effect of background processes by ensuring the following:

- all applications are closed;
- all peripherals and other hardware are disconnected, for our experiment these included:
    - External monitor
    - Bluetooth keyboard
    - Bluetooth mouse
- turn off notifications;
- remove any unnecessary services running in the background (e.g., web server, file sharing, etc.);
- disconnect the computer from the internet since it's not required for our experiment

#### Warmup 

Before beginning the experiment we perform a warmup procedure. This procedure is used to warmup the CPU to ensure fairness throughout the experiment as starting with a cool CPU which later warms up can skew the results.
This is because having heat increases the resistance of an electrical circuit meaning more energy is required for the same amount of work. Therefore beginning with an already hot CPU helps prevent this.

Our warmup procedure consists of running multiple fibonacci sequences for 5 minutes on all CPU cores.


#### Running the experiement

After ensuring the computer is in "Zen mode" and that our CPU is warm we can begin running our experiment. The experiment performs the following actions:

1. Launches an editor
2. Begins measuring energy consumption using Energi Bridge
3. Types 50 characters
4. Closes the editor
5. Stops measuring energy consumption
6. Wait for 1 minute
7. Repeat

The aforementioned sequence is repeated 30 times for each of the four editors we selected making a total of 120 measuremenets.

## Results

The results from our experiments are illustrated in the violin plot below:

![image](violinplotfinal.png)

The violin plot shows the total energy consumption for NotePad++, NotePad, MS Word and Visual Studio Code.

In order to make our data 



### Analysis
## Discussion
### Implication
### Further research & limitations

## References
## Replication
