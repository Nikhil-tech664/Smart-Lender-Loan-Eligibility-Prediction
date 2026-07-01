# Scalability & Future Plan

| Field | Details |
| :--- | :--- |
| **Date** | 15 March 2026 |
| **Team ID** | PNT2022TMID124356 |
| **Project Name** | SmartLender AI – Loan Eligibility Prediction |
| **Maximum Marks** | 1 Mark |

---

## Current System Limitations

Document the current architectural limitations of the implemented solution.

| S.No | Limitation | Impact | Priority to Address (High / Medium / Low) |
| :--- | :--- | :--- | :--- |
| **1** | Local joblib Model Store | Swapping models requires manual file replacement inside workspace cache. | Medium |
| **2** | Single Instance Web Server | High concurrent traffic might saturate the single-threaded Flask development server. | High |
| **3** | Lack of Historical Logs | Admin cannot trace past prediction outputs for auditing purposes. | Medium |

---

## Scalability Plan

Outline the upgrades needed to scale the application to handle higher enterprise workloads.

| S.No | Scalability Aspect | Current State | Proposed Upgrade / Solution |
| :--- | :--- | :--- | :--- |
| **1** | User Load | Serves local requests on single server thread. | Deploy via Nginx load balancers on Gunicorn workers. |
| **2** | Data Storage | Relies on simple CSV file models. | Implement a PostgreSQL relational store to save applicant query profiles. |
| **3** | Performance | In-memory classification processing. | Use Redis caching for redundant identical profiles. |
| **4** | Security | Standard HTTP data transmission. | Implement TLS certificates (HTTPS) and API JWT token validation. |

---

## Future Roadmap

Map out the multi-phase deployment roadmap for future features:

| Phase | Planned Feature / Enhancement | Target Timeline | Expected Impact |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Model Registry Integration | Month 1 | Automatic staging and swapping of new ML models. |
| **Phase 2** | Customer Login Dashboard | Month 2 | Applicants can view and trace past submission outcomes. |
| **Phase 3** | Multi-Branch Analytics | Month 4 | Visual aggregate charts for banking directors to monitor approvals. |
| **Phase 4** | Automated Retraining | Month 6 | Continuous model optimization loops based on realized defaults. |
