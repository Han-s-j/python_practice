# 주석 ctrl + /
print("hello") # 콘솔 프린트
# 문자열 '' or "" or '''''' or """"""
a = "hi"
print(a)
print(type(a)) # 타입 자동 인식 /type : 내장함수
b = """
 긴 문자열
 ' or "  
"""
print(b)
print(a * 100) # 문자열 곱하기 가능
# python 식별자 : 변수, 함수, 클래스, 모듈...의 이름
# 규칙
# 1.알파벳, 숫자, 언더스코어(_)로 구성
# 2.숫자로 시작할 수 없음.
# 3.대소문자를 구별함.
# 4.예약어를 사용할 수 없음(for, if, while, ..)
# 5.보통 변수는 스네이크 표기법 사용(_)
my_var = 10 # 선언과 할당
print(my_var, type(my_var))
my_var = 10.1 # 재할당, 자동으로 타입을 인식
print(my_var,type(my_var))

