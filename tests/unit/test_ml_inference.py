import pytest
from PIL import Image
import numpy as np
from app.services.ml_inference import MLInferenceService
from app.config.settings import settings

def test_preprocess_image():
    """Test image preprocessing"""
    service = MLInferenceService()
    test_image = Image.new('RGB', (256, 256), color='red')
    processed = service.preprocess_image(test_image)
    assert isinstance(processed, np.ndarray)
    assert processed.shape == (256, 256, 3)

def test_classify_image(mock_model):
    """Test image classification"""
    service = MLInferenceService()
    test_image = Image.new('RGB', (256, 256), color='red')
    
    # Mock model response
    mock_model.return_value = {
        "classification": "urban_area",
        "confidence": 0.95
    }
    
    result = service.classify_image(test_image, "test_model")
    assert "classification" in result
    assert "confidence" in result
    assert result["confidence"] >= 0 and result["confidence"] <= 1
