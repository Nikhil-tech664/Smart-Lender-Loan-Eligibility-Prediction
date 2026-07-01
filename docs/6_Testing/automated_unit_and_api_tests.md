# Automated Unit and API Testing

Automated testing is performed using Python's standard `unittest` framework (`testing/unit_test_examples.py`).

## 1. Automated Test Cases & Assertions

### A. Test Case 1: HTML Index Route Validation (`test_home_route`)
- **Action:** Sends a HTTP GET request to `/`.
- **Assertions:**
  - Status code is `200 OK`.
  - Response contains HTML structures (`<!DOCTYPE html>`, `SmartLender`).

### B. Test Case 2: System Health Status (`test_health_route`)
- **Action:** Sends a HTTP GET request to `/health`.
- **Assertions:**
  - Status code is `200 OK`.
  - JSON payload contains keys: `status` = `"healthy"` and `model_loaded` = `True`.

### C. Test Case 3: Telemetry Dashboard Data (`test_telemetry_route`)
- **Action:** Sends a HTTP GET request to `/model-telemetry`.
- **Assertions:**
  - Status code is `200 OK`.
  - JSON payload confirms the presence of metrics keys for all 6 models, dataset stats, and feature importance ratings.

### D. Test Case 4: Complete Prediction Pipeline (`test_prediction_route`)
- **Action:** Sends a HTTP POST request to `/predict` with a valid applicant JSON payload.
- **Assertions:**
  - Status code is `200 OK`.
  - Response contains keys: `success` = `True`, `eligible`, `status`, and `probability`.

### E. Test Case 5: Missing Parameter Handling (`test_missing_params_validation`)
- **Action:** Sends a HTTP POST request to `/predict` with a payload missing the `Credit_History` parameter.
- **Assertions:**
  - Status code is `400 Bad Request`.
  - Response returns an error message listing the missing field.
