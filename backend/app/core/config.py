from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FocusLine"
    
    # Database
    DATABASE_URL: str = "sqlite:///./focusline.db"
    
    # OpenAI API
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4"
    
    # Scraper Settings
    SCRAPER_INTERVAL_HOURS: int = 1
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    
    # News Sources
    ENABLE_NHK: bool = True
    ENABLE_YAHOO_NEWS: bool = True
    ENABLE_TWITTER: bool = False  # Requires API key
    
    # Twitter/X API (optional)
    TWITTER_BEARER_TOKEN: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
