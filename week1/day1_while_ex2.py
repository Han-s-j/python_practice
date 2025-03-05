import random

# 업다운 게임
# 3번의 기회
# 사용자 입력이 맞으면 '정답', 작으면 '업', 크면 '다운' 출력
# 틀릴 때 마다 몇 번의 기회가 있는지 출력
# computer의 랜덥 값은 1 ~ 10 사이의 정수
# 기회, 중복없는 빈 변수 만들기
chance = 3
num = (random.randint(1, 10))
print(num)
# 조건문
print(("=" * 20) + "업다운 게임 시작" + ("=" * 20))
while chance > 0:
    user_num = int(input("1 ~ 10사이의 정수를 입력하세요!:"))
    if num == user_num:
        print("정답")
        break
    elif num > user_num:
        print("업")
        chance -=1
        # if chance != 0:
        #     print("남은 기회:", chance)
        # else:
        #     print("다음 기회에....")
        if chance == 0:
            break
        print("남은 기회 ",chance)
        continue
    else:
        print("다운")
        chance -=1
        if chance == 0:
            break
        print("남은 기회 ",chance)
        continue
if chance == 0:
    print("다음 기회에.. 정답은: ", num)


