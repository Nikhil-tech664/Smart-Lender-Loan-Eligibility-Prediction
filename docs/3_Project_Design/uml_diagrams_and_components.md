# Use Case, Sequence, and Component Diagrams

## 1. Use Case Diagram
The primary actors and their interactions with the system modules:

```
                  +----------------------------------------------+
                  |               SmartLender AI                 |
                  |                                              |
 (Applicant) ---->| -- Input Applicant Details                   |
                  | -- View Eligibility Verdict & Explanations   |
                  | -- Export Results (PDF, CSV, JSON)           |
                  |                                              |
 (Risk Manager) ->| -- View 6-Model Comparative Telemetries      |
                  | -- View Model Matrix Visualizations          |
                  | -- Inspect Application History               |
                  +----------------------------------------------+
```

---

## 2. Sequence Diagram (Real-Time Scoring Execution)
Traces the chronological exchange of messages between key components during a prediction:

```
[Browser Client]     [Flask app.py]      [Preprocessor]     [Model Agent]
       |                   |                   |                  |
       |--- POST/predict ->|                   |                  |
       |                   |--- fit_transform >|                  |
       |                   |<-- scaled array --|                  |
       |                   |------------------ predict_proba ---->|
       |                   |<----------------- return [prob] -----|
       |                   |-- Guardrail Check |                  |
       |<-- return JSON ---|                   |                  |
```
*Latency Target:* Total duration across all steps must remain under **25ms**.
