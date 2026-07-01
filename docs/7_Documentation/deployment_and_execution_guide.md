# Deployment and Execution Guide

This guide details how to execute and deploy the **SmartLender AI** application:

## 1. Running Locally

### Step A: Train the Models
Train the machine learning models and generate the required visualization assets:
```bash
python train_model.py
```

### Step B: Run Automated Tests
Verify pipeline stability before starting the web server:
```bash
python -m unittest testing/unit_test_examples.py
```

### Step C: Launch the Web Application
Start the local Flask development server:
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your web browser to access the application.

---

## 2. Production Deployment (Render)
To deploy the application to Render:
1. Log in to your **Render.com** account and select **New Web Service**.
2. Connect your GitHub repository.
3. Configure the following runtime parameters:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Under Environment Variables, add:
   - `MODEL_PATH=model/loan_model.pkl`

---

## 3. Sharing via Public Tunnel (Ngrok)
If you want to share the app running on your local machine with mobile devices or external evaluators:
```bash
ngrok http 5000
```
This generates a secure HTTPS forwarding link (e.g. `https://xxxx.ngrok-free.app`) that can be accessed on any device.
