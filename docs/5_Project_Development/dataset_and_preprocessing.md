# Dataset Description and Preprocessing Pipeline

The data pipeline for **SmartLender AI** processes 614 applicant records with 11 distinct feature variables:

## 1. Feature Specifications

| Feature Name | Data Type | Description / Range |
|---|---|---|
| **Gender** | Categorical | Male, Female |
| **Married** | Categorical | Yes, No |
| **Dependents** | Categorical | 0, 1, 2, 3+ |
| **Education** | Categorical | Graduate, Not Graduate |
| **Self_Employed** | Categorical | Yes, No |
| **ApplicantIncome** | Numeric | Monthly income ($ USD) |
| **CoapplicantIncome**| Numeric | Co-applicant monthly income ($ USD) |
| **LoanAmount** | Numeric | Requested loan ($ USD in Thousands) |
| **Loan_Amount_Term** | Numeric | Tenure term in months |
| **Credit_History** | Numeric | Compliance index (1.0 = Clean, 0.0 = Poor) |
| **Property_Area** | Categorical | Rural, Semiurban, Urban |

---

## 2. Data Preprocessing & Cleaning

### A. Missing Value Imputation
* **Categorical Imputation:** Columns (`Gender`, `Married`, `Dependents`, `Self_Employed`, `Credit_History`, `Loan_Amount_Term`) are filled with their dataset statistical mode.
* **Numerical Imputation:** Missing `LoanAmount` values are filled with the dataset median ($231.78k USD) to prevent outlier distortion.

### B. Categorical Encoding
Uses individual Scikit-learn `LabelEncoder` objects for all categorical columns to preserve text-to-integer mappings. Encoders are packaged into the joblib artifact to decode future API payloads reliably.

### C. Scaling
Fits a `StandardScaler` to ensure all features have a mean of 0 and unit variance, preventing high-value columns (like monthly income) from dominating model coefficients.
