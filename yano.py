#encoding:utf-8
from selenium import webdriver
import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib2
from HTMLParser import HTMLParser

class htmlParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False

    def handle_starttag(self, tag, attrs):
        if tag == "span":
            self.flag = True

    def handle_data(self, data):
    	if self.flag:
            match = rp.match(data)
            if match:
            	arr_Icon_str.append(match.group())
            	print match.group()
            self.flag = False

def getParser(html):
		parser = htmlParser()
		parser.feed(html)
		parser.close()

if __name__ == '__main__':
	iconFlg = True
	arr_Icon_str = []
	defPage = 0
	keyword = u'ロボット'
	driver = webdriver.Chrome(executable_path='/Users/soichiro_rin/Desktop/Python/selenium/chromedriver')
	url = 'https://www.yano.co.jp/'
	pattern = r"[A-Z]\d{8}"
	rp = re.compile(pattern)

	driver.get(url)
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.NAME, "query"))
	    )
	finally:
		time.sleep(1)
	query = driver.find_element_by_name('query')
	query.send_keys(keyword)
	query.submit()

	while iconFlg:
		html = driver.page_source
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		link = driver.find_element_by_xpath("//div[@id='AreaAct']/div[4]/ul/li[7]/a/span")
		page = driver.find_element_by_xpath("//li[@class='active']")
		activePage = page.text.replace(u"(current)", "").strip()
		if defPage == activePage:
			iconFlg = False
		else:
			getParser(html)
			link.click()
			time.sleep(0.8)
			defPage = activePage
	print arr_Icon_str
	print len(arr_Icon_str)
