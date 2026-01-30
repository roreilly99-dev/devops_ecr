# Quick Start Guide - Perth Events Scraper

This guide will help you get the Perth Events Scraper running locally in under 5 minutes.

## Prerequisites

- Python 3.11+ installed
- Node.js 18+ installed
- Git installed

## Option 1: Quick Start with Docker Compose (Recommended)

If you have Docker installed:

```bash
# Clone the repository
git clone https://github.com/roreilly99-dev/devops_ecr.git
cd devops_ecr

# Start both backend and frontend
docker-compose up --build

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

That's it! The application is now running.

## Option 2: Manual Setup

### Step 1: Start the Backend

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the backend API
uvicorn api.main:app --reload
```

Backend is now running at `http://localhost:8000`

### Step 2: Start the Frontend (in a new terminal)

```bash
# Navigate to frontend directory
cd my-app

# Install dependencies
npm install

# Run the development server
npm run dev
```

Frontend is now running at `http://localhost:3000`

## First Steps

1. **Open your browser** to `http://localhost:3000`

2. **Click "Update Events"** button to trigger scraping (this will populate sample events)

3. **Explore the features:**
   - Switch between Calendar and List views
   - Filter by event categories (Dining, Cinema, Markets, Sports)
   - Click on events in the calendar to see details
   - Browse events in list view

## API Endpoints

Once the backend is running, you can access:

- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Get Events**: http://localhost:8000/api/events
- **Get Categories**: http://localhost:8000/api/categories
- **Trigger Scraping**: POST http://localhost:8000/api/scrape

## Testing

### Run Backend Tests
```bash
cd backend
source venv/bin/activate
pytest
```

### Build Frontend
```bash
cd my-app
npm run build
```

## Next Steps

- **Add Real Scrapers**: Edit the scraper files in `backend/scrapers/` to scrape real event sources
- **Deploy to AWS**: Follow the infrastructure README in `infrastructure/`
- **Customize Frontend**: Modify components in `my-app/app/components/`
- **Add Database**: Configure DynamoDB or MongoDB in `backend/utils/database.py`

## Troubleshooting

### Backend won't start
- Ensure Python 3.11+ is installed: `python --version`
- Check if port 8000 is available: `lsof -i :8000`
- Verify all dependencies installed: `pip list`

### Frontend won't start
- Ensure Node.js 18+ is installed: `node --version`
- Check if port 3000 is available: `lsof -i :3000`
- Try deleting node_modules and reinstalling: `rm -rf node_modules && npm install`

### No events showing
- Click the "Update Events" button to trigger scraping
- Check backend is running at http://localhost:8000/health
- Check browser console for errors
- Verify API URL in frontend (should be http://localhost:8000)

## Getting Help

- Check the main [README.md](README.md) for detailed documentation
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Check GitHub Issues for known problems
- Review backend logs: `backend/logs/` (if configured)

## What's Next?

Now that you have the application running:

1. **Explore the codebase** - understand how scrapers, API, and frontend work together
2. **Add real data sources** - replace sample data with actual Perth event sources
3. **Customize the UI** - modify colors, layouts, or add new features
4. **Deploy to production** - use the Terraform infrastructure to deploy to AWS

Happy coding! 🎉
