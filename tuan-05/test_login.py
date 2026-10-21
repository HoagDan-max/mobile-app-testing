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
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = ".MainActivity"

    # Đường dẫn tới file APK ở thư mục gốc dự án
    current_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    options.app = os.path.join(
        current_dir,
        "Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
    )

    # Cấu hình từ uiautomator2-driver: Tăng timeout lên 300s để tránh ngắt kết nối
    options.new_command_timeout = 300

    # Kết nối Appium Server
    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    try:
        yield driver
    finally:
        driver.quit()


def test_login_success(driver):
    """Test Case 1: Đăng nhập thành công với tài khoản chuẩn"""
    # 1. Định vị ô Username và điền "standard_user"
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))
    )
    username_field.send_keys("standard_user")

    # 2. Định vị ô Password và điền "secret_sauce"
    password_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password")
    password_field.send_keys("secret_sauce")

    # 3. Bấm nút LOGIN
    login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    login_button.click()

    # 4. Kiểm tra chuyển màn hình: Dùng ANDROID_UIAUTOMATOR tìm text "PRODUCTS"
    products_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("PRODUCTS")'
        ))
    )
    assert products_title.is_displayed(), "Đăng nhập thất bại: Không tìm thấy tiêu đề PRODUCTS"


def test_login_fail_invalid_password(driver):
    """Test Case 2: Đăng nhập thất bại do sai mật khẩu"""
    # 1. Nhập username chuẩn
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))
    )
    username_field.send_keys("standard_user")

    # 2. Nhập mật khẩu sai
    password_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password")
    password_field.send_keys("sai_mat_khau_roi")

    # 3. Bấm nút LOGIN
    login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    login_button.click()

    # 4. Kiểm tra thông báo lỗi có chứa chuỗi "do not match" bằng UiSelector textContains
    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("do not match")'
        ))
    )
    assert error_msg.is_displayed(), "Không hiển thị thông báo lỗi sai mật khẩu"


def test_login_fail_locked_out_user(driver):
    """Test Case 3: Đăng nhập thất bại do tài khoản bị khóa"""
    # 1. Nhập tài khoản bị khóa
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))
    )
    username_field.send_keys("locked_out_user")

    # 2. Nhập mật khẩu chuẩn
    password_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password")
    password_field.send_keys("secret_sauce")

    # 3. Bấm nút LOGIN
    login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    login_button.click()

    # 4. Kiểm tra thông báo lỗi chứa chuỗi "locked out" bằng UiSelector textContains
    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("locked out")'
        ))
    )
    assert error_msg.is_displayed(), "Không hiển thị thông báo lỗi tài khoản bị khóa"