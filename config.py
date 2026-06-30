import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_smartlender_key_super_secret')
    DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'
    PORT = int(os.getenv('PORT', 5000))
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'loan_model.pkl')
    DATASET_PATH = os.path.join(os.path.dirname(__file__), 'dataset', 'loan_data.csv')
    SCREENSHOTS_PATH = os.path.join(os.path.dirname(__file__), 'static', 'screenshots')
