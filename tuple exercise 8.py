# Exercise 56. 데이터 구조 (딕셔너리)
# * 다음 영어 사전 데이터를 딕셔너리 변수로 만들어서 다음과 같이 출력하세요.
#   - 단, 반복문을 사용하세요.


# environment : 환경
# company : 회사
# gonernment : 정부, 정치
# face : 얼굴

data = {"environment" : "환경", "company": "회사", "goverment": "정부,정치", "face" : "얼굴"}
for toy in data.keys():
    print(toy,":", data[toy])
    
# 답을 구해내지 못함.
#  dict는 반복문 구할때 
#  for 변수 in 사전변수.keys(): 
#      해당 keys 값만 변수로 출력을 한다는것을 기억해야 해당 키값이 순서대로 출력이 되고,
#      해당 value 값을 알고 싶으면 key 값이 하나씩 출력이 될때, 해당 dict 변수에 [반복되는 변수]를 넣어 
#      key 값이 출력됨에 따라 그 key 값을 넣고 value 값이 나오게 된다.