#day1-3
import csv
import requests
from bs4 import BeautifulSoup

def get_paxnset(page):
    url ="https://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10841&page=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup.prettify())
    # print(soup.prettity())
    # id:comm-list
    # 의 li 출력
    div = soup.select_one('#comm-list') # 이 클래스 이름을 가져오겠다
    lis = div.find_all('li') # li태그에 있는 걸 싹 다 가져오겠다
    data_rows = []
    for i, li in enumerate(lis):    # 인덱스 활용하기
        if i !=0:
            seq = li.select_one('.type')
            if seq:
                seq_num = seq.get('data-seq')
                # title 출력
                title = li.select_one('.title .best-title').text.strip()
                data_rows.append([seq_num, title])
            #print(seq)
            #print("="*100)
    with open('paxnet.csv', 'a', encoding='utf-8', newline='') as f:
        write = csv.writer(f, delimiter='|')
        write.writerow(data_rows)

if __name__ == '__main__':
    for p in range(1, 11):  # 1페이지 부터
        get_paxnset(p)