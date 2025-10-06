# FocusLine - Quick Reference

## 5-Minute Quick Start

```bash
# 1. Clone
git clone https://github.com/rakei076/FocusLine.git
cd FocusLine

# 2. Configure (optional - works without AI)
cp .env.example .env
# Edit .env and add OPENAI_API_KEY if you have one

# 3. Start with Docker
docker-compose up -d

# 4. Access
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/api/v1/docs
```

## Common Commands

### Docker

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Restart a service
docker-compose restart backend
docker-compose restart frontend

# Rebuild after code changes
docker-compose up -d --build
```

### Development

```bash
# Backend development
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd app && python main.py

# Frontend development
cd frontend
npm install
npm run dev
```

### Database

```bash
# Access database
sqlite3 backend/focusline.db

# View tables
.tables

# Query events
SELECT id, title, status FROM events;

# Query timeline
SELECT e.title, t.title, t.timestamp 
FROM events e 
JOIN timeline_entries t ON e.id = t.event_id 
ORDER BY t.timestamp DESC;
```

### API Testing

```bash
# Health check
curl http://localhost:8000/health

# Get all events
curl http://localhost:8000/api/v1/events

# Get event details
curl http://localhost:8000/api/v1/events/1

# Trigger scraping
curl -X POST http://localhost:8000/api/v1/scrape

# Filter by status
curl "http://localhost:8000/api/v1/events?status=active"
```

## File Structure

```
FocusLine/
├── backend/                    # Python backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   ├── core/              # Config, database, scheduler
│   │   ├── models/            # Database models
│   │   ├── scrapers/          # News scrapers
│   │   ├── services/          # Business logic
│   │   └── main.py            # App entry point
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile
│
├── frontend/                   # Next.js frontend
│   ├── src/
│   │   ├── app/               # Pages
│   │   ├── components/        # React components
│   │   ├── lib/               # Utilities
│   │   └── types/             # TypeScript types
│   ├── package.json           # Node dependencies
│   └── Dockerfile
│
├── docker-compose.yml         # Docker orchestration
├── .env.example               # Environment template
├── README.md                  # Main documentation
└── start.sh                   # Quick start script
```

## Environment Variables

### Backend (.env)

```bash
OPENAI_API_KEY=sk-...          # Optional, for AI analysis
DATABASE_URL=sqlite:///./focusline.db
SCRAPER_INTERVAL_HOURS=1       # Scraping frequency
OPENAI_MODEL=gpt-4             # AI model to use
```

### Frontend (.env.local)

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

## Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root info |
| `/health` | GET | Health check |
| `/api/v1/events` | GET | List events |
| `/api/v1/events/{id}` | GET | Event details |
| `/api/v1/scrape` | POST | Trigger scraping |

## Troubleshooting

### Backend won't start
```bash
# Check Python version (need 3.11+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Frontend won't start
```bash
# Check Node version (need 18+)
node --version

# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### No articles scraped
```bash
# Check logs
docker-compose logs backend | grep -i scrape

# Manually trigger
curl -X POST http://localhost:8000/api/v1/scrape

# Check internet connectivity
curl -I https://www3.nhk.or.jp
```

### Database locked
```bash
# Stop all services
docker-compose down

# Remove database
rm backend/focusline.db

# Restart
docker-compose up -d
```

## Performance Tips

1. **Use PostgreSQL** for production (better concurrent access)
2. **Add Redis** for caching API responses
3. **Increase scraping interval** for high-traffic sites
4. **Use CDN** for frontend static assets
5. **Enable database indexes** for faster queries

## Security Checklist

- [ ] Change default ports in production
- [ ] Set strong CORS policies
- [ ] Use HTTPS in production
- [ ] Don't commit `.env` files
- [ ] Rotate API keys regularly
- [ ] Set up rate limiting
- [ ] Enable authentication if public

## Monitoring

```bash
# Check service status
docker-compose ps

# View resource usage
docker stats

# Check disk space
df -h

# View database size
du -h backend/focusline.db
```

## Backup

```bash
# Backup database
cp backend/focusline.db backup/focusline_$(date +%Y%m%d).db

# Restore database
cp backup/focusline_20240101.db backend/focusline.db
docker-compose restart backend
```

## Update

```bash
# Pull latest code
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose up -d --build
```

## Support

- Documentation: See README.md, DEVELOPMENT.md, USAGE.md
- Issues: https://github.com/rakei076/FocusLine/issues
- API Docs: http://localhost:8000/api/v1/docs

## Resources

- FastAPI: https://fastapi.tiangolo.com/
- Next.js: https://nextjs.org/
- OpenAI: https://platform.openai.com/docs
- Docker: https://docs.docker.com/
