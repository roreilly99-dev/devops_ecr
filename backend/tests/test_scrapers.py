"""
Tests for scrapers
"""
import pytest
from scrapers import (
    RestaurantScraper,
    CinemaScraper,
    MarketScraper,
    SportsScraper
)
from models.event import EventCategory


def test_restaurant_scraper():
    """Test restaurant scraper"""
    scraper = RestaurantScraper()
    events = scraper.scrape()
    
    assert len(events) > 0
    for event in events:
        assert event.category == EventCategory.DINING
        assert event.source == "RestaurantScraper"


def test_cinema_scraper():
    """Test cinema scraper"""
    scraper = CinemaScraper()
    events = scraper.scrape()
    
    assert len(events) > 0
    for event in events:
        assert event.category == EventCategory.CINEMA
        assert event.source == "CinemaScraper"


def test_market_scraper():
    """Test market scraper"""
    scraper = MarketScraper()
    events = scraper.scrape()
    
    assert len(events) > 0
    for event in events:
        assert event.category == EventCategory.MARKET
        assert event.source == "MarketScraper"


def test_sports_scraper():
    """Test sports scraper"""
    scraper = SportsScraper()
    events = scraper.scrape()
    
    assert len(events) > 0
    for event in events:
        assert event.category == EventCategory.SPORTS
        assert event.source == "SportsScraper"
