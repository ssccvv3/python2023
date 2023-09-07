# Exercise 61.  데이터 구조 (집합)
# number_list가 다음과 같은 리스트일 때 중복 숫자를 제거한 number_list1 집합을 만들고, 출력하세요

# number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]

number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]

number_list1 = set(number_list)
print(number_list1)

#처음에 해당 list 형태를 확인 " list " 집합은 중복이 없다. 집합으로 변경하면 중복된것이 사라질거라 추정