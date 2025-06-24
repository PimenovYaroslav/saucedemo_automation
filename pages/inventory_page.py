from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.item_remove_button = (By.ID, "remove-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item_to_cart(self):
        self.driver.find_element(*self.item_add_button).click()

    def remove_item_from_cart(self):
        self.driver.find_element(*self.item_remove_button).click()

    def get_cart_count(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.cart_badge)
        )
        return self.driver.find_element(*self.cart_badge).text
