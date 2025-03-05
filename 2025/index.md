---
layout: default
hide_from_navbar: false
redirect_from:
  - /
title: 2025
project-1:
  deadline: 28-02-2025
project-2:
  deadline: 04-04-2025
  presentation: 11-04-2025
---

# Sustainable Software Engineering 🌱
Edition of 2024/25<br/>
[MSc Computer Science] and [MSc Data Science and Artificial Intelligence Technology], [Delft University of Technology]


**Sustainable Software Engineering** is an overarching discipline that addresses the long-term consequences of designing, building, and releasing a software project.
By definition, sustainability covers five main perspectives: **environmental**, **social**, **individual**, economic, technical.
This course focuses on the first three.

![Sustainability Domains](./img/domains.svg){: style="display:block; margin-left:auto; margin-right:auto" width="260px" }

Software Engineering (SE) has long addressed sustainability by **narrowing it down to economical and technical sustainability**.
However, our society is facing major sustainability challenges that can no longer be overlooked by software engineers and computer scientists.
It was estimated that, **by 2040, the ICT sector will contribute to 14% of the global carbon footprint**. Hence, environmental, social, and individual ought to be part of the equation when it comes to design, build, and release software systems.
The problem is far from simple, but **we need expert computer scientists** to bring sustainability into the core values of the next generation of tech-leading organisations.

This course covers a set of competencies needed to leverage sustainable software systems.
It has a **strong component on Green SE**, covering techniques to measure and improve the energy-efficiency at any stage of the software lifecycle.
Students learn **state-of-the-art practices on energy efficiency** and apply them in real software projects. Moreover, the course will cover core principles of **empirical software engineering**, and **social and individual sustainability**.

## Organisation

