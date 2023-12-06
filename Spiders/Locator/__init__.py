from Resource import By


class Locator:
    USERNAME_FORM = (By.XPATH, '//input[@autocomplete ="username"]')
    PASSWORD_FORM = (By.XPATH, '//input[@autocomplete ="current-password"]')
    NEXT_BUTTON = (By.XPATH, '//div[@role="button"]//span[text()="Next"]')
    LOGIN_BUTTON = (By.XPATH , '//div[@role="button"]//span[text()="Log in"]')
    
    TWEETS = (By.XPATH, "//article[@role='article']")
    TWEETS_USER = (By.XPATH, ".//span[contains(text(), '@')]")
    TWEETS_TEXT = (By.XPATH, ".//div[@lang]")
    