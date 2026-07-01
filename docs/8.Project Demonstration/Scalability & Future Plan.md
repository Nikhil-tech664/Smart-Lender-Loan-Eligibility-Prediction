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
| **1** | Local joblib storage | Retraining models requires manual replacement of the pkl model artifact. | Medium |
| **2** | Local browser history | Historical query tracking is isolated to local browser cache. | Medium |
| **3** | Single-threaded server | High concurrent user load can saturate Flask backend performance. | High |

---

## Scalability Plan

Outline the upgrades needed to scale the application to handle higher enterprise workloads.

| S.No | Scalability Aspect | Current State | Proposed Upgrade / Solution |
| :--- | :--- | :--- | :--- |
| **1** | Server Load | Single thread local process. | Deploy on Gunicorn workers with Nginx web proxy. |
| **2** | Data Storage | Memory model cache, local storage history. | Integrate PostgreSQL server databases to log queries. |
| **3** | Performance | Real-time classification scaler transforms. | Cache predictions for recurring profiles using Redis. |
| **4** | Security | Unencrypted HTTP API. | Enforce HTTPS TLS certs and protect routes via JWT tokens. |

---

## Future Roadmap

Map out the multi-phase deployment roadmap for future features:

| Phase | Planned Feature / Enhancement | Target Timeline | Expected Impact |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Model Registry Deployment | Month 1 | Seamless swapping of optimized classifiers. |
| **Phase 2** | Customer Logins | Month 2 | Secure portal for users to view past approvals. |
| **Phase 3** | Admin Analytics Panel | Month 4 | Real-time graphs showing monthly loan volumes. |
| **Phase 4** | Automated Retraining Loops | Month 6 | Automatically update weights based on loan default data. |
