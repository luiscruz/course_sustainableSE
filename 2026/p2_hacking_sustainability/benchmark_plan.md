# Plan: LLM Energy-Accuracy Benchmark

## Research Question (Refined)

**Primary Question:** How can we create a standardized benchmark that relates LLM energy efficiency to task accuracy, enabling organizations to make informed trade-offs between model performance and energy consumption for local deployment?

**Sub-questions:**
- Does the energy-accuracy relationship vary across different task types?
- Can we identify Pareto-optimal models (best accuracy for given energy budget)?
- How do different accuracy metrics affect the energy-accuracy correlation?

---

## 1. Accuracy Metrics Selection

### Recommended Approach: Multi-Metric Evaluation

Rather than choosing a single metric, use **task-appropriate metrics** for each category, then aggregate:

### Task Category 1: Code Generation
**Metric: Pass Rate (from unit tests)**
- **Benchmark:** HumanEval or MBPP (Mostly Basic Python Problems)
- **Justification:** 
  - Binary correctness (pass/fail) is unambiguous
  - Reproducible via automated test execution
  - Directly measures practical utility
  - Used successfully in previous course projects (g7_llm_quantization.md)
- **Calculation:** `Pass Rate = (Tasks Passed) / (Total Tasks)`

### Task Category 2: Question Answering / Knowledge
**Metric: Exact Match (EM) or F1 Score**
- **Benchmark:** MMLU (Massive Multitask Language Understanding) subset, or SQuAD
- **Justification:**
  - EM measures exact correctness (critical for factual tasks)
  - F1 captures partial credit for partially correct answers
  - Standard in QA evaluation
- **Calculation:** 
  - `EM = 1 if answer matches exactly, else 0`
  - `F1 = 2 × (Precision × Recall) / (Precision + Recall)`

### Task Category 3: Text Classification
**Metric: Accuracy or F1-Score (macro-averaged)**
- **Benchmark:** GLUE or custom classification dataset
- **Justification:**
  - Standard classification metrics
  - F1 handles class imbalance better than accuracy
- **Calculation:** `Accuracy = (Correct Predictions) / (Total Predictions)`

### Task Category 4: Text Generation / Summarization
**Metric: ROUGE-L or BLEU**
- **Benchmark:** Custom prompts or summarization dataset
- **Justification:**
  - ROUGE-L measures longest common subsequence (captures semantic similarity)
  - Standard for generation tasks
- **Calculation:** Use standard ROUGE/BLEU libraries

### Aggregation Strategy
For the energy label, compute a **composite accuracy score**:
- Normalize each metric to 0-1 scale
- Weight by task importance (or equal weights)
- `Composite Accuracy = Σ(weight_i × normalized_metric_i)`

**Alternative (Simpler):** Focus on 2-3 task categories initially (e.g., Code + QA) to keep scope manageable.

---

## 2. Energy-Accuracy Efficiency Metric

### Primary Metric: Energy per Correct Answer (EPCA)

**Formula:**
```
EPCA = Total Energy (J) / Number of Correct Answers
```

**Why this metric:**
- Directly measures efficiency: lower EPCA = more efficient
- Accounts for both energy AND accuracy (a model with 100% accuracy but high energy gets penalized)
- Intuitive for end users: "How much energy does it cost to get one correct answer?"

### Secondary Metrics:
- **Energy per token** (for comparison with existing work)
- **Accuracy per Joule** (alternative perspective: `Accuracy / Total Energy`)
- **Pareto efficiency score** (distance from Pareto frontier)

---

## 3. Task Categories & Standardization

### Recommended Task Categories (Start with 2-3):

1. **Simple Classification** (e.g., sentiment analysis, topic classification)
   - Low complexity, should favor smaller models
   - Expected: Small models achieve good accuracy with low energy

2. **Code Generation** (e.g., HumanEval, MBPP)
   - Medium complexity, requires reasoning
   - Expected: Medium models may be optimal

3. **Complex Reasoning** (e.g., math problems, multi-step QA)
   - High complexity, may require larger models
   - Expected: Larger models needed, but energy cost is high

### Standardization Requirements:
- **Fixed prompts:** Same prompts across all models
- **Fixed context length:** Control for context window effects
- **Fixed generation parameters:** Temperature, max_tokens, etc.
- **Multiple runs:** 3-5 runs per model-task combination for statistical validity

---

## 4. Model Selection Strategy

### Recommended Models (Covering Size Range):

**Small Models (1-3B parameters):**
- Phi-3 Mini (3.8B)
- Qwen2.5-1.5B
- Llama 3.2-3B

**Medium Models (7-13B parameters):**
- Llama 3.1-8B
- Mistral 7B
- Qwen2.5-7B

**Large Models (30B+ parameters):**
- Llama 3-70B (if hardware allows)
- Or focus on smaller range if limited by hardware

**Selection Criteria:**
- Available in local deployment formats (Ollama, vLLM, LM Studio)
- Cover different architectures (if possible)
- Similar quantization levels (e.g., all Q4 or all FP16)

---

## 5. Energy Measurement Methodology

### Tools:
- **GPU Energy:** nvidia-smi (poll every 250ms)
- **CPU Energy:** Intel RAPL (via EnergiBridge or direct MSR access)
- **Total Energy:** GPU + CPU (or GPU-only if CPU is minimal)

### Measurement Protocol:
1. **Baseline:** Measure idle power for 10 seconds
2. **Warm-up:** Run one inference to stabilize system
3. **Measurement:** 
   - Start energy monitoring
   - Run inference with standardized prompt
   - Stop monitoring after completion
