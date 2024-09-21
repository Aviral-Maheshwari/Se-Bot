import booking.constants as const
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
import time
from booking.booking_filteration import BookingFilteration
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
    def change_currency(self,):
        currency_element=self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()
        time.sleep(1)
        selected_currency_element = self.find_element(
              By.XPATH,"//div[@class='dc5041d860 c72df67c95 fb60b9836d']//span[contains(@class, 'Picker_selection-text') and contains(., 'United States Dollar')]"
        )
        selected_currency_element.click()

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
    def selected_dates(self, check_in_date,check_out_date):
        check_in_element=self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_in_date}"]'
        )
        check_out_element=self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_out_date}"]'
        )
        check_in_element.click()
        #time.sleep(0.5)
        check_out_element.click()

    def select_adults(self,count):
        selection_count=self.find_element(
            By.CSS_SELECTOR,
            f'button[data-testid="occupancy-config"]'
        )
        selection_count.click()
        decrease_adult = self.find_element(
            By.CSS_SELECTOR,
            f'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 e91c91fa93"]'
        )
        decrease_adult.click()
    def searchButton(self):
        clickSubmit=self.find_element(
            By.CSS_SELECTOR,
            f'button[class= "a83ed08757 c21c56c305 a4c1805887 f671049264 a2abacf76b c082d89982 cceeb8986b b9fd3c6b3c"]'
        )
        clickSubmit.click()


    def apply_filterations(self,rating):
        star_rating = self.find_element(By.XPATH,
        f"//div[contains(text(), '{rating} stars')]"
        )
        star_rating.click()


