# # exercise 1
# # 1~10까지의 숫자를 모두 더한 값을 출력하는 프로그램을 for 문으로 작성

# sum = 0
# for i in range(1, 11):
#     sum = sum + i
#     print(i,sum)
# print("답:",sum)

# # # exercise 2
# # # 사용자로 부터 2-9 사이의 숫자를 입력 받은 후, 해당 숫자에 대한 구구단 제출

# number = int(input("2-9 숫자를 넣어주세요 ")) #정수 int 사용하여 입력값이 숫자라는걸 인식
# for i in range(1, 10): 
#     sum = number * i
#     print(number,"x", i,"=", sum)
#     # (내가 만든것은 10단 20단 넘어가버림)
    
# # #강의 정답
# number = int(input())
# for i in range(1, 10): 
#     print(number,"x", i,"=", number*i)

# # #강의는 해당값을 각각 대입하여 계산하지 않고, 결과값은 앞의 두 수를 곱으로 간단하게 처리.
# # 조건문과 반복문 함께 사용 경우 
# number = int(input())
# if number >= 2 and number <= 9:
#         for i in range(1, 10): 
#             print(number,"x", i,"=", number*i)

# # exercise 3
# # 사용자로 부터 ' , ' 로 구분된 여러 이름을 입력 받아, 한줄에 하나씩 이름을 출력
# name = input("이름을 ',' 사용하여 넣어주세요. ")
# name2 = name.split(',')
# for i in name2:
#     print(i)

# # exercise 4
# # 사용자로부터 [이름1],[이름2],[이름3] 과 같은 형식으로 데이터를 입력받아서, 한 줄에 하나씩 이름을 출력하세요
# #   - 사용자 입력: [Dave],[David],[Andy],[Arthor]

# name = input("이름을 []와, 사용하여 각각 넣어주세요. ")
# name2 = name.split(',') # => ['[a]', '[b]', '[c]', '[d]', '[e]'] 각각 , 기준으로 인덱스 리스트 정리
# for i in name2:  # i변수는 name2에 있는 인덱스 리스트들을 전채 수량만큼 차례대로 도출해냄을 반복 줄 변경도됨
#     print(i[1:-1],type(i)) 
#     #여기서 i(name2 인덱스 값) 만 입력하면 []포함된 상태로 출력됨,
#     # i는 즉 [a], 인덱스 값, 문자열임
    
# Exercise 4 반복문과 조건문
# * 1부터 30까지의 숫자 중 3의 배수만 출력하세요.

# 내가 푼 출력값, 
# for num in range(1,31):
#     if num <= 9:
#         print(num*3)
        
#강의 정답 해당 풀이가 더 정확함
# for num in range(1,31):
#     if num % 3 == 0:    # %는 나머지 값을 산출함. 즉 3으로 나누었을때 나머지가 0 이면 3의 배수임.
#         print(num)

#  Exercise 36. 반복문 (while)
# * 1부터 100까지 숫자를 모두 더한 값을 출력하세요.
#   - 단 while 구문을 사용해서 작성하세요.

i = int("")
while int(i < 101):
    print(i)