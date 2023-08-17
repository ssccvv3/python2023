location = ['서울시','인천시','경기도'];
# 다른 방법으로는 location = [] , location.append('값') 추가 추가로 가능
#location = list() 로도 가능
print(location);
print(location[1]);
location.append('부산시');
location.append("대전시");
# 1개씩만 추가 가능
print(location);

#작업을 하다가 " line 1, SyntaxError: invalid syntax " 발생했다. 런이 되지 않았다.
#아래 터미널에서  " ctl + z " 입력하여 빠져나왔다. 혹은 "exit()"

print(location[1:4]);
location.remove('대전시');
# .remove를 통해서 특정 데이터 삭제
print(location);
del location[3]
# 다른 방법은 del 함수를 사용하여 인덱스 값을 넣고 삭제
print(location);
location.insert(3, '부산시');
#변수.insert 함수로 (인덱스 위치, 추가 값) 리스트에 추가를 할 수 있다.
print(location);

#선언
#-리스트 변수 = []
#-리스트 변수 = list()
#-리스트 변수 = [데이터1, 데이터2...]

# 추가
# -리스트변수.append(데이터)
# -리스트변수.insert(인덱스번호, 데이터)

# 삭제
# -리스트변수.remove(데이터)
# -del.리스트변수[인덱스번호]

# 수정
# - 리스트변수[인덱스번호] = 수정할데이터
# - location[1] = '서울시'

# strip = 양 옆 제거
# 변수.strip('')
# # strip은 왼쪽 오른쪽 string 문자열을 제거함. 가운데 제거 불가, \
# #  양옆 제거한후 가운데는 제거가능 

# count = 해당 매서드는 문자열 내부에서 특정 문자 등장 횟수
# 변수.count('') 주의, 대소문자 구분함, 전부 찾음 
# 변수.count('a', 5) 해당 문자열에서 인덱스 5번째 부터 시작하여 a를 전부 찾는다
# 변수.count('a', 3, 5) 해당 문자열에서 인덱스 3번째 부터 시작하여 5번째 까지 찾음

# find = 문자열 내부에 있는 값을 찾아서 인덱스 위치를 출력함, 없으면 "-1" 출력함(0 출력아님! -1임 !)
# 변수.find('') 주의, 대소문자 구분함, 전부 찾음 
# 변수.find('a', 5) 해당 문자열에서 인덱스 5번째 부터 시작하여 a를 전부 찾는다
# 변수.find('a', 3, 5) 해당 문자열에서 인덱스 3번째 부터 시작하여 5번째 까지 찾음

# split = 문자열을 일정한 규칙을 리스트를 만들어줌, 리스트로 변경됨,
        #   이미 리스트 상태에서는 안됨, 문자열 상태에서 가능
# 변수.split('')