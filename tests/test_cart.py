import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_and_add_item(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()


def test_add_item_to_cart():
    driver = webdriver.Chrome()
    login_and_add_item(driver)

    inventory_page = InventoryPage(driver)
    cart_count = inventory_page.get_cart_count()
    assert cart_count == "1", f"❌ Кількість товарів у кошику очікується 1, отримано {cart_count}"

    driver.quit()


def test_remove_item_from_cart():
    driver = webdriver.Chrome()
    login_and_add_item(driver)

    inventory_page = InventoryPage(driver)

    # 🔎 Перевірка передумови: товар додано
    cart_count = inventory_page.get_cart_count()
    assert cart_count == "1", "❌ Товар не доданий до кошика перед видаленням"

    # 🗑️ Видаляємо товар
    inventory_page.remove_item_from_cart()

    # ✅ Перевірка, що товар видалено (елемент кошика зник)
    cart_badge_elements = driver.find_elements(*inventory_page.cart_badge)
    assert len(cart_badge_elements) == 0, "❌ Товар не був видалений з кошика"

    driver.quit()
