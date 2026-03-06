---
author: "Dragoș Erhan, Alexandru Verhovețchi, Ion Tulei"
title: "Dockerfile Carbon Optimizer"
image: "img/g228_dockerfile_carbon/cover.png"
summary: "A CLI linter that analyzes Dockerfiles for energy-wasteful patterns and estimates the carbon cost of image bloat across builds and pulls."
paper: "../papers/g228_dockerfile_carbon.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
group_number: 228
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## The Problem

Docker images are routinely built for convenience, not efficiency. Common anti-patterns, such as: using `python:3.12` (1 GB) instead of `python:3.12-slim` (155 MB), leaving `gcc` installed after compilation, skipping multi-stage builds, missing `.dockerignore`. These inflate image sizes by hundreds of megabytes. This bloat compounds: every `docker build` wastes build energy, and every `docker pull` transfers unnecessary bytes over the network. For popular images pulled millions of times per month, the cumulative energy waste is significant.

Existing Dockerfile linters like [hadolint](https://github.com/hadolint/hadolint) and [dockle](https://github.com/goodwithtech/dockle) check for best practices and security, but none quantify the environmental cost of Dockerfile choices.

## The Solution

Dockerfile Carbon Optimizer is a CLI tool that parses a Dockerfile, detects energy-wasteful patterns, and reports the estimated carbon cost of each issue. For every finding, it suggests a concrete fix and estimates the size reduction, energy savings, and CO2 impact.

### Detected patterns include:
- Oversized base images when slimmer alternatives exist
- Uncombined `RUN` layers creating unnecessary intermediate images
- Dev dependencies (compilers, build tools) left in production images
- Missing `.dockerignore` causing large build contexts
- Missing multi-stage builds for compiled languages
- Unpinned base image tags pulling unexpectedly large versions

### Carbon cost estimation

The tool estimates carbon impact across three dimensions:

**Network transfer energy** - the largest contributor at scale. Each pull transfers the full image. We use the network energy intensity model from Aslan et al. (2018), *"Electricity Intensity of Internet Data Transmission"*, which estimates ~0.06 kWh per GB transferred, adjusted for year-over-year efficiency improvements. Combined with pull frequency (from Docker Hub API) and regional grid carbon intensity (from IEA emission factors or the Electricity Maps API), this yields a per-issue carbon estimate.

**Build energy** - measured directly. We build the original and optimized Dockerfiles on the same machine and measure energy consumption using one of several available tools:

- [CodeCarbon](https://github.com/mlco2/codecarbon) - Python library that tracks CPU/GPU/RAM electricity consumption and converts to CO2 emissions
- [EnergiBridge](https://github.com/tdurieux/EnergiBridge) - cross-platform energy measurement utility supporting Intel, AMD, and ARM architectures (with a [Python wrapper](https://github.com/luiscruz/pyEnergiBridge))
- [Scaphandre](https://github.com/hubblo-org/scaphandre) - energy consumption metrology agent with native Docker and Kubernetes support
- [PowerJoular](https://github.com/joular/powerjoular) - monitors CPU and GPU power consumption using Intel RAPL and ARM power interfaces
- Linux `perf stat` - built-in profiler that can read RAPL energy counters directly

This produces concrete before/after energy comparisons for the paper.

### Example output

| Issue | Fix | Size Saved | Est. CO2/month (at 100K pulls) |
|-------|-----|-----------|-------------------------------|
| Use `python:3.12-slim` instead of `python:3.12` | Change `FROM` line | 855 MB | ~2.2 kg CO2 |
| Combine 4 `RUN` layers into 1 | Merge with `&&` | ~120 MB | ~0.3 kg CO2 |
| Remove `gcc` after build | Add `apt-get purge` | ~200 MB | ~0.5 kg CO2 |

### Validation

We plan to run the tool on 30-50 real Dockerfiles from popular open-source repositories, apply the suggested optimizations, and measure actual image size reduction and build energy difference. The paper will report aggregate savings and discuss the sensitivity of carbon estimates to the underlying energy model assumptions.

### Key references

- Aslan et al. (2018). [*Electricity Intensity of Internet Data Transmission: Untangling the Estimates.*](https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.12630) Journal of Industrial Ecology, 22(4), 785-798.
- Masanet et al. (2020). [*Recalibrating global data center energy-use estimates.*](https://www.science.org/doi/abs/10.1126/science.aba3758) Science.
- IEA (2023). [*Emission Factors*](https://www.iea.org/data-and-statistics/data-tools/emissions-factors) - grid carbon intensity by country.
- [CO2.js](https://github.com/thegreenwebfoundation/co2.js) by The Green Web Foundation - open-source library for data-to-carbon conversion.
