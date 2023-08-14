# # exercise 1 
# #  10, 2.2, "apple" 각각을 변수에 넣고, 각 데이터 타입을 출력하세요
# a = 10
# b = 2.2
# c = "apple"
# # 한번에 타입을 알아보고 싶었지만 아직 찾을 수 없었다.
# print(type(a))
# print(type(b))
# print(type(c))

# # exercise 2
# # 다음 코드를 실행 해보고 \t 와 \n의 역할을 설명하세요

# #     code = '000660\n00000102\t12312312'
# #     print (code)
# code = '000660\n00000102\t12312312'
# print (code)
# # \n은 문단 변경, \t는 사이 간격 탭

# # exercise 3
# # 사용자로 부터 두 개의 숫자를 입력 받은 후 큰 숫자를 화면 출력

# a = int(input('숫자 입력'))
# b = int(input('숫자 입력'))

# if a > b:
#     print(a)
# else:
#     print(b)
    
# # exercise 4 
# #  사용자로부터 입력 받은 숫자가 홀수인지 짝수인지 출력

# data1 = int(input('숫자입력')) % 2
# data2 = int(input('숫자입력')) % 2

# if data1 == 0:
#     print("짝수")
# else:
#     print("홀수")
# if data2 == 0:
#     print("짝수")
# else:
#     print("홀수")
    
# # exercise 5 
# # 사용자로 부터 3개의 숫자를 입력 받은 후 가장 작은 숫자를 출력하세요.

# number1 = int(input('숫자입력1'))
# number2 = int(input('숫자입력2'))
# number3 = int(input('숫자입력3'))

# if number1 <= number2 and number1 <= number3:
#     print("number1",number1)
# elif number2 <= number1 and number2 <= number3:
#     print('number2',number2)
# else:
#     print('number3',number3)
    
# # 세 수를 비교하여 가장 작은 값을 도출하도록 if 반복문을 작성한다.

# exercise 6
# 사용자로 부터 점수를 입력 받은 후 등급을 출력
#   (A: 100 ~ 81 B: 80 ~ 61 C: 60 ~ 0)

# grade = int(input('시험 점수를 입력하세요.'))

# if grade <= 100 and grade >= 81:
#     print("A등급")
# elif grade >= 61 and grade <=80:
#     print("B등급")
# elif grade >= 0 and grade <= 60:
#     print("C등급")