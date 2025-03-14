import requests
import json

from week2.ex_db.sqlite03 import json_data

# db 에서 krx_yn 이 Y인 종목만 요청
def get_bbs(code):
    url=f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}"
    res = requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data['result']:
        print(v)


