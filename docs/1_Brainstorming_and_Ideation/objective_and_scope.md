# Objective and Scope

## 1. Project Objective
The core objective of **SmartLender AI** is to design, develop, test, and deploy a secure, responsive, and highly accurate web-based automated underwriting engine. The system integrates standard demographic and financial data points of applicants and applies machine learning classifier models to evaluate credit solvency in under 25 milliseconds.

## 2. Scope of Implementation
* **Machine Learning Pipeline:** Trains and evaluates 6 predictive models (Logistic Regression, Decision Tree, Random Forest, KNN, SVM, Gradient Boosting). Implements automated pipeline scaling and standard LabelEncoding.
* **Underwriting Guardrails:** Enforces institutional guidelines (such as strict rejections for bad credit history, high loan-to-income ratios, and extreme debt-to-income ratios).
* **Flask Web Services:** Lightweight REST API serving prediction endpoints and analytics telemetries.
* **Responsive Frontend Dashboard:** Modern UI/UX interface supporting dark mode toggles, micro-animations, local history search/filter/sort, and PDF/CSV/JSON export tools.

## 3. Exclusions from Scope
* **Direct Credit Bureau Integration:** Historical credit data is passed via manual form parameters or mock API payloads rather than live Equifax/Experian connections.
* **Automated Capital Disbursement:** The app provides underwriting eligibility decisions; actual capital transfer is excluded from the current build.
