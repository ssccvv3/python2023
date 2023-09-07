# 입력값을 내부에서 어떤 처리를 통해 결과값을 출력
# 인자 또는 인풋

# 함수 function
# def function(parameter1, parameter2):  매개, 변수/ 변수명은 아무렇게나
#    실행문1(parameter1,2)
#    실행문2(parameter1)
#    function("임의1", "임의2")
#    return output                    # 위 변수를 2개면 실행문에서도 기입해주어야하며
#                                     # 아래 function 값을 통해 위 실행문이 실행됨

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

def awe_sum(a,b):          
    result = a + b
    return result
a=2
b=3
print(awe_sum(a,b)) # 위 해당값 a=2 , b=3가 위 def 함수에 대입되어 어래 result는 5가 되고, 출력도 5가 출력됨

def awe_sum(a,b):          # 함수안의 값은 지역변수(local variable), 함수 밖은 전역변수(global variable)
    c=1 # 지역변수, 함수 밖에 출력을 하려고 해도 사라졌기 때문에 아래에 출력이 안됨 , 함수안에서만 살아있고 식이 끝나면 없어짐.
    result = a + b
    return result
a=2  # 함수 밖, 전역변수
b=3
print(awe_sum(a,b))

def print_hello(): #인자가 없음, 입력이 없는 함수는 그냥 괄호로 호출
    return "hello"
result_hello = print_hello() #괄호로 호출함 , 우측 print가 좌측 result로 저장이 됨
print(result_hello)          #결과적으로 hello 문자열을 가진 변수 마찬가지 기능

def func_wo_return(a): 
    print("this is function without return for" + str(a) + "times.")
func_wo_return(1)  # 1이 인자 a의 값으로 결국 아래의 a= 1 허나 str 문자열로 변환해서 출력이 된다, str이 없으면
                   # 숫자로 인지하여 오류가 뜨며 출력이 안된다.   
                   
def mul_return(a): 
    b = a + 1
    return a,b
print(mul_return(1)) #return 값은 1,2 나옴,  @ 합수 안에서  return 다음 코드는 원래 실행을 안함.


def id_check(id):
    if id == "admin":
        print("invalid id : admin")
        return  # 만약 아이디가 admin 이면 위 출력과 함께 return 을 만나 아랫값이 출력이 안됨
    print("valid id: ", id) # 만약 admin 아이디가 아니면 return 값위의 식이 아닌 아래 출력값이 출력이 됨