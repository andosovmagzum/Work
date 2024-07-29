import random
import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

first_name = driver.find_element(By.ID, "input-firstname")
first_name.send_keys(fake.first_name())

last_name = driver.find_element(By.ID, "input-lastname")
last_name.send_keys(fake.last_name())

#random_email = str(random.randint (0, 99999)) + "myemail@example.com"

email = driver.find_element(By.ID, "input-email")
email.send_keys(fake.email())

telephone = driver.find_element(By.ID, "input-telephone")
telephone.send_keys(fake.phone_number())

fakePassword = fake.password()
password = driver.find_element(By.ID, "input-password")
password.send_keys(fakePassword)

password_confirm = driver.find_element(By.ID,"input-confirm")
password_confirm.send_keys(fakePassword)

newsletter = driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]")
newsletter.click()

terms = driver.find_element(By.XPATH, "//label[@for='input-agree']")
terms.click()

continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
continue_button.click()

try:
    assert driver.title == "Your Account Has Been Created!"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is Different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "//h1[@class='page-title my-3']")
try:
    assert driver.title == "My Account"
except AssertionError:
    print("Title is Different. Current Title is:", driver.title)

continue_button1 = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
continue_button1.click()

driver.find_element(By.XPATH, "//i[contains(@class,'fas fa-2x mb-1 fa-user-edit')]")

driver.find_element(By.LINK_TEXT, "Edit Account"). click()
time.sleep(0.5)

try:
    assert driver.title == "My Account Information"
except AssertionError:
    print("Title is Different. Current Title is:", driver.title)

driver.quit()
