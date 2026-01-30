# Perth Events Scraper - Backend

Python backend for scraping and serving Perth events data.

## Features

- Web scraping for various event types:
  - Restaurant deals and special dinners
  - Outdoor cinema screenings
  - Markets
  - Sports events (footy, rugby, tennis, cricket, basketball)
- RESTful API for event data
- Database integration (DynamoDB/MongoDB)
- Scheduled scraping jobs

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the API

```bash
# Development
uvicorn api.main:app --reload

# Production
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

## Running Scrapers

```bash
# Run all scrapers
python -m scrapers.run_all

# Run specific scraper
python -m scrapers.restaurants_scraper
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html
```
