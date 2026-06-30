# SmartBridge SDLC Phase 6: Testing & Results

## 1. Functional Testing Execution
All automated unit tests (`testing/unit_test_examples.py`) executed with 100% pass rates across test scenarios validating home route HTTP 200 responses, health status checks, and `/predict` endpoint payload evaluation.

## 2. Model Accuracy & Confusion Matrix Analysis
- **Random Forest Model Accuracy:** 82.93%
- **Precision:** 80.72%
- **Recall:** 95.71%
- **F1 Score:** 0.8758

The high recall metric confirms the model minimizes false negatives, ensuring eligible applicants are rarely turned away improperly.
