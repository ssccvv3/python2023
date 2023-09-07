#  Exercise 62.  데이터 구조 (집합)
# number_list2에 다음과 같은 데이터를 순서대로 추가하고, 제거하세요

# 선언: [1, 2, 3]
# 추가: 4
# 추가(업데이트): [5, 6]
# 제거: 2

number_list2 = {1, 2, 3}
number_list2.add(4)  #하나의 데이터를 추가할대
number_list2.update([5,6]) # 여러데이터를 추가 및 리스트 [] 괄호 기입
number_list2.remove(2) # 삭제할때
print(number_list2)