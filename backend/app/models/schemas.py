from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class TimelineEntryBase(BaseModel):
    """Base timeline entry schema"""
    timestamp: datetime
    title: str
    description: Optional[str] = None
    source_url: Optional[str] = None
    source_name: Optional[str] = None


class TimelineEntryCreate(TimelineEntryBase):
    """Schema for creating timeline entry"""
    event_id: int


class TimelineEntry(TimelineEntryBase):
    """Timeline entry response schema"""
    id: int
    event_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class EventBase(BaseModel):
    """Base event schema"""
    title: str
    description: Optional[str] = None
    summary: Optional[str] = None
    category: Optional[str] = None


class EventCreate(EventBase):
    """Schema for creating event"""
    pass


class EventUpdate(BaseModel):
    """Schema for updating event"""
    title: Optional[str] = None
    description: Optional[str] = None
    summary: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None


class Event(EventBase):
    """Event response schema"""
    id: int
    status: str
    first_seen: datetime
    last_updated: datetime
    timeline_entries: List[TimelineEntry] = []
    
    class Config:
        from_attributes = True


class EventList(BaseModel):
    """Event list response"""
    id: int
    title: str
    summary: Optional[str] = None
    category: Optional[str] = None
    status: str
    first_seen: datetime
    last_updated: datetime
    entry_count: int = 0
    
    class Config:
        from_attributes = True


class ArticleBase(BaseModel):
    """Base article schema"""
    title: str
    content: Optional[str] = None
    url: str
    source: str
    published_at: Optional[datetime] = None


class ArticleCreate(ArticleBase):
    """Schema for creating article"""
    pass


class Article(ArticleBase):
    """Article response schema"""
    id: int
    event_id: Optional[int] = None
    scraped_at: datetime
    processed: bool
    
    class Config:
        from_attributes = True
