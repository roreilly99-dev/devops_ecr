"""
FastAPI application for Perth Events API
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from datetime import datetime
from models.event import Event, EventList, EventCategory
from utils.database import get_database
from scrapers.run_all import run_all_scrapers

app = FastAPI(
    title="Perth Events API",
    description="API for Perth events including dining, cinema, markets, and sports",
    version="1.0.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = get_database()


@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "Perth Events API",
        "version": "1.0.0",
        "endpoints": {
            "events": "/api/events",
            "event_by_id": "/api/events/{event_id}",
            "categories": "/api/categories",
            "scrape": "/api/scrape"
        }
    }


@app.get("/api/events", response_model=EventList)
async def get_events(
    category: Optional[EventCategory] = None,
    start_date: Optional[str] = Query(None, description="ISO format date"),
    end_date: Optional[str] = Query(None, description="ISO format date"),
    limit: int = Query(100, ge=1, le=500)
):
    """
    Get events with optional filters
    
    - **category**: Filter by event category (dining, cinema, market, sports)
    - **start_date**: Filter events from this date onwards
    - **end_date**: Filter events up to this date
    - **limit**: Maximum number of events to return
    """
    # Parse dates
    start_dt = datetime.fromisoformat(start_date) if start_date else None
    end_dt = datetime.fromisoformat(end_date) if end_date else None
    
    events = db.get_events(
        category=category,
        start_date=start_dt,
        end_date=end_dt,
        limit=limit
    )
    
    return EventList(
        events=events,
        total=len(events),
        category=category,
        start_date=start_dt,
        end_date=end_dt
    )


@app.get("/api/events/{event_id}", response_model=Event)
async def get_event(event_id: str):
    """Get a specific event by ID"""
    event = db.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.get("/api/categories")
async def get_categories():
    """Get list of available event categories"""
    return {
        "categories": [
            {"id": "dining", "name": "Dining", "icon": "🍽️"},
            {"id": "cinema", "name": "Cinema", "icon": "🎬"},
            {"id": "market", "name": "Markets", "icon": "🛍️"},
            {"id": "sports", "name": "Sports", "icon": "⚽"}
        ]
    }


@app.post("/api/scrape")
async def trigger_scrape():
    """
    Trigger manual scraping of all sources
    (In production, this would be protected with authentication)
    """
    try:
        total = run_all_scrapers()
        return {
            "status": "success",
            "message": f"Scraped {total} events",
            "total_events": total
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scraping failed: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
