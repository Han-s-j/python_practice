#day1-6
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv
url = 'https://www.melon.com/chart/index.htm'
# 406 상황
# res = requests.get(url)
# print(res.status_code)
# soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
tbody = soup.find('tbody')
trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    rank = tds[1].select_one('span.rank').text # id가 무조건 하나일 때
    a_tags = tds[5].find_all('a')
    title = a_tags[0].text
    singer = a_tags[1].text
    print(rank, title, singer)
    print("="*100)

# print(soup.prettify())
# tr = soup.select_one('#lst50')
# tds = tr.find_all('td')
# data_rows = []
# for i, tds in enumerate(tds):  # 인덱스 활용하기
#     if i != 0:
#         seq = tds.select_one('.title')
#         if seq:
#             seq_num = seq.get('data-seq')
#             # title 출력
#             title = tds.select_one('.title').text.strip()
#             data_rows.append([seq_num, title])
#     with open('melon.csv', 'a', encoding='utf-8', newline='') as f:
#         write = csv.writer(f, delimiter='|')
#         write.writerow(data_rows)
#         print(data_rows)