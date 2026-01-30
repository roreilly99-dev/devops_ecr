"""
Scraper for outdoor cinema events in Perth
"""
from datetime import datetime, timedelta
from typing import List
from models.event import Event, EventCategory, EventType, Location
from .base_scraper import BaseScraper


class CinemaScraper(BaseScraper):
    """Scraper for outdoor cinema events"""
    
    def __init__(self):
        super().__init__("CinemaScraper")
    
    def scrape(self) -> List[Event]:
        """
        Scrape outdoor cinema events
        
        Sample implementation with mock data.
        In production, scrape from Moonlight Cinema, Rooftop Movies, etc.
        """
        events = []
        
        # Sample cinema events
        sample_cinemas = [
            {
                "title": "Moonlight Cinema - The Grand Budapest Hotel",
                "location": "Kings Park",
                "description": "Classic film under the stars",
                "day_offset": 2,
                "price": "$20"
            },
            {
                "title": "Rooftop Movies - Barbie",
                "location": "Northbridge Rooftop",
                "suburb": "Northbridge",
                "description": "Recent blockbuster on the rooftop",
                "day_offset": 5,
                "price": "$18"
            },
            {
                "title": "Sunset Cinema - Top Gun: Maverick",
                "location": "Burswood Park",
                "suburb": "Burswood",
                "description": "Action movie with Perth skyline views",
                "day_offset": 10,
                "price": "$22"
            }
        ]
        
        for cinema in sample_cinemas:
            event = Event(
                title=cinema["title"],
                description=cinema["description"],
                category=EventCategory.CINEMA,
                event_type=EventType.OUTDOOR_CINEMA,
                start_date=datetime.now() + timedelta(days=cinema["day_offset"]),
                location=Location(
                    name=cinema["location"],
                    suburb=cinema.get("suburb", "Perth")
                ),
                price=cinema.get("price"),
                source=self.source_name,
                url="https://example.com/cinema"
            )
            events.append(event)
        
        return events


if __name__ == "__main__":
    scraper = CinemaScraper()
    scraper.run()
