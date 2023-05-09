import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def departFrom(self, departLocation):

        depart_from = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys(departLocation)
        time.sleep(5)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(5)

    def goingTo(self, goingToLocation):

        going_to = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(2)
        going_to.send_keys(goingToLocation)
        time.sleep(5)

        search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break

        time.sleep(5)

    def selectDate(self, departureDate):
        self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()

        all_dates = self.wait_until_element_is_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")\
            .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for date in all_dates:
            if date.get_attribute("data-date") == departureDate:
                date.click()
                break


    def clickSearch(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(4)