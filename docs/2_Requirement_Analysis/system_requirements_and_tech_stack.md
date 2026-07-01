# System Requirements and Technology Stack

## 1. System Software Requirements
* **Operating System:** Windows 10/11, macOS, or Linux (Ubuntu 20.04+).
* **Python Runtime Environment:** Python 3.10.x or 3.11.x.
* **Web Browser:** Modern browser with LocalStorage and JS support.
* **WSGI Container (Production):** Gunicorn 21.2+ (for Linux deployments).

---

## 2. Technology Stack

### A. Core Backend Engine
* **Flask (v3.0.0):** Micro-framework hosting REST API routing and HTML page rendering.
* **Joblib (v1.3.2):** Used for loading serialized preprocessing pipelines and ML model classifiers.

### B. Machine Learning Pipeline
* **Scikit-learn (v1.3.0):** Underpins scaling, encoding, and model classifier fitting.
* **Pandas (v2.0.3) & NumPy (v1.24.3):** Structured data matrix manipulations and mathematical computations.

### C. Frontend Interface
* **HTML5 & CSS3:** Semantic banking structure, custom layouts, custom range sliders.
* **Bootstrap (v5.3.2):** Responsive grids, modals, and styling utilities.
* **Chart.js (v4.4.0):** Used for building the semi-circular probability gauge meter.
* **Canvas-Confetti:** Celebration effects upon application approval.
