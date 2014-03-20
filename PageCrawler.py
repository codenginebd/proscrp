from HttpBrowser import *
from Parser import *
import time
from random import randint
from DBWraper import *
from Formatter import *

proxies = [
    '89.47.28.61:8800',
    '173.208.46.100:8800',
    '173.208.46.104:8800',
    '173.234.181.253:8800',
    '173.234.181.141:8800',
    '173.234.59.194:8800',
    '173.208.46.182:8800',
    '173.234.59.72:8800',
    '89.47.28.157:8800'
    '173.208.46.111:8800'
]

class PageFetcher:
    def __init__(self):
        self.db = DBWraper()
    def start_crawling(self):
        start = 0
        limit = 20
        while True:
            urls = self.db.read_urls(start=start,limit=limit)
            if not urls:
                break
            for each_url in urls:
                print each_url[1]
                try:
                    index = randint(0,len(proxies) - 1)
                    proxy = proxies[index]
                    page = HttpBrowser.OpenURL(each_url[1],proxy=proxy)
                    refined_page = Formatter.refine_page(page)
                    self.db.save_page(each_url[0],refined_page)
                    self.db.update_url_status_read(each_url[0])
                except Exception,msg:
                    print msg
                timetosleep = randint(1,5)
                time.sleep(timetosleep)
            start += limit
            
PageFetcher().start_crawling()
            