Use only this template to open a pull request for project 2: Hacking Sustainability.
Use the title below for your pull request title.

# Group <group-number>: <give Energy-Aware Code Analyzer>

Make sure to fill out the information under each of the headers, as far as possible.
We will assign you a group number + coach after receiving the pull request.

Open the pull request from a repository + branch everyone in your group has access to, and use that branch to contiuously update your work throughout the project weeks.
This way your coach can view your progress and give you feedback.

## Group number on Brightspace:
*(We will give a group number on brightspace after reviewing the initial pull request)*

## Coach:
*(We will assign you a coach after reviewing the initial pull request)*

## Group members (only names, leave out student numbers):
*(Project 2 should have groups of 5 members)*
Maciej Wierzbicki, Mikołaj Magiera, Figen Ulusal, We are still looking for 2 more members unfortunately

## Channel name on Mattermost:
<TODO: fill out>

## Your topic idea for Project 2:
*(Consider discussing your project idea with the course staff before submitting this pull request to make sure it is somewhat suitable for project 2.)*

*Give an overview of what solution/tool/technique you will develop for Project 2*
*Make sure to clearly explain which aspect of **sustainable software engineering** you are targeting and how your solution will improve it.*
*Please also sketch briefly how you could showcase/evaluate/discuss the effectiveness of your solution. Clarify here whether you will use any data collected from humans*

In this project we would develop an Energy-Aware Code Analyzer, a lightweight static analysis tool designed to help developers identify programming patterns that may lead to unnecessary energy consumption. In current software development practices, developers typically focus on correctness, performance, and security, while the energy efficiency of code is rarely evaluated during development. As a result, inefficient algorithms, repeated network calls, unnecessary polling loops, and other energy-intensive patterns are often introduced into production systems without awareness of their environmental impact.

The proposed tool will target the energy efficiecny aspect of sustaibale software engineering. We will focus on addressing how everyday coding decisions influence computational resource usage,and, consequently, energy conusmption and carbon emissions. The analyzer will scan source code and detect known patterns associated with inefficient resource use, such as nested loops with quadratic complexity, repeated computations inside loops, or excessive polling operations. For each detected issue, the tool will provide a warning along with suggestions for more energy-efficient alternatives. By providing developers with immediate feedback during development, the tool aims to encourage more sustainable coding practices and reduce unnecessary energy usage in software systems.

To evaluate the effectiveness of the solution, the tool will be tested on a set of sample programs and selected open-source repositories. The evaluation will demonstrate how many potential energy inefficiencies can be detected and how suggested improvements could reduce computational complexity or unnecessary operations. The results will be discussed in terms of potential resource savings and improved sustainability awareness among developers. This project will not involve data collected from human participants, as the evaluation will rely solely on automated analysis of publicly available source code.

## Filename of your Project 2 entry in `p2_hacking_sustainability/` (contributed in this pull request): 
*(Fill out the yaml header fitting to your group. Ideally include a template of the paper file already)*
gX_Energy-Aware_Code_analyzer.md


## Did you succeed to build the website locally and look at your report?
yes
