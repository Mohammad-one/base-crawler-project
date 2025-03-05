from fastapi import FastAPI
from src.controller.crawler_controller import router as crawler_router
from src.controller.crawled_data_controller import router as crawled_data_router

app = FastAPI(title="Crawler Service API")

app.include_router(crawler_router, prefix="/api/v1", tags=["Crawler"])
app.include_router(crawled_data_router, prefix="/api/v1", tags=["Crawled Data"])


@app.get("/")
def root():
    return {"message": "Crawler Service API is running!"}
