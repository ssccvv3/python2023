# cash = int(input('지금 얼마 있어 ?'))
# #input 값을 따로 정수로 만들 필요없이, cash 값에 int(정수)를 넣어 cash 값이 정수가 됨

# print("현재 소지금:",cash,type(cash))
# if cash >= 100000 :
#     print("레스토랑에 가자")
# else:
#     print("방콕이나 하자ㅠ")
age = int(input("몇살 입니까?"))
if age >= 19:
    print("당신은 성인입니다.")
elif age >= 10 and age < 19:
    print("당신은 청소년 입니다.")
else:
    print("당신은 아동입니다.")