import MySQLdb

db_name = 'spiderbot'
uname = 'root'
password = 'root'
host = '127.0.0.1'

class DBWraper:
    def __init__(self):
        try:
            self.dbconn = MySQLdb.connect(host=host,user=uname,passwd=password,db=db_name)
        except Exception,msg:
            self.dbconn = None
            
    def save_urls(self,urls):
        if self.dbconn:
            with self.dbconn:
                for each_url in urls:
                    cur = self.dbconn.cursor()
                    query = "insert into page_urls(page_link,fetching_done) values('%s',0)" % each_url
                    cur.execute(query)
                    
    def read_urls(self):
        if self.dbconn:
            cur = self.dbconn.cursor()
            query = "select * from page_urls"
            cur.execute(query)
            rows = cur.fetchall()
            return rows
            
    def save_page(self,url,page):
        if self.dbconn:
            with self.dbconn:
                cur = self.dbconn.cursor()
                query = "insert into html_page(page_url_id,page_content) values('%s','%s')" % (url,page)
                cur.execute(query)
                
    def read_pages(self,start=0,count=20):
        if self.dbconn:
            cur = self.dbconn.cursor()
            query = "select * from html_page limit %s,%s" % (str(start),str(start+count))
            cur.execute(query)
            rows = cur.fetchall()
            return rows                    
            
    def close(self):
        if self.dbconn:
            self.dbconn.close()
            
#db = DBWraper()
#db.update_current_state((1,1,1,'LINK',1,1,1))
#db.save_category_info([(1,'','cat_name','http://stackoverflow.com/questions/5687718/python-mysql-insert-data')])
#print len('http://stackoverflow.com/questions/5687718/python-mysql-insert-data')



