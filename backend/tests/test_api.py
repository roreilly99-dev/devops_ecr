"""
Tests for API endpoints
"""
import pytest
from fastapi.testclient import TestClient
from api.main import app
from utils.database import get_database


@pytest.fixture
def client():
    """Create a test client"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    """Clear database before each test"""
    db = get_database()
    db.clear_all()
    yield
    db.clear_all()


def test_root_endpoint(client):
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Perth Events API"


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_categories(client):
    """Test getting categories"""
    response = client.get("/api/categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert len(data["categories"]) > 0


def test_get_events_empty(client):
    """Test getting events when database is empty"""
    response = client.get("/api/events")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 0
    assert data["events"] == []


def test_scrape_endpoint(client):
    """Test manual scraping endpoint"""
    response = client.post("/api/scrape")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "total_events" in data
    assert data["total_events"] > 0


def test_get_events_after_scraping(client):
    """Test getting events after scraping"""
    # First scrape
    client.post("/api/scrape")
    
    # Then get events
    response = client.get("/api/events")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] > 0
    assert len(data["events"]) > 0


def test_get_events_by_category(client):
    """Test filtering events by category"""
    # Scrape events
    client.post("/api/scrape")
    
    # Get dining events
    response = client.get("/api/events?category=dining")
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "dining"
    # All returned events should be dining
    for event in data["events"]:
        assert event["category"] == "dining"


def test_get_nonexistent_event(client):
    """Test getting an event that doesn't exist"""
    response = client.get("/api/events/nonexistent")
    assert response.status_code == 404
