# Smart Lender - Deployment & Operations Guide

## Overview
This operational guide outlines step-by-step instructions to deploy the Smart Lender application across multiple environments including local development, production cloud hosting (Render), secured tunneled instances (Ngrok), and production WSGI containers (Gunicorn).

---

## 1. Local Development Deployment
### Prerequisites
- Python 3.11+
- Git

### Step-by-Step Setup
```bash
# 1. Clone Repository
git clone https://github.com/smartbridge/Loan-Eligibility-Prediction.git
cd Loan-Eligibility-Prediction

# 2. Create and Activate Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Train Machine Learning Models & Generate Artifacts
python train_model.py

# 5. Launch Development Server
python app.py
```
Access the web application at `http://127.0.0.1:5000`.

---

## 2. Production Deployment via Gunicorn WSGI
For production Linux servers (e.g., AWS EC2, DigitalOcean):
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

---

## 3. Cloud Deployment on Render
1. Create a new **Web Service** on Render connected to your GitHub repository.
2. Select **Python 3.11** environment.
3. Set Build Command: `pip install -r requirements.txt && python train_model.py`
4. Set Start Command: `gunicorn app:app`
5. Configure Environment Variables in Render Dashboard:
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: `<your-secure-production-key>`

---

## 4. Tunneling for Remote Demonstrations (Ngrok)
To share a live public link during SmartBridge evaluations:
```bash
# Run local server in terminal 1
python app.py

# Launch Ngrok tunnel in terminal 2
ngrok http 5000
```
Copy the generated HTTPS forwarding URL (e.g., `https://xxxx.ngrok-free.app`) to access remotely.
