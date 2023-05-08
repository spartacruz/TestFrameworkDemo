import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class SearchFlightResults(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def filter_flights(self):
        self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(4)