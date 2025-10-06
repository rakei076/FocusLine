from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Event(Base):
    """Hot news event being tracked"""
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    description = Column(Text)
    summary = Column(Text)
    category = Column(String(100))
    status = Column(String(50), default="active")  # active, archived
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    timeline_entries = relationship("TimelineEntry", back_populates="event", cascade="all, delete-orphan")
    articles = relationship("Article", back_populates="event", cascade="all, delete-orphan")


class TimelineEntry(Base):
    """Timeline entry for an event"""
    __tablename__ = "timeline_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    title = Column(String(500), nullable=False)
    description = Column(Text)
    source_url = Column(String(1000))
    source_name = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    event = relationship("Event", back_populates="timeline_entries")


class Article(Base):
    """Raw article data from scrapers"""
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    title = Column(String(500), nullable=False)
    content = Column(Text)
    url = Column(String(1000), unique=True, nullable=False)
    source = Column(String(100))  # nhk, yahoo, twitter
    published_at = Column(DateTime)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    processed = Column(Boolean, default=False)
    
    # Relationships
    event = relationship("Event", back_populates="articles")
