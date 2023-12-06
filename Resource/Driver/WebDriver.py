from Resource import webdriver


class WebDriver:
    def __init__(self, headless=False):
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("window-size=1920x1080")
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = webdriver.Chrome()