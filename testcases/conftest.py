import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("no-sandbox")  # Bypass OS security model
    options.add_argument("disable-notifications")
    # options.add_argument("disable-dev-shm-usage")  # overcome limited resource problems
    # options.add_argument(r"--disable-infobars")  # disabling infobars
    # options.add_argument("disable-extensions")  # disabling extensions
    # options.add_argument(r"--disable-gpu")  # applicable to windows os only
    # options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    # options.add_argument(r"--user-data-dir=C:\Users\speci\AppData\Local\Google\Chrome\User Data")
    # options.add_argument(r'--profile-directory=Profile 2')  # e.g. Profile 3
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)


    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(executable_path="C:/Users/speci/Downloads/chromedriver_win32 (2)/chromedriver.exe", chrome_options=options)

    # Selenium Stealth settings
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    # create action chain object
    action = ActionChains(driver)

    driver.get("https://www.yatra.com/")

    # When a class that called this fixture, both of this var will be returned
    # so, the var object can be used within the test class (self)
    request.cls.driver = driver
    request.cls.action = action

    #yeild works like tear down. Will be executed after all process / testcase done
    yield

    driver.close()
    driver.quit()

