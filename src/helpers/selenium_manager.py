from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import logging
from src.configs.config import settings


class SeleniumManager:
    def __init__(self):
        self.options = Options()
        self.options.add_argument(f"window-size={settings.SELENIUM_WINDOW_SIZE}")
        self.options.add_argument(f"user-agent={settings.SELENIUM_USER_AGENT}")
        self.options.add_argument(f"disable-blink-features = AutomationControlled")
        self.options.add_argument(f"no-sandbox")
        self.options.add_argument(f"disable-dev-shm-usage")

        self.service = Service(settings.SELENIUM_DRIVER_PATH)
        self.driver = None

    def start_driver(self):
        if self.driver is None:
            self.driver = webdriver.Firefox(service=self.service, options=self.options)
            # self.driver = webdriver.Chrome(service=self.service, options=self.options)
            self.driver.implicitly_wait(settings.SELENIUM_TIMEOUT)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            logging.info("Selenium webdriver closed")


selenium_manager = SeleniumManager()
