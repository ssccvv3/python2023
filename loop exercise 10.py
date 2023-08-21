# ### Exercise 10. 데이터 구조 (리스트), 반복문, 문자열 다루기
# * 다음과 같이 파일 이름(확장자 포함) 저장하고 있는 리스트가 있을 때 확장자를 제거하고 파일 이름만 출력하세요.

# ```python
# filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']

filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']

# # 내가 푼 문제
# for i in filelist: # list를 문자열로 변경 
#     endd = i.split(".") # 문자열 상태에서 split로 확장명과 이름을 분리
#     del endd[1]   # 삭제로 인덱스 1번인 확장명 삭제
#     print(endd) # 출력을 했으나 괄호가 있는 상태가됨. 인덱스로 나눠진 값이라, 값만 얻을려면 [0] 해야함, 두번 일함
    
# # 강의 정답
for filename in filelist:
    print(filename)
    filelist_item = filename.split(".")
    # print (filelist_item[0]) # 삭제가 없이 해당 인덱스의 값만 출력, 괄호가 없음
    