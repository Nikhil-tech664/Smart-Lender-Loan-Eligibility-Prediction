# SmartBridge SDLC Phase 8: Demonstration Script

## Demonstration Flow & Script Notes

1. **Introduction (1 min):** Present project objectives, technology stack, and banking domain problem statement.
2. **Architecture & Preprocessing Overview (2 mins):** Explain dataset features, imputation strategy, label encoding, and model benchmarks generated in `static/screenshots/`.
3. **Live UI Evaluation (3 mins):**
   - Demonstrate theme toggling (Dark to Light mode).
   - Enter high credit history applicant ($6,000 income, Graduate, Semiurban) -> Show instantaneous dynamic green "APPROVED" result.
   - Enter low credit history applicant ($1,500 income, 0.0 Credit History, Rural) -> Show dynamic red "REJECTED" result.
4. **API & Deployment Overview (1 min):** Highlight Gunicorn WSGI and Render deployment readiness.
