---
author: "Roham Koohestani, Kunal Narwani, Nina Semjanová, Caio Miranda Haschelevici, Georgios Markozanis"
title: "Nuclear Mix for Code Carbon"
image: "img/g7_template/cover.png"
summary: "This paper presents NuclearMix, a CodeCarbon extension supporting lifecycle-aware electricity-mix accounting, alongside a scrollytelling website on nuclear emissions. A paired pre/post survey (N=17) showed statistically significant knowledge gains (Cohen's d=1.08). Technical analysis revealed that reported software emissions vary substantially depending on nuclear share and lifecycle factor choice."
paper: "../papers/g7_nuclearmix.pdf"
source: "https://github.com/RebelOfDeath/codecarbon_nuclear_code"
website: https://rohamkoohestani.com/nuclear_footprint/
video: https://youtu.be/j7jOuuFkxuc
group_number: 7
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## Project Overview

**NuclearMix for CodeCarbon** addresses a gap in software carbon-footprint measurement, nemely, the lack of contract-based electricity mix accounting and lifecycle-aware emission factors for nuclear energy.

### The Problem

Current carbon-footprint tools like CodeCarbon use grid-average emission factors, which don't reflect organizations' actual electricity procurement contracts. For nuclear energy specifically, emissions occur across the entire lifecycle—from uranium mining and enrichment to waste management and decommissioning—yet are often oversimplified or omitted.

### Our Solution

We deliver two interconnected artifacts:

1. **`codecarbon-nuclearmix` Library Extension**
   - User-specified electricity mixes (market-based accounting)
   - Lifecycle-aware emission factors for nuclear and other sources
   - Transparent factor provenance and optional uncertainty ranges
   - Backward-compatible with existing CodeCarbon workflows

2. **Interactive Educational Website**
   - Scroll-driven narrative explaining nuclear electricity lifecycle stages
   - Animated visualizations of where CO₂e emissions arise
   - Interactive mix calculator mirroring the tool's computation
   - Direct links to open-source repository and replication package

### Key Features

- **Electricity Mix Input**: Specify contractual shares (e.g., 60% nuclear, 40% wind) instead of relying on grid averages
- **Lifecycle-Aware Factors**: Comprehensive emission factors covering construction, fuel extraction/processing, operations, waste management, and decommissioning
- **Dual Accounting Modes**: Location-based (grid-average) and market-based (contract-specific)
- **Transparency**: Outputs include accounting mode, factor sets, mix breakdown, and optional uncertainty intervals
- **Developer-Friendly**: Extended APIs, comprehensive tests, and clear examples
