---
author: "Andrea Vezzuto, Jan Kuhta, Rodrigo Montero Gonzalez, Aadesh Ramai, Samuel van den Houten"
title: "Group 21: Jamanota middleware for tracking energy usage in Langchain"
image: "img/g21_jamanota/cover.jpeg"
summary: "The rapid growth of AI agent systems in recent years has introduced significant environmental concerns. However, developers currently lack the tools to assess the energy and carbon footprint of their applications. Existing observability platforms expose token usage as a proxy for cost, but do not translate this into meaningful environmental metrics. Furthermore, no existing solution addresses environmental resource tracking within multi-agent LangChain workflows.

In this paper, we present Jamanota, a middleware tool for the LangChain framework that enables developers to gain insights into the resource consumption of their agentic pipelines. By improving the transparency of otherwise hidden environmental costs in AI systems, Jamanota helps bridge a gap in sustainable AI development. The middleware intercepts model calls, extracts associated execution metadata, and uses them to derive and store estimated environmental metrics such as energy usage and carbon emissions. These metrics are exposed through a Python API, providing functions that return total or average consumption, as well as aggregations by model or agent, with optional filtering by the last $N$ prompts or time intervals. 

We evaluate the tool through a scenario-based analysis across three different developer personas, assessing several key aspects such as its transparency, interpretability, and actionability. The results show that the middleware increases visibility into environmental resource consumption of model calls with meaningful insights. While the solution is a step closer to more sustainable and environmentally interpretable agentic AI systems, our work highlights limitations in evaluation and estimation precision, and outlines future directions including energy-aware optimisation and more fine-grained energy modelling."
paper: "../papers/g21_jamanota.pdf"
source: "https://github.com/SSE-project2/jamanota-energy-middleware"
website: https://pypi.org/project/jamanota/
group_number: 21
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---
