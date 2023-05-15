import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class SearchFlightResults(BaseDriver):
    def __init__(self, driver, action):
        super().__init__(driver)
        self.driver = driver
        self.action = action

    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULT = "//span[contains(text(), 'Non Stops') or contains(text(), '1 Stop') or contains(text(), '2 Stops')]"
    EXPAND_MORE_FLIGHTS = "//div[contains(@ng-click, 'showmoretoggle(flt.showmore,legid,true)')]"

    def get_filter_by_one_stop_icon(self):
        # return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULT)

    def get_expand_more_flights(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXPAND_MORE_FLIGHTS), \
            self.wait_for_presence_of_all_elements(By.XPATH, self.EXPAND_MORE_FLIGHTS)

    def expand_more_flights(self):
        more_flight_list = self.get_expand_more_flights()
        print(len(more_flight_list))

        locat = self.driver.find_elements(By.XPATH, "//div[contains(@ng-click, 'showmoretoggle(flt.showmore,legid,true)')]")

        # for i in range(0, len(more_flight_list[1])):
        #     argsz = "arguments[{}].click();".format(str(i))
        #     self.driver.execute_script(argsz, locat)
        #     time.sleep(2)

        self.wait_until_element_is_clickable()

        # for flight in more_flight_list:
        #     self.driver.execute_script("arguments[0].scrollIntoView();", flight)
        #     time.sleep(2)
        #     # try:
        #     #     flight.click()
        #     # except ElementClickInterceptedException:
        #     #     pass
        #
        #     self.action.click(on_element=flight).perform()


        print("All flight has been expanded")


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

        self.page_scroll_to_top()

        time.sleep(3)
        # self.expand_more_flights()

        time.sleep(3)