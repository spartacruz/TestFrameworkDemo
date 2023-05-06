import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class DemoExplicitWait():
    def demo_exp_wait(self):
        # Launching browser and opening the travel website
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        # Provide going from location
        depart_from = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        # Provide going to location
        going_to = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(2)
        going_to.send_keys("New York")
        search_results = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break

        # To resolve sync issues
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"
                                        ))).click()
        all_dates = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
                                        ))).find_elements(By.XPATH,
                                                          "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        # Select the departure date
        for date in all_dates:
            if date.get_attribute("data-date") == "23/08/2021":
                date.click()
                break

        # Click on flight search button
        driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(4)

        pageLength = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pagelength;"
        )
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pagelength;"
            )
            if lastCount == pageLength:
                match = True

        time.sleep(4)

        # Select the filter 1 stop
        # allstops = wait.until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Non Stops' or contains(text(), '1 Stop' or contains(text(), '2 Stops')]"
        # )))
        # print(len(allstops))

        # Select the filter 1 stop
        driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(4)
        allstops1 = wait.until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 "//span[contains(text(), 'Non Stops' or contains(text(), '1 Stop' or contains(text(), '2 Stops')]"
                                                 )))
        print(len(allstops1))

        # Verify that the filtered results show flights having only 1 stop
        for stop in allstops1:
            print("The text is: " + stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")


dExpl = DemoExplicitWait()
dExpl.demo_exp_wait()
