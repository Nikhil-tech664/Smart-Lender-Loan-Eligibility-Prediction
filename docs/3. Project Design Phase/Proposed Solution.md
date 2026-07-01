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
| **Objective** | To automate the loan pre-qualification and eligibility prediction process using machine learning to replace slow, manual credit reviews. |
| **Scope** | Includes applicant data acquisition, pipeline data cleaning, machine learning model training, and a Flask web service for public eligibility checking. |

---

## Problem Statement

| Parameter | Details |
| :--- | :--- |
| **Description** | Traditional manual underwriting causes significant delays, inconsistencies, and high rejection rates for creditworthy applicants. |
| **Impact** | Increases customer churn, delays real-estate transactions, and leads to operational inefficiencies inside banking branches. |

---

## Proposed Solution

| Parameter | Details |
| :--- | :--- |
| **Approach** | Train a highly tuned Random Forest classifier alongside helper classifiers, and host them inside a responsive Flask micro-service. |
| **Key Features** | - Dark/Light mode theme toggle UI.<br>- Real-time validation error alerts.<br>- ML probability scoring combined with strict credit veto rules. |

---

## Resource Requirements

### Hardware Requirements
- **Computing Resources:** CPU/GPU for training (e.g. CPU or basic T4 GPU for training benchmarks).
- **Memory:** 8 GB RAM minimum.
- **Storage:** 1 TB SSD for development workspace, model checkpoints, and documentation assets.

### Software Requirements
- **Frameworks:** Python Flask Framework.
- **Libraries:** scikit-learn, pandas, numpy, matplotlib, seaborn.
- **Development Environment:** VS Code, Jupyter Notebook.

### Data Requirements
- **Data Source:** Kaggle Loan Prediction Dataset.
- **Size & Format:** 614 rows × 13 columns, CSV format.
