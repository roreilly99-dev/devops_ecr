"""
Scraper for sports events in Perth
"""
from datetime import datetime, timedelta
from typing import List
from models.event import Event, EventCategory, EventType, Location
from .base_scraper import BaseScraper


class SportsScraper(BaseScraper):
    """Scraper for sports events"""
    
    def __init__(self):
        super().__init__("SportsScraper")
    
    def scrape(self) -> List[Event]:
        """
        Scrape sports events
        
        Sample implementation. In production, scrape from AFL, NRL, 
        Tennis Australia, Cricket Australia, NBL websites.
        """
        events = []
        
        # Sample sports events
        sample_sports = [
            {
                "title": "West Coast Eagles vs Collingwood",
                "location": "Optus Stadium",
                "suburb": "Burswood",
                "description": "AFL Round 10",
                "day_offset": 14,
                "event_type": EventType.FOOTY,
                "price": "From $30"
            },
            {
                "title": "Fremantle Dockers vs Sydney Swans",
                "location": "Optus Stadium",
                "suburb": "Burswood",
                "description": "AFL Round 11",
                "day_offset": 21,
                "event_type": EventType.FOOTY,
                "price": "From $28"
            },
            {
                "title": "Western Force vs Waratahs",
                "location": "HBF Park",
                "suburb": "Perth",
                "description": "Super Rugby Pacific",
                "day_offset": 7,
                "event_type": EventType.RUGBY,
                "price": "From $25"
            },
            {
                "title": "Perth Wildcats vs Sydney Kings",
                "location": "RAC Arena",
                "suburb": "Perth CBD",
                "description": "NBL Finals",
                "day_offset": 10,
                "event_type": EventType.BASKETBALL,
                "price": "From $35"
            },
            {
                "title": "Perth Scorchers vs Melbourne Stars",
                "location": "Perth Stadium",
                "suburb": "Burswood",
                "description": "Big Bash League",
                "day_offset": 5,
                "event_type": EventType.CRICKET,
                "price": "From $20"
            }
        ]
        
        for sport in sample_sports:
            event = Event(
                title=sport["title"],
                description=sport["description"],
                category=EventCategory.SPORTS,
                event_type=sport["event_type"],
                start_date=datetime.now() + timedelta(days=sport["day_offset"]),
                location=Location(
                    name=sport["location"],
                    suburb=sport["suburb"]
                ),
                price=sport.get("price"),
                source=self.source_name,
                url="https://example.com/sports"
            )
            events.append(event)
        
        return events


if __name__ == "__main__":
    scraper = SportsScraper()
    scraper.run()
