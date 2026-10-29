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


def test_sort_by_price_and_cancel_sort_dialog(driver):
	wait = WebDriverWait(driver, WAIT_SECONDS)
	driver.find_element(
		AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button"
	).click()

	# Xác nhận popup có lựa chọn và đóng được bằng Cancel.
	low_to_high = (
		AppiumBy.ANDROID_UIAUTOMATOR,
		'new UiSelector().text("Price (low to high)")',
	)
	wait.until(EC.visibility_of_element_located(low_to_high))
	driver.find_element(
		AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cancel")'
	).click()
	wait.until(EC.invisibility_of_element_located(low_to_high))

	# Mở lại popup và sắp xếp giá tăng dần.
	driver.find_element(
		AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button"
	).click()
	wait.until(EC.element_to_be_clickable(low_to_high)).click()
	wait.until(
		lambda current_driver: _visible_product_titles(current_driver)[:1]
		== ["Sauce Labs Onesie"]
	)
	prices = [
		float(price.text.replace("$", ""))
		for price in driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Price")
	]
	assert prices == sorted(prices)
	assert prices[0] == 7.99


def test_add_and_remove_product_from_cart(driver):
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART").click()
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
	WebDriverWait(driver, WAIT_SECONDS).until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Cart Content")
		)
	)
	assert "Sauce Labs Backpack" in driver.page_source

	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-REMOVE").click()
	WebDriverWait(driver, WAIT_SECONDS).until(
		lambda current_driver: "Sauce Labs Backpack" not in current_driver.page_source
	)
	with pytest.raises(NoSuchElementException):
		driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")


def test_drag_product_into_cart(driver):
	wait = WebDriverWait(driver, WAIT_SECONDS)
	drag_handle = wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Drag Handle")
		)
	)
	drop_zone = wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Cart drop zone")
		)
	)
	drop_bounds = drop_zone.rect

	driver.execute_script(
		"mobile: dragGesture",
		{
			"elementId": drag_handle.id,
			"endX": drop_bounds["x"] + drop_bounds["width"] // 2,
			"endY": drop_bounds["y"] + drop_bounds["height"] // 2,
		},
	)
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
	wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Cart Content")
		)
	)
	assert "Sauce Labs Backpack" in driver.page_source


def test_scroll_products_and_save_element_screenshot(driver):
	before_scroll = _visible_product_titles(driver)
	moved = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )
	
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


def test_remote_session_menu_and_logout(driver):
	assert driver.session_id
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Menu").click()
	logout = WebDriverWait(driver, WAIT_SECONDS).until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-LOGOUT")
		)
	)
	logout.click()
	WebDriverWait(driver, WAIT_SECONDS).until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Username")
		)
	)