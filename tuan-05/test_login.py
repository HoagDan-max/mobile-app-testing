from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
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
			"deviceName": "Android Emulator",
			"appPackage": PACKAGE_NAME,
			"appActivity": ACTIVITY_NAME,
			"noReset": False,
		}
	)

	# Khởi tạo phiên Appium mới để mỗi ca bắt đầu từ màn hình đăng nhập.
	app_driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
	SCREENSHOT_DIR.mkdir(exist_ok=True)

	try:
		yield app_driver
	finally:
		# Lưu ảnh kết quả trước khi đóng ứng dụng để làm bằng chứng chạy test.
		try:
			app_driver.save_screenshot(
				str(SCREENSHOT_DIR / f"{request.node.name}.png")
			)
		finally:
			app_driver.quit()


def _login(driver, username, password):
	wait = WebDriverWait(driver, WAIT_SECONDS)
	username_field = wait.until(
		EC.presence_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Username")
		)
	)
	password_field = driver.find_element(
		AppiumBy.ACCESSIBILITY_ID, "test-Password"
	)

	# Nhập dữ liệu qua accessibility id và nhấn nút đăng nhập.
	if username:
		username_field.send_keys(username)
	if password:
		password_field.send_keys(password)
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()


def _error_text(driver):
	wait = WebDriverWait(driver, WAIT_SECONDS)
	error = wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Error message")
		)
	)
	return " ".join(
		element.text
		for element in error.find_elements(
			AppiumBy.CLASS_NAME, "android.widget.TextView"
		)
	)


def test_login_with_valid_credentials(driver):
	_login(driver, "standard_user", "secret_sauce")

	# Kiểm tra trang danh sách sản phẩm sau khi đăng nhập thành công.
	product = WebDriverWait(driver, WAIT_SECONDS).until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Item title")
		)
	)
	assert product.text == "Sauce Labs Backpack"


def test_login_with_invalid_password(driver):
	_login(driver, "standard_user", "wrong_password")

	# Kiểm tra ứng dụng từ chối thông tin đăng nhập không hợp lệ.
	assert "Username and password do not match any user in this service." in (
		_error_text(driver)
	)


def test_login_without_username(driver):
	_login(driver, "", "secret_sauce")

	# Kiểm tra thông báo khi bỏ trống trường tên đăng nhập.
	assert "Username is required" in _error_text(driver)
