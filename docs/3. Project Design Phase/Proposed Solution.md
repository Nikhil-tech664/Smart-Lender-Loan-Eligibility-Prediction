# Proposed Solution Report

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Project Overview

| Parameter | Details |
| :--- | :--- |
| **Objective** | Develop an automated credit evaluation and decision system using scikit-learn classifiers and Flask to provide real-time loan eligibility predictions. |
| **Scope** | Includes preprocessing data pipelines, model optimization, underwriting rules integration, and responsive dark/light mode frontends. |

---

## Problem Statement

| Parameter | Details |
| :--- | :--- |
| **Description** | Manual lending desks create transaction backlogs, lack consistency, and result in false rejections for qualified non-traditional applicants. |
| **Impact** | Increases customer dropouts, leads to lost commission revenue, and increases administrative processing costs. |

---

## Proposed Solution

| Parameter | Details |
| :--- | :--- |
| **Approach** | Build a unified ML service loaded from joblib binaries. Check applicant profiles through a combined rules veto and Random Forest probability engine. |
| **Key Features** | - Dynamic sliders for Applicant Income ($100 - $81,000) and Loan Amount ($10 - $700k).<br>- Instant status cards with confidence classifications (Low Risk vs High Risk). |

---

## Resource Requirements

### Hardware Requirements
- **Computing Resources:** CPU/GPU training resources (standard multi-core CPU is sufficient for training the 6 classification algorithms in seconds).
- **Memory:** 8 GB DDR4 RAM.
- **Storage:** 200 MB disk space for code files, data, and serialized pickle files.

### Software Requirements
- **Frameworks & Libraries:** Python 3.9+, Flask, scikit-learn, joblib, pandas, numpy, matplotlib, seaborn.
- **Development Tooling:** VS Code, Git, Chrome DevTools.

### Data Requirements
- **Data Source:** Synthetic dataset mimicking standard Kaggle Loan Prediction criteria.
- **Attributes:** 614 rows containing 11 features and 1 label column.
