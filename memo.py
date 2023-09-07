def func2(data1, data2):
    print(data1 + data2)
    return(data1 + data2) # return까지의 코드만 실행이 되고 아래 코드는 실행이 안됨.
y = func2(1, 2)
print("답",y)