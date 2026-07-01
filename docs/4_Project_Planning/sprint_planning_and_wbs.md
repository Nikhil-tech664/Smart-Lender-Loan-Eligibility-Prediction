# Sprint Planning and Work Breakdown Structure (WBS)

## 1. Agile Sprint Structure
The project was divided into two distinct, 2-week agile sprints:

### Sprint 1: Data Modeling & Core Backend Core
- **Goals:** Set up the repository, generate synthetic tabular training records, evaluate classifier models, serialize the preprocessor pipeline, and establish HTTP routes.
- **Deliverables:** `train_model.py`, `app.py` core routes, and initial testing hooks.

### Sprint 2: Frontend UX & Quality Assurance Integration
- **Goals:** Implement CSS theme parameters, synchronize HTML slider tags, structure modular modals, and execute unit testing.
- **Deliverables:** `style.css`, `main.js`, custom gauge meter, history management, CSV/JSON exports, and `unit_test_examples.py`.

---

## 2. Work Breakdown Structure (WBS)

```
SmartLender AI Project
 ├── 1. Requirements & Research
 │    ├── 1.1 Empathy Mapping
 │    └── 1.2 Tech Stack Selection
 ├── 2. Machine Learning Modeling
 │    ├── 2.1 Synthetic Dataset Generation
 │    ├── 2.2 Model Training (6 Algorithms)
 │    └── 2.3 Preprocessor & Model Serialization (.pkl)
 ├── 3. Web Service Construction
 │    ├── 3.1 Flask app.py API Implementation
 │    └── 3.2 Underwriting Veto Guardrails Integration
 ├── 4. Client Interface Development
 │    ├── 4.1 Glassmorphism CSS Stylesheet
 │    ├── 4.2 Chart.js & History Controller
 │    └── 4.3 Multi-Format Export tools
 └── 5. Validation & Quality Assurance
      ├── 5.1 Automated Route Assertions
      └── 5.2 Responsive Layout Verification
```
