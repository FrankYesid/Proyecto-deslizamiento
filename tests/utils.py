import os
from pathlib import Path
import pytest
from PIL import Image

def create_test_image(path: str, size: tuple = (256, 256)) -> str:
    """Create a test image file"""
    img = Image.new('RGB', size, color='red')
    img.save(path)
    return path

def create_large_test_image(path: str, size: tuple = (1024, 1024)) -> str:
    """Create a large test image file"""
    img = Image.new('RGB', size, color='blue')
    img.save(path)
    return path

@pytest.fixture
def test_image_path(tmp_path) -> str:
    """Create a test image file"""
    path = tmp_path / "test.jpg"
    return create_test_image(str(path))

@pytest.fixture
def large_image_path(tmp_path) -> str:
    """Create a large test image file"""
    path = tmp_path / "large.jpg"
    return create_large_test_image(str(path))
