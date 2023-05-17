import pytest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utilities

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver, self.action)
        self.ut = Utilities()

    def test_search_flights_1stop(self):
        # Launching browser and opening the travel website
        # Provide going from location
        sf = self.lp.searchFlight("New Delhi", "New York", "15/05/2023")
        # Click on flight search button
        self.lp.clickSearch()
        #scrolling element
        self.lp.page_scroll()
        # Select the filter 1 stop
        sf.filter_flights_by_stop("1 Stop")
        # Verify that the filtered results show flights having only 1 stop
        allstops1 = sf.get_search_flight_results()
        print(len(allstops1))
        self.ut.assertListItemText(allstops1, "1 Stop")