4. **Cooldown:** 10-second idle period
5. **Repeat:** 3-5 runs per model-task combination
6. **Calculate:** Subtract baseline, average across runs

### Data to Record:
- Total energy (J)
- Inference time (s)
- Tokens generated
- Tokens in prompt
- Accuracy metric value
- Model parameters (size, quantization)

---

## 6. Label Derivation System

### Step 1: Compute EPCA for each model-task combination

### Step 2: Normalize EPCA
- Find min and max EPCA across all models for each task
- Normalize to 0-1 scale: `normalized_EPCA = (EPCA - min) / (max - min)`

### Step 3: Map to A-G Scale
- **A (Best):** Top 10% efficiency (lowest EPCA)
- **B:** Next 15%
- **C:** Next 15%
- **D:** Next 20%
- **E:** Next 20%
- **F:** Next 15%
- **G (Worst):** Bottom 5%

**Alternative:** Use percentile-based thresholds:
- A: 0-10th percentile
- B: 10-25th percentile
- C: 25-40th percentile
- D: 40-60th percentile
- E: 60-75th percentile
- F: 75-90th percentile
- G: 90-100th percentile

### Step 4: Task-Specific Labels
- Each model gets separate labels for each task category
- Example: "Llama 3.2-3B: Code Generation (B), QA (C), Classification (A)"

---

## 7. Implementation Plan

### Phase 1: Tool Development (Week 1-2)
- [ ] Set up energy measurement infrastructure (nvidia-smi + RAPL wrapper)
- [ ] Create benchmarking script that:
  - Loads models via Ollama/vLLM/LM Studio
  - Runs standardized prompts
  - Measures energy concurrently
  - Evaluates accuracy (unit tests, EM, etc.)
  - Logs all metrics to CSV/JSON
- [ ] Test on 1-2 models to validate pipeline

### Phase 2: Data Collection (Week 3-4)
- [ ] Run benchmarks for all model-task combinations
- [ ] Collect 3-5 runs per combination
- [ ] Validate data quality (outlier detection, consistency checks)

### Phase 3: Analysis & Label Generation (Week 5)
- [ ] Compute EPCA for all combinations
- [ ] Generate labels using defined thresholds
- [ ] Create visualizations:
  - Energy vs Accuracy scatter plots
  - Pareto frontier plots
  - Label distribution charts
- [ ] Statistical analysis (correlations, significance tests)

### Phase 4: Paper Writing & Tool Documentation (Week 6)
- [ ] Write methodology section
- [ ] Document findings and insights
- [ ] Create user guide for the benchmarking tool
- [ ] Prepare replication package

---

## 8. Expected Findings & Insights

### Hypotheses to Test:
1. **H1:** Smaller models achieve better EPCA for simple tasks
2. **H2:** Energy-accuracy tradeoff is non-linear (diminishing returns)
3. **H3:** Task type significantly affects optimal model choice
4. **H4:** Some models are Pareto-dominated (always worse than alternatives)

### Key Questions to Answer:
- Is there a "sweet spot" model size for each task type?
- How much accuracy do you sacrifice for 50% energy savings?
- Are there models that are both more accurate AND more efficient?

---

## 9. Limitations & Future Work

### Limitations to Acknowledge:
- Hardware-specific (results may vary on different GPUs)
- Limited to local deployment (cloud inference excluded)
- Fixed quantization levels (may not reflect all deployment scenarios)
- Task selection may not cover all use cases

### Future Work:
- Extend to more task categories
- Include different quantization levels
- Test on multiple hardware configurations
- Develop online tool for interactive label lookup
- Incorporate latency as additional dimension

---

## 10. Success Criteria

### Minimum Viable Benchmark:
- ✅ Measure energy + accuracy for 5+ models across 2+ task categories
- ✅ Demonstrate energy-accuracy tradeoff exists and varies by task
- ✅ Generate reproducible labels for tested models
- ✅ Document methodology clearly

### Stretch Goals:
- 🌟 10+ models, 3+ task categories
- 🌟 Interactive web tool for label lookup
- 🌟 Statistical validation of label reliability
- 🌟 Comparison with existing benchmarks (if any)

---

## 11. Deliverables Checklist

- [ ] **Benchmarking Tool:** Automated script/tool for energy+accuracy measurement
- [ ] **Dataset:** CSV/JSON with all measurements
- [ ] **Labels:** A-G labels for each model-task combination
- [ ] **Paper:** IEEE format paper documenting methodology and findings
- [ ] **Replication Package:** Code, data, instructions for reproducing results
- [ ] **Visualizations:** Charts showing energy-accuracy relationships
- [ ] **Website/README:** User-friendly documentation

---

## Next Steps

1. **Finalize task categories** (recommend starting with Code + QA)
2. **Select specific benchmarks** (HumanEval, MMLU subset, etc.)
3. **Choose initial model set** (5-7 models covering size range)
4. **Set up measurement infrastructure** (test nvidia-smi + RAPL)
5. **Run pilot study** (1-2 models, 1 task category) to validate approach
6. **Iterate based on pilot results**

---

## References from Course Projects

- **g7_llm_quantization.md:** Used MBPP with pass rate, computed energy per correct solution
- **g1_LLM_power_usage.md:** Used nvidia-smi + RAPL, standardized prompts
- **g6_llms_energy_consumption.md:** Used Intel RAPL, baseline measurements, multiple runs
