from WebBrowser import *
from Parser import *
import time
from random import randint
from DBWraper import *

domain_list = [
    "https://www.google.com.bd/?gws_rd=cr&ei=22IpU7bRC4jRrQeLloGgAg#q=site:http://wetter.de&start=",
    "https://www.google.com.bd/?gws_rd=cr&ei=22IpU7bRC4jRrQeLloGgAg#q=site:http://reise.com&start=",
    "https://www.google.com.bd/?gws_rd=cr&ei=22IpU7bRC4jRrQeLloGgAg#q=site:http://sixx.de&start=",
    "https://www.google.com.bd/?gws_rd=cr&ei=22IpU7bRC4jRrQeLloGgAg#q=site:http://myvideo.de&start="
]

class LinkFetcher:
    def __init__(self):
        self.db = DBWraper()
        pass
    def start_fetching(self):
        for each_link in domain_list:
            start = 10
            browser = WebBrowser()
            while True:
                complete_link = each_link + str(start)
                browser.OpenURL(complete_link)
                page = browser.GetPage()
                page_links = Parser.parse_all_links(page)
                print page_links
                if len(page_links) < 10:
                    break
                self.db.save_urls(page_links,start)
                start += 10
                timetosleep = randint(1,5)
                time.sleep(timetosleep)
            browser.Close()
            
link_fetcher = LinkFetcher()
link_fetcher.start_fetching()
            