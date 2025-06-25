import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.base import Base
from app.config.settings import settings

@pytest.fixture(scope="module")
def test_db():
    """Create a test database"""
    # Use a different database URL for testing
    test_db_url = "sqlite:///./test_satellite.db"
    engine = create_engine(test_db_url)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    yield TestingSessionLocal()
    
    # Clean up
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    """Create a test client for FastAPI"""
    with TestClient(app) as c:
        yield c
