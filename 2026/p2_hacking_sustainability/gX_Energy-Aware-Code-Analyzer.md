---
author: "Maciej Wierzbicki, Mikołaj Magiera, Figen Ulusal, Radu Chiriac, Ibrahim Badr"
title: "Energy-Aware Code Analyzer"
image: "img/gX_template/cover.png"
summary: "This is a summary with a max of 200 characters; The links below should send the reader to your paper, the tool you folks built (source code or website), and optionally your presentation video. Please remove yaml entries for links you do not use."
paper: "../papers/gX_template.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

In this project we would develop an Energy-Aware Code Analyzer, a lightweight static analysis tool designed to help developers identify programming patterns that may lead to unnecessary energy consumption. In current software development practices, developers typically focus on correctness, performance, and security, while the energy efficiency of code is rarely evaluated during development. As a result, inefficient algorithms, repeated network calls, unnecessary polling loops, and other energy-intensive patterns are often introduced into production systems without awareness of their environmental impact.

The proposed tool will target the energy efficiecny aspect of sustaibale software engineering. We will focus on addressing how everyday coding decisions influence computational resource usage,and, consequently, energy conusmption and carbon emissions. The analyzer will scan source code and detect known patterns associated with inefficient resource use, such as nested loops with quadratic complexity, repeated computations inside loops, or excessive polling operations. For each detected issue, the tool will provide a warning along with suggestions for more energy-efficient alternatives. By providing developers with immediate feedback during development, the tool aims to encourage more sustainable coding practices and reduce unnecessary energy usage in software systems.