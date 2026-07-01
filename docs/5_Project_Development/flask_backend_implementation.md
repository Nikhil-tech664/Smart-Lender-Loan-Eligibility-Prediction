# Flask Backend Architecture and Endpoints

The backend engine (`app.py`) is written in Python using Flask to host the model inference services:

## 1. Modular Routing & API Endpoints

### A. Health Route (`GET /health`)
Determines if `loan_model.pkl` is loaded and ready, returning the active model's name. Used by deployment staging tools to verify startup stability.

### B. Telemetry Dashboard Route (`GET /model-telemetry`)
Parses `loan_model.pkl` and returns F1 benchmarks for all 6 models, dataset metrics, and feature importances to populate the analytics interface.

### C. Predictive Engine Route (`POST /predict`)
Processes POST requests with JSON applicant parameters.
1. **JSON Validation:** Validates that all 11 fields are present and converts entries to floats or strings.
2. **Preprocessing Pipeline:** Encodes categorical features using LabelEncoders and scales inputs using the StandardScaler.
3. **Underwriting Guardrail Check:**
   - Automatically overrides predictions to **REJECTED** if Credit_History = `0.0`, loan ratio > `8.0x` annual income, or DTI ratio > `85%`.
4. **Model Inference:** Passes the scaled array to `model.predict_proba()` to compute probability indexes and confidence ratings.
5. **Execution Latency Logging:** Returns the status, probability, confidence level, risk rating, and execution speed in milliseconds (`prediction_time_ms`).
