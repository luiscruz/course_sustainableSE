---
author: "Miroslav atanasov, Andreas Tsatsanis, Francisco Duque De Morais Amaro, Raluca Alexia Neatu, Thomas van der Boon"
title: "What is killing my computer? Measuring and recording background energy consumption"
image: "img/gX_template/cover.png"
summary: "While many energy profiling tools and methods are out there, there is little incentive for application developers to spend their time optimising for energy consumption. This widespread practice takes a toll on consumer hardware, and can result in premature end-of-life of otherwise capable devices. Our goal is to provide a lightweight tool to monitor and report energy consumption across all applications running on the user's system, in order to confront developers on the sustainability of their software."
paper: "../papers/g11_greenB.pdf"
source: "https://github.com/Hacking-Sustainably/dev"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 11
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---


# Submission
- [repository](https://github.com/Hacking-Sustainably/dev)
- [report](https://github.com/Hacking-Sustainably/report/blob/main/2026/papers/g11_greenB.pdf)


# `greenb` for monitoring energy consumption across all applications on your system
While many energy profiling tools and methods are out there, there is little incentive for application developers to spend their time optimising for energy consumption. This widespread practice takes a toll on consumer hardware, and can result in premature end-of-life of otherwise capable devices. Our goal is to provide a lightweight tool to monitor and report energy consumption across all applications running on the user's system, in order to confront developers on the sustainability of their software.

Sustainable aspect: by providing a comprehensible analysis of running apps on a user's system, we can make the users more aware of their battery consumption. 
If users notice that specific applications are consuming large amounts of energy, they will be tempted to find a replacement that won't impact their battery lifespan as much.
This can provide strong incentive for developers to optimize their applications to consume less energy. 
On a global scale, even small energy optimisations can have a big impact.


## Research Directions

### Monitoring techniques
- periodic sampling
- continuous sampling
- using OS primitives
- using hardware primitives?
- building on top of existing applications
- vendor-provided applications: how they do it?
- third-party applications and their implementations

### Data management
- what data are we collecting
- what data are we storing
- how to store all the monitoring data
- data size estimates

### Data analysis and presentation
- what can the average user learn from our data
- how can we layer the data so:
    - it isn't overwhelming for average users
    - can be informative for more interested users
- what can developers learn from our data

### Impact analysis
- what can we do to encourage users to speak up










