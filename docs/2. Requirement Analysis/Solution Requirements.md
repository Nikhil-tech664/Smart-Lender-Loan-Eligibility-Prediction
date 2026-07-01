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
| **1** | Input Processing | The Flask application must parse 11 input attributes: Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, and Property_Area. | High |
| **2** | Label Encoding | Backend must load the pre-trained LabelEncoder dictionaries to transform categorical labels (e.g. Property_Area = "Semiurban" to encoded value) dynamically. | High |
| **3** | Underwriting Safeguards | Backend must veto any applicant who has a credit history of 0.0, a Loan-to-Income ratio > 8.0, or an estimated monthly Debt-to-Income ratio > 85.0, capping their approval probability at 32.50%. | High |
| **4** | Telemetry Feed | Expose a `/model-telemetry` endpoint returning the classifier statistics, features importances, and relative model comparison charts. | Medium |
| **5** | Dynamic Result Presentation | The UI must display explicit explanation bullets detailing positive factors (stable education, low DTI) and risk flags (no co-applicant, bad credit history). | High |

---

## Step 2: Non-Functional Requirements (NFR)

Non-functional requirements specify the operational criteria that judge the quality of system behaviors.

| S.No | NFR Category | Requirement Description | Target Metric / Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **1** | Performance & Speed | The prediction endpoint response latency must be minimal. | Average calculation time under 200 milliseconds. |
| **2** | Predict Accuracy | The serialized classifier model must maintain high predictive power on unseen data. | Model F1-Score exceeding 80% on standard test sets. |
| **3** | Portability | Decouple scaling parameters and label encoders from standard configurations. | Store preprocessors in a single serialized `loan_model.pkl` artifact. |
| **4** | UI Responsiveness | Interface must adjust layout grids automatically between high-res monitors and mobile screen dimensions. | Complies with modern mobile viewports (minimum width 320px). |
| **5** | Security & Integrity | Input parameters must be validated before scaling. | Prevent server exceptions by returning validation error JSON (status code 400). |
