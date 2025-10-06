from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
from app.models import models, schemas
from app.scrapers.manager import scraper_manager
from app.services.ai_service import ai_analyzer


class NewsService:
    """Service for managing news events and articles"""
    
    @staticmethod
    async def scrape_and_process(db: Session) -> int:
        """Scrape news and process into events
        
        Returns:
            Number of new articles processed
        """
        # Scrape articles
        articles = await scraper_manager.scrape_all()
        
        # Save articles to database
        new_count = 0
        article_objs = []
        
        for article_data in articles:
            # Check if article already exists
            existing = db.query(models.Article).filter(
                models.Article.url == article_data['url']
            ).first()
            
            if not existing:
                article = models.Article(**article_data)
                db.add(article)
                article_objs.append(article)
                new_count += 1
        
        db.commit()
        
        # Process unprocessed articles
        await NewsService.process_articles(db)
        
        return new_count
    
    @staticmethod
    async def process_articles(db: Session):
        """Process articles and create/update events"""
        # Get unprocessed articles from last 24 hours
        cutoff_time = datetime.utcnow() - timedelta(hours=24)
        unprocessed = db.query(models.Article).filter(
            models.Article.processed == False,
            models.Article.scraped_at >= cutoff_time
        ).all()
        
        if not unprocessed:
            return
        
        # Convert to dict for AI processing
        article_dicts = [
            {
                'id': a.id,
                'title': a.title,
                'content': a.content,
                'url': a.url,
                'source': a.source,
                'published_at': a.published_at
            }
            for a in unprocessed
        ]
        
        # Cluster articles into events
        clusters = await ai_analyzer.cluster_articles(article_dicts)
        
        for cluster in clusters:
            # Analyze event
            analysis = await ai_analyzer.analyze_event(cluster['articles'])
            
            # Create or update event
            event = models.Event(
                title=cluster['title'],
                summary=analysis.get('summary', ''),
                description=analysis.get('description', ''),
                category=cluster.get('category', 'その他')
            )
            db.add(event)
            db.flush()  # Get event ID
            
            # Associate articles with event
            for article_data in cluster['articles']:
                article = db.query(models.Article).filter(
                    models.Article.id == article_data['id']
                ).first()
                if article:
                    article.event_id = event.id
                    article.processed = True
            
            # Create timeline entries
            for timeline_data in analysis.get('timeline', []):
                try:
                    timestamp = datetime.strptime(
                        timeline_data['timestamp'], 
                        '%Y-%m-%d %H:%M:%S'
                    )
                except:
                    timestamp = datetime.utcnow()
                
                timeline_entry = models.TimelineEntry(
                    event_id=event.id,
                    timestamp=timestamp,
                    title=timeline_data['title'],
                    description=timeline_data.get('description', ''),
                    source_name=cluster['articles'][0].get('source', '')
                )
                db.add(timeline_entry)
        
        db.commit()
    
    @staticmethod
    def get_events(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        status: Optional[str] = None
    ) -> List[models.Event]:
        """Get list of events"""
        query = db.query(models.Event)
        
        if status:
            query = query.filter(models.Event.status == status)
        
        return query.order_by(models.Event.last_updated.desc()).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_event(db: Session, event_id: int) -> Optional[models.Event]:
        """Get event by ID with timeline"""
        return db.query(models.Event).filter(models.Event.id == event_id).first()
    
    @staticmethod
    def update_event(
        db: Session, 
        event_id: int, 
        event_update: schemas.EventUpdate
    ) -> Optional[models.Event]:
        """Update event"""
        event = db.query(models.Event).filter(models.Event.id == event_id).first()
        
        if not event:
            return None
        
        update_data = event_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(event, field, value)
        
        event.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(event)
        
        return event


news_service = NewsService()
