import time
class BaseDriver:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pagelength;"
        )
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pagelength;"
            )
            if lastCount == pageLength:
                match = True

        time.sleep(4)