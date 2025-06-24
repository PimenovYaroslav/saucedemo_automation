import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import LoginPage  # ⬅ імпортуємо наш клас LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)      # ⬅ створюємо об'єкт логін-сторінки
    login_page.open()                   # ⬅ відкриваємо сайт
    login_page.login("standard_user", "secret_sauce")  # ⬅ виконуємо логін

    assert login_page.get_header_text() == "Swag Labs", "❌ Логін неуспішний або неправильний заголовок"
    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    error = login_page.get_error_message()
    assert "Username and password do not match any user" in error, "❌ Повідомлення про помилку не з'явилося"
    driver.quit()