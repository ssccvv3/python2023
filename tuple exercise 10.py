#   Exercise 58. 데이터 구조 (딕셔너리)
# * 다음 영어 사전 데이터를 딕셔너리 변수로 만들고 사용자로부터 영어단어를 입력받으면 해당 영어단어의 외움표시를 O로 수정하고, 외움표시가 X 인 단어만 출력하는 프로그램을 작성하세요.
#   - 단, key는 영어단어, value는 의미와 외움표시 두 데이터를 넣습니다.

# environment : 환경 x
# company : 회사 o
# gonernment : 정부, 정치 x 
# face : 얼굴 x

data = {"environment": ["환경","X"], "company":["회사","O"], "goverment":["정치,정부","X"], "face":["얼굴","X"]}

word = input()
if word in data.keys():
    data[word][1] = "O"

for keys in data.keys():
    item = data[keys]
    if item[1] == "X":
        print(keys)