from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


APPIUM_SERVER_URL = "http://127.0.0.1:4723"
PACKAGE_NAME = "com.swaglabsmobileapp"
ACTIVITY_NAME = "com.swaglabsmobileapp.SplashActivity"
SCREENSHOT_DIR = Path(__file__).parent / "anh"
WAIT_SECONDS = 20


@pytest.fixture
def driver(request):
    options = UiAutomator2Options()
    options.load_capabilities(
        {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Samsung A12",
            "udid": "R58R51YD6BL",
            "appPackage": PACKAGE_NAME,
            "appActivity": ACTIVITY_NAME,
            "noReset": False,
        }
    )

    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    app_driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    try:
        wait = WebDriverWait(app_driver, WAIT_SECONDS)
        username = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Username")
            )
        )
        username.send_keys("standard_user")
        app_driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Password"
        ).send_keys("secret_sauce")
        app_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
        wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Item title")
            )
        )

        yield app_driver
    finally:
        # Lưu ảnh cuối ca để lưu lại trạng thái kiểm thử.
        try:
            app_driver.save_screenshot(
                str(SCREENSHOT_DIR / f"{request.node.name}.png")
            )
        finally:
            app_driver.quit()


def _visible_product_titles(driver):
    return [
        item.text
        for item in driver.find_elements(
            AppiumBy.ACCESSIBILITY_ID, "test-Item title"
        )
    ]

def test_scroll_products_and_save_element_screenshot(driver):
    before_scroll = _visible_product_titles(driver)

    # Cuộn thẳng xuống cuối danh sách (tối đa 10 lần vuốt cho đến khi kịch sàn)
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)'
    )

    # Chờ danh sách sản phẩm hiển thị các sản phẩm ở cuối trang
    WebDriverWait(driver, WAIT_SECONDS).until(
        lambda current_driver: _visible_product_titles(current_driver)
        != before_scroll
    )

    # Lưu ảnh màn hình và ảnh riêng của tiêu đề sản phẩm đang hiển thị.
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    assert driver.save_screenshot(str(SCREENSHOT_DIR / "products_scrolled.png"))
    product_title = WebDriverWait(driver, WAIT_SECONDS).until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Item title")
        )
    )
    assert product_title.screenshot(
        str(SCREENSHOT_DIR / "product_title_scrolled.png")
    )