---
author: "Emre Cebi, Alexandru Mitteltu, Kevin Shan, Anton Cosmins, Mohammed Nassiri"
title: "Our Project"
image: "../../img/g16_template/cover.png"
summary: "An application that integrates with GitHub Actions to track energy consumption and provide developers with actionable insights on their sustainability impact."
paper: "../papers/gX_template.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 16
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

# Problem
Modern software development often overlooks the environmental impact of CI/CD pipelines, despite the frequent creation of resource-intensive runners.

# Solution
Our proposal is an application that integrates with GitHub Actions to track energy consumption and provide developers with actionable insights on their sustainability impact.

In modern software development, it has become common to rely on CI/CD tooling like GitHub Actions or Jenkins to build, test, or publish an application using remote workers. In many cases, these machines get spun up after making a new commit or a merge to a branch in a repository.

These runners are generally created from separate workflows, and during fast development or with large teams, it could mean that every day a lot of machines are created to run these. Depending on the tasks, the machines can take a long time to complete and can be resource intensive.

Currently, many developers do not know the effects of their CI/CD pipelines on sustainability.

Our proposal is an application that can integrate with GitHub Actions to keep track of resource usage, such as energy consumption, and, on each run, give software developers an overview of their impact. This is not just for one run: the application will track the total effect the project is creating. If a limit is reached, it will warn the developers and suggest strategies they can use to minimize their impact.