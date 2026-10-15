import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Fixture tự động mở và dọn dẹp trình duyệt cho MỌI hàm test
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/login")
    yield browser  # Trả trình duyệt cho hàm test dùng
    browser.quit() # Tự động đóng trình duyệt sau khi test xong (thay thế cho finally)


def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Dùng WebDriverWait chuẩn như code của bạn
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "You logged into a secure area!" in message.text