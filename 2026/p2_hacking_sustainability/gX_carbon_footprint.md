---
author: "Roham Koohestani, Kunal Narwani, Nina Semjanová, Caio Miranda Haschelevici, Georgios Markozanis"
title: "NuclearMix for CodeCarbon"
image: "img/gX_template/cover.png"
summary: "A CodeCarbon extension enabling contract-based electricity mixes and lifecycle-aware nuclear emission factors, paired with an interactive educational website on nuclear electricity lifecycle."
paper: "../papers/gX_carbon_footprint.pdf"
source: "https://github.com/YOUR_REPO/codecarbon-nuclearmix"
website: https://YOUR_WEBSITE_URL/
video: https://YOUR_VIDEO_URL/
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## Project Overview

**NuclearMix for CodeCarbon** addresses a critical gap in software carbon-footprint measurement: the lack of contract-based electricity mix accounting and lifecycle-aware emission factors for nuclear energy.

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

### Impact

This project enables organizations to accurately measure and report their software's carbon footprint based on actual procurement contracts, while educating the community about lifecycle emissions in energy production. The tool supports more informed decision-making around sustainable computing infrastructure.

---

📄 [Read the full paper](../papers/gX_carbon_footprint.pdf)
💻 [View source code](https://github.com/YOUR_REPO/codecarbon-nuclearmix)
🌐 [Try the interactive website](https://YOUR_WEBSITE_URL/)
🎥 [Watch the presentation](https://YOUR_VIDEO_URL/)
