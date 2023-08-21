#  Exercise 46. 이중 반복문
# * 구구단을 2단부터 9단까지 다음과 같이 출력하세요

for loop in range(2,10):
    print(loop, "단 시작")
    for loop2 in range(1,10):
        print(loop,"X",loop2,"=",loop*loop2)
    print("------------")
print("구구단 종료")

# 처음 for 문을 통해 나열을 print 확인
# 혹시나 해서 아래에 for문을 다시 넣고 1~9숫자를 범위 지정 프린트.
# 예상대로 중첩된 for 문의 1~9 숫자를 다 돌고 다시 상위 for 문의 다음 숫자로 진행되어 반복됨을 확인.
# 뒤 결과값 또한 위 for 문의 숫자와 아래 for 문의 숫자를 곱으로 출력 마무리를 함으로써. 계속 반복됨.