import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, roc_curve, auc)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from config import Config

os.makedirs(os.path.dirname(Config.DATASET_PATH), exist_ok=True)
os.makedirs(os.path.dirname(Config.MODEL_PATH), exist_ok=True)
os.makedirs(Config.SCREENSHOTS_PATH, exist_ok=True)

def generate_synthetic_dataset(filepath, n_samples=614):
    """Generates realistic Loan Prediction Dataset with balanced rejection cases."""
    np.random.seed(42)
    gender = np.random.choice(['Male', 'Female'], size=n_samples, p=[0.81, 0.19])
    married = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.65, 0.35])
    dependents = np.random.choice(['0', '1', '2', '3+'], size=n_samples, p=[0.57, 0.17, 0.17, 0.09])
    education = np.random.choice(['Graduate', 'Not Graduate'], size=n_samples, p=[0.78, 0.22])
    self_employed = np.random.choice(['No', 'Yes'], size=n_samples, p=[0.86, 0.14])
    
    applicant_income = np.random.exponential(scale=3500, size=n_samples) + 1500
    coapplicant_income = np.random.choice([0, 1500, 2500, 4000], size=n_samples, p=[0.4, 0.3, 0.2, 0.1]) + np.random.normal(0, 200, size=n_samples)
    coapplicant_income = np.clip(coapplicant_income, 0, None)
    
    # Generate realistic independent loan amounts ($15k to $500k)
    loan_amount = np.random.uniform(20, 450, size=n_samples)
    loan_amount_term = np.random.choice([120, 180, 240, 300, 360, 480], size=n_samples, p=[0.02, 0.07, 0.03, 0.03, 0.82, 0.03])
    credit_history = np.random.choice([1.0, 0.0], size=n_samples, p=[0.75, 0.25])
    property_area = np.random.choice(['Semiurban', 'Urban', 'Rural'], size=n_samples, p=[0.38, 0.33, 0.29])
    
    total_income = applicant_income + coapplicant_income
    annual_income = total_income * 12
    loan_actual = loan_amount * 1000
    lti_ratio = loan_actual / (annual_income + 1e-5)
    
    # Realistic Banking Underwriting Scoring
    # Credit History is mandatory (penalty -5.0), High LTI ratio penalized
    score = (
        (credit_history * 5.0) - 3.0 +
        (education == 'Graduate') * 0.6 +
        (married == 'Yes') * 0.4 +
        (property_area == 'Semiurban') * 0.5 -
        (lti_ratio * 0.8)
    )
    
    # Hard cutoff for unverified credit history or extreme debt ratio > 5.0
    loan_status = np.where((credit_history == 1.0) & (lti_ratio <= 6.0) & (score > 0), 'Y', 'N')
    
    idx_nan = np.random.choice(n_samples, size=15, replace=False)
    gender[idx_nan[:3]] = np.nan
    married[idx_nan[3:6]] = np.nan
    self_employed[idx_nan[6:9]] = np.nan
    credit_history[idx_nan[9:12]] = np.nan
    loan_amount[idx_nan[12:]] = np.nan

    df = pd.DataFrame({
        'Loan_ID': [f'LP00{1000+i}' for i in range(n_samples)],
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': np.round(applicant_income).astype(float),
        'CoapplicantIncome': np.round(coapplicant_income).astype(float),
        'LoanAmount': np.round(loan_amount).astype(float),
        'Loan_Amount_Term': loan_amount_term.astype(float),
        'Credit_History': credit_history,
        'Property_Area': property_area,
        'Loan_Status': loan_status
    })
    df.to_csv(filepath, index=False)
    print(f"[+] Synthetic Loan Prediction dataset generated and saved to {filepath}")

