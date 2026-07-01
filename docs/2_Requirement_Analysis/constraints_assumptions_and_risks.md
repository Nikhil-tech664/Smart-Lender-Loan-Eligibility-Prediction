# Constraints, Assumptions, and Risks

## 1. Project Constraints
* **Local State Memory:** History and logs are maintained inside browser-based LocalStorage rather than an external database, limiting data persistence to individual browser environments.
* **CPU Inference:** Preprocessing and model classification are processed on standard CPUs. Heavy GPU architectures (e.g. PyTorch deep learning models) are excluded.

## 2. Development Assumptions
* **Applicant Data Formats:** Assumes applicants input realistic numerical figures (non-negative incomes and strictly positive loan amounts).
* **Credit Status Suffixes:** Assumes the user enters a valid numeric indicator (`1.0` or `0.0`) for credit history compliance matching the training distributions.

## 3. Risk Assessment and Mitigation Plans

| Identified Risk | Impact | Likelihood | Mitigation Strategy |
|---|---|---|---|
| **Pipeline Drift:** Model trained on synthetic data performs poorly on live applicant profiles. | High | Medium | Implemented a periodic retraining pipeline script (`train_model.py`) to easily refresh saved preprocessors and metrics. |
| **Input Type Crashes:** String values passed to mathematical inputs trigger runtime errors. | Critical | Low | Added explicit JS client-side input restrictions and Flask try-except type coercion filters. |
| **Model Drift/Loss ofpkl:** Serialized classifier is corrupted or deleted. | Critical | Low | Implemented automatic health route flags and a fallback loader fallback. |
