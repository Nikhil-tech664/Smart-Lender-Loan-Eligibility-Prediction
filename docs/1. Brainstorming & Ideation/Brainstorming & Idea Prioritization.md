# Brainstorming & Idea Prioritization

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Step 1: Brainstorm and Idea Listing

Identify potential solutions, components, and enhancements for the automated loan eligibility prediction system.

| S.No | Idea Category | Description / Proposed Idea | Focus Area |
| :--- | :--- | :--- | :--- |
| **1** | Machine Learning | Train a Random Forest Classifier and scale categorical inputs using a robust scikit-learn LabelEncoder pipeline. | Model Predictive Power |
| **2** | Rules Safeguards | Add a strict credit veto module in the Flask app to instantly reject Credit_History = 0.0 profiles, mimicking real bank risk limits. | Risk Management |
| **3** | Dynamic Telemetry | Build a backend `/model-telemetry` endpoint to feed the model accuracy, training duration, and feature importance to the frontend. | System Transparency |
| **4** | UI Theme Control | Build a lightweight theme toggler between Dark Mode (deep blue/slate) and Light Mode (clean gray) using CSS variables. | Interface Ergonomics |
| **5** | Stepped AI Loader | Create a multi-stage loading animation during POST requests to outline the AI evaluation phases to the user. | User Engagement |

---

## Step 2: Idea Prioritization

Evaluate the brainstorming ideas against feasibility and importance metrics to select the core features for implementation.

| S.No | Idea | Feasibility (1-5) | Importance (1-5) | Priority Rank | Selected (Yes / No) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Multi-Classifier Pipeline (RF, GB, SVM, KNN) | 5 | 5 | 1 | **Yes** |
| **2** | Hard Cutoff Credit Underwriting Veto Rules | 5 | 5 | 1 | **Yes** |
| **3** | Responsive Glassmorphism Input Form | 5 | 4 | 2 | **Yes** |
| **4** | Real-Time Telemetry and Insights REST Endpoint | 4 | 5 | 2 | **Yes** |
| **5** | Stepped Loader Visual Feedback | 5 | 4 | 3 | **Yes** |
