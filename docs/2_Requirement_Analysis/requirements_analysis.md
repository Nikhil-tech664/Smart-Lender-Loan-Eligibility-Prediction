# SmartBridge SDLC Phase 2: Requirement Analysis

## 1. Functional Requirements
- **FR-1:** System must collect 11 distinct applicant parameters (Gender, Marital Status, Dependents, Education, Employment, Incomes, Loan Amount, Term, Credit History, Property Area).
- **FR-2:** Backend must perform automated data preprocessing and feature scaling on incoming requests.
- **FR-3:** System must return instantaneous eligibility classification (`Approved` vs `Rejected`) along with an exact probability index score (0-100%).
- **FR-4:** Frontend must support dynamic theme toggling (Dark/Light mode).

## 2. Non-Functional Requirements
- **NFR-1 (Performance):** Sub-100ms API response latency for single predictions.
- **NFR-2 (Reliability):** Robust exception handling returning standard HTTP status codes (400, 500) and user-friendly error messages.
- **NFR-3 (Usability):** Glassmorphic responsive interface functional across mobile, tablet, and desktop viewports.

## 3. Technology Stack Specification
- **Programming Language:** Python 3.11
- **Web Framework:** Flask 3.0
- **Frontend Core:** HTML5, CSS3, Bootstrap 5, Vanilla JavaScript (Fetch API)
- **Machine Learning Libraries:** Scikit-Learn, Pandas, NumPy, Joblib
- **Deployment & Server:** Gunicorn WSGI, Render, Ngrok

## 4. Data Flow Diagram (DFD) Summary
`[User Form]` -> `(HTML5/JS Validation)` -> `POST /predict (JSON)` -> `[Flask Controller]` -> `[Scikit-Learn Preprocessor & Model]` -> `(Prediction Output)` -> `[Dynamic UI Render]`
