from typing import List, Dict, Any
from datetime import datetime
import feedparser
from app.scrapers.base import BaseScraper


class YahooNewsScraper(BaseScraper):
    """Scraper for Yahoo News Japan"""
    
    RSS_FEEDS = [
        "https://news.yahoo.co.jp/rss/topics/top-picks.xml",
        "https://news.yahoo.co.jp/rss/topics/domestic.xml",
        "https://news.yahoo.co.jp/rss/topics/world.xml",
        "https://news.yahoo.co.jp/rss/topics/business.xml",
        "https://news.yahoo.co.jp/rss/topics/entertainment.xml",
        "https://news.yahoo.co.jp/rss/topics/sports.xml",
        "https://news.yahoo.co.jp/rss/topics/it.xml",
        "https://news.yahoo.co.jp/rss/topics/science.xml",
    ]
    
    async def scrape(self) -> List[Dict[str, Any]]:
        """Scrape Yahoo News Japan via RSS feeds"""
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
                        'source': 'yahoo',
                        'published_at': published_at or datetime.utcnow()
                    }
                    articles.append(article)
                    
            except Exception as e:
                print(f"Error scraping Yahoo News feed {feed_url}: {e}")
                continue
        
        return articles
