"""
Data models for Perth events
"""
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum


class EventCategory(str, Enum):
    """Event category types"""
    DINING = "dining"
    CINEMA = "cinema"
    MARKET = "market"
    SPORTS = "sports"


class EventType(str, Enum):
    """Specific event types"""
    WEEKLY_DEAL = "weekly_deal"
    SPECIAL_DINNER = "special_dinner"
    OUTDOOR_CINEMA = "outdoor_cinema"
    MARKET = "market"
    FOOTY = "footy"
    RUGBY = "rugby"
    TENNIS = "tennis"
    CRICKET = "cricket"
    BASKETBALL = "basketball"


class Location(BaseModel):
    """Location information"""
    name: str
    address: Optional[str] = None
    suburb: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class Event(BaseModel):
    """Event data model"""
    id: Optional[str] = Field(default=None, description="Unique event ID")
    title: str = Field(..., description="Event title")
    description: Optional[str] = Field(default=None, description="Event description")
    category: EventCategory = Field(..., description="Event category")
    event_type: EventType = Field(..., description="Specific event type")
    
    # Date and time
    start_date: datetime = Field(..., description="Event start date/time")
    end_date: Optional[datetime] = Field(default=None, description="Event end date/time")
    
    # Location
    location: Location = Field(..., description="Event location")
    
    # Additional info
    price: Optional[str] = Field(default=None, description="Price information")
    url: Optional[str] = Field(default=None, description="Event URL")
    image_url: Optional[str] = Field(default=None, description="Event image URL")
    
    # Metadata
    source: str = Field(..., description="Data source")
    scraped_at: datetime = Field(default_factory=datetime.utcnow, description="Scraping timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Italian Night at The Grand",
                "description": "Special 3-course Italian dinner menu",
                "category": "dining",
                "event_type": "special_dinner",
                "start_date": "2024-02-15T18:00:00",
                "end_date": "2024-02-15T22:00:00",
                "location": {
                    "name": "The Grand Hotel",
                    "address": "123 Main St",
                    "suburb": "Perth CBD"
                },
                "price": "$75pp",
                "url": "https://example.com/event",
                "source": "restaurant_website"
            }
        }


class EventList(BaseModel):
    """List of events with metadata"""
    events: List[Event]
    total: int
    category: Optional[EventCategory] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
