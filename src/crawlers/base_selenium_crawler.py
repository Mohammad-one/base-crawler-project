from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.core.selenium_manager import selenium_manager
import time


class BaseSeleniumCrawler:
    def __init__(self):
        self.driver = selenium_manager.start_driver()

    def navigate_to(self, url: str):
        self.driver.get(url)
        time.sleep(2)

    def find_element(self, by: By, value: str, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            return None

    def find_elements(self, by: By, value: str, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by, value)))
        except TimeoutException:
            return []

    def click_element(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()
        time.sleep(1)

    def extract_text(self, element):
        return element.text.strip() if element else ""

    def extract_attribute(self, element, attribute: str):
        return element.get_attribute(attribute) if element else ""

    def scroll_page(self, pixels: int = 500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(1)

    def wait_for_element_visible(self, by: By, value: str, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to.frame(frame_reference)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def close(self):
        selenium_manager.close_driver()
