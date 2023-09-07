#  Exercise 55. 데이터 구조 (딕셔너리)
# * 다음 영어 사전 데이터를 딕셔너리 변수로 만들고, 딕셔너리 변수의 key 값인 영어단어, value 값인 의미 만을 가진 리스트 변수를 각각 만들고, 두 리스트 변수를 출력하세요.


# * 출력 예

# {'environment': '환경', 'company': '회사', 'government': '정부, 정치', 'face': '얼굴'}
# ['environment', 'company', 'government', 'face']
# ['환경', '회사', '정부, 정치', '얼굴']

data = {'environment': '환경', 'company': '회사', 'government': '정부, 정치', 'face': '얼굴'}
keyss = data.keys()
valuess = data.values()

print(list(keyss))
print(list(valuess))

#리스트로 출력을 하지 않으면 독특한 타입의 리스트, 딕셔너리에서 파생됨.