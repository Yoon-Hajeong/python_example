#a = input() #입력 받으 값을 a라는 변수에 넣어준다.

#print(a)
#print("okay") #파이썬에서 인풋은 숫자를 입력해도 무조건 str, 무조건 문자다!

'''
입력을 몇가지 변수에 담아서
f-string, 문자붙이기, 문자반복하기 등 여러 기술ㄷ을 활용해 출력하세요.

'''
'''
b = input()
c = input()
print(f"내가 원하는 디저트는 {b}(이)랑 {c}(이)야.")
print(b+c)
print(b * 30)

'''

#형변환 : 문자를 숫자로, 숫자를 문자로 변환하기
'''
a = input()
print(type(a))
b = int(a) #문자를 숫자로
print(type(b))
'
a = 1
print(type(str(a)))
'''

#문자열 메서드 abc를 자동으로 대문자로, 소문자로 바꿀 수 없을까? 변환기능?
s = 'wenive CEO licat'
#print(s.lower())
#print(s.upper())
#슬라이싱, 인덱싱 등을 통해서도 특정 문자를 추출할 수 있고, 변환할 수 있음
#***단, a = CEO 로 데이터를 넘겨받음. b, 데이터 저장 로직(저장 a.lower이게 변환이 될까?)
#a는 원본데이터, 얘를 밑에서 수정하면 될까? No, a는 훼손되면 안됨. (예를들어. a = 1 a = str(a)같은거는 안됨. 덮어씌우는거니까. 원본은 삭제하지 말것)
#차라리 새로운 변수를 만들어서 할당하는게 좋다.

#find, index() : 특정한 것을 찾아서 보여주는 것. 
#차이점 find:특정 문자열 없을때 -1을 반환, index는 오류


s = 'wenive CEO good licat'


print(s.find("wenivee"))
print(s.index("good")) #인덱스는 에러가 터지니까 예외처리가 필요함. 어떻게 해결할지 코드로 짜줘야 함. 그냥 조직마다 쓰는게 다름
print(s.count("i"))

#replace
s2 = s.replace("CEO","CTO")
print(s2)

'''
#***split
s3 = "weniv-corp" #- 기준으로 쪼갤 때 사용함
#s3.split() #공백 기준으로 나눔 
s3.split("-") #-기준으로 나눔. 쪼개면 데이터 2개가 됨. 그래서 
s4,s5 = s3.split("-")
print(s4,s5)

'''

#입력이 들어온다. 키 몸무게 성별 나이 이름
#예시 180 60 남 25 김아무개
#이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
#이름을 f-string통해 세번 반복해서 출력한다.

# # 실패한 코딩 print("키/몸무게/성별/나이/이름")
# # a = input()
# # b,c,d,e,f = a.split()
# # print(b,c,d,e,f)
# #정답

# #합치는거
# # s20 = ["modu","labs","good"]
# # print("-".join(s20))

# # #포맷
# # print("제 이름은 {}이고, 나이는 {}살입니다.".format(name, age))
# # print(f"제 이름은 {name}이고, 나이는 {age}살입니다.") #요즘에는 이렇게 대체된다.

# '''
# #이스케이프 문자 
# print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
# print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
# print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
# print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
# print("Backslash: \\") # 백슬래시를 출력합니다.

# '''
# #논리형
# # #bool타입은 참, 거짓밖에 없음(0과1)
# # #bool타입 
# # a = 10 > 3 #(부등호 왼쪽 기준으로 보고있음, 이것은 참)
# # print(type(a))

# #gudqusghks
# a = 1
# b = 0 #0을 제외한 모든 숫자값은 true
# c = -1
# d = "okay"
# f = ""

# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(f))

# print(a==b) #a가 b와 같니? 라는 뜻
# # X  = None(dkanrjteh djqtek. X는 대문자임)
# #산술연산
# result = 5+3
# print(result) #결과 8
# result = 5-(-3)
# # print(result)

# #나눗셈****
# print(11/2) #그냥 나눗셈
# print(10/2)
# print(type(10/2))#정수로 나누어 떨어져도 그 결과는 무조건 실수로 나오게 해놓음
# print(11//2) #몫만 구했음
#5.0d을 5로 바꾸고 싶으면 해야할 것? 
#//연산은 내림을 전산함. 결과가 -2.5여도 //쓰면 -3
#나머지를 이용해서 할 수 있는것? 홀수 짝수 10/2 = 0? 묻는다면, 짝수로 나오기 때문에 거짓으로 판명 가능
# #제곱연산자
# print(10%3)
# #10의 세제곱 : 10 * 10 * 10,상당히 귀찮음
# print(10**5)#10의 5제곱이라는 뜻

#사칙연산
a = (10*10) + 10 + 10 * (20*20)
print(a)

