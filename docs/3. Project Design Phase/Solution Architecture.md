# Solution Architecture

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Solution Architecture Diagram

Replicate the structural layout to map the presentation, application gateway, core logic, and storage systems.

```
+-----------------------------------------------------------+
|                 PRESENTATION / CLIENT LAYER               |
|  - Web UI Panel (Responsive HTML5 / Vanilla CSS3)         |
|  - AJAX Fetch Request Handler (Vanilla JavaScript ES6)    |
+-----------------------------------------------------------+
                             | |
                             | | (JSON REST Request/Response)
                             v v
+-----------------------------------------------------------+
|                 API GATEWAY / ROUTING LAYER               |
|  - Flask Application Server (`app.py` routing engine)     |
|  - Input Validation & Error Handling Middleware           |
+-----------------------------------------------------------+
                             | |
                             | | (Preprocessed Vector)
                             v v
+-----------------------------------------------------------+
|                     CORE SERVICE LAYER                    |
|  - Machine Learning Predictor (Random Forest Model)        |
|  - Underwriting Rules Engine (Credit History Veto)        |
+-----------------------------------------------------------+
                             | |
                             | | (Load Preprocessor/Model)
                             v v
+-----------------------------------------------------------+
|                    DATA / STORAGE LAYER                   |
|  - Model Storage (`model/loan_model.pkl` cache)          |
|  - Logs / Analytics File Stores                           |
+-----------------------------------------------------------+
```

---

## Component Description Table

Define the roles and responsibilities of each architectural component.

| Component Name | Description / Role in Architecture | Technologies Used |
| :--- | :--- | :--- |
| **Presentation Layer** | Renders the applicant form, dark/light theme switch, AJAX results display. | HTML5, CSS3, JavaScript (Fetch API) |
| **API Gateway** | Directs client URL requests to specific controller routes, validating request headers. | Flask Route Controllers |
| **Core Services** | Performs numerical scaling, processes prediction metrics, and implements logic vetos. | Python, scikit-learn, joblib |
| **Database / Storage** | Serializes the trained Random Forest classifier model and feature scalers. | joblib (.pkl) storage |
