# Expected Questions and Answers

Prepare for the following questions during your SmartBridge project defense:

## 1. Core Model Performance

### Q1: Why did you select Gradient Boosting over other machine learning models?
- **Answer:** *"We trained and compared 6 different models. While all performed well, the Gradient Boosting Classifier achieved the highest validation F1-score of 98.11% with a very low training duration, making it the most optimal choice for deployment."*

### Q2: What features were the most important drivers for your model?
- **Answer:** *"The primary decision drivers identified by the feature importances calculation were LoanAmount (38.02%), Credit_History (30.88%), and ApplicantIncome (24.44%)."*

---

## 2. System and Operations

### Q3: How does your system handle security and prevent invalid inputs?
- **Answer:** *"The Flask backend validates every incoming payload, converting parameters to floats or strings. We also implement try-except blocks to catch formatting errors and return clean error responses instead of leaking system stack traces."*

### Q4: How does the local history management feature work?
- **Answer:** *"To keep the system lightweight and avoid database maintenance costs, we store up to 20 past results locally in the browser's LocalStorage. Users can search, filter, and sort past records directly on the client side."*
