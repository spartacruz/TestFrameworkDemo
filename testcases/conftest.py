import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request, browser, options, url):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    if driver.capabilities['browserName'] == "chrome":
        # Selenium Stealth settings - bypass bot checking
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.er",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    # create action chain object
    action = ActionChains(driver)

    # driver.get("https://www.yatra.com/")
    if url == None:
        #default url
        url = "https://www.yatra.com/"

    driver.get(url)

    # When a class that called this fixture, both of this var will be returned
    # so, the var object can be used within the test class (self)
    request.cls.driver = driver
    request.cls.action = action

    #yeild works like tear down. Will be executed after all process / testcase done
    yield

    driver.close()
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="class", autouse=True)
def options(request):
    options = Options()
    options.add_argument("no-sandbox")  # Bypass OS security model
    options.add_argument("disable-notifications")
    options.add_argument("disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("disable-infobars")  # disabling infobars
    options.add_argument("disable-extensions")  # disabling extensions
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    return options
