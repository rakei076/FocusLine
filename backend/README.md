# FocusLine Backend

This is the backend service for FocusLine, a Japanese hot news tracking and timeline generation system.

## Features

- Automatic news scraping from Japanese sources (NHK, Yahoo News Japan)
- AI-powered article clustering and event analysis
- Timeline generation for news events
- RESTful API for frontend integration
- Automated hourly scraping

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```env
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./focusline.db
SCRAPER_INTERVAL_HOURS=1
```

3. Run the application:
```bash
cd app
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /api/v1/events` - List all events
- `GET /api/v1/events/{id}` - Get event details with timeline
- `PUT /api/v1/events/{id}` - Update event
- `POST /api/v1/scrape` - Manually trigger scraping

## API Documentation

Interactive API documentation available at:
- Swagger UI: `http://localhost:8000/api/v1/docs`
- ReDoc: `http://localhost:8000/api/v1/redoc`

## Architecture

- **Scrapers**: RSS-based scrapers for Japanese news sources
- **AI Service**: OpenAI-based analysis for Japanese text
- **News Service**: Business logic for event management
- **Scheduler**: Automated scraping every hour
- **API**: FastAPI-based REST endpoints
