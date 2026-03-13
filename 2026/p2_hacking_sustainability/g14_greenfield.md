---
author: "Preethika Ajaykumar, Atharva Dagaonkar, Riya Gupta, Sneha Prashanth, Deon Saji"
title: "GreenField — Cross-Boundary JSON Field Analysis"
image: "img/gX_template/cover.png"
summary: "Modern full-stack applications silently accumulate unused JSON fields, data the backend sends but the frontend never reads, or fields the frontend submits but the backend never processes. This unused payload wastes CPU cycles on serialisation, consumes unnecessary network bandwidth, and drains mobile battery at every request, yet no existing tool detects it. GreenField performs static cross-boundary analysis across a full-stack workspace, tracing which fields are defined on one side and never accessed on the other, surfacing violations as inline diagnostics with estimated byte impact. We validate the tool on real open-source full-stack repositories, quantifying unused field prevalence and its measurable energy cost at realistic request volumes."
paper: "../papers/gX_template.pdf"
source: "https://github.com/luiscruz/course_sustainableSE"
website: https://luiscruz.github.io/course_sustainableSE/
video: https://luiscruz.github.io/course_sustainableSE/
group_number: 0
identifier: "p2_hacking_sustainability_2026" # Do not change this
all_projects_page: "../p2_hacking_sustainability" # Do not change this
---

## Overview

GreenField performs static cross-boundary analysis across a full-stack workspace to detect unused JSON fields, fields the backend sends but the frontend never reads, or fields the frontend submits but the backend never processes. It parses both codebases simultaneously using AST analysis, maps each API endpoint to its associated request and response fields, and traces actual field access patterns on the receiving side. Unused fields are surfaced as inline editor diagnostics with estimated wasted bytes per request, and a summary panel gives a per-endpoint payload efficiency breakdown.

## Sustainability Target

The tool targets network and computational efficiency in software systems. Every unused JSON field incurs a real energy cost: CPU cycles spent serialising and deserialising data that is never used, bytes transmitted over the network at every request, and unnecessary memory allocation and garbage collection on both ends. At scale — millions of requests per day — this represents measurable and entirely avoidable energy waste.

## Evaluation

A real-world impact study: we run GreenField on a set of publicly available open-source full-stack repositories and report the prevalence of dead fields, the estimated wasted payload per request, and the quantified energy reduction achievable by removing them. No human data will be collected; all evaluation is code and energy-based.
