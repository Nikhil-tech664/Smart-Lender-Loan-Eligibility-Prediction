# Requirement Traceability Matrix (RTM)

The matrix below maps identified system requirements directly to their implementation components and test cases:

| Req ID | Description | Source File / Implementation | Test Case ID | Status |
|---|---|---|---|---|
| **FR1** | Collect 11 applicant input fields | `templates/index.html` (Form tags) | `TC-001` (Validation Test) | Completed |
| **FR2** | Real-time ML prediction scoring | `app.py` (`/predict` POST endpoint) | `TC-002` (API Prediction test) | Completed |
| **FR3** | Underwriting Guardrails (Credit veto) | `app.py` (Guardrail conditional checks)| `TC-003` (Edge Case Rejection) | Completed |
| **FR4** | Decision Explanations & Advice | `app.py` (`explanations` list return) | `TC-004` (Insight Verification) | Completed |
| **FR5** | Analytics and Telemetry comparisons | `app.py` (`/model-telemetry` endpoint) | `TC-005` (Telemetry API Test) | Completed |
| **FR6** | History LocalStorage search/sort | `static/js/main.js` (`renderHistory()`) | `TC-006` (Local Storage Test) | Completed |
| **NFR1**| Low latency response (<25 ms) | `app.py` (Time evaluation calculation) | `TC-007` (Performance SLA Test)| Completed |
| **NFR2**| Mobile Responsive Interface | `static/css/style.css` (CSS media queries) | `TC-008` (Responsiveness Audit) | Completed |
