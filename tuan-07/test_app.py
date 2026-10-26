from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
	StaleElementReferenceException,
	UnknownMethodException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


APPIUM_SERVER_URL = "http://127.0.0.1:4723"
PACKAGE_NAME = "com.swaglabsmobileapp"
ACTIVITY_NAME = "com.swaglabsmobileapp.SplashActivity"
SCREENSHOT_DIR = Path(__file__).parent / "anh"
WAIT_SECONDS = 20
PRODUCTS = (AppiumBy.ACCESSIBILITY_ID, "test-Item title")


def _login(driver):
	wait = WebDriverWait(
		driver,
		WAIT_SECONDS,
		ignored_exceptions=(StaleElementReferenceException,),
	)
	username = wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Username")
		)
	)
	username.send_keys("standard_user")
	driver.find_element(
		AppiumBy.ACCESSIBILITY_ID, "test-Password"
	).send_keys("secret_sauce")
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
	wait.until(EC.visibility_of_element_located(PRODUCTS))


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

	SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
	app_driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
	try:
		_login(app_driver)
		yield app_driver
	finally:
		try:
			app_driver.save_screenshot(
				str(SCREENSHOT_DIR / f"{request.node.name}.png")
			)
		finally:
			app_driver.quit()


def test_open_product_details_and_navigate_back(driver):
	wait = WebDriverWait(
		driver,
		WAIT_SECONDS,
		ignored_exceptions=(StaleElementReferenceException,),
	)
	product_title = wait.until(EC.visibility_of_element_located(PRODUCTS))
	product_title.click()

	detail_description = wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Description")
		)
	)
	assert detail_description.is_displayed()
	assert driver.current_package == PACKAGE_NAME
	assert driver.current_activity == ".MainActivity"
	wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.XPATH, '//*[@text="Sauce Labs Backpack"]')
		)
	)

	detail_page = driver.find_element(
		AppiumBy.ACCESSIBILITY_ID, "test-Inventory item page"
	)
	driver.execute_script(
		"mobile: scrollGesture",
		{
			"elementId": detail_page.id,
			"direction": "down",
			"percent": 0.5,
		},
	)
	driver.back()

	returned_title = wait.until(EC.visibility_of_element_located(PRODUCTS))
	assert returned_title.text == "Sauce Labs Backpack"
	assert driver.current_activity == ".MainActivity"


def test_reset_app_state_and_restart_app(driver):
	wait = WebDriverWait(driver, WAIT_SECONDS)
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART").click()
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Menu").click()
	driver.find_element(
		AppiumBy.ACCESSIBILITY_ID, "test-RESET APP STATE"
	).click()

	wait.until(
		EC.invisibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-RESET APP STATE")
		)
	)
	wait.until(EC.visibility_of_element_located(PRODUCTS))
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
	wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Cart Content")
		)
	)
	assert "Sauce Labs Backpack" not in driver.page_source
	assert not driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")

	driver.back()
	wait.until(EC.visibility_of_element_located(PRODUCTS))
	driver.terminate_app(PACKAGE_NAME)
	assert driver.query_app_state(PACKAGE_NAME) == 1
	driver.activate_app(PACKAGE_NAME)
	reopened_screen = wait.until(
		lambda current: current.find_elements(*PRODUCTS)
		or current.find_elements(
			AppiumBy.ACCESSIBILITY_ID, "test-Username"
		)
	)
	if reopened_screen[0].get_attribute("contentDescription") == "test-Username":
		_login(driver)
	else:
		assert reopened_screen[0].get_attribute("contentDescription") == "test-Item title"


@pytest.mark.xfail(
	raises=UnknownMethodException,
	strict=True,
	reason="Native app context does not provide the browser cookie endpoint",
)
def test_native_app_cookie_endpoint_is_not_available(driver):
	driver.get_cookies()


@pytest.mark.parametrize(
	("first_name", "last_name", "postal_code", "expected_error"),
	[
		("", "", "", "First Name is required"),
		("An", "", "700000", "Last Name is required"),
		("An", "Nguyen", "", "Postal Code is required"),
		("An", "Nguyen", "700000", None),
	],
	ids=("missing-first-name", "missing-last-name", "missing-postal-code", "complete"),
)
def test_checkout_information_validation(
	driver,
	first_name,
	last_name,
	postal_code,
	expected_error,
):
	wait = WebDriverWait(driver, WAIT_SECONDS)
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART").click()
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
	wait.until(
		EC.visibility_of_element_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Cart Content")
		)
	)
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT").click()

	fields = (
		("test-First Name", first_name),
		("test-Last Name", last_name),
		("test-Zip/Postal Code", postal_code),
	)
	for accessibility_id, value in fields:
		field = wait.until(
			EC.visibility_of_element_located(
				(AppiumBy.ACCESSIBILITY_ID, accessibility_id)
			)
		)
		field.clear()
		if value:
			field.send_keys(value)

	if driver.is_keyboard_shown():
		driver.hide_keyboard()
	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE").click()

	if expected_error:
		error_message = wait.until(
			EC.visibility_of_element_located(
				(AppiumBy.XPATH, f'//*[@text="{expected_error}"]')
			)
		)
		assert error_message.text == expected_error
	else:
		wait.until(
			EC.visibility_of_element_located(
				(AppiumBy.XPATH, '//*[@text="CHECKOUT: OVERVIEW"]')
			)
		)
		assert "Sauce Labs Backpack" in driver.page_source


def _inventory_items(driver):
	return driver.find_elements(
		AppiumBy.XPATH, "//*[@content-desc='test-Item']"
	)


def _wait_for_layout(driver, expected_same_row, minimum_width):
	items = _inventory_items(driver)
	if len(items) < 2:
		return False
	first, second = items[:2]
	same_row = first.location["x"] == second.location["x"]
	return same_row is expected_same_row and first.size["width"] >= minimum_width


def test_toggle_product_grid_and_list_layout(driver):
	wait = WebDriverWait(
		driver,
		WAIT_SECONDS,
		ignored_exceptions=(StaleElementReferenceException,),
	)
	items = wait.until(
		EC.presence_of_all_elements_located(
			(AppiumBy.ACCESSIBILITY_ID, "test-Item")
		)
	)
	assert len(items) >= 2

	if items[0].location["x"] == items[1].location["x"]:
		driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Toggle").click()
		wait.until(lambda current: _wait_for_layout(current, False, 1))

	grid_items = _inventory_items(driver)
	assert len(grid_items) >= 2
	grid_width = grid_items[0].size["width"]
	assert grid_items[0].location["x"] != grid_items[1].location["x"]

	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Toggle").click()
	wait.until(lambda current: _wait_for_layout(current, True, grid_width + 1))
	list_items = _inventory_items(driver)
	assert len(list_items) >= 2
	assert list_items[0].size["width"] > grid_width

	driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Toggle").click()
	wait.until(lambda current: _wait_for_layout(current, False, grid_width))
	assert len(
		driver.find_elements(
			AppiumBy.XPATH, "//*[@content-desc='test-Item']"
		)
	) >= 2
