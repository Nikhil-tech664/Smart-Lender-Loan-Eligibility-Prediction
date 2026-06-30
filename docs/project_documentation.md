# Smart Lender - Complete Project Master Documentation

## 1. Project Description
Smart Lender is an enterprise-ready automated loan eligibility prediction web system engineered under the SmartBridge Software Development Life Cycle (SDLC) framework. The system replaces manual, error-prone underwriting procedures with transparent, real-time machine learning inference engines.

## 2. Problem Statement
Commercial banks and financial institutions process thousands of loan applications daily. Traditional manual underwriting is sluggish, inconsistent, and highly vulnerable to human bias, leading to elevated default rates or improper loan rejections for qualified applicants.

## 3. System Architecture & Workflow
1. **Data Ingestion & Cleaning:** Handles missing numerical and categorical parameters through statistical imputation (mode/median).
2. **Feature Transformation:** Applies Label Encoding to categorical fields (`Gender`, `Education`, `Property_Area`, etc.) and Standard Scaling to numerical inputs (`ApplicantIncome`, `LoanAmount`).
3. **Machine Learning Core:** Evaluates 6 models (Logistic Regression, Decision Tree, Random Forest, KNN, SVM, Gradient Boosting) selecting the optimal model based on cross-validated F1 scores.
4. **Flask REST API Services:** Exposes `/predict` endpoint validating inputs and orchestrating realtime predictions.
5. **Glassmorphic Web Interface:** Modern dark/light mode responsive frontend built with Bootstrap 5 and asynchronous JavaScript fetch calls.

## 4. Dataset Telemetry & Features
- `Loan_ID`: Unique Application Identifier
- `Gender`: Male / Female
- `Married`: Marital status indicator
- `Dependents`: Dependent headcount (0, 1, 2, 3+)
- `Education`: Educational attainment (Graduate / Not Graduate)
- `Self_Employed`: Business ownership status
- `ApplicantIncome`: Primary applicant gross monthly income ($)
- `CoapplicantIncome`: Secondary applicant gross monthly income ($)
- `LoanAmount`: Requested credit facility size (in Thousands $)
- `Loan_Amount_Term`: Tenure duration (Months)
- `Credit_History`: Historical repayment guideline compliance (1.0 vs 0.0)
- `Property_Area`: Geographic location category (Urban, Semiurban, Rural)
- `Loan_Status`: Target class label (Y = Approved, N = Rejected)

## 5. Deployment & Sustainability
The project is containerized for seamless execution across local development instances, Gunicorn production WSGI containers, and cloud environments like Render and Vercel.
