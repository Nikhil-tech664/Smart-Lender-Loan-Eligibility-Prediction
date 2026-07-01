# Empathy and Customer Journey Maps

## 1. Empathy Map

### A. What does the Retail Applicant THINK & FEEL?
- "I hope my loan gets approved quickly so I don't lose the property."
- "The bank's application processes are always so slow and confusing."
- "I want to know why my application is rejected and how to fix it."

### B. What does the Credit Underwriter SAY & DO?
- "I spend too much time calculating DTI ratios manually."
- "I need an objective backup prediction to cross-verify application risk."
- "I want to see which features (like Credit History or Income) are driving the decision."

---

## 2. Customer Journey Map (Retail Applicant)

| Phase | Touchpoint | Applicant Action | System Action | Pain Point / Opportunity |
|---|---|---|---|---|
| **Discovery** | Mobile Browser | Navigates to SmartLender AI landing page. | Serves secure, responsive web shell. | Opportunity: Deliver immediate, high-speed page loads. |
| **Data Entry** | Form Fields | Inputs income, requested loan, tenure, and credit status. | Syncs slider controls, validates fields dynamically. | Pain Point: Too many inputs. Opportunity: Floating labels, pre-filled values. |
| **Evaluation**| Submit CTA | Clicks "Run Risk Assessment". | Triggers 6-stage stepped loader, queries Flask backend. | Opportunity: Smooth micro-animations reduce perceived latency. |
| **Result** | Verdict Panel | Views verdict, probability, and risk explanations. | Renders semi-circular gauge and detailed insights list. | Opportunity: Actionable feedback on rejection. |
| **Export** | Action Buttons| Clicks "Export CSV" or "Print Result". | Downloads raw details locally in the requested format. | Opportunity: Offline archival. |
```
                               Customer Journey Flow
                               
+-------------+     +-------------+     +-------------+     +-------------+
| Landing     | --> | Form Input  | --> | Stepped     | --> | Result      |
| Page Access |     | & Validation|     | Loader      |     | & Analytics |
+-------------+     +-------------+     +-------------+     +-------------+
```
