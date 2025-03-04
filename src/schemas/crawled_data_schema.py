from pydantic import BaseModel
from datetime import datetime

class CrawledDataBase(BaseModel):
    url: str
    title: str
    content: str | None = None

class CrawledDataCreate(CrawledDataBase):
    pass
class CrawledDataResponse(CrawledDataBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True