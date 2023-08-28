# Exercise 52. 데이터 구조 (튜플)
# * 다음 코드에서 두번째 데이터부터 마지막 데이터를 다음과 같이 출력하세요

# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')

# 출력:
# ('fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')

# #내가 푼 문제 
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
# print(tupledata[1:])
# # 출력을 했으며 근본적이게 바뀌지 않음

#강의 답변
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
data1=list(tupledata)  # tuple로는 삭제가 안됨, list로 변경하여 삭제 시도
del data1[0] # del 을 사용하여 인덱스 0, 첫번째 데이터 삭제
print(tuple(data1)) # 다시 튜플로 변환하면서 출력