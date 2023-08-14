#디버깅 ctl + shift + d , 인풋값을 아래 터미널에 입력 가능
age = input("나이는?")
age_int = int(age)
# 인풋의 문자열을 정수로 변경을 해주어야 인식
if age_int >= 19:
    print("당신은 성인입니다.")
elif age_int >= 10 and age_int < 19:
    print("당신은 청소년입니다.")
else :
    print("당신은 아동입니다.")
# else는 항상 마지막에. elif 다시 한번더 사용 가능
    
age1 = input("a의 나이는?")
age1_int = int(age1)
age2 = input("b의 나이는?")
age2_int = int(age2)

if age1_int >= 19 and age2_int >= 18:
    print("두 분 입장 가능합니다")
#둘다 조건식의 참인 경우 가능

if not age1_int >= 19:
    print("두분 혹은 한분은 성인이 아닙니다")