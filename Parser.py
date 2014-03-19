from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        pass
    @staticmethod
    def parse_all_links(page):
        urls = []
        try:
            soup = BeautifulSoup(page)
            all_lis = soup.findAll('li',{'class':'g'})
            for each_li in all_lis:
                if each_li:
                    h3 = each_li.find('h3',{'class':'r'})
                    if h3:
                        anchor = h3.find('a')
                        #urls += [anchor]
                        if anchor:
                            url = anchor['href']
                            if url:
                                urls += [url]
            return urls
        except Exception,msg:
            print msg
            return []