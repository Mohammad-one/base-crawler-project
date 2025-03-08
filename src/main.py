from fastapi import FastAPI
from starlette.responses import JSONResponse
from src.controller.crawler_controller import router as crawler_router
from src.controller.crawled_data_controller import router as crawled_data_router
import logging

app = FastAPI(title="Crawler Service API")

app.include_router(crawler_router, prefix="/api/v1", tags=["Crawler"])
app.include_router(crawled_data_router, prefix="/api/v1", tags=["Crawled Data"])

app.include_router(crawler_router, prefix="/api/v1", tags=["Crawler"])


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logging.error(f"Unhandled exception: {exc}")
    return JSONResponse(status_code=500, content={"message": "Internal Server Error", "error": str(exc)})


@app.get("/")
def root():
    return {"message": "Crawler Service API is running!"}
