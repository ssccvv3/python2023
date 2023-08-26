### Exercise 53. 데이터 구조 (튜플과 리스트)
* 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding4' 데이터를 마지막에 추가하고, 다시 튜플 데이터로 변환하세요.
```python
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
data = list(tupledata)
data.append('fun-coding4')
tuple(data)