from fastapi.testclient import TestClient
from app import app

# Initialize a mock client to test the API without running the full server
client = TestClient(app)

def test_read_root():
    # Simulate a GET request to the root endpoint
    response = client.get("/")
    # Verify the API responds with a 200 OK status
    assert response.status_code == 200
    # Verify the JSON payload matches our expected output
    assert response.json() == {"status": "FleetFlow CI/CD Online!"}