from sqlalchemy import Column, Integer, String, Text, DateTime, func
from src.configs.database import Base


class CrawledData(Base):
    __tablename__ = "crawled_data"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
