"""
Scraper for restaurant deals and special dinners in Perth
This is a sample implementation that demonstrates the structure
"""
from datetime import datetime, timedelta
from typing import List
from models.event import Event, EventCategory, EventType, Location
from .base_scraper import BaseScraper


class RestaurantScraper(BaseScraper):
    """Scraper for restaurant events in Perth"""
    
    def __init__(self):
        super().__init__("RestaurantScraper")
    
    def scrape(self) -> List[Event]:
        """
        Scrape restaurant events
        
        This is a sample implementation with mock data.
        In production, this would scrape actual restaurant websites,
        social media pages, or aggregator sites.
        """
        events = []
        
        # Sample mock data for demonstration
        # In production, replace with actual web scraping logic
        sample_restaurants = [
            {
                "title": "Taco Tuesday Special",
                "location": "La Cholita",
                "suburb": "Perth CBD",
                "description": "$10 tacos and $8 margaritas every Tuesday",
                "day_offset": 0,
                "event_type": EventType.WEEKLY_DEAL
            },
            {
                "title": "Friday Fish & Chips",
                "location": "The Breakwater",
                "suburb": "Hillarys",
                "description": "Fresh fish and chips special every Friday",
                "day_offset": 3,
                "event_type": EventType.WEEKLY_DEAL
            },
            {
                "title": "Italian Wine Dinner",
                "location": "Bivouac",
                "suburb": "Subiaco",
                "description": "5-course Italian dinner with wine pairing",
                "day_offset": 7,
                "event_type": EventType.SPECIAL_DINNER
            }
        ]
        
        for restaurant in sample_restaurants:
            event = Event(
                title=restaurant["title"],
                description=restaurant["description"],
                category=EventCategory.DINING,
                event_type=restaurant["event_type"],
                start_date=datetime.now() + timedelta(days=restaurant["day_offset"]),
                location=Location(
                    name=restaurant["location"],
                    suburb=restaurant["suburb"]
                ),
                source=self.source_name,
                url="https://example.com/events"  # Would be actual URL
            )
            events.append(event)
        
        return events


if __name__ == "__main__":
    scraper = RestaurantScraper()
    scraper.run()
