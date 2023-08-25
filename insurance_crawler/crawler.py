## crawler.py
import scrapy
from typing import Dict
from scrapy.crawler import CrawlerProcess
from .settings import DEFAULT_SETTINGS

class InsuranceCrawler(scrapy.Spider):
    name = "insurance_crawler"
    start_urls = [DEFAULT_SETTINGS.get_url()]

    def parse(self, response):
        # Extract product details
        for product in response.css('div.product'):
            yield {
                'name': product.css('h2 ::text').get(),
                'plan': product.css('div.plan ::text').get(),
                'coverage': product.css('div.coverage ::text').get(),
                'benefits': product.css('div.benefits ::text').get(),
                'clauses': product.css('div.clauses ::text').get(),
            }

        # Follow links to next pages
        for next_page in response.css('a.next-page'):
            yield response.follow(next_page, self.parse)

def start_crawler():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })
    process.crawl(InsuranceCrawler)
    process.start()  # the script will block here until the crawling is finished
