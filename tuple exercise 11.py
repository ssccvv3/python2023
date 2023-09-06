# Exercise 59. 데이터 구조 (딕셔너리)
# * 다음 dict_all, dict2, dict3 딕셔너리 변수가 있을 때, dict2와 dict3 두 데이터를 dict_all 딕셔너리 변수에 추가한 후,
# dict_all 변수를 출력하세요.

# dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
# dict2 = {'company': '회사', 'face':'얼굴'}
# dict3 = {'apple': '사과'}

dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
dict2 = {'company': '회사', 'face':'얼굴'}
dict3 = {'apple': '사과'}

for result in dict2.keys():
    dict_all[result] = dict2[result]
    print(dict_all)
    
    dict2_keys