from Resource import By, WebDriverWait, EC, json, webdriver, time
from Resource.Driver.WebDriver import WebDriver
from Spiders.Locator import Locator

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = WebDriver().driver
        self.driver.maximize_window()

    def navigate_to_website(self):
        print("Navigating to the website...")
        self.driver.get("https://twitter.com/i/flow/login")

    def username_form(self):
        username = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(Locator.USERNAME_FORM)
        )
        username.send_keys(self.username)

    def password_form(self):
        password = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(Locator.PASSWORD_FORM)
        )
        password.send_keys(self.password)

    def next_button(self):
        next_button = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(Locator.NEXT_BUTTON)
        )
        next_button.click()

    def login_button(self):
        login_button = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located(Locator.LOGIN_BUTTON)
        )
        login_button.click()

    def save_cookies(self):
        time.sleep(9)
        cookies = self.driver.get_cookies()
        with open("cookies_x.json", "w") as file:
            json.dump(cookies, file)

    def exec(self):
        self.navigate_to_website()
        self.username_form()
        self.next_button()
        self.password_form()
        self.login_button()
        self.save_cookies()


        