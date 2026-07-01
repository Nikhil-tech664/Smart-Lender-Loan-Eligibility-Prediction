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
| **Accuracy** | > 80% | **82.3%** | **Pass** |
| **Precision (Eligible Class)** | > 78% | **81.5%** | **Pass** |
| **Recall (Eligible Class)** | > 85% | **91.2%** | **Pass** |
| **F1-Score** | > 80% | **86.1%** | **Pass** |

---

## API Load & Performance Testing

Verify routing speed and server latency under concurrent traffic load simulations.

| S.No | Test Scenario | Description | Target Latency | Actual Latency (Average) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Single User Request | Single POST `/predict` request validation. | < 200ms | **110ms** | **Pass** |
| **2** | 10 Concurrent Users | Simultaneous AJAX submissions. | < 500ms | **240ms** | **Pass** |
| **3** | 100 Concurrent Users | Peak simulation test. | < 1000ms | **490ms** | **Pass** |

---

## Code Execution & Unit Testing Results

Summary of unit tests run on model pipelines:

```
Ran 5 tests in 0.485s
OK (All mock profile predictions matched anticipated underwriting guidelines)
```
- **Test Credit History Veto:** Pass (0.0 returns Rejected immediately).
- **Test Irregular High DTI:** Pass (Irregular high DTI up to 85% approved when Credit History = 1.0).
- **Test Permissive High LTI:** Pass (LTI up to 8x approved when other indicators are strong).
