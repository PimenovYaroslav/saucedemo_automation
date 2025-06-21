from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

try:
    # Очікуємо, поки з'явиться елемент з класом app_logo
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    if header.text == "Swag Labs":
        print("✅ Заголовок на сторінці правильний")
    else:
        print("❌ Заголовок на сторінці неправильний")
except:
    print("❌ Не вдалося знайти заголовок на сторінці")
finally:
    driver.quit()