#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

db_name = 'proscrp'
uname = 'root'
password = 'root'
host = '127.0.0.1'

class DBWraper:
    def __init__(self):
        try:
            self.dbconn = MySQLdb.connect(host=host,user=uname,passwd=password,db=db_name)
            print 'Connected.'
        except Exception,msg:
            self.dbconn = None
            print 'Not Connected.'
            print msg
            
    def save_urls(self,urls,page_start):
        if self.dbconn:
            with self.dbconn:
                for each_url in urls:
                    cur = self.dbconn.cursor()
                    query = "insert into page_urls(page_link,start_val,fetching_done) values('%s',%s,0)" % (each_url,str(page_start))
                    print query
                    cur.execute(query)
                    
    def read_urls(self,start=0,limit=20):
        urls = []
        if self.dbconn:
            cur = self.dbconn.cursor()
            query = "select * from page_urls where fetching_done=0 limit %s,%s" % (str(start),str(start+limit))
            cur.execute(query)
            rows = cur.fetchall()
            for each_row in rows:
                urls += [each_row]
        return urls
            
    def save_page(self,url_id,page):
        if self.dbconn:
            with self.dbconn:
                cur = self.dbconn.cursor()
                query = "insert into html_page(page_url_id,page_content) values(%s,'%s')" % (str(url_id),MySQLdb.escape_string(page))
                cur.execute(query)
                
    def update_url_status_read(self,url_id):
        if self.dbconn:
            with self.dbconn:
                cur = self.dbconn.cursor()
                query = "update page_urls set fetching_done=1 where id=%s" % str(url_id)
                cur.execute(query)
                
    def read_pages(self,start=0,count=20):
        pages = []
        if self.dbconn:
            cur = self.dbconn.cursor()
            query = "select * from html_page limit %s,%s" % (str(start),str(start+count))
            cur.execute(query)
            rows = cur.fetchall()
            for each_row in rows:
                pages += [each_row]
        return pages
            
    def close(self):
        if self.dbconn:
            self.dbconn.close()
            

#db = DBWraper()
#print db.read_urls()
#db.save_urls(['http://www.vogella.de'],0)
#import urllib2
#response = urllib2.urlopen('http://www.google.com')
#page = response.read()
#p = open('page.html','w')
#print page.replace('"','\"').replace("'","\'")
#page = """ 

#"""
 
#print len(page)
#db.save_page(2,page)
#print db.read_pages(0,20)
#db.update_current_state((1,1,1,'LINK',1,1,1))
#db.save_category_info([(1,'','cat_name','http://stackoverflow.com/questions/5687718/python-mysql-insert-data')])
#print len('http://stackoverflow.com/questions/5687718/python-mysql-insert-data')



