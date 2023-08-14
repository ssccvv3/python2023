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
