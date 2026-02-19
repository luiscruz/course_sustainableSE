---
author: Konstantinos Syrros, Samuel van den Houten, Sydney Kho, Alessandro Valmori
group_number: 11
title: "A Study on the Energy Efficiency of Minecraft Shaders"
image: "img/g11_minecraft_shaders/banner.png"
date: 27/02/2026
summary: |-
  Minecraft is a popular sandbox video game that allows players to build and explore virtual worlds. Shaders are modifications that enhance the graphics and visual effects of the game, but they can also increase energy consumption. In this project, we will analyze the energy efficiency of Minecraft shaders by measuring the energy consumption of the game with and without shaders, and across different shader packs. The study will provide insights into the trade-offs between visual quality and energy efficiency, helping players make informed decisions about which shaders to use based on their hardware capabilities and energy consumption preferences.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

Minecraft is an extremely popular sandbox video game that allows players to build and explore virtual worlds. It has a very extensive and moddable ecosystem, and many developers have created content and performance mods to enhance the gaming experience. One of the most popular types of modifications are shaders, which are used to improve the graphics and visual effects of the game, vastly improving the experience for players with high-end hardware.

Shaders add features such as dynamic lighting, shadows, reflections, complex environmental animations, and more. However, as it is expected, these improvements require more computational resources, especially from the GPU, and can lead to a significant increase in energy consumption, when compared to the vanilla version of Minecraft. Further, different shader packs can differ in the extent of the graphical improvements they provide, and thus in their energy consumption varies.

In this project, we will analyze the energy efficiency of Minecraft shaders by measuring the energy consumption of the game with and without shaders, and across different shader packs. The study will provide insights into the trade-offs between visual quality and energy efficiency, and will help players make informed decisions about which shaders to use based on their hardware capabilities and energy consumption preferences.

---
## ❓ Research Questions

In order to stay in track and within scope of the goals of this exploration, we have defined the following research questions:

**RQ1.** How does the energy consumption of Minecraft change when using shaders compared to the vanilla version of the game?

**RQ2.** How does the energy consumption vary across different shader packs, and what are the factors that contribute to these differences?

---
## 🔬 Methodology

For this exploration, we will be using a dedicated Linux machine for testing, which is equipped with a high-end Nvidia GPU and AMD CPU to ensure that we can run Minecraft with shaders without performance bottlenecks. We will be using the [EnergiBridge](https://github.com/tdurieux/energibridge) software to measure the energy consumption of the CPU and GPU.

The latest version of Minecraft will be used, on the latest supported Java version. Since Vanilla Minecraft does not support shaders or mods by default, a mod loader will be needed. We will be using the [Fabric Mod Loader](https://fabricmc.net/) for this purpose, which is a popular and modern modding platform for Minecraft. To install shaders, we will be using the [Iris](https://irisshaders.dev/) mod. For reproducibility of the tests, we will be using the [Replay Mod](https://www.replaymod.com/), which allows taking snapshots of gameplay and re-rendering them to replay them. This way, we will have a consistent game scenario for each test, which we can re-render with the different shaders. The above setup will be considered the "vanilla" setup.

A base test will be conducted to measure the energy consumption of the vanilla setup, without any shaders. Then, we will select from a set of popular shader packs (list TBD) and make tests using each individual pack, collecting consumption data.