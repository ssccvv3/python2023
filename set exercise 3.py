# Exercise 63.  데이터 구조 (집합)
# number_list1과 number_list2의 교집합, 차집합을 출력하세요

number_list1 = {1,2,3,4}
number_list2 = {3,4,5,6}

print(number_list1 & number_list2) # & 교집합
print(number_list1 - number_list2) # - 차집합
print(number_list1 | number_list2) # | 합집합