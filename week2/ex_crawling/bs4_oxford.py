import os.path
from os import write
from bs4 import BeautifulSoup
import requests
import csv
import urllib.request as req
from selenium import webdriver
import time
url = 'https://www.oxfordlearnersdictionaries.com/definition/english/star_1?q=star'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)

# res = requests.get(url)
# print(res.status_code)
# soup = BeautifulSoup(res.content, 'html.parser')
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
#print(soup.prettify())

div = soup.select_one('#star_1')
#print(div)
ols = div.find_all('ol')
#print(ols)
for ol in ols:
    uls = ol.find_all('ul')
    print(uls)
    # examples = uls[0].find_all('li').text
    # print(examples)

##
# tbody = soup.find('tbody')
# trs = tbody.find_all('tr')
# for tr in trs:
#     tds = tr.find_all('td')
#     rank = tds[1].select_one('span.rank').text # id가 무조건 하나일 때
#     a_tags = tds[5].find_all('a')
#     title = a_tags[0].text
#     singer = a_tags[1].text
#     print(rank, title, singer)
#     print("="*100)