"""
Tests for database utilities
"""
import pytest
from datetime import datetime, timedelta
from models.event import Event, EventCategory, EventType, Location
from utils.database import EventDatabase


@pytest.fixture
def db():
    """Create a fresh database for each test"""
    database = EventDatabase()
    database.clear_all()
    return database


@pytest.fixture
def sample_event():
    """Create a sample event"""
    return Event(
        title="Test Event",
        category=EventCategory.DINING,
        event_type=EventType.WEEKLY_DEAL,
        start_date=datetime.now(),
        location=Location(name="Test Location", suburb="Perth"),
        source="test"
    )


def test_save_event(db, sample_event):
    """Test saving a single event"""
    event_id = db.save_event(sample_event)
    assert event_id is not None
    assert sample_event.id == event_id


def test_get_event(db, sample_event):
    """Test retrieving an event"""
    event_id = db.save_event(sample_event)
    retrieved = db.get_event(event_id)
    assert retrieved is not None
    assert retrieved.title == sample_event.title


def test_get_events_by_category(db):
    """Test filtering events by category"""
    # Create events of different categories
    dining_event = Event(
        title="Dining Event",
        category=EventCategory.DINING,
        event_type=EventType.WEEKLY_DEAL,
        start_date=datetime.now(),
        location=Location(name="Restaurant", suburb="Perth"),
        source="test"
    )
    
    sports_event = Event(
        title="Sports Event",
        category=EventCategory.SPORTS,
        event_type=EventType.FOOTY,
        start_date=datetime.now(),
        location=Location(name="Stadium", suburb="Perth"),
        source="test"
    )
    
    db.save_event(dining_event)
    db.save_event(sports_event)
    
    dining_events = db.get_events(category=EventCategory.DINING)
    assert len(dining_events) == 1
    assert dining_events[0].category == EventCategory.DINING


def test_delete_event(db, sample_event):
    """Test deleting an event"""
    event_id = db.save_event(sample_event)
    assert db.get_event(event_id) is not None
    
    db.delete_event(event_id)
    assert db.get_event(event_id) is None
