from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import schemas
from app.services.news_service import news_service

router = APIRouter()


@router.get("/events", response_model=List[schemas.EventList])
async def get_events(
    skip: int = 0,
    limit: int = 100,
    status: str = None,
    db: Session = Depends(get_db)
):
    """Get list of events"""
    events = news_service.get_events(db, skip=skip, limit=limit, status=status)
    
    # Convert to list response with entry count
    result = []
    for event in events:
        result.append(schemas.EventList(
            id=event.id,
            title=event.title,
            summary=event.summary,
            category=event.category,
            status=event.status,
            first_seen=event.first_seen,
            last_updated=event.last_updated,
            entry_count=len(event.timeline_entries)
        ))
    
    return result


@router.get("/events/{event_id}", response_model=schemas.Event)
async def get_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    """Get event details with timeline"""
    event = news_service.get_event(db, event_id)
    
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    return event


@router.put("/events/{event_id}", response_model=schemas.Event)
async def update_event(
    event_id: int,
    event_update: schemas.EventUpdate,
    db: Session = Depends(get_db)
):
    """Update event"""
    event = news_service.update_event(db, event_id, event_update)
    
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    return event


@router.post("/scrape")
async def trigger_scrape(db: Session = Depends(get_db)):
    """Manually trigger scraping and processing"""
    count = await news_service.scrape_and_process(db)
    return {"message": f"Scraped and processed {count} new articles"}
