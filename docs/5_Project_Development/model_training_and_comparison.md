# Model Training, Comparison, and Selection

## 1. Machine Learning Algorithms Evaluated
The training pipeline (`train_model.py`) splits data (80% Train, 20% Test) and evaluates 6 different classifiers:

1. **Logistic Regression:** Serves as a baseline statistical classifier.
2. **Decision Tree:** Provides a hierarchical rule-based classifier.
3. **Random Forest:** Implements an ensemble of bagged decision trees.
4. **K-Nearest Neighbors (KNN):** Renders instance-based classifications.
5. **Support Vector Machine (SVM):** Implements optimal hyperplane mapping.
6. **Gradient Boosting Classifier:** Fits sequential decision trees.

---

## 2. Comparative Performance Matrix
The model telemetry output evaluated the models as follows:

* **Selected Model:** **Gradient Boosting Classifier**
* **Validation Accuracy:** **98.37%**
* **Precision Score:** **96.3%**
* **Recall Score:** **100%**
* **F1 Score:** **98.11%**
* **ROC-AUC Index:** **99.81%**
* **Train Time:** **0.4962 seconds**

---

## 3. Feature Importance Ratings
During model selection, feature importances are calculated:
1. **LoanAmount (38.02%):** Primary decision driver.
2. **Credit_History (30.88%):** Essential risk check.
3. **ApplicantIncome (24.44%):** Capacity indicator.
4. **CoapplicantIncome (5.44%):** Additional financial support.
5. **Categorical features (under 1.0% combined):** Minimal predictive influence.
