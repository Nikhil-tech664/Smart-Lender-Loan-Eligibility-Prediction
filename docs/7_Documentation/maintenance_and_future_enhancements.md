# Maintenance and Future Enhancements Guide

## 1. Routine Maintenance Actions
To ensure the long-term stability of the **SmartLender AI** application:
* **Model Retraining:** Re-run `train_model.py` periodically when new, verified loan application datasets become available.
* **Dependency Upgrades:** Keep security patches up to date by checking the versions in `requirements.txt`.
* **Telemetry Visualizations:** Verify that EDA plots in `static/screenshots/` refresh cleanly after retraining.

---

## 2. Future System Enhancements
The following features are planned for future versions of the platform:
* **Live Credit Bureau Integrations:** Connect the system directly to credit bureaus (e.g. Experian, Equifax) via REST APIs to pull credit scores automatically instead of relying on manual form fields.
* **Explainable AI Integration (SHAP/LIME):** Implement SHAP or LIME force plots to display detailed visual explanations for individual applicant predictions.
* **Multi-Factor Authentication (MFA):** Integrate security controls to protect applicant records and ensure compliance with financial regulations.
