#  Exercise 57. 데이터 구조 (딕셔너리)
# * 다음 영어 사전 데이터를 딕셔너리 변수로 만들고 외움표시가 X 인 영어단어만 출력하세요
#   - 단, key는 영어단어, value는 의미와 외움표시 두 데이터를 넣습니다.

# environment : 환경 x
# company : 회사 o
# government : 정부, 정치 x
# face : 얼굴 x


# data = {"environment":"환경,X", "company":"회사,O", "goverment":"정치,정부,X", "face":"얼굴,X"}
# for keys in data.keys():
#     if data[keys].find("X") >= 0:
#         print(keys)
        
# value에 두 데이터를 넣는것에 힌트를 얻음, for 반복문을 통해서 keys 변수값을 지정해서 출력을 하면
# str 문자열로 출력이 됨. 즉 key 값을 차례대로 나열해서 출력이됨
# 여기서 value 가 x 가 포함된 것만 출력을 해야하니, value 값을 추출해야함
# dict data 변수에서 변수[키] 해당 key 값의 valuse 값을 뽑게됨. 
# 여기서 print(keys, data[keys]) 하면 key 값과 그 key 값이 출력된 dict의 value 값이 같이 출력됨 (keys,value)
# value 값을 불러오면 x만 소거하여 추출하면 되므로, find("")사용한다. 해당값이 존재하면 인덱스 0~123 나오며, 없으면 -1 추출
# 즉 x 값만 소거하면 되니 x가 아닌값은 -1이 나옴. if 문을 통하여 마지막 소거, 인덱스 0이 존재 할 수 잇으므로, 0보다 같거나 크게
# 그러면 최종적으로 아래로 읽어 내려간 keys 값이 x만 소거되어 출력이 된다
# 이건 o 아님 x 라서 정확하게 x를 찾는 방법이 아니다.

# 강좌 정답
data = {"environment": ["환경","X"], "company":["회사","O"], "goverment":["정치,정부","X"], "face":["얼굴","X"]}
for keys in data.keys():
    item = data[keys]
    if item[1] == "X":
        print(keys)
# 정확하게 x 값만 찾아서 출력할 수 있다., value 값에 또 다른 list 형태로 만들어 인덱스 문자열을 통해서 출력을 한다.
# list에서 인덱스 찾는것을 타입으로 확인하면 str 문자열로 나온다! 그렇기에 해당 x 값을 정확하게 찾을 수 있다.