---
author: "Rebecca Andrei, Boris Annink, Paul Anton, Kasper van Maasdam, Radu Serban"
title: "A Linter and Guideline Framework for Sustainable GitHub Actions Workflows"
image: "img/g10_cover/cover.png"
summary: "We created a CI/CD rulebook and workflow linter for GitHub Actions named 'suslint' to assist developers in creating more sustainable workflows."
paper: "papers/g10_linter.pdf"
source: "https://github.com/KaspervanM/sustainable-gh-workflow-linter"
website: "https://kaspervanm.github.io/sustainable-gh-workflow-linter/"
experiments: "https://github.com/PaulAnton03/suslint-experiments-SE/"
group_number: 10
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

CI/CD pipelines are widely used in modern software development, but many workflows are configured inefficiently. Common issues such as unnecessary workflow triggers, missing dependency caching, and redundant jobs can lead to excessive compute usage and wasted resources. Developers often lack clear guidance on how to design more sustainable CI/CD workflows.

We propose creating a CI/CD rulebook and workflow linter for GitHub Actions, named `suslint`. The project consists of a website that provides practical guidelines for designing efficient workflows, along with a tool that analyzes GitHub Actions YAML files. The tool will parse GitHub Actions workflow files, identify potential inefficiencies (e.g., missing caching, overly broad triggers, unnecessary matrix builds), and suggest recommendations that developers can apply directly. The guidelines and tool are released as an open-source project under the GPL3.0 licence ([https://github.com/KaspervanM/sustainable-gh-workflow-linter](https://github.com/KaspervanM/sustainable-gh-workflow-linter)) and made available through a public website ([https://kaspervanm.github.io/sustainable-gh-workflow-linter/](https://kaspervanm.github.io/sustainable-gh-workflow-linter/)).

We have evaluated the approach by analyzing several open-source repositories that use GitHub Actions. For each repository, we compared their energy consumption before and after applying the recommended optimizations. The experiment replication package ([https://github.com/PaulAnton03/suslint-experiments-SE/](https://github.com/PaulAnton03/suslint-experiments-SE/)) used the following forked repositories:

* [https://github.com/PaulAnton03/ArchiSteamFarm-SE](https://github.com/PaulAnton03/ArchiSteamFarm-SE)
* [https://github.com/PaulAnton03/congo-SE](https://github.com/PaulAnton03/congo-SE)
* [https://github.com/PaulAnton03/rq-SE](https://github.com/PaulAnton03/rq-SE)
* [https://github.com/PaulAnton03/django-compressor-SE](https://github.com/PaulAnton03/django-compressor-SE)
