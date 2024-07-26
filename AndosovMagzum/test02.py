from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url_google = "https://www.google.com/"
url_yahoo = "https://www.yahoo.com/"
url_tesla = "https://www.tesla.com/"
driver.get(url_google)
driver.maximize_window()

assert driver.current_url == url_google
current_url = driver.current_url
if current_url == url_google:
    print("Current URL is OK")
else:
    print("Current URL is different than Expect URL", driver.current_url)

pageGoogle_ExpectedTitle = "Google"
pageYahoo_ExpectedTitle = "Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos"
pageTesla_ExpectedTitle = "Electric Cars, Solar & Clean Energy | Tesla"
current_title == driver.title

if current_title == pageGoogle_ExpectedTitle:
    print("Current Title is OK")
else:
    print("Current Title is different than Expected Title. Current Title is", driver.title)

if current_url == url_google:
    GoogleIcon = driver.find_element(By.XPATH, value="//img[@id='hplogo']")
elif current_url == url_yahoo:
    YahooIcon = driver.find_element(By.XPATH, value="/header/div[@id='module-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]/*[1]")
elif current_url == url_tesla:
    TeslaIcon = driver.find_element(By.XPATH, value="/header/h1[1]/a[1]/*[1]")
else:
    print("Current Url is out of scope", driver.current_url)

if GoogleIcon:
    print("Google Logo is OK", driver.get_screenshot_as_file("current_page.png"))
else:
    print("No Google Logo", driver.get_screenshot_as_file("wrong_current_page.png"))
driver.quit()
