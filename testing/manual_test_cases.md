# Smart Lender - Manual Test Cases Specification

## Test Suite Summary
This document outlines comprehensive manual test scenarios covering functional UI, input validation, backend processing, edge cases, and theme toggling.

| Test Case ID | Feature / Module | Test Description | Input Data | Expected Result | Pass/Fail Criteria |
|---|---|---|---|---|---|
| TC-001 | Dynamic UI | Verify Page Load & Glassmorphic UI rendering | N/A | Navigation bar, title, forms, and footer render cleanly without visual layout bugs. | Pass if all elements render properly |
| TC-002 | Theme Switcher | Toggle Light/Dark Mode | Click Sun/Moon icon | Theme switches smoothly between dark slate and bright banking themes. Preference persists on refresh. | Pass if attribute `data-theme` changes |
| TC-003 | Validation | Submit Empty Form | All fields empty | Browser HTML5 validation prevents submission and highlights missing fields in red. | Pass if submit is blocked |
| TC-004 | Loan Evaluation | Standard Eligible Applicant Test | Gender: Male, Married: Yes, Dependents: 1, Education: Graduate, Self_Employed: No, ApplicantIncome: 6000, CoapplicantIncome: 2000, LoanAmount: 120, Term: 360, Credit_History: 1.0, Area: Semiurban | Dynamic green success banner appears: "APPROVED" with high probability index (>75%). | Pass if status is Approved |
| TC-005 | Loan Evaluation | High Risk Applicant Test | Gender: Female, Married: No, Dependents: 3+, Education: Not Graduate, Self_Employed: Yes, ApplicantIncome: 1500, CoapplicantIncome: 0, LoanAmount: 400, Term: 360, Credit_History: 0.0, Area: Rural | Red rejection banner appears: "REJECTED" with low probability index (<30%). | Pass if status is Rejected |
| TC-006 | Boundary Test | Zero/Negative Income Validation | ApplicantIncome: -500 | Form validation catches negative input or API returns 400 Bad Request. | Pass if handled gracefully |
