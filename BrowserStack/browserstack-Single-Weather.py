from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
from BrowserStack import my_key

BROWSERSTACK_USERNAME = my_key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = my_key.BROWSERSTACK_ACCESS_KEY
URL = "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-Single-Weather"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Single-Weather-test",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
        "selfHeal": "true"
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)

    # test1 Chrome
    driver.get('http://www.google.com')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
    time.sleep(1)  # simulate long running test

    search = driver.find_element(By.NAME, "q")
    search.clear()
    search.send_keys("Weather San Jose")
    search.submit()
    time.sleep(1)

    # Check if the search returns any result
    assert "No results found." not in driver.page_source, "No results found in Chrome"
    assert "Weather San Jose - Google Search" in driver.title
    print("Page title in Chrome is:", driver.title)

    # Check Weather frame functionality
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
    wait.until(EC.visibility_of_element_located((By.ID, 'wob_rain')))
    print("Precipitation button is visible")
    wait.until(EC.element_to_be_clickable((By.ID, 'wob_rain')))
    print("Precipitation button is clickable")
    driver.find_element(By.ID, "wob_rain").click()
    time.sleep(1)
    wait.until(EC.visibility_of_element_located((By.ID, 'wob_wind')))
    print("Wind button is visible")
    wait.until(EC.element_to_be_clickable((By.ID, 'wob_wind')))
    print("Wind button is clickable")
    driver.find_element(By.ID, "wob_wind").click()
    time.sleep(1.5)
    wait.until(EC.visibility_of_element_located((By.ID, 'wob_temp')))
    print("Temperature button is visible")
    wait.until(EC.element_to_be_clickable((By.ID, 'wob_temp')))
    print("Temperature button is clickable")
    driver.find_element(By.ID, "wob_temp").click()
    try:
        WebDriverWait(driver, 5).until(EC.title_contains("Weather San Jose - Google Search"))
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched - Weather San Jose!"}}')
    except TimeoutException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()