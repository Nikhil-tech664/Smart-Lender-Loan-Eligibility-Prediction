# Data Flow Diagram and Flowcharts

## 1. Level 0 Data Flow Diagram (DFD)
The DFD below describes the flow of telemetry parameters from the applicant interface to the backend and back:

```
+---------------+      11 Inputs Payload      +---------------+
|   Applicant   | --------------------------> |  SmartLender  |
|  Web Console  | <-------------------------- |  REST Backend |
+---------------+     Predict Output JSON     +---------------+
```

---

## 2. Level 1 Data Flow Diagram (DFD)
A detailed view of how inputs traverse the system, passing through preprocessors, model evaluators, and underwriting guardrails:

```
 [ Form Input ]
       |
       v
 [ Type Validation ] ---> (If fail: Return HTTP 400 Bad Request)
       |
       v
 [ Label Encoding ]  ---> (Gender, Married, Dependents, Education, etc.)
       |
       v
 [ StandardScaler ]  ---> (Apply fitted mean & variance)
       |
       v
 [ Model Inference ] ---> (Query best trained classifier object)
       |
       v
 [ Underwriting Vetoes ] -(If credit_history == 0.0 or DTI > 85%): Override Approved to REJECTED
       |
       v
 [ Return JSON Payload] -> (Send status, probability, time_ms, explanations)
```
