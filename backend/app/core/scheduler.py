from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.news_service import news_service
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler()


async def scheduled_scrape():
    """Scheduled task to scrape and process news"""
    logger.info("Starting scheduled scrape...")
    db = SessionLocal()
    try:
        count = await news_service.scrape_and_process(db)
        logger.info(f"Scheduled scrape completed: {count} new articles")
    except Exception as e:
        logger.error(f"Error in scheduled scrape: {e}")
    finally:
        db.close()


def start_scheduler():
    """Start the scheduler"""
    # Schedule scraping every hour
    scheduler.add_job(
        scheduled_scrape,
        trigger=IntervalTrigger(hours=settings.SCRAPER_INTERVAL_HOURS),
        id='scrape_news',
        name='Scrape news articles',
        replace_existing=True
    )
    
    scheduler.start()
    logger.info(f"Scheduler started. Scraping every {settings.SCRAPER_INTERVAL_HOURS} hour(s)")


def stop_scheduler():
    """Stop the scheduler"""
    scheduler.shutdown()
    logger.info("Scheduler stopped")
