---
layout: default
hide_from_navbar: false
redirect_from:
  - /
title: 2023
---

# Sustainable Software Engineering 🌱
Edition of 2022/23<br/>
[MSc in Computer Science], [Delft University of Technology]


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

**Course code**       | [CS4415]
**Brightspace 🔒**    | <https://brightspace.tudelft.nl/d2l/home/499381>
**Instructors**       | [Luís Cruz], [June Sallou]
**Schedule**          |	Tuesdays 8:45, Thursdays 8:45, Fridays 10:45. 🔗 [MyTimetable].
**Mattermost**        | 🔗 [Sign-up link](https://mattermost.tudelft.nl/signup_user_complete/?id=nob1cyhto3nstp7muqhahs95nh)
**Zoom link**        | Link shared on [Brightspace](https://brightspace.tudelft.nl/d2l/home/499381).
**ECTS** 	            | 5.0
**Quarter**           | Q3
**Format**            | Classes are optimised for in-person attendance;<br/>Online attendance is allowed in most classes.
**Examination type**  | Project 1 - Essay (30%); Project 2 - Software Repository and Essay (60%); Presentations (15%).
**Target audience**   |	Students of the [M.Sc. in Computer Science].
**Requirements** 	    | - Intermediate understanding of OOP languages;<br/> - Basic understanding of data analysis techniques.


## Learning Objectives

By the end of this course you will be able to:

- LO1. Measure software energy consumption.
- LO2. Automate carbon-awareness in software development.
- LO3. Discuss sustainability principles.
- LO4. Solve sustainability issues in real software projects.
- LO5. Propose innovative strategies to monitor software sustainability.

## Outline

**⚠️ Please note:** **Recordings are only available to the students** because they are not edited and may include students' interactions.


 Class | Week| Summary
-------| ----|----------|
 1     | 1   | **Lecture.** Course introduction. Sustainable Software: What, Why and How. [📊Slides][slides01] [🎥Recording][recording01] {% include tag.html name="hybrid" %}
 2     | 1   | **Lecture.** Social and Individual Sustainability in SE. {% include tag.html name="hybrid" %} <!-- [📊Slides][slides02] -->
 3     | 1   | **Lab.** Measuring software energy consumption. Introduction to [Project 1](#project1). <!-- [📊Slides][slides05] [🎥Recording][recording05]  -->{% include tag.html name="hybrid" %}
 4     | 2   | **Presentation.** Present a summary of a research paper on Social and Individual SE Sustainability. {% include tag.html name="in-person" %}
 5     | 2   | **Lecture.** Green Software Engineering — Part I: units of energy. <!-- [📊Slides][slides06] [🎥Recording][recording06] --> {% include tag.html name="hybrid" %}
 6     | 2   | **Project.** Project 1 - steering meeting and formative assessment. {% include tag.html name="online/in-person" %}
 7     | 3   | **Lecture.** Green Software Engineering — Part II: Scientific guide for reliable energy measurements. <!-- [📊Slides][slides08] [🎥Recording part2][recording08] --> {% include tag.html name="hybrid" %}
 8     | 3   | **Lecture.** Green Software Engineering — Part III: Energy efficiency in mobile computing; carbon-aware data centres. <!-- [📊Slides][slides09] [🎥Recording][recording09] --> {% include tag.html name="hybrid" %}
 9     | 3   | **Project.** Project 1 - steering meeting. {% include tag.html name="online/in-person" %}
 10    | 4   | **Lecture.** Approximate Computing for Green Software. <!-- [📊Slides][slides10]. [🎥Recording][recording10] --> {% include tag.html name="hybrid" %}
 11    | 4   | **Lecture.** Green AI. <!-- [📊Slides][slides11]. [🎥Recording][recording11] --> {% include tag.html name="hybrid" %}
 12    | 4   | **Guest Lecture.** TBA {% include tag.html name="hybrid" %} 
 13    | 5   | **Project.** Project 2 - Description and kick-off. {% include tag.html name="hybrid" %}
 14    | 5   | **Guest Lecture.** TBA {% include tag.html name="hybrid" %} 
 15    | 5   | **Steering Meeting 1.** {% include tag.html name="hybrid" %}
 16    | 6   | **Steering Meeting 2.** {% include tag.html name="hybrid" %}
 17    | 7   | **Steering Meeting 3.** {% include tag.html name="online" %} Project 2 1st Deadline (Mar 31).
 18    | 8   | Holidays
 19    | 9   | Project 2 Final Deadline (Apr 14).
 20    | 10  | Presentation. (April 19)
 
## Assignments

Below the description of each project.

### 📚 Literature Review

- Groups of `TBD`
- Select 1 academic paper that talks about social or individual sustainability in the context of software engineering.
  - Google Scholar, DBLP
- Double check with the lecturer whether your selected paper is good enough (use mattermost).
- Write a short summary about it (min 200 words; max 500).
- Prepare a presentation for class 4 (Feb 21).
  - 7 min + 3 min Q&A.
- Presentation is 7.5% of the grade. (But you can recover in the presentation of project 2)
- Submission by pull request to the website. Instructions [here](/course_sustainableSE/2023/literature_review.html).
- **Deadline** Tuesday, Feb 21.

### 🛠 **Project 1** Measuring Software Energy Consumption
{: #project1}

- Goal: Compare energy consumption in common software use cases.
  - Examples:
    - Different versions of the same app;
      - Same use case but different apps
      - Same version, same app, but different user settings (e.g., enable/disable GPU optimisation)
      - Same version, same app, but different running environment
- Blog-style report (markdown, approx 2500 words).
  - Bonus if you can automate the experiment and there is a replication package.
- Submission by pull request to the website. Instructions [here](/course_sustainableSE/2022/p1_measuring_software/). **⭐️(new)**
- **Weight in final grade**: 30%
- **Steering meeting/formative assessment**: Tuesday, Feb 22
- **Deadline** Thursday, Mar 3


### 🛠 Project 2 – Hacking Sustainability

- **Goal:** Solve a Sustainable Software Engineering problem.
  - Identify/Describe 1 problem that should be fixed to help enabling sustainability in the software engineering industry/community.
  - Propose a solution. It can be a tool, framework, guidelines, etc.
  - Implement the solution.
  - Validation. (Depending on the idea) (side note: the cancelled class was all about this)
  - Dissemination/social impact. (Solution should be open source, welcome contributors, post on twitter, hacker news, reddit? Tool website?)
- **Deliverables.**
  - Paper-like article. (Min 4 pages, max 10)
  - Online git repo with open source codebase and/or replication package.
  - Presentation: 7 min + 5min Q&A
- **Weight in final grade**: 60% (extra 7.5% for the presentation)
- **Steering meeting/formative assessments**: Every week from week 5 to 9.
- **Deadline** Tuesday, April 5. (Grace period until April 8).
 

## Further reading (optional)

- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). Experimentation in software engineering. Springer Science & Business Media.
- Cruz, L., & Abreu, R. (2017, May). Performance-based guidelines for energy efficient mobile applications. In 2017 IEEE/ACM 4th International Conference on Mobile Software Engineering and Systems (MOBILESoft) (pp. 46-57). IEEE.
- Cruz, L., & Abreu, R. (2019). [Catalog of energy patterns for mobile applications](https://arxiv.org/abs/1901.03302). Empirical Software Engineering, 24(4), 2209-2235.
- Stol, K. J., & Fitzgerald, B. (2018). The ABC of software engineering research. ACM Transactions on Software Engineering and Methodology (TOSEM), 27(3), 1-51.
- Spinellis, Diomidis (2017). [The Social Responsibility of Software Development](https://ieeexplore.ieee.org/document/7888390). IEEE Software.

## Interesting pointers

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
[MSc in Computer Science]: https://www.tudelft.nl/onderwijs/opleidingen/masters/cs/msc-computer-science
[Luís Cruz]: https://luiscruz.github.io
[June Sallou]: https://jnsll.github.io
[CS4415]: https://www.studiegids.tudelft.nl/a101_displayCourse.do?course_id=61596
[Stefanos Georgiou]: https://twitter.com/stefanosgeorgi1/
[Daniel Feitosa]: https://feitosa-daniel.github.io
[Tim Yarally]: https://www.linkedin.com/in/tim-yarally-64b77412b/?originalSubdomain=nl

[Building 62, Hall G]: https://esviewer.tudelft.nl/space/72/
[Building 35, Room 4]: https://esviewer.tudelft.nl/space/46/

[MyTimetable]: https://mytimetable.tudelft.nl/link?timetable.id=2021!module!01CD7133098AD9A864150E64E74F6D7F

[slides01]: https://surfdrive.surf.nl/files/index.php/s/e00qM7HCKffK0rj
[slides02]: 
[slides05]: 
[slides06]: 
[slides08]: 
[slides09]:  
[slides12]: 
[slides14]: 
[slides15]: 

[recording01]: https://surfdrive.surf.nl/files/index.php/s/n0D3PW0sLJ3Sk3K
[recording05]: 
[recording06]: 
[recording08]: 
[recording09]: 
[recording11]: 
[recording12]: 
[recording14]: 
