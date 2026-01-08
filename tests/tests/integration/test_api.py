# tests/integration/test_api.py
def test_predict(client):
    response = client.post("/predict")
    assert response.status_code == 200