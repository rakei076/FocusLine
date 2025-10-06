# FocusLine Usage Examples

## Quick Start

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/rakei076/FocusLine.git
cd FocusLine

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY (optional)

# Start the services
./start.sh
# Or manually: docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/api/v1/docs
```

### Manual Setup

#### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start server
cd app
python main.py
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.local.example .env.local
# Edit .env.local if needed

# Start development server
npm run dev
```

## API Usage Examples

### Get All Events

```bash
curl http://localhost:8000/api/v1/events
```

Response:
```json
[
  {
    "id": 1,
    "title": "重要なニュースイベント",
    "summary": "イベントの要約",
    "category": "政治",
    "status": "active",
    "first_seen": "2024-01-01T10:00:00",
    "last_updated": "2024-01-01T15:00:00",
    "entry_count": 5
  }
]
```

### Get Event Details with Timeline

```bash
curl http://localhost:8000/api/v1/events/1
```

Response:
```json
{
  "id": 1,
  "title": "重要なニュースイベント",
  "summary": "イベントの要約",
  "description": "詳細な説明",
  "category": "政治",
  "status": "active",
  "first_seen": "2024-01-01T10:00:00",
  "last_updated": "2024-01-01T15:00:00",
  "timeline_entries": [
    {
      "id": 1,
      "timestamp": "2024-01-01T10:00:00",
      "title": "イベント発生",
      "description": "説明",
      "source_url": "https://example.com/article",
      "source_name": "nhk",
      "created_at": "2024-01-01T10:05:00"
    }
  ]
}
```

### Trigger Manual Scraping

```bash
curl -X POST http://localhost:8000/api/v1/scrape
```

Response:
```json
{
  "message": "Scraped and processed 25 new articles"
}
```

### Filter Events by Status

```bash
# Get only active events
curl http://localhost:8000/api/v1/events?status=active

# Get archived events
curl http://localhost:8000/api/v1/events?status=archived
```

### Pagination

```bash
# Get first 10 events
curl http://localhost:8000/api/v1/events?skip=0&limit=10

# Get next 10 events
curl http://localhost:8000/api/v1/events?skip=10&limit=10
```

## Python Client Example

```python
import requests

BASE_URL = "http://localhost:8000/api/v1"

# Get all events
response = requests.get(f"{BASE_URL}/events")
events = response.json()

for event in events:
    print(f"Event: {event['title']}")
    print(f"  Entries: {event['entry_count']}")
    print(f"  Last Updated: {event['last_updated']}")
    print()

# Get event details
event_id = events[0]['id']
response = requests.get(f"{BASE_URL}/events/{event_id}")
event_detail = response.json()

print(f"Timeline for: {event_detail['title']}")
for entry in event_detail['timeline_entries']:
    print(f"  [{entry['timestamp']}] {entry['title']}")

# Trigger scraping
response = requests.post(f"{BASE_URL}/scrape")
print(response.json()['message'])
```

## JavaScript/TypeScript Client Example

```typescript
const API_URL = 'http://localhost:8000/api/v1';

// Get all events
async function getEvents() {
  const response = await fetch(`${API_URL}/events`);
  const events = await response.json();
  
  events.forEach(event => {
    console.log(`Event: ${event.title}`);
    console.log(`  Entries: ${event.entry_count}`);
    console.log(`  Last Updated: ${event.last_updated}`);
  });
  
  return events;
}

// Get event details
async function getEventDetails(eventId: number) {
  const response = await fetch(`${API_URL}/events/${eventId}`);
  const event = await response.json();
  
  console.log(`Timeline for: ${event.title}`);
  event.timeline_entries.forEach(entry => {
    console.log(`  [${entry.timestamp}] ${entry.title}`);
  });
  
  return event;
}

// Trigger scraping
async function triggerScrape() {
  const response = await fetch(`${API_URL}/scrape`, {
    method: 'POST',
  });
  const result = await response.json();
  console.log(result.message);
}

// Usage
getEvents().then(events => {
  if (events.length > 0) {
    getEventDetails(events[0].id);
  }
});
```

## Configuration Examples

### Backend Configuration (.env)

```env
# OpenAI API (optional, but recommended for better analysis)
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Database
DATABASE_URL=sqlite:///./focusline.db

# Scraper Settings
SCRAPER_INTERVAL_HOURS=1
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

# News Sources
ENABLE_NHK=true
ENABLE_YAHOO_NEWS=true
ENABLE_TWITTER=false  # Requires Twitter API

# OpenAI Model
OPENAI_MODEL=gpt-4
```

### Frontend Configuration (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

## Docker Compose Configuration

### Production Setup

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=sqlite:///./focusline.db
      - SCRAPER_INTERVAL_HOURS=1
    volumes:
      - backend-data:/app
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
    depends_on:
      - backend
    restart: unless-stopped

volumes:
  backend-data:
```

## Monitoring and Logs

### View Logs

```bash
# All services
docker-compose logs -f

# Backend only
docker-compose logs -f backend

# Frontend only
docker-compose logs -f frontend

# Last 100 lines
docker-compose logs --tail=100
```

### Check Service Status

```bash
docker-compose ps
```

### Database Inspection

```bash
# Connect to database
docker-compose exec backend sqlite3 /app/focusline.db

# Inside SQLite
.tables
SELECT COUNT(*) FROM events;
SELECT COUNT(*) FROM articles;
SELECT COUNT(*) FROM timeline_entries;
.quit
```

## Troubleshooting

### Backend not starting

```bash
# Check logs
docker-compose logs backend

# Restart backend
docker-compose restart backend
```

### Frontend not connecting to backend

1. Check backend is running: `curl http://localhost:8000/health`
2. Verify NEXT_PUBLIC_API_URL in .env.local
3. Check CORS settings in backend/app/main.py

### No articles being scraped

1. Check internet connectivity
2. Verify news source URLs are accessible
3. Check scraper logs: `docker-compose logs backend | grep -i scraper`

### AI analysis not working

1. Verify OPENAI_API_KEY is set correctly
2. Check OpenAI API status
3. System will fall back to simple keyword-based clustering

## Advanced Usage

### Custom News Sources

Add your own scraper in `backend/app/scrapers/`:

```python
from app.scrapers.base import BaseScraper
from typing import List, Dict, Any

class CustomScraper(BaseScraper):
    async def scrape(self) -> List[Dict[str, Any]]:
        articles = []
        # Your scraping logic here
        return articles
```

Then register it in `backend/app/scrapers/manager.py`:

```python
from app.scrapers.custom_scraper import CustomScraper

class ScraperManager:
    def __init__(self):
        self.scrapers = [
            NHKScraper(),
            YahooNewsScraper(),
            CustomScraper(),  # Add your scraper
        ]
```

### Backup and Restore

```bash
# Backup database
docker-compose exec backend cp /app/focusline.db /app/focusline_backup.db

# Copy to host
docker cp focusline_backend_1:/app/focusline.db ./backup/

# Restore database
docker cp ./backup/focusline.db focusline_backend_1:/app/focusline.db
docker-compose restart backend
```
