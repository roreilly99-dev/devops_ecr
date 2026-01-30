"""
Tests for event models
"""
import pytest
from datetime import datetime
from models.event import Event, EventCategory, EventType, Location


def test_event_creation():
    """Test creating a basic event"""
    location = Location(name="Test Venue", suburb="Perth CBD")
    event = Event(
        title="Test Event",
        category=EventCategory.DINING,
        event_type=EventType.WEEKLY_DEAL,
        start_date=datetime.now(),
        location=location,
        source="test"
    )
    
    assert event.title == "Test Event"
    assert event.category == EventCategory.DINING
    assert event.location.name == "Test Venue"


def test_event_with_optional_fields():
    """Test creating an event with optional fields"""
    location = Location(
        name="Test Stadium",
        address="123 Test St",
        suburb="Subiaco",
        latitude=-31.9505,
        longitude=115.8605
    )
    
    event = Event(
        title="Test Sports Event",
        description="A test sports event",
        category=EventCategory.SPORTS,
        event_type=EventType.FOOTY,
        start_date=datetime.now(),
        location=location,
        price="$50",
        url="https://example.com",
        source="test"
    )
    
    assert event.description == "A test sports event"
    assert event.price == "$50"
    assert event.url == "https://example.com"
    assert event.location.latitude == -31.9505
