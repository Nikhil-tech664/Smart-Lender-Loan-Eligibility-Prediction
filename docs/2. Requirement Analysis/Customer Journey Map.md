# Customer Journey Map

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 2 Marks |

---

## Customer Journey Map Table

Map out the applicant's experience step-by-step when applying for a loan eligibility assessment using SmartLender AI.

| Phase of Journey | Stage 1: Landing & Exploration | Stage 2: Form Input & Validation | Stage 3: Instant Decision |
| :--- | :--- | :--- | :--- |
| **Actions**<br>*What does the customer do?* | - Navigates to the web portal.<br>- Views the dynamic statistics header.<br>- Evaluates their ready documentation. | - Fills in personal details (Married, Education).<br>- Uses sliders to set Income ($3,500) and Term (360).<br>- Triggers "Evaluate Eligibility". | - Monitors the stepped loading checklist.<br>- Receives the APPROVED/REJECTED card.<br>- Reads explanations (e.g. Credit History Veto). |
| **Touchpoint**<br>*What part of the service do they interact with?* | - Clean dark/light toggle header.<br>- Hero counter cards (95%+ accuracy, <25ms latency). | - Dynamic form inputs.<br>- Range slider synchronization widgets. | - Multistage status stepper.<br>- Structured result panel with custom recommendations. |
| **Customer Thought**<br>*What is the customer thinking?* | - "Is my private financial data secure?"<br>- "Is this portal fast enough?" | - "Do I need to include my co-applicant's income?"<br>- "How does the Loan Term affect my DTI?" | - "Why was my application flagged as High Risk?"<br>- "I can reduce my loan amount to check again!" |
| **Customer Feeling**<br>*What is the customer feeling?* | - Curious and hopeful. | - Engaged but cautious about numeric ranges. | - Clear understanding of the outcome and empowered to retoggle. |
| **Process Ownership**<br>*Who is in the lead on this?* | - UI Front-End (HTML/CSS). | - Frontend Validation Script (`main.js`). | - Flask Backend (`app.py` & `loan_model.pkl`). |
| **Opportunities**<br>*How can we improve this stage?* | - Add tooltips describing property areas (Semiurban vs Rural). | - Impute missing values locally before submission. | - Provide a print button for qualified pre-approval. |
