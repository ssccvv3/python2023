데이터 구조
*선언 + 입력: 변수명 = {}, dict() # 중괄호, 변수명 ={키:값, 키:값}
*읽기 : 변수명[키]
*추가 : 변수명[새로운키] = 새로운값
*삭제 : del 변수명[삭제할수]
*수정 : 변수명[수정할키] = 수정값

data_dict = {"한국" : "kr", "일본" : "jp"} 
print(data_dict["한국"])
data_dict["미국"] = "us" # 키 추가방법
del data_dict["미국"]
print(data_dict["일본"] = "일일")

# 키만 출력할때
data_dict.keys()
# 키를 리스트 형태로 추출, 반복문으로 
for keys in data_dict.keys():
    print(keys)  
# 값만 출력할때
data_dict.values()