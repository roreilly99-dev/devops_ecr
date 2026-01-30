"""
Scraper for markets in Perth
"""
from datetime import datetime, timedelta
from typing import List
from models.event import Event, EventCategory, EventType, Location
from .base_scraper import BaseScraper


class MarketScraper(BaseScraper):
    """Scraper for market events"""
    
    def __init__(self):
        super().__init__("MarketScraper")
    
    def scrape(self) -> List[Event]:
        """
        Scrape market events
        
        Sample implementation. In production, scrape from market websites
        and local council event listings.
        """
        events = []
        
        # Sample markets
        sample_markets = [
            {
                "title": "Fremantle Markets",
                "location": "Fremantle Markets",
                "suburb": "Fremantle",
                "description": "Arts, crafts, and fresh produce",
                "day_offset": 1,
                "recurring": "Friday-Sunday"
            },
            {
                "title": "Perth Upmarket",
                "location": "Perth Cultural Centre",
                "suburb": "Perth CBD",
                "description": "Local designers and artisans market",
                "day_offset": 6,
                "recurring": "First Saturday of month"
            },
            {
                "title": "Twilight Hawkers Market",
                "location": "Esplanade Park",
                "suburb": "Perth CBD",
                "description": "Food trucks and street food",
                "day_offset": 3,
                "recurring": "Every Friday evening"
            }
        ]
        
        for market in sample_markets:
            event = Event(
                title=market["title"],
                description=f"{market['description']} - {market['recurring']}",
                category=EventCategory.MARKET,
                event_type=EventType.MARKET,
                start_date=datetime.now() + timedelta(days=market["day_offset"]),
                location=Location(
                    name=market["location"],
                    suburb=market["suburb"]
                ),
                source=self.source_name,
                url="https://example.com/markets"
            )
            events.append(event)
        
        return events


if __name__ == "__main__":
    scraper = MarketScraper()
    scraper.run()
