# # exercise 1 
# #  10, 2.2, "apple" 각각을 변수에 넣고, 각 데이터 타입을 출력하세요
# a = 10
# b = 2.2
# c = "apple"
# # 한번에 타입을 알아보고 싶었지만 아직 찾을 수 없었다.
# print(type(a))
# print(type(b))
# print(type(c))

# # exercise 2
# # 다음 코드를 실행 해보고 \t 와 \n의 역할을 설명하세요

# #     code = '000660\n00000102\t12312312'
# #     print (code)
# code = '000660\n00000102\t12312312'
# print (code)
# # \n은 문단 변경, \t는 사이 간격 탭

# # exercise 3
# # 사용자로 부터 두 개의 숫자를 입력 받은 후 큰 숫자를 화면 출력

# a = int(input('숫자 입력'))
# b = int(input('숫자 입력'))

# if a > b:
#     print(a)
# else:
#     print(b)
    
# # exercise 4 
# #  사용자로부터 입력 받은 숫자가 홀수인지 짝수인지 출력

# data1 = int(input('숫자입력')) % 2
# data2 = int(input('숫자입력')) % 2

# if data1 == 0:
#     print("짝수")
# else:
#     print("홀수")
# if data2 == 0:
#     print("짝수")
# else:
#     print("홀수")
    
# # exercise 5 
# # 사용자로 부터 3개의 숫자를 입력 받은 후 가장 작은 숫자를 출력하세요.

# number1 = int(input('숫자입력1'))
# number2 = int(input('숫자입력2'))
# number3 = int(input('숫자입력3'))

# if number1 <= number2 and number1 <= number3:
#     print("number1",number1)
# elif number2 <= number1 and number2 <= number3:
#     print('number2',number2)
# else:
#     print('number3',number3)
    
# # 세 수를 비교하여 가장 작은 값을 도출하도록 if 반복문을 작성한다.

# exercise 6
# 사용자로 부터 점수를 입력 받은 후 등급을 출력
#   (A: 100 ~ 81 B: 80 ~ 61 C: 60 ~ 0)

# grade = int(input('시험 점수를 입력하세요.'))

# if grade <= 100 and grade >= 81:
#     print("A등급")
# elif grade >= 61 and grade <=80:
#     print("B등급")
# elif grade >= 0 and grade <= 60:
#     print("C등급")

# # excercise 7
# # 사용자로 부터 주민등록 번호를 입력받아 출생 연도를 출력
# # 앞 2자리만.

# years = input('주민등록 번호 입력')
# print('출생년도:',years[0:2],'년생')

# # exercise 8

# # 사용자로부터 주민등록번호를 입력 받아 뒷자리 맨 앞의 숫자를 출력하세요
# # 성별을 의미하는 번호 

# years2 = input('주민등록 번호를 입력하세요.')
# print(years2[-7])

# exercise 9

# 사용자로 부터 주민등록번호를 입력 받아, 성별을 표기 (남성, 여성)
# 성별을 구분하는 숫자는 1남성 2여성 으로만 구분

# years3 = input("주민번호를 입력하세요")
# # 혹은 years3[-7] =='1': 이렇게 가능
# gender = years3[-7] # 배열은 문자열로 출력됨, 정수가 아님
# if gender == '1': 
#     print("남성입니다.")
# elif gender =='2':
#     print("여성입니다.")
# else:
#     print("성별을 숫자 1,2로 입력해주세요")

# # exercise 10
# # 문자열에서 ... 제거하라
# # mystr = "a man goes into the room..."

# mystr = "a man goes in to the room..."
# print(mystr.strip('.'))

# # 변수.strip('')
# # 해당 값을 제거 함

# # exercise 11

# # 공백과 줄바꿈을 제거하여 코드만 추출

# # code = '        000660\n      '

# code ='     000660#     '
# print(code.strip())
# # strip은 왼쪽 오른쪽 string 문자열을 제거함. 가운데 제거 불가, \
# #  양옆 제거한후 가운데는 제거가능 

# # exercise 12

# # Python 문자 빈도수 출력

# # "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
# # Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural),
# # object-oriented and functional programming. It is often described as a batteries included language due to its comprehensive standard library."

# words = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a batteries included language due to its comprehensive standard library."

# print(words.count('Python'))
# # 주의, 대소문자 구분함 

# # exercise 13

# # letters 변수에 들어있는 두번째와 네번째 문자를 출력하라(인덱스 아님)

# letters = "python"
# print(letters[1], letters[3])

# # exercise 14
# # letters 변수에 사용자로 부터 문자열 입력을 받아 문자 n 이 있는지 출력 ( n 이 있으면 0, 없으면 -1 출력)

# letters = input('단어 입력')

# if letters.find('n') == -1:
#     print(-1)
# else:
#     print(0)

# # exercise 15
# # letters1 변수에 사용자로 부터 문자열 입력을 받아 문자 n 이 있는지 출력 ( n 이 있으면 n이 들어있습니다, 없으면 n이 안들어 있습니다 출력)

# letters1 = input('영단어를 입력해주세요: ')
# if letters1.find('n') >= 0:
#     print('n이 들어있습니다.')
# else:
#     print('n이 들어있지 않습니다.')

# ★ exercise 16

# 주민등록번호 뒷자리 중 2~3번째는 출생코드.
# 주민등록 번호를 입력 받은 후 출생지를 출력
#  00~08 : 서울
#  09~12 : 부산

# birth_city = input("주민번호를 입력해주세요: ")
# birth = birth_city[-6:-4]
# print(type(birth),birth)

# if birth >= "00" and birth <= "08":
#     print("서울 출생")
# elif birth >= "09" and birth <= "12":
#     print("부산 출생")
# else:
#     print("오류 다시")
    
# # 인풋에 인트로 변경하니 문자열에서 찾지를 못함. 오류 뜸
# # 문자열에서 0을 빼니 전부 서울출신되어버림.
# # 문자열 방법


# birth_city1 = input("주민번호를 입력해주세요: ")
# birth1 = int(birth_city1[-6:-4])
# print(type(birth1),birth1)

# if birth1 >= 0 and birth1 <= 8:
#     print("서울 출생")
# elif birth1 >= 9 and birth1 <= 12:
#     print("부산 출생")
# else:
#     print("오류 다시")
# # 인풋에 인트로 변경하니 문자열에서 찾지를 못함.오류 뜸
# # 숫자 앞에 0을 빼줘야함 , 정수int
# # 정수 방법

# # exercise 17
# # names 변수 안에 dave, david, andy가 있다, 해당 변수값을 ',' 기준으로 분리하여 출력

# names = "Dave, David, Andy"
# print(names.split(','))

# # exercise 18
# # 확장자를 제거한 파일 이름만 출력

# filename = 'exercise01.docx'
# filelist = filename.split('.')
# # #split 메소는 문자열을 리스트로 바꿈
# print(filelist[0])

# filename = ['exercise01.docx']
# filename.append('.docx')
# filename.remove('.docx')
# print(filename)

# # # 보다시피 위에 식은 성립이 안됨, '.' 기점으로 split 메소드를 사용하여 나눠야함.