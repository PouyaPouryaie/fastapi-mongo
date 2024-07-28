from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_todos():
    response = client.get("/todo")
    assert response.status_code == 200
    
    print(response.json())