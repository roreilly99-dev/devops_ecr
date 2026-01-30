"""
Run all scrapers
"""
from .restaurants_scraper import RestaurantScraper
from .cinema_scraper import CinemaScraper
from .markets_scraper import MarketScraper
from .sports_scraper import SportsScraper


def run_all_scrapers():
    """Run all available scrapers"""
    scrapers = [
        RestaurantScraper(),
        CinemaScraper(),
        MarketScraper(),
        SportsScraper()
    ]
    
    total_events = 0
    for scraper in scrapers:
        count = scraper.run()
        total_events += count
    
    print(f"\n=== Scraping Complete ===")
    print(f"Total events scraped: {total_events}")
    return total_events


if __name__ == "__main__":
    run_all_scrapers()
