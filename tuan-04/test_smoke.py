
import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Cấu hình kết nối Appium với Samsung A12
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.udid = "R58R51YD6BL"
    options.platform_version = "12"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = ".MainActivity"

    # Lấy đường dẫn tuyệt đối tới file APK ở thư mục gốc
    current_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    options.app = os.path.join(
        current_dir,
        "Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
    )

    # Khởi tạo driver
    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        yield driver
    finally:
        driver.quit()


def test_smoke_app_has_login_field(driver):
    """
    Test Tuần 4: Mở ứng dụng Swag Labs
    và kiểm tra ô nhập Username có hiển thị.
    """
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Username") 
        )
    )

    assert username_field.is_displayed(), (
        "Không tìm thấy ô nhập Username trên màn hình"
    )
