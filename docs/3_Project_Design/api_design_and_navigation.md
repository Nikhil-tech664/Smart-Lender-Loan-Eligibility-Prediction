# API Design and Navigation Flow

## 1. REST API Endpoint Specifications

### A. Home Route
* **Endpoint:** `GET /`
* **Response:** Renders the master SPA layout HTML index.

### B. Favicon Route
* **Endpoint:** `GET /favicon.ico`
* **Response:** Returns an empty body with HTTP 204 No Content to eliminate console warning flags.

### C. Health Check Route
* **Endpoint:** `GET /health`
* **Response:** JSON status payload verifying that `loan_model.pkl` is loaded and identifying the active classifier.

### D. Model Telemetry Route
* **Endpoint:** `GET /model-telemetry`
* **Response:** JSON payload detailing F1/accuracy benchmarks for all 6 models, dataset statistics, and feature importances.

### E. Risk Scoring Route
* **Endpoint:** `POST /predict`
* **Content-Type:** `application/json`
* **Request Payload:** JSON mapping of all 11 required applicant parameters.
* **Response Payload:** Returns JSON containing eligibility status, probability index, risk evaluation levels, and bulleted reasoning.

---

## 2. Screen Navigation Flow
The layout is designed as a high-speed Single Page Application (SPA). Users navigate fluidly via navbar hooks:

```
                            [ Navigation Bar ]
                                    |
          +-------------------------+-------------------------+
          v                         v                         v
 [ Predict Form ]          [ Analytics Modal ]        [ History Modal ]
  - Applicant inputs        - 6-Model table            - Search / Sort inputs
  - Real-time slider        - Confusion Matrix         - Filter approved
  - Scoring results         - ROC curves               - Reuse inputs
```
- **Modals:** Configured with Bootstrap glassmorphic backdrops that stack and close without page reloads.
- **Form State:** Features a 1-click **Reset Form** button to clear entries and collapse prior result cards instantly.
