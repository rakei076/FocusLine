from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from app.core.config import settings


class BaseScraper(ABC):
    """Base class for news scrapers"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': settings.USER_AGENT
        }
    
    @abstractmethod
    async def scrape(self) -> List[Dict[str, Any]]:
        """Scrape news articles
        
        Returns:
            List of article dictionaries with keys: title, content, url, published_at
        """
        pass
    
    def _get_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a web page"""
        response = requests.get(url, headers=self.headers, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
