# No. of Functional Features Included in the Solution

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Functional Features Overview

Detail the actual core features implemented in the final SmartLender AI web application.

| S.No | Feature Name | Feature Description | Module / Component | Status (Done / In Progress / Pending) | Marks Contribution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | User Input Form | Standard HTML input fields for Gender, Married, Dependents, Education, Self-Employed, Incomes, Loan details. | Frontend (index.html) | **Done** | 1 Mark |
| **2** | Dark/Light Mode | Theme toggle button allowing dynamic transitions between banking dark/light themes. | Frontend (style.css/main.js) | **Done** | 1 Mark |
| **3** | REST API Backend | Endpoint `/predict` processing incoming parameters and returning prediction probabilities. | Backend (app.py) | **Done** | 1 Mark |
| **4** | ML Preprocessing | Input scaler pipelines to impute null values and scale parameters dynamically. | ML Model (loan_model.pkl) | **Done** | 1 Mark |
| **5** | Credit History Veto | Safeguard routing to reject applicants with Credit History of 0.0 directly. | Rules Engine (app.py) | **Done** | 1 Mark |

---

## Feature Summary

Summarize implementation count statistics:

| Metric | Count / Value |
| :--- | :--- |
| **Total Features Planned** | 5 |
| **Total Features Implemented** | 5 |
| **Core / Must-Have Features** | 4 |
| **Additional / Nice-to-Have Features** | 1 |
| **Features Tested & Verified** | 5 |

---

## Feature Category Breakdown

Break down the features into standard logical architectural areas:

| S.No | Category | Features in Category | Example Features |
| :--- | :--- | :--- | :--- |
| **1** | User Interface (UI) | Form entries, Theme toggle buttons, Result display card. | responsive CSS grid layouts, AJAX loader spinner. |
| **2** | Backend / Logic | Flask app router, request parser, preprocessor triggers. | numerical conversion, JSON response assembler. |
| **3** | Database / Storage | joblib model cache directories. | load pre-compiled pipeline. |
| **4** | API / Integration | POST `/predict` REST endpoint. | AJAX fetch request connector. |
| **5** | Security / Authentication | Underwriting credit rules and DTI verification vetos. | credit check interceptor. |
