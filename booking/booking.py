import booking.constants as const
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
import time

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\SeleniumDrivers",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self):
        self.get(const.BASE_URL)
    # #def change_currency(self,currency=None):
    #     currency_element=self.find_element(
    #         By.CSS_SELECTOR,
    #         'button[data-testid="header-currency-picker-trigger"]'
    #     )
    #     currency_element.click()
        # selected_currency_element=self.find_element(
        #     By.CLASS_NAME,
        #     f'class[Picker_selection-text="{currency}"]'
        # )
        # selected_currency_element.click()

    def select_place_to_go(self,place_to_go):
        search_field=self.find_element(
            By.ID,":rh:")
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(1)
        first_result=self.find_element(
            By.ID,"autocomplete-result-0"
        )
        first_result.click()
