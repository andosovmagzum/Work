from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://htmltestpage.w3spaces.com/testpage.html")
driver.maximize_window()

assert "HTML5 Test Page" in driver.title
driver.find_element(By.XPATH, "//h1[contains(.,'HTML5 Test Page')]")

driver.find_element(By.XPATH, "//a[@href='#text']").click()
time.sleep(1)

driver.find_element(By.XPATH, "(//a[@href='#top'])[1]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//a[contains(.,'Video')]").click()
time.sleep(1)

naMarsVideo = driver.find_element(By.XPATH, "//h2[contains(.,'Video2-"Na Mars"')]")
naMarsVideo.click()
action = ActionChains(driver)

action.double_click(naMarsVideo).perform()

time.sleep(50)

action.double_click(naMarsVideo).perform()
time.sleep(2)

print("End of test")

driver.quit()
