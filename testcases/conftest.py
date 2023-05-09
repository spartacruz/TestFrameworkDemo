import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument(r"--no-sandbox")  # Bypass OS security model
    options.add_argument(r"--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument(r"--disable-infobars")  # disabling infobars
    options.add_argument(r"--disable-extensions")  # disabling extensions
    options.add_argument(r"--disable-gpu")  # applicable to windows os only
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument(r"--user-data-dir=C:\Users\speci\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r'--profile-directory=Profile 2')  # e.g. Profile 3

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(executable_path="C:/Users/speci/Downloads/chromedriver_win32 (2)/chromedriver.exe", chrome_options=options)

    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    # When a class that called this fixture, both of this var will be returned
    # so, the var object can be used within the test class (self)
    request.cls.driver = driver

    #yeild works like tear down. Will be executed after all process / testcase done
    yield

    driver.close()
    driver.quit()

