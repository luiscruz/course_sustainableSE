---
author: "Konstantina Anastasiadou, Zofia Rogacka-Trojak, Amy van der Meijden, Andriana Tzanidou, Jimmy Oei"
title: "Flow-Sate: Developer Well-being Plugin "
image: "img/g13_wellbeing_plugin/logo.png"
summary: "A local IDE plugin protecting developer well-being. It monitors Flow State to prompt breaks, and analyzes uncommitted code's Cognitive Load to prevent reviewer burnout from complex PRs."
paper: "../papers/g13_template.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 13
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

The *Developer Well-being Plugin* is a locally run IDE extension designed to support Individual and Social Sustainability right at the source of code creation. This plugin will be designed to protect developers from burnout while they write code. It focuses on the developer's "Flow State" a key part of the *SPACE framework*[^1] by tracking how much time they spend actively coding compared to how often they switch contexts or get distracted. If their focus drops, the plugin privately suggests taking a break. Because all data is processed and stored locally on the developer's machine, it supports Individual Sustainability without acting as a surveillance tool for management.

Beyond helping the person writing the code, the plugin also protects the team members who have to review it (Social Sustainability). Large, complicated Pull Requests (PRs) cause reviewer fatigue and lead to poor code reviews. Instead of waiting for a PR to be opened on GitHub, our tool analyzes the developer's uncommitted code right inside the IDE. It calculates a running "Cognitive Load Score" based on cyclomatic complexity, the number of modified files, and subsystems touched in the current working tree. If the score gets too high, the plugin gently warns the developer to commit their work or split the feature into smaller parts, preventing burnout for future reviewers.

# References
[^1]: Developer experience, Microsoft Developer. (n.d.). Microsoft Developer. [Read Article](https://developer.microsoft.com/en-us/developer-experience#:~:text=The%20SPACE%20framework%20was%20developed,Partner%20Research%20Manager%20at%20Microsoft)