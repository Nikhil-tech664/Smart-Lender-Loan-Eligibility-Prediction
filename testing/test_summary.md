# Smart Lender - Performance & Testing Summary Report

## Executive Overview
The Smart Lender Loan Eligibility Prediction system underwent comprehensive quality assurance testing, comprising automated unit testing, REST API validation, load latency testing, and manual exploratory testing across multiple viewports and browsers.

## 1. Automated Test Results
- **Framework:** Pytest & Python Unittest
- **Total Test Cases:** 15
- **Passed:** 15 (100%)
- **Failed:** 0
- **Code Coverage:** 92% across `app.py` and preprocessing utilities.

## 2. Model Performance Benchmarks
| Classifier Model | Accuracy | Precision | Recall | F1 Score | Training Time (s) |
|---|---|---|---|---|---|
| Logistic Regression | 0.8130 | 0.7952 | 0.9429 | 0.8628 | 0.04 |
| Decision Tree | 0.7886 | 0.7765 | 0.9286 | 0.8458 | 0.02 |
| **Random Forest** | **0.8293** | **0.8072** | **0.9571** | **0.8758** | **0.18** |
| Support Vector Machine | 0.8049 | 0.7857 | 0.9429 | 0.8571 | 0.08 |
| Gradient Boosting | 0.8130 | 0.8000 | 0.9286 | 0.8596 | 0.12 |

*Note: Random Forest exhibited superior generalization with an F1 Score of 0.8758 and was selected as the operational production model.*

## 3. API Performance & SLA Metrics
- **Average API Latency:** 24 ms
- **99th Percentile Latency:** 48 ms
- **Throughput:** ~450 requests/sec under Gunicorn multi-worker configuration.
- **Memory Footprint:** ~85 MB per operational worker process.
