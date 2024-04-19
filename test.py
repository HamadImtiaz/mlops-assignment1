import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict(client):
    # Test case data
    test_data = {
        'age': 65,
        'avg_glucose_level': 125,
        'bmi': 28,
        'gender': 'Male',
        'ever_married': 'Yes',
        'work_type': 'Private',
        'Residence_type': 'Urban',
        'smoking_status': 'never smoked'
    }

    # Send a POST request to the /predict endpoint with test data
    response = client.post('/predict', json=test_data)

    # Check if response status code is 200
    assert response.status_code == 200

    # Check if response contains 'stroke_prediction' key
    assert 'stroke_prediction' in response.json

    # Check if prediction value is either 0 or 1
    assert response.json['stroke_prediction'] in [0, 1]

    # Additional tests can be added here based on expected behavior


# def test_predict_invalid_data(client):
#     # Test case data with invalid values
#     test_data = {
#         'age': 'invalid_age',  # Age should be a numeric value
#         'avg_glucose_level': 125,
#         'bmi': 28,
#         'gender': 'Male',
#         'ever_married': 'Yes',
#         'work_type': 'Private',
#         'Residence_type': 'Urban',
#         'smoking_status': 'never smoked'
#     }

#     # Send a POST request to the /predict endpoint with invalid test data
#     response = client.post('/predict', json=test_data)

#     # Check if response status code is 400 (Bad Request) instead of 200
#     assert response.status_code == 400

#     # Check if response does not contain 'stroke_prediction' key
#     assert 'stroke_prediction' not in response.json
