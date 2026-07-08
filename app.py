import os
import time
from datetime import datetime
import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

model_artifact = None

def load_ml_artifact():
    global model_artifact
    if os.path.exists(Config.MODEL_PATH):
        try:
            model_artifact = joblib.load(Config.MODEL_PATH)
            print(f"[+] Model artifact loaded successfully from {Config.MODEL_PATH}")
        except Exception as e:
            print(f"[-] Error loading model artifact: {e}")
            model_artifact = None
    else:
        print(f"[-] Model file not found at {Config.MODEL_PATH}")
        model_artifact = None

load_ml_artifact()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/health', methods=['GET'])
def health():
    status = "healthy" if model_artifact is not None else "model_missing"
    return jsonify({
        "status": status,
        "model_loaded": model_artifact is not None,
        "best_model": model_artifact.get('best_model_name') if model_artifact else None
    })

@app.route('/model-telemetry', methods=['GET'])
def model_telemetry():
    global model_artifact
    if model_artifact is None:
        load_ml_artifact()
        if model_artifact is None:
            return jsonify({'success': False, 'error': 'Model not loaded'}), 500

    metrics = model_artifact.get('metrics', {})
    benchmarks = model_artifact.get('all_models_benchmarks', {})
    importances = model_artifact.get('feature_importances', {})
    dataset_stats = model_artifact.get('dataset_stats', {})

    return jsonify({
        'success': True,
        'model_name': model_artifact.get('best_model_name', 'Random Forest Classifier'),
        'metrics': metrics,
        'all_models_benchmarks': benchmarks,
        'feature_importances': importances,
        'dataset_stats': dataset_stats
    })

