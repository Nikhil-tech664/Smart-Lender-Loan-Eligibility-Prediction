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
|  - Web UI Panel (index.html, style.css)                   |
|  - AJAX Fetch controller (main.js)                        |
+-----------------------------------------------------------+
                             | |
                             | | (JSON REST Request/Response)
                             v v
+-----------------------------------------------------------+
|                 API GATEWAY / ROUTING LAYER               |
|  - Flask Application Server (`app.py`)                    |
|  - Input Validation & Error Payload Controller            |
+-----------------------------------------------------------+
                             | |
                             | | (Scaled Feature DataFrame)
                             v v
+-----------------------------------------------------------+
|                     CORE SERVICE LAYER                    |
|  - LabelEncoder & StandardScaler preprocessing           |
|  - Random Forest Classifier probability check             |
|  - Rules Guardrails Veto Logic (Credit history checks)     |
+-----------------------------------------------------------+
                             | |
                             | | (Load Preprocessor/Model)
                             v v
+-----------------------------------------------------------+
|                    DATA / STORAGE LAYER                   |
|  - joblib Model Storage (`model/loan_model.pkl`)          |
|  - Synthetic Dataset repository (`dataset/loan_data.csv`) |
+-----------------------------------------------------------+
```

---

## Component Description Table

Define the roles and responsibilities of each architectural component.

| Component Name | Description / Role in Architecture | Technologies Used |
| :--- | :--- | :--- |
| **Presentation Layer** | Serves as the interactive form frontend, implementing visual loaders and dark/light toggles. | HTML5, CSS Variables, JavaScript |
| **API Gateway** | Manages routing endpoints (`/`, `/health`, `/predict`, `/model-telemetry`), parsing JSON input payloads. | Flask Routing |
| **Core Services** | Preprocesses raw inputs using StandardScaler, handles categorical label conversions, and checks veto conditions. | Python, Pandas, NumPy, scikit-learn |
| **Database / Storage** | Stores pre-calculated encoders, scalers, best model artifacts, and evaluation telemetry metrics. | joblib Serialization |
