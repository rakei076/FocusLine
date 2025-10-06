from typing import List, Dict, Any
from datetime import datetime
import feedparser
from app.scrapers.base import BaseScraper


class NHKScraper(BaseScraper):
    """Scraper for NHK News"""
    
    RSS_FEEDS = [
        "https://www3.nhk.or.jp/rss/news/cat0.xml",  # Main news
        "https://www3.nhk.or.jp/rss/news/cat1.xml",  # Social
        "https://www3.nhk.or.jp/rss/news/cat2.xml",  # Culture
        "https://www3.nhk.or.jp/rss/news/cat3.xml",  # Politics
    ]
    
    async def scrape(self) -> List[Dict[str, Any]]:
        """Scrape NHK news via RSS feeds"""
        articles = []
        
        for feed_url in self.RSS_FEEDS:
            try:
                feed = feedparser.parse(feed_url)
                
                for entry in feed.entries[:10]:  # Get top 10 from each feed
                    published_at = None
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        published_at = datetime(*entry.published_parsed[:6])
                    
                    article = {
                        'title': entry.get('title', ''),
                        'content': entry.get('description', entry.get('summary', '')),
                        'url': entry.get('link', ''),
                        'source': 'nhk',
                        'published_at': published_at or datetime.utcnow()
                    }
                    articles.append(article)
                    
            except Exception as e:
                print(f"Error scraping NHK feed {feed_url}: {e}")
                continue
        
        return articles
