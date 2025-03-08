from src.services.crawler_service import crawler_service

def test_crawler_registration():
    service = crawler_service()
    service.register_crawler("test_crawler", crawler_service)
    assert "test_crawler" in service.crawlers
