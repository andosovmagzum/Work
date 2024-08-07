import unittest
import time
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

fake = Faker()

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_weather_chrome(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.maximize_window()

        print(driver.title)
        print(driver.current_url)

        driver.quit()

