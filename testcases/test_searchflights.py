import pytest
from selenium.webdriver.common.by import By
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utilities

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        # Launching browser and opening the travel website

        # Provide going from location
        lp = LaunchPage(self.driver)
        lp.enterDepartFromLocation("New Delhi")

        # Provide going to location
        lp.goingTo("New York")

        # Select the departure date
        lp.selectDate("10/05/2023")

        # Click on flight search button
        lp.clickSearch()

        #scrolling element
        lp.page_scroll()

        # Select the filter 1 stop
        sf = SearchFlightResults(self.driver)
        sf.filter_flights()

        # Verify that the filtered results show flights having only 1 stop
        allstops1 = self.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(), 'Non Stops' or contains(text(), '1 Stop' or contains(text(), '2 Stops')]")
        print(len(allstops1))

        ut = Utilities()
        ut.assertListItemText(allstops1, "1 Stop")
