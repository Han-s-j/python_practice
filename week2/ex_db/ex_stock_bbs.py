import pandas as pd
import requests
import json

from week2.ex_db.DBManager import DBManager
db = DBManager()
sql_merge = """
MERGE INTO stock_bbs a
USING DUAL
ON(    a.rsno = :rsno
   AND a.discussion_id = :discussion_id
   AND a.item_code = :item_code)
WHEN MATCHED THEN
    UPDATE SET a.read_count = :read_count
            , a.good_count = :good_count
            , a.bad_count = :bad_count
            , a.comment_count = :comment_count
            , a.update_date = SYSDATE
WHEN NOT MATCHED THEN
    INSERT (a.rsno, a.discussion_id, a.item_code, a.title, a.bbs_contents, a.writer_id
            , a.read_count, a.good_count, a.bad_count, a.comment_count, a.end_path, a.update_date)
    VALUES (:rsno, :discussion_id, :item_code, :title, :bbs_contents, :writer_id
            , :read_count, :good_count, :bad_count, :comment_count, :end_path, TO_DATE(:update_date,'YYYY-MM-DD HH24:MI:SS'))
"""

# db 에서 krx_yn 이 Y인 종목만 요청
def get_bbs(code):
    url=f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}"
    res = requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data['result']:
        row = {
            "rsno": v["rsno"]
            ,"discussion_id":v["discussionId"]
            ,"item_code":v["itemCode"]
            ,"title":v["title"]
            ,"bbs_contents":v["contents"][:1300]
            ,"writer_id" :v["writerId"]
            ,"read_count":v["readCount"]
            ,"good_count":v["goodCount"]
            ,"bad_count":v["badCount"]
            ,"comment_count":v["commentCount"]
            ,"end_path":v["endPath"]
            ,"update_date":v["date"][:19]
        }
        # {'rsno': -298951926, 'discussionId': 298951926, 'type': 'localStock', 'itemCode': '069080', 'replyDepth': 0, 'title': '병관이 부모님도 불쌍함', 'contents': '자식이라고 낳은놈이 동성 성추행이나 하고 있고. 자식놈이 4년동안 ㅆ레기짓 해서 항상 언제 해를 입을까 두려움에 산다 생각하니\r<br>병관이 부모님이 젤 불쌍하시지 않냐?\r<br>', 'writerId': 'kys6****', 'date': '2025-03-17 15:46:55.0', 'readCount': 4, 'goodCount': 0, 'badCount': 0, 'commentCount': 0, 'itemName': '웹젠', 'endPath': '/domestic/stock/069080', 'isHolding': False, 'isHideCleanbot': True}
        try:
            print(row)
            db.insert(sql_merge, row)
        except Exception as e:
            print(str(e))
if __name__ == '__main__':
    db = DBManager()
    conn = db.get_connection()
    selec_sql = """ SELECT krx_code
                         , krx_name
                         , krx_market
                    FROM tb_krx
                    WHERE krx_yn = 'Y'  """
    df = pd.read_sql(con=conn, sql=selec_sql)
    for i, v in df.iterrows():
        code = v['KRX_CODE']
        get_bbs(code)
    print(df.head())
    # get_bbs('069080')

