# Coding & Solution Report

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 5 Marks |

---

## Solution Summary

Summarize the key attributes of the implemented code and repository hosting details.

| Field | Details |
| :--- | :--- |
| **Repository Link / URL** | https://github.com/Nikhil-tech664/Smart-Lender-Loan-Eligibility-Prediction.git |
| **Programming Language(s)** | Python, HTML5, CSS3, JavaScript |
| **Framework(s) Used** | Flask, scikit-learn, Pandas, NumPy |
| **Key Features Implemented** | - Real-time ML eligibility scoring.<br>- Hard credit history veto checks.<br>- Sleek responsive user form interface with dark/light mode toggle. |
| **Pending / Incomplete Features** | - Automatic email result notification reports.<br>- Historical prediction audit logging dashboard. |
| **Setup / Run Instructions** | 1. Clone repository.<br>2. Run `pip install -r requirements.txt`.<br>3. Start app using `python app.py`. |

---

## Code Quality Checklist

Rate the alignment of the codebase against standard software engineering and design criteria.

| S.No | Criteria | Status (Yes / No) | Remarks |
| :--- | :--- | :--- | :--- |
| **1** | Code is modular and organized into functions / classes | **Yes** | Standard modular files: `app.py` for routing, `train_model.py` for training pipeline. |
| **2** | Meaningful variable and function names are used | **Yes** | Explicit domain mappings: `ApplicantIncome`, `Credit_History`, `check_eligibility`. |
| **3** | Code includes comments / documentation where necessary | **Yes** | Comprehensive inline comments mapping input JSON parsing steps and DTI calculation rules. |
| **4** | Error handling is implemented for critical operations | **Yes** | Try-catch block wraps the joblib pickle loader and scales the numerical columns safely. |
| **5** | The application runs without critical errors | **Yes** | Integration tests verified clean execution of the web server routes. |
| **6** | Code is committed to a version control repository | **Yes** | Standard commits logged on the GitHub main branch. |

### Additional Notes / Comments
The underwriting logic implements strict safeguards: an applicant with `Credit_History` equal to `0.0` is immediately rejected. Permissive limits have been established for high Debt-to-Income (DTI up to 85%) and Loan-to-Income (LTI up to 8x annual income) to prevent false rejections of valid applicants.
