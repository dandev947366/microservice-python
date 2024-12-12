from fastapi.testclient import TestClient
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from main import app
client = TestClient(app)

def test_get():
    expected = "Dan"
    res = client.get(f"/v1/resource/resource/{expected}")
    assert expected in res.json()


