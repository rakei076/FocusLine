from typing import List, Dict, Any
from app.scrapers.nhk_scraper import NHKScraper
from app.scrapers.yahoo_scraper import YahooNewsScraper
from app.core.config import settings


class ScraperManager:
    """Manage all news scrapers"""
    
    def __init__(self):
        self.scrapers = []
        
        if settings.ENABLE_NHK:
            self.scrapers.append(NHKScraper())
        
        if settings.ENABLE_YAHOO_NEWS:
            self.scrapers.append(YahooNewsScraper())
    
    async def scrape_all(self) -> List[Dict[str, Any]]:
        """Run all enabled scrapers and collect articles"""
        all_articles = []
        
        for scraper in self.scrapers:
            try:
                articles = await scraper.scrape()
                all_articles.extend(articles)
            except Exception as e:
                print(f"Error in scraper {scraper.__class__.__name__}: {e}")
                continue
        
        return all_articles


scraper_manager = ScraperManager()
