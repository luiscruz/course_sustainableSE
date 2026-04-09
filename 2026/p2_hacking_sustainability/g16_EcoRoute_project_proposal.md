# Project Proposal: EcoRoute - A Carbon-Aware Scheduler for CI/CD Workloads

## 1. Problem Statement

The software industry's reliance on Continuous Integration and Continuous Deployment (CI/CD) pipelines results in significant and continuous energy consumption. Many workloads, such as nightly end-to-end tests, machine learning model training, and large data processing jobs, are compute-heavy but not time-critical, meaning their immediate execution is not required.

Currently, CI/CD platforms are "carbon-unaware." They execute these jobs as soon as a runner is available, often in data centers powered by high-carbon energy grids, without considering the potential for optimization. This represents a missed opportunity to reduce the carbon footprint of software development by intelligently scheduling workloads based on geographic location (spatial shifting) and time of day (temporal shifting).

## 2. Proposed Solution

We propose **EcoRoute**, a lightweight, developer-centric tool that acts as a smart scheduler for CI/CD workloads. EcoRoute integrates into existing CI/CD pipelines as a "pre-flight" check to determine the most sustainable execution path for a given job.

The core functionality is as follows:
1.  **Configuration:** A developer defines their available compute regions (e.g., `aws-us-west-2`, `gcp-europe-north1`), job constraints (e.g., estimated runtime, maximum acceptable delay), and optimization priorities (cost, emissions, speed) in a simple `.ecoroute.yml` file within their repository.
2.  **Analysis:** When the pipeline runs, EcoRoute fetches real-time and forecasted carbon intensity data for the specified regions using sources like the Carbon Aware SDK.
3.  **Optimization:** It performs a multi-objective optimization to calculate a "penalty score" for every possible execution slot (a combination of region and time within the delay window). This calculation uniquely considers both the **compute emissions** at the target location and the estimated **data transfer emissions** required to move the workload.
4.  **Action:** The tool outputs an actionable decision. It either instructs the CI/CD platform to route the job to the optimal geographic runner immediately or schedules the job to run at a future time in the optimal location.

This approach empowers developers to significantly reduce their carbon footprint without requiring complex infrastructure changes or deep knowledge of energy grids.

## 3. Target Audience & Use Cases

EcoRoute is designed for non-blocking, asynchronous, and compute-intensive tasks where a delay is acceptable.

*   **Machine Learning Engineers:** Training models, running hyperparameter optimization.
*   **Data Engineers:** Executing large ETL batch jobs or data warehouse backfills.
*   **QA & Test Automation Engineers:** Running extensive nightly E2E test suites.
*   **Platform Engineers:** Building sustainable infrastructure and providing green tooling for their organization.

## 4. Key Differentiators & Novelty

Our project builds upon existing academic research but introduces key improvements for practical application:

1.  **Holistic Carbon Model:** Unlike existing research such as GreenCourier, which focuses solely on compute emissions, EcoRoute's optimization model will account for both **compute carbon** and **data transfer carbon**. This provides a more accurate and realistic assessment of the total carbon cost of relocating a job.
2.  **Developer-Centric Tooling:** In contrast to complex, infrastructure-heavy solutions that require managing Kubernetes clusters, EcoRoute is a lightweight, non-intrusive tool. Its simple YAML configuration and focus on direct integration with popular CI/CD platforms (e.g., GitHub Actions, GitLab CI) dramatically lowers the barrier to adoption.
3.  **Action-Oriented:** EcoRoute is not just a reporting tool. It actively intervenes in the CI/CD pipeline to enact its scheduling decisions, making it a practical solution for automated carbon reduction.

## 5. Implementation & Validation Plan

*   **Implementation:** We will develop the core optimization logic as a Python or Node.js script. This script will integrate with the Carbon Aware SDK to fetch energy data and will parse the user's `.ecoroute.yml` configuration. We will then develop proof-of-concept integrations for GitHub Actions and/or GitLab CI to demonstrate its practical use.
*   **Validation:** We will validate the effectiveness of EcoRoute by running a sample compute-heavy workload under two scenarios: a baseline (default CI/CD behavior) and with EcoRoute's scheduling. We will measure the resulting carbon emissions for each scenario using the Software Carbon Intensity (SCI) specification to quantify the savings.
*   **Dissemination:** The project will be open-sourced on GitHub with comprehensive documentation. We will create a presentation video to explain the concept and demonstrate its impact, fulfilling the project's social impact goal.

## 6. Open Research Questions

As we begin this project, we have identified several key questions to guide our research and development:

*   Is there an existing paper or project that actively uses the Carbon Aware SDK to schedule tasks in a production-like CI/CD environment?
*   How can we reliably convert the relative scores or ratings from the SDK into an absolute carbon estimate (e.g., in grams of CO₂) for a variety of scheduled tasks?
*   Is there a real need to automate the setup of the Carbon Aware SDK for users, and is it feasible to do so for a more seamless experience?
*   What are the barriers to adoption for tools like the Carbon Aware SDK in industry? Which companies currently use it, and which do not?
*   How can we accurately estimate the data transfer cost (in terms of energy and carbon) for moving a CI/CD job? Can we design a simple yet effective heuristic for this if a precise model is too complex?


## How can we reliably convert the relative scores or ratings from the SDK into an absolute carbon estimate (e.g., in grams of CO₂) for a variety of scheduled tasks?

A: Realistically, we can't. We can get the expected carbon emissions for a region and time per next consumed kwh from the SDK (or the mean marginal carbon intensity - how much carbon is expected to be emitted for the next kwh). But we can't really write a solution that can estimate the energy use for *any* task. If we have a very specific task, we can attempt such a calculation. But our tool is meant to work for any developer trying to use this for a myriad of tasks. It's not realistic to build a suite that basically takes in a script or entire codebase, and spits out an energy use estimate. 