from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH, value="//img[@id='hplogo']")
driver.find_element(By.XPATH, value="//a[contains(text(),'Почта')]")

GoogleIcon = driver.find_element(By.XPATH, value="//img[@id='hplogo']")

if GoogleIcon:
    print("Google Logo is OK")
else:
    print("No Google Logo")

driver.quit()

