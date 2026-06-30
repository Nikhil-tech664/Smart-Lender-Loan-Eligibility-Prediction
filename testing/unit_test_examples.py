import unittest
import json
from app import app

class TestSmartLenderAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        """Test home route returns HTTP 200 OK."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_health_route(self):
        """Test health check route returns valid JSON."""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('status', data)

    def test_model_telemetry_route(self):
        """Test model telemetry endpoint returns metrics and benchmarks."""
        response = self.app.get('/model-telemetry')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('metrics', data)
        self.assertIn('all_models_benchmarks', data)

    def test_predict_success(self):
        """Test valid loan prediction request."""
        payload = {
            "Gender": "Male",
            "Married": "Yes",
            "Dependents": "1",
            "Education": "Graduate",
            "Self_Employed": "No",
            "ApplicantIncome": 6000,
            "CoapplicantIncome": 2000,
            "LoanAmount": 150,
            "Loan_Amount_Term": 360,
            "Credit_History": 1.0,
            "Property_Area": "Semiurban"
        }
        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('status', data)
        self.assertIn('probability', data)

    def test_predict_missing_field(self):
        """Test loan prediction missing required fields."""
        payload = {
            "Gender": "Male",
            "ApplicantIncome": 5000
        }
        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

if __name__ == '__main__':
    unittest.main()
