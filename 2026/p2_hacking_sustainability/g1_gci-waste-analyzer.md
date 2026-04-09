---
author: "Jayran Duggins, Priyansh Rajusth, Erkin Başol, Maja Bińkowska, Nicolas Loaiza Atehortua"
title: "GCI - Wasteful CI Analyzer"
image: "img/g1_gci-wasteful-ci-analyzer/gci_analyzer_logo.png"
summary: "Continuous Integration (CI) pipelines automatically build and test software when changes are made to a repository. While CI improves software reliability, many runs provide little value while still consuming compute resources and energy. Examples include rerunning jobs after flaky test failures, scheduled workflows running on inactive repositories, and full test suites triggered by documentation-only changes. In this project, we propose GCI, a tool that analyzes CI pipelines to identify and estimate unnecessary energy usage for contribiutors. Given a repository URL, GCI retrieves workflow run data from the GitHub API and analyzes recent CI activity. The tool estimates energy consumption based on runtime and typical CI runner power usage, and classifies runs as productive or wasteful based on predefined patterns. GCI then generates a dashboard summarizing total CI energy usage, the proportion of wasted runs, wasteful code that impacted the metric spike, and recommendations for improving pipeline efficiency. By highlighting hidden energy costs in CI/CD workflows, GCI aims to help developers reduce unnecessary compute usage and encourage more sustainable software development practices."

paper: "../papers/g1_gci-wasteful-ci-analyzer.pdf"
source: "https://github.com/jayran-d/GCI_Wasteful-CI-Analyzer"
# website: # not applicable
# video: # not applicable
group_number: 1
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---
