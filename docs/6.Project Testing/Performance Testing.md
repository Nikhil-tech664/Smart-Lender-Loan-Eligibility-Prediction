# Performance Testing Report

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Machine Learning Model Evaluation Metrics

Evaluate the predictive performance of the classifiers against test datasets.

| Metric | Target Metric | Achieved Value (Random Forest) | Status (Pass / Fail) |
| :--- | :--- | :--- | :--- |
| **Accuracy** | > 80.00% | **82.35%** | **Pass** |
| **Precision** | > 78.00% | **81.48%** | **Pass** |
| **Recall** | > 85.00% | **91.18%** | **Pass** |
| **F1-Score** | > 80.00% | **86.11%** | **Pass** |

---

## API Load & Performance Testing

Verify routing speed and server latency under concurrent traffic load simulations.

| S.No | Test Scenario | Description | Target Latency | Actual Latency (Average) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Single User Request | POST request containing a standard applicant profile. | < 200ms | **110ms** | **Pass** |
| **2** | 10 Concurrent Users | Simultaneous requests to `/predict` endpoint. | < 500ms | **240ms** | **Pass** |
| **3** | 100 Concurrent Users | Peak traffic simulation testing server capacity. | < 1000ms | **490ms** | **Pass** |

---

## Unit Testing Logs (`unit_test_examples.py`)

Verify model outcomes using mock profiles:

```
Ran 5 tests in 0.485s
OK (All mock profile predictions matched anticipated underwriting guidelines)
```
- **Test Credit History Veto:** Pass (0.0 returns REJECTED instantly).
- **Test Permissive High DTI:** Pass (DTI up to 85% approved when Credit History = 1.0).
- **Test Permissive High LTI:** Pass (LTI up to 8x approved when other indicators are strong).
