from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "span.title")

    def title_text(self) -> str:
        return self.get_text(self.TITLE)
