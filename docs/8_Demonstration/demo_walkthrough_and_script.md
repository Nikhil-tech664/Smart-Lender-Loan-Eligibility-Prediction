# Demo Walkthrough and Script

Use this step-by-step guide to run a live demonstration of **SmartLender AI**:

## 1. Scene 1: Welcome and Hero Dashboard
* **Action:** Open your browser and navigate to `http://127.0.0.1:5000` (or your live Render URL).
* **Script:** *"Welcome to SmartLender AI, an automated risk assessment and underwriting engine designed to evaluate loan applicants. The home dashboard features a premium glassmorphic layout, background animated blobs, and a quick-action 'Start Evaluation' button."*
* **Highlight:** Point out the floating statistics cards: `95%+ Model Accuracy` and `<25 ms Prediction Latency`.

---

## 2. Scene 2: Submitting an Application (Approval Case)
* **Action:** Scroll to the form section. Enter: Income = `5000`, Co-applicant = `2000`, Loan Amount = `150`, Term = `360`, Credit History = `Guidelines Fully Met`, Property = `Semiurban`. Click **Run Risk Assessment**.
* **Script:** *"We will submit a qualified applicant profile. The stepped loader simulates real-time banking risk checks. Upon execution, you will see a green banner indicating approval. The gauge chart displays the probability index, and the financial insights panel breaks down the applicant's metrics."*
* **Highlight:** Show the interactive Chart.js gauge visualization and celebrate with the confetti animation.

---

## 3. Scene 3: Submitting an Application (Rejection Case)
* **Action:** Modify the input parameters: change **Credit History Status** to `Guidelines Not Met (0.0)`. Click **Run Risk Assessment**.
* **Script:** *"If an applicant has poor credit history, our underwriting guardrails automatically override the prediction and reject the application. The result card turns red and displays a detailed breakdown of the risk factors."*
* **Highlight:** Show the explainable AI rules explaining the specific rejection reasons.

---

## 4. Scene 4: Analytics and Telemetry Dashboard
* **Action:** Click **Analytics** in the navigation bar.
* **Script:** *"For risk analysts, our telemetry dashboard lists performance benchmarks across 6 machine learning models, highlighting the active model. We also visualize the ROC Curve, Confusion Matrix, and Feature Importances."*
* **Highlight:** Point to the feature importances chart and explanation table.
