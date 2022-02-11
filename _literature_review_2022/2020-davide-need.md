---
layout: publication
readby: Hana Jirovská, Sára Juhošová
journal: "IEEE Transactions on Software Engineering"
paper_author: Davide Fucci, Giuseppe Scanniello, Simone Romano, Natalia Juristo
paper_title: "Need for Sleep: The Impact of a Night of Sleep Deprivation on Novice Developers’ Performance"
year: 2020
doi: 10.1109/TSE.2018.2834900
slides: link://to.slides
abstract: |-
  We present a quasi-experiment to investigate whether, and to what extent, sleep deprivation impacts the performance of novice software developers using the agile practice of test-first development (TFD). We recruited 45 undergraduates, and asked them to tackle a programming task. Among the participants, 23 agreed to stay awake the night before carrying out the task, while 22 slept normally. We analyzed the quality (i.e., the functional correctness) of the implementations delivered by the participants in both groups, their engagement in writing source code (i.e., the amount of activities performed in the IDE while tackling the programming task) and ability to apply TFD (i.e., the extent to which a participant is able to apply this practice). By comparing the two groups of participants, we found that a single night of sleep deprivation leads to a reduction of 50 percent in the quality of the implementations. There is notable evidence that the developers' engagement and their prowess to apply TFD are negatively impacted. Our results also show that sleep-deprived developers make more fixes to syntactic mistakes in the source code. We conclude that sleep deprivation has possibly disruptive effects on software development activities. The results open opportunities for improving developers' performance by integrating the study of sleep with other psycho-physiological factors in which the software engineering research community has recently taken an interest in.

bibtex: |-
  @article{8357494,
    author = {D. Fucci and G. Scanniello and S. Romano and N. Juristo},
    journal = {IEEE Transactions on Software Engineering},
    title = {Need for Sleep: The Impact of a Night of Sleep Deprivation on Novice Developers' Performance},
    year = {2020},
    volume = {46},
    number = {01},
    issn = {1939-3520},
    pages = {1-19},
    keywords = {sleep;software;task analysis;biomedical monitoring;software engineering;programming;functional magnetic resonance imaging},
    doi = {10.1109/TSE.2018.2834900},
    publisher = {IEEE Computer Society},
    address = {Los Alamitos, CA, USA},
    month = {jan}
  }

tags:
  - Computer Aided Instruction
  - Computer Science Education
  - Sleep
  - Software Engineering
  - Source Code
  - Sleep Deprivation
  - Software Development Activities
  - Novice Software Developers
  - TFD
  - Programming Task
  - Sleep Deprived Developers
  - Sleep
  - Software
  - Task Analysis
  - Biomedical Monitoring
  - Software Engineering
  - Programming
  - Functional Magnetic Resonance Imaging
  - Sleep Deprivation
  - Psycho Physiological Factors
  - Test First Development

annotation: |-
  The effects of sleep deprivation have recently been studied in many contexts, including economics, management, and the general performance of humans in daily life. This paper draws on research already done on sleep deprivation and explores the impact it has on the performance of software developers.

  The "quasi-experiment" (named thus due to the authors' inability to pick the candidates) was executed on 45 undergraduate Computer Science and Software Engineering students who were asked to solve tasks under different amounts of sleep deprivation. These tasks consisted of implementing a series of requirements using test-first development (TFD).
  
  The group was divided into two subgroups: the control group, which was asked to sleep normally the night before the test, and the sleep deprivation group, which was asked to spend the entire night awake. These two groups were then compared on the quality of their solutions, the engagement they displayed towards the task, and their ability to apply TFD.

  It was, unfortunately, not possible to execute the entire experiment in a controlled environment and thus other methods had to be developed to assess whether candidates slept the required amount. To complement the participants' own assessment, the psychomotor vigilance task (PVT) was used to, comparing the sleep deprivation group's results after a day of good sleep and on the day of the task itself. This resulted in a "cleaned" dataset with 8 less participants who had claimed to not have slept the night before but their PVTs seemed to indicate otherwise.

  From the results, it was concluded that sleep deprivation indeed has an effect on external software quality and that it is of medium gravity (about 50% deterioration). However, there was not enough evidence to reject the null hypotheses for the engagement and the TFD abilities even though there did seem to be a negative effect.

  The experiment was largely influenced by the limitation in candidate choice. The candidates were selected on a voluntary basis, both to take part in the experiment as well as to be allocated to the sleep deprivation group. This provided a small and non-flexible experiment group which posed several challenges, including the limitation on the experiment design, the difficulty to check treatment conformance (whether the participants slept the amount they were supposed to), and the cost of implementing a dry-run.
---

<!--mandatory fields: paper_title, readby, paper_author, journal, year, doi or preprint or arxiv, slides (if you have), abstract, annotation -->
