---
author: "Calin Georgescu, Nick van Luijk, Vincent Ruijgrok, Radu Andrei Vasile, Arnas Venskūnas"
title: "Patching software inefficiencies"
# image: "img/gX_template/cover.png"
summary: |
    This paper explores a novel set of guidelines to practically apply energy-saving optimizations at runtime for desktop applications. Currently, many tactics exist to optimize energy efficiency, but a central, practical, and industry-oriented set of guidelines is lacking. To address this gap, we conduct an investigation of prior research describing profiler techniques and academic optimization methods. Then, based on the research, we develop and incorporate a novel solution of machine learning-based reverse engineering and devise a set of general practical guidelines for desktop application engineers to follow. This, in turn, should reduce energy consumption stemming from insufficient optimization in desktop applications. We then validate this by applying the workflow to the "Scrap Mechanic" video game, showing a significant reduction in CPU usage as well as an average of 10-15% savings in energy consumption, proving the efficiency of the suggested framework.
paper: "../papers/g3_patching_software_inefficiencies.pdf"
source: "https://github.com/TechnologicNick/SMInjector/tree/main/PluginDevFolder/Scraptifine"
# website: https://luiscruz.github.io/course_sustainableSE/
# video: https://luiscruz.github.io/course_sustainableSE/
group_number: 3
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

Scraptifine, the Scrap Mechanic mod that we developed to demonstrate the practical application of our guidelines, can be found at [https://github.com/TechnologicNick/SMInjector/tree/main/PluginDevFolder/Scraptifine](https://github.com/TechnologicNick/SMInjector/tree/main/PluginDevFolder/Scraptifine).

Our fork of Rikugan, a reverse-engineering agent for IDA Pro and Binary Ninja with support for ChatGPT subscriptions, can be found at [https://github.com/TechnologicNick/Rikugan](https://github.com/TechnologicNick/Rikugan).
