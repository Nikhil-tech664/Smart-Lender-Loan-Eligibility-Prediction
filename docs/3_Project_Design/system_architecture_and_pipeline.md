# System Architecture and Machine Learning Pipeline

## 1. System Architecture Design
The architecture of **SmartLender AI** follows a decoupled, client-server design pattern for low-latency web operations:

```
+-----------------------------------------------------------+
|                      CLIENT BROWSER                       |
|  - HTML5 & CSS3 Glassmorphism UI                          |
|  - JavaScript Controller (Dynamic Sync, Form Validations) |
|  - LocalStorage State Manager (History History, Search)   |
|  - Chart.js Dashboard Render                              |
+-----------------------------------------------------------+
                             |
                   HTTP GET / POST Request
                             v
+-----------------------------------------------------------+
|                       FLASK BACKEND                       |
|  - app.py (REST Endpoints, JSON Inputs Parsing)           |
|  - config.py (App Port/File Path Telemetry)               |
+-----------------------------------------------------------+
                             |
                     Joblib Model Query
                             v
+-----------------------------------------------------------+
|                 MACHINE LEARNING ARTIFACT                 |
|  - loan_model.pkl (Optimized Gradient Boosting Classifier) |
|  - Serialized preprocessors (scaler, LabelEncoders)       |
+-----------------------------------------------------------+
```

---

## 2. Machine Learning Pipeline Architecture
The training pipeline (`train_model.py`) executes 6 distinct operational stages to ensure zero data leakage and high model reliability:

1. **Synthetic Data Generation:** Generates a structured tabular dataset of 614 samples mimicking lending demographics and financial parameters.
2. **Missing Values Imputation:** Imputes missing strings using category modes, and missing numeric elements using target feature medians.
3. **Categorical Encoding:** Applies individual Scikit-learn LabelEncoders to categorical properties to convert text into numeric mappings.
4. **Feature Scaling:** Scales numeric attributes (Applicant Income, Co-applicant Income, Loan Amount, Tenure, Credit History, Property Area) using a StandardScaler.
5. **Model Evaluation Matrix:** Trains 6 algorithms (Logistic Regression, Decision Tree, Random Forest, KNN, SVM, Gradient Boosting) on scaled vectors.
6. **Serialization:** Selects the model with the highest F1-score and serializes the model object, encoders, and scaler into `loan_model.pkl`.
