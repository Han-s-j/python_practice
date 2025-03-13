import cx_Oracle
from mylogger import make_logger
logger = make_logger("DBM.log", "get_connection")

class DBManager:

    def __init__(self):
        self.conn = None

    def get_connection(self):
        try:
            if self.conn is None or self.conn.closed:
                self.conn = cx_Oracle.connect("member","oracle","localhost:1521/xe")
            return self.conn
        except Exception as e:
            print(f"DB 연결 오류:{e}")
            return None
    def __del__(self):
        """객체 소멸 시 연결 종료"""
        if self.conn:
            self.conn.close()
            print("db 연결이 정상적으로 종료되었습니다.")
    def insert(self, query, param):
        """데이터 삽입"""
        cursor = None
        try:
            if self.conn is None:
                self.get_connection()
            cursor = self.conn.cursor()
            cursor.execute(query, param)
            self.conn.commit()
            print("저장!")
        except Exception as e:
            print(f"저장 오류!{e}")
            if self.conn:
                self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

if __name__ == '__main__':
    db = DBManager()
    conn = db.get_connection()
    if conn:
        db.insert("INSERT INTO 학생 (학번, 이름) VALUES(:1, :2)", [1, "동수"] )
