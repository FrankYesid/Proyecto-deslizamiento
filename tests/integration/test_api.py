import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config.settings import settings

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": "0.1.0"}

def test_classify_image(client, test_image_path):
    """Test the image classification endpoint"""
    with open(test_image_path, "rb") as f:
        response = client.post(
            "/api/v1/classify",
            files={"file": ("test.jpg", f, "image/jpeg")}
        )
    
    assert response.status_code == 200
    result = response.json()
    assert "classification" in result
    assert "confidence" in result
    assert result["confidence"] >= 0 and result["confidence"] <= 1

def test_classify_image_with_invalid_file(client):
    """Test classification with invalid file type"""
    with open("test.txt", "rb") as f:
        response = client.post(
            "/api/v1/classify",
            files={"file": ("test.txt", f, "text/plain")}
        )
    
    assert response.status_code == 400
    assert "Unsupported file format" in response.json()["detail"]

def test_classify_image_with_large_file(client, large_image_path):
    """Test classification with too large file"""
    with open(large_image_path, "rb") as f:
        response = client.post(
            "/api/v1/classify",
            files={"file": ("large.jpg", f, "image/jpeg")}
        )
    
    assert response.status_code == 413
    assert "File size exceeds maximum allowed size" in response.json()["detail"]
