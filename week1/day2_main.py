# day2-5
import my_util # 파이썬 파일 하나가 모듈 하나이기 때문에 import해서 사용가능
#help(my_util) # 설명보기
from my_util import get_lotto # 다이렉트로 가져오기 (자체적으로 있는 것 처럼 사용)
from my_util import  get_lotto as l #별칭 사용

print(my_util.get_lotto())
print(get_lotto())
print(l())

