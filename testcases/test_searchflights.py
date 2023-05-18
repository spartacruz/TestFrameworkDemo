import pytest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utilities
from ddt import ddt, data, unpack
import softest

@ddt()
@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver, self.action)
        self.ut = Utilities()

    #can be multiple case - just make a second tuple
    #@data(("New Delhi", "New York", "20/05/2023", "1 Stop"), ("New Delhi", "jfk", "23/05/2023", "1 Stop"))
    @data(("New Delhi", "New York", "20/05/2023", "1 Stop"))
    @unpack
    def test_search_flights_1stop(self, goingfrom, goingto, date, stops):
        # Launching browser and opening the travel website
        # Provide going from location
        sf = self.lp.searchFlight(goingfrom, goingto, date)
        # Click on flight search button
        self.lp.clickSearch()
        #scrolling element
        self.lp.page_scroll()
        # Select the filter 1 stop
        sf.filter_flights_by_stop(stops)
        # Verify that the filtered results show flights having only 1 stop
        allstops1 = sf.get_search_flight_results()
        print(len(allstops1))
        self.ut.assertListItemText(allstops1, stops)