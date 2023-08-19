데이터 구조(tuple)
    데이터 구조: 리스트, 튜플, 딕셔너리, 집합
tuple은 괄호를 이용하여 선언

turple = (1,2,3,4)

tuple은 삭제나 추가가 불가
del tuple[1]
tuple1[1] = "c"

tuple끼리 더하거나 반복은 가능
tuple2 = (5, 6)
print(tuple1 + tuple2)
print(tuple1*3)

데이터 구조
*선언 + 입력: 변수명 = (1,2,3,4)
*읽기 : 변수명[인덱스 번호]
*추가 : 불가
*삭제 : 불가
*수정 : 불가

data = () #튜플 선언 , 소괄호
data = (1, 2, 3) 
print(type(data),data) # 타입은 tuple, 데이터 변수는 (1, 2, 3)
print(data[0]) #읽기 데이터 값의 인덱스 0번
# 
data=()

data1 = (1, 2, 3)
data2 = (4, 5, 6)

print(data1 + data2, data2, data1)
# 튜플 끼리 더하는것 가능
print(data1*3) 
# 곱하면 같은값 3번 나옴  (1, 2, 3, 1, 2, 3, 1, 2, 3)
# data1 * data2 는 안됨, data1 - data2 도 안됨

# 사용 예시
x = 1
y = 2   # 두 변수의 값을 교환해야한다.
temp = x
x = y
y = temp  # 이렇게 교환을 하나 tuple을 사용하면

x,y = y,x # (x,y) = (y,x) 로 인식하여 x는 y, y는 x로 들어감 , 우선 뒤의 값을 환산 후에 앞에 값에 넣음

def a_and_b(x,y):
    a = x // y       #정수  0나옴 나눠지지 않음
    b = x % y        #나머지 3 나머지를 구할 수 없으므로 그대로 출력
    return a, b       0, 3 
a,b = a_and_b(3,10)


list <=> tuple
# tuple을 list로 바꾸면 수정, 삭제,추가 기능을 전부 사용후 다시 tuple로 변경 가능
list((1,2))
tuple([1,2])
data1 = (1, 2, 3) # tuple
print(type(data1)) # tuple
print(list(data1)) # list