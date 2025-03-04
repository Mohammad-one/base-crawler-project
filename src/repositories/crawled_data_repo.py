from sqlalchemy.orm import Session
from src.models.crawled_data import CrawledData


class CrawledDataRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_crawled_data(self, url: str, title: str = None, content: str = None):
        new_entry = CrawledData(url=url, title=title, content=content)
        self.db.add(new_entry)
        self.db.commit()
        self.db.refresh(new_entry)
        return new_entry

    def get_crawled_data(self, data_id: int):
        return self.db.query(CrawledData).filter(CrawledData.id == data_id).first()

    def get_all_crawled_data(self, limit: int = 10):
        return self.db.query(CrawledData).order_by(CrawledData.created_at.desc()).limit(limit).all()

    def delete_crawled_data(self, data_id: int):
        entry = self.db.query(CrawledData).filter(CrawledData.id == data_id).first()
        if entry:
            self.db.delete(entry)
            self.db.commit()
            return True
        return False
