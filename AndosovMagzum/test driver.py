from selenium import webdriver
import locators as lc

driver = webdriver.Chrome()
driver.get(lc.g_url)
driver.maximize_window()

print(driver.title)
print(driver.current_url)
assert "Google" in driver.title

driver.quit()
