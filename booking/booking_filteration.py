# This file will include a class with instance methods.
# That will be responsible to interact with our website.
# After we have some results, to apply filterations
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
class BookingFilteration:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def apply_star_rating(self,rating):
        star_filter= self.driver.find_element(
            By.CSS_SELECTOR,
            f"input[value='class={rating}']"
        )
        star_filter.click()


