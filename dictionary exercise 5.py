# Exercise 59. 데이터 구조 (딕셔너리)
# * 다음 dict_all, dict2, dict3 딕셔너리 변수가 있을 때, dict2와 dict3 두 데이터를 dict_all 딕셔너리 변수에 추가한 후,
# dict_all 변수를 출력하세요.

# dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
# dict2 = {'company': '회사', 'face':'얼굴'}
# dict3 = {'apple': '사과'}

dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
dict2 = {'company': '회사', 'face':'얼굴'}
dict3 = {'apple': '사과'}

# 강의 정답
# 처음에 접근법을 전혀 모르고, list로 만들어서 추가를 하려고 했다, 허나 오류가 계속뜸, 

for data1 in dict2.keys():     #변수 data1를 지정을 하고 dict2의 key 반복문 출력
    dict_all[data1] = dict2[data1]  #그리고 dict 추가하는 공식 변수[키] = [값]
                                    #메인 변수에 data1 키를 추가 허나 for 문으로 해당 변수 안에 키 추가됨, dict2 의 값을 추가해야하니 , data1 키값을 입력 값을 추가하게됨
for data2 in dict3.keys():
    dict_all[data2] = dict3[data2]
print(dict_all)