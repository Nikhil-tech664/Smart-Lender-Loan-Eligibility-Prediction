# Installation and Setup Guide

Follow these steps to set up **SmartLender AI** on your local machine:

## 1. Prerequisites
Ensure you have the following software installed:
* Python 3.10.x or 3.11.x
* Git Command Line Tool

---

## 2. Local Environment Setup

### Step A: Clone the Repository
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/Nikhil-tech664/Smart-Lender-Loan-Eligibility-Prediction.git
cd Smart-Lender-Loan-Eligibility-Prediction
```

### Step B: Create a Virtual Environment
Initialize a clean Python virtual environment to manage dependencies:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step C: Install Dependencies
Install all required libraries specified in the requirements file:
```bash
pip install -r requirements.txt
```

---

## 3. Configuration & Environment Variables
Copy the template `.env.example` file to create your active `.env` configuration file:
```bash
cp .env.example .env
```
Inside `.env`, configure the following properties:
* `FLASK_PORT=5000`
* `FLASK_DEBUG=False`
* `MODEL_PATH=model/loan_model.pkl`
