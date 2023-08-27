# Exercise 50. 데이터 구조 (튜플)
# * 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.

#   - 실행코드
#     tupledata = ('dave', 'fun-coding', 'endless')
#     tupledata[0] = 'david'
    
#   - 에러
#     TypeError   Traceback (most recent call last)
#     <ipython-input-2-db4a259aad24> in <module>()
#           1 tupledata = ('dave', 'fun-coding', 'endless')
#     ----> 2 tupledata[0] = 'david'

#     TypeError: 'tuple' object does not support item assignment

tupledata = ('dave','fun-coding','endless')
tupledata[0] = 'david'

# tuple은 추가나 삭제가 안된다 , 해당은 인덱스 0에다가 david를 추가하려고 해서 생기는 오류임.