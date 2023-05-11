import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResultList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getSearchDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDates(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)


    def enterDepartFromLocation(self, departLocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departLocation)
        time.sleep(3)
        self.getDepartFromField().send_keys(Keys.ENTER)
        time.sleep(3)

    def enterGoingToLocation(self, goingToLocation):
        self.getGoingToField().click()
        time.sleep(3)
        self.getGoingToField().send_keys(goingToLocation)
        time.sleep(3)

        search_results = self.getGoingToResultList()

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break

        time.sleep(3)

    def selectDate(self, departureDate):
        self.getSearchDateField().click()

        all_dates = self.getAllDates().find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for date in all_dates:
            if date.get_attribute("data-date") == departureDate:
                date.click()
                break


    def clickSearch(self):
        time.sleep(4)
        self.getSearchButton().click()
        time.sleep(4)