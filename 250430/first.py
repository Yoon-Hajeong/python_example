



# a = 10
# b = 20

# if a > 10:
#     print("good") #거짓
# elif b == 20: #if가 들어갔으니, 첫if를 봤는데, 거짓이네? 두번째 if문.
#     print("20입니다")
# elif a == 10:
#     print("10입니다") #이래도 20이 나온다. 파이썬은 위에서 아래로 내려오기 때문
# else :
#     print("이도 저도 아니다") #이도 저도 아닐때는 else를 쓴다.

'''***중요한 문제
split() 활용
a,b 변수를 활용,
키,몸무게를 입력받는다.
키와 몸무게를 나눈 나머지를 출력한다.
조건문을 활용해서
키(a)가 130 이상이면 a, 150 이상이면 b, 170 이상이면 c 180 이상면이면 d를 출력하세요
'''
# a = 185
# if a >= 180:
#     print("d")
# elif a >=170:
#     print("c")
# elif a >= 160:
#     print("b")
# else:
#     print("a")


#예제. 시험점수를 입력받아 90-100점은 A, 80-89 B, 70-79 C, 60-69 D 나머지 점수는 F를 출력하는 프로그램을 작성하시오. 출력해라
#첫째줄에 시험점수 주어짐. 점수는 0보다 크거나 같고 100보나 작거나 같은 정수이다
# a = input()#내답
# a = int(a) 
# if  a >=90 and a <=100:
#     print("A")
# elif a >= 80 and a <= 89:
#     print("B")
# elif a >=70 and a <= 79:
#     print("C")
# elif a >= 60 and a <=69:
#     print("D")

# 답
# score = int(input())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# a = 10
# b = 20
# if a == 10 and b == 20: #not just =, it's ==.
#     print("good")
# else:
#     print("no")

# #assignment
'''
a,b,c를 입력받는다(한줄이든 여러줄이든 상관없음)
a가 100이고, b가 200 이상이면 "a"를 출력
b가 1이면 "b"를 출력
이도 저도 아니면 c를 출력

'''
#my andswer
# a,b,c = input(),input(),input()
# a,b,c = int(a),int(b),int(c)

 

# if a == 100 and b >= 200:
#     print("a")
# elif b == 1:
#     print("b")
# else:
#     print("c")

#내답
a,b,c = int(input()),int(input()),int(input())

# if a == b == c:
#     print(int(10000)+a*int(1000))
# elif a == c and ~b == c:
#     print(int(1000)+a*int(100))
# elif a == b and ~a == c:
#     print(int(1000)+b*int(100))
# elif b == c and ~b == a:
#     print(int(1000)+b*int(100))
# elif a < b < c:
#     print(c*100)
# elif a < c < b:
#     print(b*100)
# else:
#     print(a*100)

#answer
# if a == b == c:
#     price = 10000 + a * 1000

# elif a == b:
#     price = 1000 + a * 100
# elif a == c:
#     price = 1000 + a * 100
# elif b == c:
#     price = 1000 + b * 100

# else:
#     price = 0 #값을 일단 초기화한다. #밑에서 검증 안할걸 대비해서 0으로 만든 것******혹시 모를걸 대비하는 것. 중요

# if a != b and b != c and a != c:
#     temp = a
#     if b > temp: #중첩반복문(if 안에 if, )
#         temp = b
#     if c > temp:
#         temp = c
#     price = temp * 100

# print(f"상금: {price}원")

















































