def preprocess_and_train():
    if os.path.exists(Config.DATASET_PATH):
        os.remove(Config.DATASET_PATH)
    generate_synthetic_dataset(Config.DATASET_PATH)
        
    df = pd.read_csv(Config.DATASET_PATH)
    
    # Impute missing values
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
    df['Married'].fillna(df['Married'].mode()[0], inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
    
    if df.duplicated().sum() > 0:
        df.drop_duplicates(inplace=True)
        
    plt.style.use('ggplot')
    sns.set_theme(style="whitegrid")
    
    # 1. Class Distribution Plot
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Loan_Status', data=df, hue='Loan_Status', palette='viridis', legend=False)
    plt.title('Loan Status Class Distribution (Y vs N)', fontsize=12, fontweight='bold')
    plt.xlabel('Loan Status')
    plt.ylabel('Applicant Count')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'class_distribution.png'))
    plt.close()
    
    # 2. Income Distribution Plot
    plt.figure(figsize=(8, 4))
    sns.histplot(df['ApplicantIncome'], kde=True, color='teal', bins=30)
    plt.title('Applicant Monthly Income Distribution ($ USD)', fontsize=12, fontweight='bold')
    plt.xlabel('Monthly Income ($ USD)')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'income_distribution.png'))
    plt.close()

    # 3. Loan Amount Distribution Plot
    plt.figure(figsize=(8, 4))
    sns.histplot(df['LoanAmount'], kde=True, color='coral', bins=30)
    plt.title('Requested Loan Amount Distribution ($ USD in Thousands)', fontsize=12, fontweight='bold')
    plt.xlabel('Loan Amount ($ USD in Thousands)')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'loan_amount_distribution.png'))
    plt.close()

    encoders = {}
    cat_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']
    df_encoded = df.copy()
    
    for col in cat_cols:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        encoders[col] = le

    # 4. Correlation Heatmap Plot
    plt.figure(figsize=(10, 8))
    numeric_cols = df_encoded.drop(columns=['Loan_ID'])
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Feature Correlation Heatmap', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'correlation_heatmap.png'))
    plt.close()

    X = df_encoded.drop(columns=['Loan_ID', 'Loan_Status'])
    y = df_encoded['Loan_Status']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100, max_depth=6),
        'KNN': KNeighborsClassifier(n_neighbors=5),
        'Support Vector Machine': SVC(probability=True, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42, n_estimators=100)
    }

    results = {}
    best_score = -1
    best_model_name = ""
    best_model_obj = None

    plt.figure(figsize=(8, 6))

    for name, model in models.items():
        t0 = time.time()
        model.fit(X_train_scaled, y_train)
        t1 = time.time()
        
        preds = model.predict(X_test_scaled)
        probs = model.predict_proba(X_test_scaled)[:, 1]
        
        acc = accuracy_score(y_test, preds)
        prec = precision_score(y_test, preds, zero_division=0)
        rec = recall_score(y_test, preds, zero_division=0)
        f1 = f1_score(y_test, preds, zero_division=0)
        
        fpr, tpr, _ = roc_curve(y_test, probs)
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')

        results[name] = {
            'accuracy': round(float(acc), 4),
            'precision': round(float(prec), 4),
            'recall': round(float(rec), 4),
            'f1_score': round(float(f1), 4),
            'roc_auc': round(float(roc_auc), 4),
            'train_time_sec': round(float(t1 - t0), 4)
        }

        if f1 > best_score:
            best_score = f1
            best_model_name = name
            best_model_obj = model

    # 5. ROC Curves Plot
    plt.plot([0, 1], [0, 1], 'k--', label='Chance')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves Comparison', fontsize=12, fontweight='bold')
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'roc_curve.png'))
    plt.close()

    # 6. Confusion Matrix Plot
    best_preds = best_model_obj.predict(X_test_scaled)
    cm = confusion_matrix(y_test, best_preds)
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Rejected (N)', 'Approved (Y)'], yticklabels=['Rejected (N)', 'Approved (Y)'])
    plt.title(f'Confusion Matrix - {best_model_name}', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'confusion_matrix.png'))
    plt.close()

    # 7. Feature Importance Plot
    feature_importance_dict = {}
    features = X.columns
    if hasattr(best_model_obj, 'feature_importances_'):
        importances = best_model_obj.feature_importances_
    elif hasattr(best_model_obj, 'coef_'):
        importances = np.abs(best_model_obj.coef_[0])
    else:
        importances = np.ones(len(features)) / len(features)

    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(10, 5))
    plt.title(f'Feature Importances - {best_model_name}', fontsize=12, fontweight='bold')
    plt.bar(range(X.shape[1]), importances[indices], align='center', color='indigo')
    plt.xticks(range(X.shape[1]), [features[i] for i in indices], rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(Config.SCREENSHOTS_PATH, 'feature_importance.png'))
    plt.close()

    for i in indices:
        feature_importance_dict[features[i]] = round(float(importances[i]), 4)

    total_count = len(df)
    approved_count = int((df['Loan_Status'] == 'Y').sum())
    rejected_count = int((df['Loan_Status'] == 'N').sum())

    dataset_stats = {
        'total_samples': total_count,
        'features_count': X.shape[1],
        'approved_count': approved_count,
        'rejected_count': rejected_count,
        'approval_ratio': round((approved_count / total_count) * 100, 1),
        'rejection_ratio': round((rejected_count / total_count) * 100, 1),
        'mean_income': round(float(df['ApplicantIncome'].mean()), 2),
        'mean_loan_amount': round(float(df['LoanAmount'].mean()), 2)
    }

    model_artifact = {
        'model': best_model_obj,
        'scaler': scaler,
        'encoders': encoders,
        'feature_names': list(X.columns),
        'best_model_name': best_model_name,
        'metrics': results[best_model_name],
        'all_models_benchmarks': results,
        'feature_importances': feature_importance_dict,
        'dataset_stats': dataset_stats
    }
    
    joblib.dump(model_artifact, Config.MODEL_PATH)
    print(f"[+] Trained model artifact serialized to {Config.MODEL_PATH}")

if __name__ == '__main__':
    preprocess_and_train()
