flag = True
if flag:    # () 대신 :
    print("true 입니다.")
else:
    print("false 입니다.")
print("종료")

# 문자열 기본 함수
print("hi".upper())
print("HELLO".lower())
c = "Life is to Short".replace("Short","Long") # old를 new로 변경
print(c)
# 문자열 콘솔 입력받기
msg = input("문자를 입력하세요!:") # 숫자로 입력해도 문자열로 인식
print(msg, type(msg))
num = int(msg)
print(num, type(num))
# 조건문 if 는 조건에 따라 코드 블록을 실행
num = int(input("정보를 입력하세요:"))
if num > 10:
    print("입력은 10보다 큼")
elif num == 10:
    print("입력은 10과 같음")
elif num == 9:
    pass # 아무 작업도 하지 않을 때
else:
    print("9보다 작음")
print("종료")