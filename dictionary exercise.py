#  Exercise 60. 데이터 구조 (딕셔너리)
# * 다음 actor_info 딕셔너리 변수를 만들고, 홈페이지, 배우 이름, 최근 출연 영화 갯수를 다음과 같이 출력하세요


# actor_info = {'actor_details': {'생년월일': '1971-03-01',
#                    '성별': '남',
#                    '직업': '배우',
#                    '홈페이지': 'https://www.instagram.com/madongseok'},
#  'actor_name': '마동석',
#  'actor_rate': 59361,
#  'date': '2017-10',
#  'movie_list': ['범죄도시', '부라더', '부산행']}

# * 출력 예:<br>
# 배우 이름: 마동석 <br>
# 홈페이지: https://www.instagram.com/madongseok <br>
# 출연 영화 갯수: 3 <br>

actor_info = {'actor_details': {'생년월일': '1971-03-01',
                   '성별': '남',
                   '직업': '배우',
                   '홈페이지': 'https://www.instagram.com/madongseok'},
 'actor_name': '마동석',
 'actor_rate': 59361,
 'date': '2017-10',
 'movie_list': ['범죄도시', '부라더', '부산행']}

#강의 정답
print(type(actor_info["actor_details"]))
print("배우이름 :", actor_info['actor_name'])
print("홈페이지 :", actor_info['actor_details']["홈페이지"])
print("출연 영화 갯수 :", len(actor_info['movie_list']))

# 이름은 출력하였으나, 홈페이지에서 출력을 못함. 처음에 actor_info['actor_details'] 까지 출력을 하고, 다음 홈페이지를 어떻게 불러야할지 몰랐음 
# ['actor_details'["홈페이지"]], ['actor_details'[3]] 괄호, 인덱스 시도를 하였으나 안됨.
# => 변수["키"]["사전안 키"]  사전안의 사전은 이렇게 출력 가능 , 사전안의 사진 키 불러오고 값을 내는 방법 기억하자 !
# 출연 영화 갯수 또한. 
# print(actor_info['movie_list'] 로 해당 영화 값을 불러옴 여기서 처음에 .count를 사용함. , count는 특정 문자열임, 각개개별의 인덱스를 출력하지 않음.
#       문자열 길이는 len
# 처음에 len 을 actor_info[len'movie_list'] 해당 앞에다 사용, 값이 안나옴, 강의를 보자 len 가장 최 상단에 속해야함.