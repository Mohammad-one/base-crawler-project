from src.services.base_selenium import BaseSeleniumCrawler
from src.repositories.crawled_data_repo import CrawledDataRepository
from src.configs.database import get_db
import logging


class Service(BaseSeleniumCrawler):
    def __init__(self):
        super().__init__()
        self.crawlers = {}

    def register_crawler(self, name: str, crawler_class):
        self.crawlers[name] = crawler_class
        logging.info(f"Registered crawler: {name}")

    def run_crawler(self, name: str, url: str):
        if name not in self.crawlers:
            raise ValueError(f"Crawler '{name}' not found.")

        crawler = self.crawlers[name]()
        data = crawler.crawl(url)
        crawler.close()

        db = next(get_db())
        repo = CrawledDataRepository(db)
        saved_entry = repo.create_crawled_data(url, data.get("title"), data.get("content"))

        return {"id": saved_entry.id, "url": saved_entry.url, "title": saved_entry.title,
                "content": saved_entry.content}


crawler_service = Service()