@app.route('/predict', methods=['POST'])
def predict():
    global model_artifact
    t_start = time.time()

    if model_artifact is None:
        load_ml_artifact()
        if model_artifact is None:
            return jsonify({
                'success': False,
                'error': 'Model artifact is currently unavailable. Please run train_model.py.'
            }), 500

    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'Payload empty or invalid JSON'}), 400

        required_fields = [
            'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
            'Loan_Amount_Term', 'Credit_History', 'Property_Area'
        ]
        
        missing = [f for f in required_fields if f not in data or data[f] is None or str(data[f]).strip() == '']
        if missing:
            return jsonify({'success': False, 'error': f'Missing required inputs: {", ".join(missing)}'}), 400

        gender = str(data['Gender'])
        married = str(data['Married'])
        dependents = str(data['Dependents'])
        education = str(data['Education'])
        self_employed = str(data['Self_Employed'])
        applicant_income = float(data['ApplicantIncome'])
        coapplicant_income = float(data['CoapplicantIncome'])
        loan_amount = float(data['LoanAmount'])
        loan_term = float(data['Loan_Amount_Term'])
        credit_history = float(data['Credit_History'])
        property_area = str(data['Property_Area'])

        if applicant_income < 0 or coapplicant_income < 0 or loan_amount <= 0 or loan_term <= 0:
            return jsonify({'success': False, 'error': 'Income and Loan values must be strictly positive.'}), 400

        raw_input = {
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': applicant_income,
            'CoapplicantIncome': coapplicant_income,
            'LoanAmount': loan_amount,
            'Loan_Amount_Term': loan_term,
            'Credit_History': credit_history,
            'Property_Area': property_area
        }

        encoders = model_artifact['encoders']
        encoded_input = raw_input.copy()
        
        for col in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']:
            le = encoders[col]
            if encoded_input[col] in le.classes_:
                encoded_input[col] = le.transform([encoded_input[col]])[0]
            else:
                encoded_input[col] = 0

        feature_names = model_artifact['feature_names']
        input_df = pd.DataFrame([encoded_input])[feature_names]

        scaler = model_artifact['scaler']
        input_scaled = scaler.transform(input_df)

        model = model_artifact['model']
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]
        
        raw_approval_prob = round(float(probabilities[1]) * 100, 2)

        # Financial metrics calculation
        total_income = applicant_income + coapplicant_income
        annual_income = total_income * 12
        loan_amount_actual = loan_amount * 1000
        income_to_loan_ratio = round(loan_amount_actual / (annual_income + 1e-5), 2)
        estimated_monthly_payment = round(loan_amount_actual / loan_term, 2)
        debt_ratio_estimate = round((estimated_monthly_payment / (total_income + 1e-5)) * 100, 1)

        # Permissive Underwriting Guardrails
        # Credit history is a strict banking veto. Debt ratios are capped at a generous 85% limit.
        if credit_history == 0.0 or income_to_loan_ratio > 8.0 or debt_ratio_estimate > 85.0:
            is_eligible = False
            approval_prob = min(raw_approval_prob, 32.50)
        else:
            is_eligible = bool(prediction == 1)
            approval_prob = raw_approval_prob

        # Determine Confidence Level and Risk Level
        if approval_prob > 80:
            confidence = "High Confidence"
            risk_level = "Low Risk"
        elif approval_prob > 60:
            confidence = "Moderate Confidence"
            risk_level = "Acceptable Risk"
        elif approval_prob > 40:
            confidence = "Boundary Risk Assessment"
            risk_level = "Elevated Risk"
        else:
            confidence = "High Confidence Rejection"
            risk_level = "High Risk"

        explanations = []
        smart_insights = []

        smart_insights.append(f"Combined Household Monthly Income: ₹{total_income:,.2f} INR")
        smart_insights.append(f"Requested Loan Amount represents {income_to_loan_ratio}x annual income.")
        smart_insights.append(f"Estimated Monthly Loan Obligation: ₹{estimated_monthly_payment:,.2f} INR ({debt_ratio_estimate}% debt ratio).")

        if is_eligible:
            result_message = "Congratulations! Your loan application meets institutional eligibility criteria."
            if credit_history == 1.0:
                explanations.append("✔ Strong Credit History compliance.")
            if income_to_loan_ratio <= 4.0:
                explanations.append(f"✔ Healthy Loan-to-Income ratio ({income_to_loan_ratio}x).")
            if education == 'Graduate':
                explanations.append("✔ Stable Employment and Education qualification.")
            if property_area in ['Semiurban', 'Urban']:
                explanations.append(f"✔ Property Risk Low in active zone ({property_area}).")
            if not explanations:
                explanations.append("✔ Financial telemetry satisfies overall underwriting thresholds.")
        else:
            result_message = "Regrettably, your application currently falls below underwriting threshold parameters."
            if credit_history == 0.0:
                explanations.append("✖ Credit History guidelines were not met (Highest risk factor).")
            if income_to_loan_ratio > 8.0:
                explanations.append(f"✖ High requested loan amount relative to income ({income_to_loan_ratio}x annual income).")
            if debt_ratio_estimate > 85.0:
                explanations.append(f"✖ High estimated debt-to-income ratio ({debt_ratio_estimate}% of monthly income).")
            if coapplicant_income == 0:
                explanations.append("✖ Absence of co-applicant income support.")
            if not explanations:
                explanations.append("✖ Combined financial risk metrics exceed acceptable variance.")

        t_end = time.time()
        latency_ms = round((t_end - t_start) * 1000, 2)
        timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

        return jsonify({
            'success': True,
            'eligible': is_eligible,
            'status': 'APPROVED' if is_eligible else 'REJECTED',
            'probability': approval_prob,
            'confidence_level': confidence,
            'risk_level': risk_level,
            'message': result_message,
            'model_used': model_artifact.get('best_model_name', 'Random Forest Classifier'),
            'prediction_time_ms': latency_ms,
            'prediction_timestamp': timestamp_str,
            'explanations': explanations,
            'smart_insights': smart_insights,
            'raw_inputs': raw_input
        })

    except ValueError as ve:
        return jsonify({'success': False, 'error': f'Invalid numeric formatting: {str(ve)}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Server evaluation exception: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)
