# # Exercise 11. 데이터 구조 (리스트), 반복문, 조건문, 문자열 다루기
# * 파일 이름이 다음과 같은 리스트에 저장되어 있을 때 확장자가 .txt 인 파일에 대한 리스트를 출력하라

filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']

# # 내가 푼것. 여기서 방법을 모름 txt는 찾았는데..
# for i in filelist:
#     print(i.find(".txt"))
    
# 정답보다 if문 응용법에 힌트를 얻음
for i in filelist:
    if i.find(".txt") >= 0:  # if 문에 if i >= 0:  한 값이 아니라 메소드를 넣을수 있음
        print(i)             # if i.find(".text") >= 0  find가 찾은 인덱스 숫자로 표기, 없으면 -1 , 0보다 크면 그 파일임
        
# #강의 정답

# for filename in filelist:  #리스트 상태    뒤에 [1]인덱스 번호 추출하면 str 문자열로 바뀜 
#     if filename.split(".")[1] == "txt": # . split 하여 이름과 확장명의 인덱스 나누고 [1]확장명 인덱스 값만 출력 문자열로 바뀜
#         print (filename)                # 해당[1] 추출한 값 txt 문자열을 확인을 했으니 if 문으로 걸러내야함
#                                         #  == "txt" 문자열이니 문자열로 , 일치하면 해당 값 출력 >0 큰숫자 혹은 == 해당값