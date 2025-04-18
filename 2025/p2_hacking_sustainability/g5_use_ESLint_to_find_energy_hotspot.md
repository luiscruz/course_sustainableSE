---
author: Jort van Driel, Dorian Erhan, Weicheng Hu, Giannos Rekkas
title: "Finding energy hotspots in JavaScript using ESLint"
image: "../img/p2_hacking_sustainability/gX_template/cover.png"
group_number: 5
summary: "This study examines how everyday JavaScript coding decisions impact a web application’s energy use. We introduce ESLint-based rules that detect “green” or “inefficient” patterns and then compare power consumption for each variant by measuring actual CPU energy. Twelve rules were tested, examples include using lazy image loading, preloading assets, avoiding frequent console logs, and substituting updated file formats for GIFs. Results reveal that most patterns yield only small energy changes. Notably, avoid using expensive identifiers significantly reduced consumption, while avoiding GIFs or canvas elements unexpectedly consumed more energy in these tests. Findings suggest that performance optimizations do not always translate to lower energy use, highlighting the complexity of sustainable software design. Though limited to Chromium on a single laptop and with simple experiments, we want to provide early evidence that real-time energy feedback can guide better practices. Future efforts include testing additional patterns, covering diverse browsers, and validating these rules in larger, real-world codebases. Overall, our study emphasizes on the need for practical, tool-assisted approaches to curb the web’s growing environmental footprint with trade-offs between performance and sustainability."
paper: "../papers/g5_Energy_Hotspot_in_Javascript.pdf"
source: "https://github.com/JortvD/cs4575-g5-p2"
website: https://luiscruz.github.io/course_sustainableSE/
---
