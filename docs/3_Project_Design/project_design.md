# SmartBridge SDLC Phase 3: Project Design

## 1. Solution Architecture & Workflows
The Smart Lender application adopts a modular multi-layer operational pattern separating interface presentation, application routing, and machine learning inference components.

```
+-------------------------------------------------------+
|                   Client Web Browser                  |
|          (HTML5 / Bootstrap 5 / Vanilla JS)           |
+-------------------------------------------------------+
                           |
                     HTTP POST /predict (JSON)
                           v
+-------------------------------------------------------+
|                     Flask Backend                     |
|           (Input Validation & Route Controller)        |
+-------------------------------------------------------+
                           |
                Feature Extraction & Transformation
                           v
+-------------------------------------------------------+
|                  Scikit-Learn Pipeline                |
|  (StandardScaler -> LabelEncoder -> RandomForest)     |
+-------------------------------------------------------+
                           |
                   JSON Response Payload
                           v
+-------------------------------------------------------+
|                  Dynamic UI Update                    |
|          (Eligibility Badge & Progress Meter)         |
+-------------------------------------------------------+
```

## 2. Component Design Specifications
- **Data Pipeline Module (`train_model.py`):** Responsible for synthetic dataset generation, automated missing value handling, label encoding, standard feature scaling, model selection benchmarks, and model artifact serialization (`loan_model.pkl`).
- **Web Backend Module (`app.py`):** Flask controller managing application context, health endpoints, cross-origin request policies, and predictive evaluation endpoints.
- **Presentation Module (`index.html`, `style.css`, `main.js`):** Responsive interface implementing CSS custom variables for dark/light mode execution and AJAX asynchronous communication.
