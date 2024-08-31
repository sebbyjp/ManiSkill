from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
import pytest

# Define a Pydantic model for the payload
class Payload(BaseModel):
    motion_type: str
    sense_type: str
    data: dict

# Create a FastAPI app
app = FastAPI()

@app.post("/process")
async def process_payload(payload: Payload):
    # Simulate processing the payload
    return {"status": "success", "motion_type": payload.motion_type, "sense_type": payload.sense_type}

# Test class for FastAPI server and client
class TestFastAPIServerClient:
    @pytest.fixture(scope="class")
    def client(self):
        return TestClient(app)

    def test_process_payload(self, client):
        payload = {
            "motion_type": "move",
            "sense_type": "vision",
            "data": {"key": "value"}
        }
        response = client.post("/process", json=payload)
        assert response.status_code == 200
        assert response.json() == {
            "status": "success",
            "motion_type": "move",
            "sense_type": "vision"
        }
