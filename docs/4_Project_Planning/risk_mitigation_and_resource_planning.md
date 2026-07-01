# Risk Mitigation and Resource Planning

## 1. Resource Allocations
A lean development team was assigned to design and implement the system:

* **Machine Learning & Backend Engineer:** Responsible for synthetic data collection, model evaluations, API endpoint security, and Python WSGI operations.
* **UI/UX Frontend Developer:** Responsible for the Bootstrap responsive structure, canvas-confetti adjustments, Chart.js gauge visualizations, local history hooks, and CSS configurations.
* **Quality Assurance Auditor:** Responsible for writing automated unittest assertions, mapping manual edge cases, and verifying cross-browser responsiveness.

---

## 2. Risk Mitigation Matrix

| Identified Threat | Severity | Action Strategy |
|---|---|---|
| **Data Imbalance / High False Positive Rate** | High | Configured stratified train-test splits and optimized F1-scoring metrics over plain accuracy during the model selection stage. |
| **Authentication/Port Conflicts** | Medium | Configured ports and paths dynamically using environment variables to ensure zero collisions during staging. |
| **Mobile Layout Breakage** | Medium | Implemented responsive flexbox structures, viewport scale caps, and relative sizing units (`rem`/`vw`) to prevent text clipping. |