-------|----------|
**Course code**       | [CS4575]
**Brightspace 🔒**    | <https://brightspace.tudelft.nl/d2l/home/680663>
**Instructors**       | [Luís Cruz], [Carolin Brandt], [Enrique Barba Roque]
**Schedule**          |	Mondays 8:45, Wednesdays 10:45, Thursdays 10:45. 🔗 [MyTimetable].
**Mattermost**        | [Sign Up Link](https://mattermost.tudelft.nl/signup_user_complete/?id=1nj9tk6usjf8xmsws8wpq3s5uy&md=link&sbr=su).
**ECTS** 	            | 5.0
**Quarter**           | Q3
**Format**            | Classes are optimised for in-person attendance.
**Examination type**  | Group Project 1 (40%); Group Project 2 (60%).
**Target audience**   |	Students of the [MSc Computer Science] and the [MSc Data Science and Artificial Intelligence Technology].
**Requirements** 	    | - Intermediate understanding of OOP languages;<br/> - Basic understanding of data analysis techniques.

[CS4575]:https://www.studiegids.tudelft.nl/a101_displayCourse.do?course_id=70145


## Learning Objectives

By the end of this course you will be able to:

- LO1. Explain the fundamental sustainability principles and their relevance to software engineering.
- LO2. Assess the energy consumption of software systems using measurement and testing techniques.
- LO3. Create actionable strategies to address sustainability issues within software organisations.
- LO4. Evaluate and compare different solutions for sustainable software systems based on their effectiveness in achieving sustainability goals and their potential impact on various stakeholders.

## Outline

**⚠️ Please note:** The following outline is subject to changes; Recordings are available through Collegerama.


 Class | Week| Summary
-------| ----|----------|
 1     | 1   | **Lecture.** Course introduction. Sustainable Software: What, Why and How.<br/>[📊Slides][slides01]
 2     | 1   | **Lab.** Measuring software energy consumption. Introduction to [Project 1](#project1).<br/>[📊Slides][slides02]
 3     | 1   | **Lecture.** Green Software Engineering — Part I: Scientific guide for reliable energy measurements.<br/>[📊Slides][slides03]
 4     | 2   | **Lecture.** Social and Individual Sustainability.<br/>[📊Slides][slides04],[Workbook][susafwb]
 6     | 2   | **Lecture.** Green Software Engineering — Part II: units of energy.<br/>[📊Slides][slides05]
 5     | 2   | **Project.** [Project 1](#project1) - steering meeting and formative assessment.
 7     | 3   | **Lecture.** Green Software Engineering — Part III: Energy efficiency in mobile computing; carbon-aware data centres.<br/>[📊Slides][slides07]
 8     | 3   | **Lecture.** Green AI.<br/>[📊Slides][slides08]
 9     | 3   | **Project.** [Project 1](#project1) - steering meeting.
       | 3   | ⏰ Deadline for [Project 1](#project1) Friday, Feb 28.
 10    | 4   | **Project.** [Project 2](#project2) - Description and kick-off.<br/>[📊Slides][slides10]
 11    | 4   | **Guest Lecture (Mar 5).** Neuromorphic Computing, [Nergis Tömen]. <br/>[📊Slides][slides11] 
       | 5   | **Project 2 - steering meeting 1.**
       | 6   | **Project 2 - steering meeting 2.**
       | 7   | **Project 2 - steering meeting 3.**
       | 8   | **Project 2 - steering meeting 4.**
 19    | 8   | ⏰ Deadline [Project 2](#project2) – April 4.
 20    | 9   | Presentation [Project 2](#project2) – April 11.
 
## Assignments

Below the description of each project.

### 🛠 **Project 1** – Measuring Software Energy Consumption
{: #project1}

- Goal: Compare energy consumption in common software use cases.
  - Examples:
    - Different versions of the same app;
      - Same use case but different apps
      - Same version, same app, but different user settings (e.g., enable/disable GPU optimisation)
      - Same version, same app, but different running environment
- Blog-style report (markdown, approx 2500 words).
  - Bonus if you can automate the experiment and there is a replication package.
- Submission by pull request to the website. Instructions [here](/course_sustainableSE/2025/p1_measuring_software/).
  - Blog-style report (markdown, approx 2500 words).
  - Replication package.
- **Weight in final grade**: 40%
- **Deadline** Friday, Feb 28



### 🛠 **Project 2** – Hacking Sustainability
{: #project2}

- **Goal:** Solve a Sustainable Software Engineering problem.
  - Identify/Describe 1 problem that should be fixed to help enabling sustainability in the software engineering industry/community. You can reuse ideas from the slides.
  - Propose a solution. It can be a tool, framework, guidelines, etc.
  - Implement the solution.
  - Validation. (Depending on the idea)
  - Dissemination/social impact. (E.g., solution should be open source, welcome contributors, post on social media, tool website, available in package managers, etc.)
- **Deliverables.**
  - Paper-like article. (Min 4 pages, max 10)
  - Online git repo with open source codebase and/or replication package.
  - Presentation: 5 min + 5min Q&A
- **Weight in final grade**: 60%
- **Steering meeting/formative assessments**: Every week from week 5 to 9.
- **Deadline** Friday, April 4.
- **Presentation** Friday, April 11.
- Submission by pull request to the website. Instructions [here](/course_sustainableSE/2025/p2_hacking_sustainability/).



## Further reading (optional)

- Cruz, L., de Bekker, P. (2023) [All you need to know about Energy Metrics in Software Engineering](https://luiscruz.github.io/2023/05/13/energy-units.html).
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). Experimentation in software engineering. Springer Science & Business Media.
- Cruz, L., & Abreu, R. (2017, May). Performance-based guidelines for energy efficient mobile applications. In 2017 IEEE/ACM 4th International Conference on Mobile Software Engineering and Systems (MOBILESoft) (pp. 46-57). IEEE.
- Cruz, L., & Abreu, R. (2019). [Catalog of energy patterns for mobile applications](https://arxiv.org/abs/1901.03302). Empirical Software Engineering, 24(4), 2209-2235.
- Stol, K. J., & Fitzgerald, B. (2018). The ABC of software engineering research. ACM Transactions on Software Engineering and Methodology (TOSEM), 27(3), 1-51.
- Spinellis, Diomidis (2017). [The Social Responsibility of Software Development](https://ieeexplore.ieee.org/document/7888390). IEEE Software.

## Interesting pointers

- [EnergiBridge](https://github.com/tdurieux/energibridge) - Tool to measure energy consumption from almost any device.
- [Principles of Sustainable Software Engineering](https://principles.green)
- [CAT community](https://ClimateAction.tech)
- [Energy Patterns for Mobile Apps](https://tqrg.github.io/energy-patterns/).
- [Branch Magazine](https://branch.climateaction.tech).
- [Green Software Lab](https://greenlab.di.uminho.pt)
- [Website Carbon Calculator](https://www.websitecarbon.com)
- [Carbon Tracker](https://github.com/lfwa/carbontracker)
- [Greenpeace — Europe's Green Recovery As if the planet mattered](https://www.greenpeace.de/sites/www.greenpeace.de/files/publications/20201022_greenrecovery_f_es.pdf)
- [Green TU](https://www.tudelft.nl/sustainability/get-involved/greentu/)

[Delft University of Technology]: https://www.tudelft.nl
[MSc Computer Science]: https://www.tudelft.nl/onderwijs/opleidingen/masters/cs/msc-computer-science
[MSc Data Science and Artificial Intelligence Technology]: https://www.tudelft.nl/onderwijs/opleidingen/masters/dsait/msc-data-science-and-artificial-intelligence-technology
[Luís Cruz]: https://luiscruz.github.io
[Carolin Brandt]: https://carolin-brandt.de
[Enrique Barba Roque]: https://ebarba.com
[CS4575]:https://www.studiegids.tudelft.nl/a101_displayCourse.do?course_id=70145

[Nergis Tömen]:https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/intelligent-systems/pattern-recognition-bioinformatics/computer-vision-lab/people/nergis-toemen

[MyTimetable]: https://mytimetable.tudelft.nl/link?timetable.id=TimeEdit!timeedit_module!INJTINBRGU

[slides01]: https://surfdrive.surf.nl/files/index.php/s/wzc2rUchVG2MQrK
[slides02]: https://surfdrive.surf.nl/files/index.php/s/mQpQ7XoIYPqjlun
[slides03]: https://surfdrive.surf.nl/files/index.php/s/V8f66pd7V7sQYx6
[slides04]: https://surfdrive.surf.nl/files/index.php/s/3ZNl75feJ4Oa91e
[susafwb]: https://www.suso.academy/en/sustainability-awareness-framework-susaf/
[slides05]: https://surfdrive.surf.nl/files/index.php/s/UXWEHiQl4ntCxzX
[slides07]: https://surfdrive.surf.nl/files/index.php/s/3XkUS6ozbapMv5u
[slides08]: https://surfdrive.surf.nl/files/index.php/s/nY86MJyb2NrbBnm
[slides10]: https://surfdrive.surf.nl/files/index.php/s/EFjQtlgHt6tRisi
[slides11]: https://surfdrive.surf.nl/files/index.php/s/y4aua5CQ8IW7vQL
