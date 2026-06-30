# SmartLender AI – World-Class Automated Loan Eligibility Engine

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green.svg)](https://flask.palletsprojects.com/)
[![SDLC Standard](https://img.shields.io/badge/SDLC-SmartBridge%20Verified-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

SmartLender AI is a production-grade, enterprise-ready automated loan underwriting platform built under the SmartBridge Software Development Life Cycle (SDLC) framework. It evaluates loan solvency risk using high-accuracy machine learning classifiers and provides detailed underwriting explanations.

---

## 🌟 Key Features
- **Instant Loan Eligibility Assessment:** Evaluates applicant solvency risk using trained Random Forest, Logistic Regression, Gradient Boosting, SVM, KNN, and Decision Tree models.
- **Why Approved / Rejected Explanations:** Provides rule-based domain explanations breakdown (e.g., Credit History compliance, Income-to-Loan ratios).
- **Smart Financial Insights:** Dynamic financial metrics based on applicant income ratios ($ USD).
- **Model Telemetry Dashboard:** Live modal displaying accuracy, F1 score, ROC-AUC metrics, dataset stats, and visualization galleries (`feature_importance.png`, `confusion_matrix.png`, etc.).
- **Application History Memory:** Stores the last 10 applicant evaluations in browser `localStorage` with a 1-click input reuse feature.
- **Export Capabilities:** Export risk evaluation reports to JSON or trigger instant printing.
- **Glassmorphism UI/UX:** Premium dark navy banking theme (`#0b1329`) with Bootstrap 5, floating labels, animated stepped loader, ambient blobs, and theme toggling.

---

## 🏗 System Architecture
```
[Client UI Form] ---> [POST /predict] ---> [Flask Controller] ---> [StandardScaler & LabelEncoder] ---> [ML Model Artifact] ---> [Structured JSON Response]
```

---

## 📁 Repository Structure
```text
Loan-Eligibility-Prediction/
├── README.md                           # Master documentation
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
├── LICENSE                             # MIT License
├── app.py                              # Flask backend server with telemetry endpoints
├── train_model.py                      # Training script and model artifact generator
├── config.py                           # Application configuration manager
├── dataset/                            # Loan prediction dataset storage
├── model/                              # Serialized joblib model artifacts
├── templates/                          # HTML5 templates with telemetry & history modals
├── static/                             # CSS styling, JavaScript controller & screenshot gallery
├── docs/                               # SmartBridge SDLC 8-phase documentation
├── testing/                            # Automated Pytest/Unittest suite
├── deployment/                         # Deployment guide (Render, Gunicorn, Ngrok, Railway)
└── presentation/                       # Slide deck presentation outline
```

---

## 🚀 Execution Instructions

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train Machine Learning Pipeline & generate model artifacts
python train_model.py

# 3. Launch Flask Server
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

---

## ☁️ Deployment Guide
- **Production Server (Gunicorn WSGI):** `gunicorn --workers 4 --bind 0.0.0.0:5000 app:app`
- **Cloud Deployment (Render / Railway):** See `deployment/deployment_guide.md` for complete build instructions.
