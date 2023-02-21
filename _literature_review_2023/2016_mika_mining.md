---
layout: publication
readby: Ole Peder Brandtzæg, Aaron van Diepen, Rolf Piepenbrink & Jasper Teunissen
journal: "MSR '16: Proceedings of the 13th International Conference on Mining Software Repositories"
paper_author: Mika Mäntylä, Bram Adams, Giuseppe Destefanis, Daniel Graziotin, Marco Ortu
paper_title: "Mining Valence, Arousal, and Dominance: Possibilities for Detecting Burnout and Productivity?"
year: 2016
doi: https://doi.org/10.1145/2901739.2901752
slides: https://docs.google.com/presentation/d/1RaKwFbqQCu1FbigbEZRAs4La8NrcitQ4cYzhYiLmoU8/
abstract: |-
  Similar to other industries, the software engineering domain is plagued by
  psychological diseases such as burnout, which lead developers to lose
  interest, exhibit lower activity and/or feel powerless. Prevention is
  essential for such diseases, which in turn requires early identification of
  symptoms. The emotional dimensions of Valence, Arousal and Dominance (VAD)
  are able to derive a person’s interest (attraction), level of activation and
  perceived level of control for a particular situation from textual
  communication, such as emails. As an initial step towards identifying
  symptoms of productivity loss in software engineering, this paper explores
  the VAD metrics and their properties on 700,000 Jira issue reports containing
  over 2,000,000 comments, since issue reports keep track of a developer’s
  progress on addressing bugs or new features. Using a general-purpose lexicon
  of 14,000 English words with known VAD scores, our results show that issue
  reports of different type (e.g., Feature Request vs. Bug) have a fair
  variation of Valence, while increase in issue priority (e.g., from Minor to
  Critical) typically increases Arousal. Furthermore, we show that as an
  issue’s resolution time increases, so does the arousal of the individual the
  issue is assigned to. Finally, the resolution of an issue increases valence,
  especially for the issue Reporter and for quickly addressed issues. The
  existence of such relations between VAD and issue report activities shows
  promise that text mining in the future could offer an alternative way for
  work health assessment surveys.
bibtex: |-
  @inproceedings{10.1145/2901739.2901752,
  author = {M\"{a}ntyl\"{a}, Mika and Adams, Bram and Destefanis, Giuseppe and Graziotin, Daniel and Ortu, Marco},
  title = {Mining Valence, Arousal, and Dominance: Possibilities for Detecting Burnout and Productivity?},
  year = {2016},
  isbn = {9781450341868},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/2901739.2901752},
  doi = {10.1145/2901739.2901752},
  abstract = {Similar to other industries, the software engineering domain is plagued by psychological diseases such as burnout, which lead developers to lose interest, exhibit lower activity and/or feel powerless. Prevention is essential for such diseases, which in turn requires early identification of symptoms. The emotional dimensions of Valence, Arousal and Dominance (VAD) are able to derive a person's interest (attraction), level of activation and perceived level of control for a particular situation from textual communication, such as emails. As an initial step towards identifying symptoms of productivity loss in software engineering, this paper explores the VAD metrics and their properties on 700,000 Jira issue reports containing over 2,000,000 comments, since issue reports keep track of a developer's progress on addressing bugs or new features. Using a general-purpose lexicon of 14,000 English words with known VAD scores, our results show that issue reports of different type (e.g., Feature Request vs. Bug) have a fair variation of Valence, while increase in issue priority (e.g., from Minor to Critical) typically increases Arousal. Furthermore, we show that as an issue's resolution time increases, so does the arousal of the individual the issue is assigned to. Finally, the resolution of an issue increases valence, especially for the issue Reporter and for quickly addressed issues. The existence of such relations between VAD and issue report activities shows promise that text mining in the future could offer an alternative way for work health assessment surveys.},
  booktitle = {Proceedings of the 13th International Conference on Mining Software Repositories},
  pages = {247–258},
  numpages = {12},
  location = {Austin, Texas},
  series = {MSR '16}
  }
tags:
  - Individual Sustainability
annotation: |-
  Burnout, among other psychological diseases, is prevalent in the software
  engineering domain and is signified by a loss of interest, lower activity and
  a sense of powerlessness. Since these are undesirable situations, prevention
  can prove to be useful. In order to make a first attempt at identifying the
  symptoms, the paper explores a way to do this with the Valence, Arousal and
  Dominance (VAD) metrics. Here Valence relates to attractiveness or
  adverseness, Arousal represents the emotional activation levels and Dominance
  concerns the sense of control on a stimulus. The authors have extracted the
  characteristics, title, description and comments of issue reports of the
  Apache Foundation. To calculate the VAD scores of a piece of text, you use a
  VAD corpus to find the VAD scores of a subset of words, like the 13,915 word
  general-purpose lexicon the paper used. For each piece of text, the VAD
  scores are calculated by taking the difference between the maximum and
  minimum VAD scores in a piece of text. First, using this approach, the paper
  evaluates the extent to which VAD relates to issue report characteristics.
  The authors found that Blocker issues have higher Arousal than Trivial
  issues. While the differences are statistically significant, the effect sizes
  between priorities are negligible, so the difference observed in practice is
  unremarkable. Furthermore, Valence is lowest for Bugs. This supports the idea
  that developers experience more pleasure from developing new features
  compared to fixing bugs. Finally, high Dominance is associated with high
  issue resolution time. Second, a closer look is taken at the VAD change when
  issues are resolved. It was shown that from the moment an issue is reported
  to the time when the issue is closed, Valence and Dominance tend to increase,
  while Arousal has a small decrease. This paper concludes that VAD scores can
  give relevant information on the emotions associated with the development
  process. Additionally, this paper finds a correlation between the VAD scores
  and various aspects of the issue resolving process, like resolution time.
  Other research on VAD scores indicates that they can indicate an increased
  risk for various mental issues like burnout. As this paper only mined
  historical data, the paper does not look at how VAD scores could be used to
  predict a high risk of burnout or resolution time. Future research is needed
  to find out if that is possible, and if so, how such a system would be
  implemented. The method of calculating VAD scores could be improved as well.
  Right now, a generic English language VAD corpus is used. Future research
  could look into VAD corpora specialized for software engineering, handling of
  ‘booster words’ and negations (‘I really like’ or ‘I don’t like’), or finding
  ways to detect and handle different meanings of the same words. The paper
  shows that VAD scores give promising results for emotional analysis of the
  development process, and it provides a solid basis for future research in
  detecting and preventing burnout in software engineering.
---

<!--mandatory fields: paper_title, readby, paper_author, journal, year, doi or preprint or arxiv, slides (if you have), abstract, annotation -->
