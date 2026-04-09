---
author: "Maciej Wierzbicki, Mikołaj Magiera, Figen Ulusal, Radu Chiriac, Ibrahim Badr"
title: "GreenLint: Energy-Aware Code Analyzer for Python"
image: "img/gX_greenlint/cover.png"
summary: "GreenLint is a lightweight Python linter that detects energy-inefficient code patterns using static AST analysis. The tool focuses on common inefficiencies such as suboptimal loops, repeated operations, and non-vectorized data processing. Unlike existing tools that estimate overall energy consumption or focus on general code quality, GreenLint provides targeted, code-level feedback grounded in benchmark comparisons of inefficient and optimized implementations. By using runtime as a reproducible proxy for energy impact, the tool offers practical and interpretable insights without requiring specialized hardware measurements. GreenLint integrates seamlessly into existing development workflows and outputs linter-style warnings, including suggestions for improvement and an indicative energy impact score. Evaluation on both curated benchmarks and open-source repositories shows that the targeted patterns are consistently associated with higher runtime and occur in real-world code, although detection accuracy depends on context. The tool demonstrates how sustainability-oriented feedback can be incorporated into everyday software development."
paper: "../papers/group9_greenlint_report.pdf"
source: "https://github.com/Ciamek277/SustainableSE2"
group_number: 9
identifier: "p2_hacking_sustainability_2026"
all_projects_page: "../p2_hacking_sustainability"
---