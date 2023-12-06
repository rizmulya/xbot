from Resource import By, WebDriverWait, EC, Select, pd, json
from Resource.Driver.WebDriver import WebDriver
from Spiders.Locator import Locator

class TweetsSpider:
    def __init__(self, search_keywords):
        self.driver = WebDriver().driver
        self.search_keywords = search_keywords
        self.user_data = []
        self.text_data = []
        self.tweet_ids = set()

    def login(self):
        self.driver.get("https://twitter.com")
        self.driver.maximize_window()
        print("Login ...")

        with open("cookies_x.json", "r") as file:
            cookies = json.load(file)

        for cookie in cookies:
            self.driver.add_cookie(cookie) 

    def get_tweet(self, element):
        """Returns username and text"""
        try:
            user = WebDriverWait(element, 10).until(
                EC.presence_of_element_located(Locator.TWEETS_USER)
            ).text
            text = WebDriverWait(element, 10).until(
                EC.presence_of_element_located(Locator.TWEETS_TEXT)
            ).text
            tweets_data = [user, text]
        except:
            tweets_data = ['user', 'text']
        return tweets_data

    def scrape_data(self, web):
        self.driver.get(web)
        print("Scraping ...")

        scrolling = True
        while scrolling:
            try:
                tweets = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(Locator.TWEETS)
                )
                print(len(tweets))
                for tweet in tweets:
                    tweet_list = self.get_tweet(tweet)
                    tweet_id = ''.join(tweet_list)
                    if tweet_id not in self.tweet_ids:
                        self.tweet_ids.add(tweet_id)
                        self.user_data.append(tweet_list[0])
                        self.text_data.append(" ".join(tweet_list[1].split()))

                last_height = self.driver.execute_script("return document.body.scrollHeight")
                while True:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    WebDriverWait(self.driver, 10).until(
                        lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height
                    )
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        scrolling = False
                        break
                    else:
                        last_height = new_height
                        break
            except:
                scrolling = False

    def save_data(self, output_csv):
        self.driver.quit()
        df_tweets = pd.DataFrame({'user': self.user_data, 'text': self.text_data})
        df_tweets.to_csv(output_csv, index=False)
        print(df_tweets)

    def exec(self, output_csv):
        self.login()
        self.scrape_data(
            f"https://twitter.com/search?q={self.search_keywords}&src=typed_query"
            )
        self.save_data(output_csv)

