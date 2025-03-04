# src/main.py
from fastapi import FastAPI
from src.api.v1.crawler_api import router as crawler_router
from src.api.v1.crawled_data_api import router as crawled_data_router

app = FastAPI(title="Crawler Service API")

app.include_router(crawler_router, prefix="/api/v1", tags=["Crawler"])
app.include_router(crawled_data_router, prefix="/api/v1", tags=["Crawled Data"])

@app.get("/")
def root():
    return {"message": "Crawler Service API is running!"}
