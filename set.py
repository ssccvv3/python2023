데이터 구조 ( 집합 또는 set)
수학 집합 연산을 쉽게 하기 위해 만든 자료형
순서 없음
중복 없음

*선언 + 입력: set(), 변수명 = {값1, 값2,...}, 변수명=set(값1), 변수명=set({값1,값2..}) #{} 이것은 사전과 같아서 사용 안함
*읽기 :  #반복문 for 문에서는 각각의 값 출력가능, 인덱스는 불가
*추가 :
*삭제 :
*수정 :
    
data_set = {"korea", "japan", "spain", "france"} # 사전은 {"키" : "값", "키": "값"}, 집합은 {"값", "값"} 으로 가능
data_set = set("apple") # 집합이 하나가 있을때 이렇게도 가능, 2개 이상 쓰면 에러가남, ({값,값}) 중괄호를 쓰면 가능

print("canada" in data_set) # 해당 data_set에 "canada" 가 있는지 출력 없으면 false
if "korea" in data_set:
    print(data_set)    # data_set 안에 korea가 있으면 data_set 전부 출력해라

data1 = {"apple", "banana", "strawberry", "melon"} # 가게의 과일
data2 = {"strawberry", "melon", "mango"} # 좋아하는 과일
print(data1 & data2) # &는 교집합. 가게에 있는 과일중 좋아하는 과일
print(data1 | data2) # |는 합집합, 좋아하는 과일과 가게의 있는 과일들
print(data1 - data2) # 차집합, 가게의 과일에서 좋아하는 과일이 중복됨을 빼고 남은 과일들. 즉 data1 과일이 기준임.
print(data1 ^ data2) # 과일가게에서 있는 내가 좋아하는 과일을 뺀, 없는과일과 다른과일들.

# 중복이 없다, 프로그램중 수십만개의 데이터를 다룬다, 리스트안에 append 추가하다보면 중복된것이 나온다,
# 중복된것을 삭제하고 싶을때 , 집합을 사용하여 변경 , 중복된것들이 다 정리되어 하나씩 출력
# 다시 집합으로 형변환을 한 데이터를 리스트로 변경하면 중복된 데이터들이 삭제 되어 있음, 허나 위에서 출력하면 그대로 남아 있음
# 단지 형 변환하고 다시 아래에 변환을 할때 그대로 적용, 전체적으로 적용이 된것은 아님

data_list = ["apple", "banana", "strawberry", "melon", "apple", "banana", "strawberry", "melon", "kiwi", "grape"]
print(data_list)
fruit = set(data_list)
print(fruit)
print(list(fruit))