# 입력값을 내부에서 어떤 처리를 통해 결과값을 출력
# 인자 또는 인풋

# 함수 function
# def function(parameter1, parameter2):  매개, 변수/ 변수명은 아무렇게나
#    실행문1(parameter1,2)
#    실행문2(parameter1)
#    function("임의1", "임의2")
#    return output                    # 위 변수를 2개면 실행문에서도 기입해주어야하며
                                      # 아래 function 값을 통해 위 실행문이 실행됨

# 인풋(input),  인자(argument,parameter)

# def func1(abc1,abc2):
#     print("hello",abc1,abc2 )
#     print("hello",abc2 )
# func1("dsfsdff", "sdfsdf")

def func2(data1, data2):
    print(data1 + data2)
    return(data1 + data2)    # return까지의 코드만 실행이 되고 아래 코드는 실행이 안됨.
y = func2(1, 2)
print(y)

def awe_sum(a,b):          # 
    result = a + b
    return result
a=2
b=3
print(awe_sum(a,b))