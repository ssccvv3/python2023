# 반복문 (for, while)

# for 변수 in (리스트 or 문자열):
#     실행문1
# for 변수 in range(반복횟수)
#     실행문
# for 변수 in range(시작점, 끝지점전) 왜냐면 인덱스는 처음은 0으로 시작
#     실행문


# for i in ["python", "java", "golang"]:
#     print(i)
# for i in ("a","b","c","d","e"):
#     print(i)

# name = "a,b,c,d,e"
# name2 = name.split(',') # , 일정하게 구분해줌. 즉 , 기점으로 인덱스 번호 부여
# print(name2)
# for i in name2:
#     #여기서 헷갈렸는데, range(1,11) 1~10까지 숫자 반복 이것만 앎, 
#     # 허나 위에 name2 = name.split(','), 즉 ['a', 'b', 'c', 'd', 'e']
#     # a~e 하나씩 대입하여 각 결과 값이 1줄씩 나옴
#     print(i)

#sum
# sum = 0
# for index in range(1, 11):
#     sum = sum + index
# print(sum)

# while
#  while 조건: 
#      실행문1

# 반복문의 조건에서 1은 true와 같은 의미 (1 true, 0 false)
# while 1 은 언제나 참 , break 문이 조건 만족할때 까지 무한반복
# 예 while 1:
#     print("hello world") 무한으로 반복함
     
# name = ""
# while name != "foo bar":
#     name = input("what is your name?")
#     print("hi,"+ name + " so where is foo bar?")
    
# pw = ""
# while pw != "1234":
#     pw = input("비밀번호를 입력해주세요.")
#     print("비밀번호가 틀렸습니다.")
    
