import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    # When a class that called this fixture, both of this var will be returned
    # so, the var object can be used within the test class (self)
    request.cls.driver = driver
    request.cls.wait = wait

    #yeild works like tear down. Will be executed after all process / testcase done
    yield

    driver.close()
    driver.quit()

