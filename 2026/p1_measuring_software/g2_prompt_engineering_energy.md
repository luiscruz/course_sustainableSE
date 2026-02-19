---
author: Roham Koohestani, Zofia Rogacka-Trojak, Antonio-Florin Lupu, Pranav Pisupati
group_number: 2
title: "Measuring the Energy Cost of Prompt Engineering for Software Engineering Tasks"
image: "img/g2_se_prompt.webp"
date: 12/02/2026
summary: |-
  Prompt engineering often improves answer quality, but it can also increase token usage, latency,
  and the number of model calls. This project proposes a reproducible experiment design to quantify
  the energy/performance trade-offs of common prompting strategies (e.g., step-by-step, politeness,
  and few-shot examples) on software engineering tasks with (as much as possible) automated evaluation.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## Motivation

Prompt engineering is widely used to improve LLM output quality (e.g., asking for more explanation, adding examples, or adding politeness). However, these patterns can materially change:

- tokens in/out (and thus inference work),
- end-to-end latency,
- and, ultimately, energy usage.

In software engineering (SE) workflows, prompting patterns are not just a user-interface choice; they can influence the sustainability of day-to-day engineering work at scale.

This page sets up the basis of an experimental methodology to measure the energy cost of prompt engineering for SE tasks, while keeping the experiment reproducible and statistically defensible.

## Starting Point (Related Work)

We start from the following resources (motivation + high-level measurement considerations):

- [https://arxiv.org/abs/2509.22320](https://arxiv.org/abs/2509.22320)
- [https://arxiv.org/html/2501.05899v1](https://arxiv.org/html/2501.05899v1)
- [https://www.capgemini.com/insights/expert-perspectives/from-words-to-watts-how-prompting-patterns-shape-ais-environmental-impact/](https://www.capgemini.com/insights/expert-perspectives/from-words-to-watts-how-prompting-patterns-shape-ais-environmental-impact/)

## Research Questions

RQ1. How do common prompting strategies change energy per solved SE task compared to a minimal baseline prompt?

RQ2. Do prompting strategies that increase tokens (e.g., explicit explanations, few-shot) yield enough quality improvement to justify additional energy?

RQ3. Are the effects consistent across task categories (bug fixing vs. test generation vs. summarization)?

## Experimental Design

### Independent Variables (Prompting Strategies)

We treat the prompt pattern as the main factor and keep everything else constant (same model, temperature, max tokens, system prompt, and evaluation harness).

Proposed conditions (minimal set; extend if time permits):

1. `baseline_single_shot`
   - concise instruction, no extra framing.
2. `polite_single_shot`
   - same as baseline, adds politeness markers ("please", "thank you") without adding content.
3. `think_step_by_step`
   - requests an explicit step-by-step reasoning before the final answer (expected to increase completion tokens).
4. `answer_only_no_expl`
   - explicitly requests a short final answer only (expected to reduce completion tokens).
5. `few_shot_{1,3,5}`
   - includes 1, 3, or 5 short example, then the task (expected to increase prompt tokens).

Note: We avoid relying on hidden "chain-of-thought". For transparency and comparability, a condition is defined by observable prompt text and an observable output format requirement.

### Prompt Templates

All conditions share the same task payload (same input files/text, same constraints), and only differ in the wrapper text.

We will use placeholders:

- `{TASK}`: the task instructions + any provided context (code snippet, failing test output, etc.)
- `{OUTPUT_SCHEMA}`: strict output requirement (e.g., "return only a unified diff")

`baseline_single_shot`

```
{TASK}

{OUTPUT_SCHEMA}
```

`polite_single_shot`

```
Please help with the following task.

{TASK}

{OUTPUT_SCHEMA}

Thanks!
```

`think_step_by_step`

```
{TASK}

Think step-by-step. First, write your reasoning. Then provide the final output.
{OUTPUT_SCHEMA}
```

`answer_only_no_expl`

```
{TASK}

Do not provide explanations.
{OUTPUT_SCHEMA}
```

`few_shot_1`

```
Example:
{EXAMPLE_TASK}
{EXAMPLE_OUTPUT}

Now do the task:
{TASK}

{OUTPUT_SCHEMA}
```

We will keep `{EXAMPLE_TASK}` short and task-agnostic to avoid injecting extra information into the evaluated task.

### Dependent Variables (Outcomes)

Primary sustainability outcomes:

- Energy per request (J), for local inference (measured).

Secondary outcomes:

- tokens in/out; total tokens,
- latency (end-to-end),
- quality (task-specific),
- efficiency:
  - J per passing task (J/pass),
  - pass rate per Joule (pass/J).

### Design Type and Scale

Paired, within-task design:

- For each task T, we run all prompting conditions C on the same input.
- We compare conditions using per-task deltas to reduce between-task variance.

## Task Set (Software Engineering)

We want tasks that are representative, small enough to run many times, and as automatically evaluable as possible.

Proposed tasks:
TBD

## Measurement Methodology

Per run, we will log:

- hardware model, OS, driver versions,
- model name + quantization,
- backend (e.g., `ollama`, `llama.cpp`, `vllm`),
- decoding parameters (temperature, top_p, max tokens),
- timestamps for start/end of inference,
- energy in Joules.

## Protocol to Reduce Bias

We follow common energy-measurement hygiene to reduce confounding:

- Zen mode:
  - close background apps; disable notifications; disconnect peripherals when possible.
- Freeze settings:
  - fixed screen brightness; fixed power mode; fixed network type; fixed CPU/GPU power settings.
- Warm-up:
  - do warm-up runs before recording.
- Randomization:
  - randomize task and condition order to reduce time-based drift.
- Repetitions:
  - multiple runs per (task, condition).
- Output schemas:
  - enforce strict output formats to reduce verbosity variance.

## Data Collection and Logging

Each run produces a record (JSONL recommended) with:

- `task_id`, `task_type`, `condition_id`, `run_id`
- `model_id`, `backend_id`
- `prompt_text_hash` (and optionally the full prompt)
- `tokens_in`, `tokens_out`, `latency_ms`
- `energy_j_measured` OR `energy_j_estimated` + estimation method
- `quality_metrics` (e.g., `tests_passed: true/false`)
- `output_artifact_path` (captured output for auditability)

## Analysis Plan

We report both energy and quality:

- per condition vs. baseline:
  - delta tokens, delta energy, delta latency, delta quality.
- efficiency:
  - J/pass and pass/J.

Statistics (initial plan):

- paired comparisons per task (use non-parametric tests if distributions are non-normal),
- effect sizes + 95% confidence intervals,
- multiple-comparison correction if many conditions are tested.

## Next Steps

1. Pick the exact benchmark/task repositories
2. Freeze the prompt templates and output schemas for each condition.
3. Implement the runner + logging format (JSONL) and validate on a small pilot.
4. Run the full matrix and analyze energy/quality trade-offs
