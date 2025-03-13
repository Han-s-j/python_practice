import sqlite3
conn = sqlite3.connect("mydb.db")
# 1.array or tuple 순서로
sql ="""
    INSERT INTO tb_coin_detail VALUES(?, ?, ?)
"""
# 2.dict 키로 맴핑
sql2 ="""
    INSERT INTO tb_coin VALUES(:market, :price, :format_now )
"""
data = {
    "market" : "DOGE", "price":"121024000.000000000000000", "format_now":"2025-03-12 15:49:16"
}
cur = conn.cursor()
#cur.execute(sql, ['TEST', 'TEST', 'TEST'])    # 쿼리 실행
cur.execute(sql2, data)
conn.commit()
conn.close()