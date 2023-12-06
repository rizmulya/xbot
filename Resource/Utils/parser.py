from Resource import argparse

custom_help = '''
    usage: testing.py [-h] [-l] [-s <search_keywords>]

    X/Twitter Bot

    options:
        -h, --help            show this help message and exit
        -l, --login           Login with selenium
        -s <search_keywords>, --scrape <search_keywords>
                        Scraping tweets based on search keywords
    '''

def parser():
    parser = argparse.ArgumentParser(
        description='X/Twitter Bot',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('-l','--login', action='store_true', help='Login with selenium')
    parser.add_argument('-s','--scrape', help='Scraping tweets based on search keywords')

    return parser.parse_args()