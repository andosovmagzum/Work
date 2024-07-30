from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
import time

fake = Faker()

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com")
driver.maximize_window()

assert "California Real Estate" in driver.title
print(driver.title)

driver.find_element(By.ID, "g2-name").send_keys(fake.name())

driver.find_element(By.ID, "g2-email").send_keys(fake.email())

driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(fake.text())

driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

print("OK")
driver.quit()
