import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class SearchFlightResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULT = "//span[contains(text(), 'Non Stops' or contains(text(), '1 Stop' or contains(text(), '2 Stops')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULT)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            print("Selected flights with 1 Stop")
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            print("Selected flights with 2 Stop")
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            print("Selected flights with Non Stop")
        else :
            print("Please choose the right option-> 1, 2, or Non stop")