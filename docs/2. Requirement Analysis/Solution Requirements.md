# Solution Requirements

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 4 Marks |

---

## Step 1: Functional Requirements (FR)

Functional requirements define specific behaviors, functions, or features the loan prediction system must perform.

| S.No | Requirement Category | Requirement Description | Priority (High/Medium/Low) |
| :--- | :--- | :--- | :--- |
| **1** | Authentication | The system should support optional user authentication or API key check for administrative dashboard access. | Medium |
| **2** | Authorization Levels | Standard applicants can access front-facing check portals. Administrators can view metrics logs and model versions. | Low |
| **3** | Input Form Validation | Frontend must validate input bounds (e.g. non-negative incomes, non-zero loan terms) before submission. | High |
| **4** | Prediction Engine | Flask backend must load the serialized ML model and compute eligibility status in real-time. | High |
| **5** | Veto Rules Engine | Backend must veto any applicant who has a credit history value of 0.0, returning a specific explanation. | High |
| **6** | JSON REST API | Exposure of an API endpoint `/predict` accepting application JSON datasets. | Medium |

---

## Step 2: Non-Functional Requirements (NFR)

Non-functional requirements specify the operational criteria that judge the quality of system behaviors.

| S.No | NFR Category | Requirement Description | Target Metric / Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **1** | Performance & Speed | Response time for prediction calculations must be sub-second to prevent UI lag. | Prediction API response < 200ms under normal load. |
| **2** | Scalability | System must handle concurrent applicant requests without scaling degradation. | Support up to 1,000 concurrent user sessions. |
| **3** | Security & Data Privacy | Personal and financial details submitted must be protected during transit. | HTTPS encryption and CORS policy restrictions. |
| **4** | Reliability & Availability | The prediction engine must be online and functional at all times. | 99.9% uptime for the REST prediction service. |
| **5** | Usability & Accessibility | UI must be responsive across standard desktop, tablet, and mobile browsers. | Responsive CSS grid layout matching modern mobile viewports. |
| **6** | Maintainability | ML models can be swapped out easily without rebuilding frontend assets. | Pickle model decoupled from Flask route configurations. |
