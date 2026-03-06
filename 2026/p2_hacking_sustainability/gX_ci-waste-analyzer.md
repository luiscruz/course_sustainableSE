---
author: "Jayran Duggins, Priyansh Rajusth, Erkin Başol, Maja Bińkowska, Nicolas Loaiza Atehortua"
title: "EcoCI - CI Waste Analyzer"
image: "img/gX_ci-waste-analyzer/eco_ci_logo.png"
summary: "Continuous Integration (CI) pipelines automatically build and test software when changes are made to a repository. While CI improves software reliability, many runs provide little value while still consuming compute resources and energy. Examples include rerunning jobs after flaky test failures, scheduled workflows running on inactive repositories, and full test suites triggered by documentation-only changes. In this project, we propose EcoCI, a tool that analyzes CI pipelines to identify and estimate unnecessary energy usage. Given a repository URL, EcoCI retrieves workflow run data from the GitHub API and analyzes recent CI activity. The tool estimates energy consumption based on runtime and typical CI runner power usage, and classifies runs as productive or wasteful based on predefined patterns. EcoCI then generates a report summarizing total CI energy usage, the proportion of wasted runs, and recommendations for improving pipeline efficiency. By highlighting hidden energy costs in CI/CD workflows, EcoCI aims to help developers reduce unnecessary compute usage and encourage more sustainable software development practices."

paper: "../papers/gX_template.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

On this .md page you can give a brief intro to your project and link to your paper pdf, your published sourcecode or a website that shows off your tool ☀️

If you want to share your video presentation here as well, please upload it to a video platform of your choice and link it here.
