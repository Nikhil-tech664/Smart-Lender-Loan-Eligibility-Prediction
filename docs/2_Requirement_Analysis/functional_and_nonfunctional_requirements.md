# Functional and Non-Functional Requirements

## 1. Functional Requirements (FR)

### FR1: Applicant Data Collection
The system must provide a validated form interface to collect 11 demographic and financial fields: Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, and Property_Area.

### FR2: Real-time Scoring & Decision Pipeline
Upon form submission, the system must process parameters through a serialized preprocessor scaling pipeline and evaluate credit eligibility using the active machine learning model.

### FR3: Risk Override & Banking Guardrails
The system must enforce strict underwriting rule checks:
* Set verdict to **REJECTED** if Credit_History = `0.0`.
* Set verdict to **REJECTED** if Loan-to-Income ratio exceeds `8.0x`.
* Set verdict to **REJECTED** if DTI ratio exceeds `85%`.

### FR4: Insights and Explainable AI
Approved or Rejected applications must display contextual, bulleted explanations and actionable financial advice.

### FR5: Analytics Telemetry Modal
The system must query model benchmarks dynamically, displaying comparisons for accuracy, precision, recall, F1, and AUC across 6 models, alongside active model confusion matrices.

### FR6: Local History Management
The application must save up to 20 past results in the browser's local storage with interactive text search, sorting, and status filtering.

---

## 2. Non-Functional Requirements (NFR)

### NFR1: Performance & Latency
* The prediction API must execute and return decisions in under **25 milliseconds**.
* The application interface must be fully interactive in under 1 second.

### NFR2: Portability & Mobile Responsiveness
* The frontend must be fully responsive across mobile phones, tablets, and desktop resolutions.
* Supported browsers: Google Chrome, Apple Safari, Mozilla Firefox, Microsoft Edge.

### NFR3: Security
* Decouple sensitive application variables (e.g., debug modes, ports) using local environment variables.
* Enforce strict float and string validation checks to block injection payloads.
