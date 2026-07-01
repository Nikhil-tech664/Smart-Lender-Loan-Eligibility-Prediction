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
| **1** | Interactive Input Form | Responsive inputs including income sliders, property areas, and dependent counts. | Frontend UI | **Done** | 1 Mark |
| **2** | Dark/Light Mode Theme | Instant CSS theme switches with glowing underlines and glassmorphism cards. | Frontend Styles | **Done** | 1 Mark |
| **3** | ML Telemetry Dashboard | Renders classifiers benchmarks, model parameters, and feature importances. | Frontend & API | **Done** | 1 Mark |
| **4** | Underwriting Rules veto | Hard rejection intercepts for Credit History = 0.0 and DTI > 85%. | Backend Logic | **Done** | 1 Mark |
| **5** | Model Serialization | Serializes StandardScalers, LabelEncoders, and Classifiers in one object. | ML Pipeline | **Done** | 1 Mark |

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
| **1** | User Interface (UI) | Form layouts, Mode toggles, Stepped progress loader. | dark/light toggling, AJAX fetch animations. |
| **2** | Backend / Logic | Flask route mapping, error intercepts, telemetry feeds. | `/predict` API request decoding. |
| **3** | Database / Storage | joblib caching directories. | serialized preprocessors storage. |
| **4** | API / Integration | REST `/predict` JSON endpoints. | dynamic AJAX response bindings. |
| **5** | Security / Quality | Input boundary checks, validation parameters. | negative number value preventions. |
