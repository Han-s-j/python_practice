import pandas as pd
from week2.ex_db.DBManager import DBManager
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
from PIL import Image
import numpy as np
sql = """
    SELECT *
    FROM stock_bbs
"""
db = DBManager()
conn = db.get_connection()
df = pd.read_sql(con=conn, sql=sql)
for i, v in df.iterrows():
    print(v['BBS_CONTENTS'])
#1.명사 추출
okt = Okt()
nouns = []
stop_words = {"이요","더군다나","건가","쭉쭉","자동","처방","때문","사형","고아","무조건","그냥","그게","간다","보임","역시","정말","지리","자체"}    # 제외 단어 목록
for idx, row in df.iterrows():
    text = row['BBS_CONTENTS'].strip()
    word_list = okt.nouns(text) # 명사만 추출
    filter_list = [x for x in word_list if len(x) > 1 and x not in stop_words] # and x not in stop_words
    nouns +=filter_list
count = Counter(nouns)
print(nouns)
#2.단어 카운트 생성
#3.워드클라우드 생성

cloud = WordCloud(font_path="../../dataset/NanumGothicBold.ttf"
                   ,width=800, height=400, background_color="white"
                  , min_font_size=15) #최소 폰트 크기)
gen = cloud.generate_from_frequencies(count)
plt.figure(figsize=(10, 5))
plt.imshow(gen)
plt.axis("off")
plt.show()
