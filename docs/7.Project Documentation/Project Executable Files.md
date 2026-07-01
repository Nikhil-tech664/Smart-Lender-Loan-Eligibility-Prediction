# Project Executable Files

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Executable Components & Directory List

This document lists all active executable modules, models, source code, and configurations present in the repository.

| S.No | File Name | Path | Component Type | Purpose / Description |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `app.py` | `/app.py` | Python Script | Primary Flask web server containing routes, validation, and veto logic. |
| **2** | `train_model.py` | `/train_model.py` | Python Script | Model training pipeline that generates the synthetic dataset and pickles the artifact. |
| **3** | `config.py` | `/config.py` | Python Script | Global configuration mappings (paths, port numbers, debug toggles). |
| **4** | `loan_model.pkl` | `/model/loan_model.pkl` | Model Artifact | joblib binary file caching scaler, label encoders, and best Random Forest model. |
| **5** | `index.html` | `/templates/index.html` | UI Template | HTML input form page containing theme controls and slides. |
| **6** | `style.css` | `/static/css/style.css` | UI Style | CSS variables styling the dark/light layouts. |
| **7** | `main.js` | `/static/js/main.js` | UI Logic | Script handling fetch requests, loaders, and rendering output logs. |
