"""
Base scraper class with common functionality
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from datetime import datetime
from models.event import Event
from utils.database import get_database


class BaseScraper:
    """Base class for all scrapers"""
    
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.db = get_database()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch a web page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_html(self, html: str) -> BeautifulSoup:
        """Parse HTML content"""
        return BeautifulSoup(html, 'lxml')
    
    def scrape(self) -> List[Event]:
        """
        Main scraping method - to be implemented by subclasses
        Returns list of scraped events
        """
        raise NotImplementedError("Subclasses must implement scrape()")
    
    def run(self) -> int:
        """
        Run the scraper and save results
        Returns number of events scraped
        """
        print(f"Starting {self.source_name} scraper...")
        events = self.scrape()
        
        if events:
            saved_ids = self.db.save_events(events)
            print(f"Scraped and saved {len(saved_ids)} events from {self.source_name}")
            return len(saved_ids)
        else:
            print(f"No events found from {self.source_name}")
            return 0
