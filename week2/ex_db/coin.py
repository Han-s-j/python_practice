import sqlite3
import requests
import json
import datetime
from week2.ex_db.ex_date import format_now

def get_coin():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tb_coin")
    sql = """ INSERT INTO tb_coin_detail
                VALUES(:1, :2, :3)"""
    now = datetime.datetime.now()
    format_now = now.strftime("%Y-%m-%d %H:%M:%S")
    rows = cur.fetchall()
    for row in rows:
        market = row[0]
        kr_nm = row[1]
        url = f"https://api.upbit.com/v1/ticker?markets={market}"
        res = requests.get(url)
        if res.status_code == 200:
            json_data = json.loads(res.text)[0]
            price = "{:.15f}".format(json_data['trade_price'])
            print(market, kr_nm, price, format_now)
            # tb_coin_detail (모든 컬럼은 문자열로)
            # 1. 테이블 생성
            # 2.실시간 가격정보 저장 (마켓코드, 가격, 수집기간 저장)
            # market, price, update_date
            cur.execute(sql, [market, price, format_now])
            conn.commit()



    conn.close()
