#day1-4
import csv
data_list = []
with open('pacnet.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')   # 잘 안 쓰는 기호가 | 여서. but 다른 기호로 변경가능함
    for row in reader:
        data_list.append(row)
for v in data_list:
    url = f"https://www.paxnet.co.kr/tbbs/view?id=N10841&seq=150357589104478={v[0]}"
    print(v[1])
    print(url)
