from Resource.Utils.parser import parser, custom_help
from settings import username, password, output_csv
from Spiders.tweets import TweetsSpider
from Spiders.login import Login


def main():
    args = parser()

    if args.login:
        Login(username,password).exec()
    elif args.scrape:
        TweetsSpider(search_keywords=args.scrape).exec(output_csv)
    else:
        print(custom_help)

if __name__ == "__main__":
    main()
