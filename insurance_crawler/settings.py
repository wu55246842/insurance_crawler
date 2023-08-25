"""
settings.py
This file contains the settings for the web crawler. These settings include the URL to be crawled, the depth of the crawl, and any other parameters required by the Scrapy framework.
"""

from typing import Dict

class Settings:
    def __init__(self, url: str, depth: int, parameters: Dict[str, str]):
        self.url = url
        self.depth = depth
        self.parameters = parameters

    def get_url(self) -> str:
        return self.url

    def get_depth(self) -> int:
        return self.depth

    def get_parameters(self) -> Dict[str, str]:
        return self.parameters

# Default settings
DEFAULT_SETTINGS = Settings(
    url="http://www.example.com",
    depth=2,
    parameters={
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "AUTOTHROTTLE_ENABLED": True,
        "HTTPCACHE_ENABLED": True,
        "LOG_LEVEL": 'INFO',
    }
)
