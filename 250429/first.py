# #비교연산
# x,y = 10,10
# print(x==y)
# print(x>y) #초과 이상 이하 미만 중에 Is x greater than y?
# print(x>=y) #Is it true or false?
# print('apple' < 'banana') #Alphabet a is ahead b, so result is true
# print(5 < X < 15)

# print('키와 몸무게를 입력하세요')
# a,b = input().split()
# print(a,b)



# #글자에 대한 문자 수 불러오기
# a = "dsfjkhawekjhfkwejfklweuhflkejwhlkjhljfhljaw"
# print(len(a))

"""
input() 두 번을 사용하여, 두개의 변수의 임의의 문자열을 넣고,
len() 을 사용하여 문자의 수를 변수에 넣는다.

'첫번째 변수의 문자 수는 {문자의 수} 입니다.'
'두두번째 변수의 문자 수는 {문자의 수} 입니다.'
"""
# a = input()
# b = input()

# print(f"첫번째 변수의 문자 수는 {len(a)}입니다.")
# print(f"두번째 변수의 문자 수는 {len(b)}입니다.")

# #실수 자릿수
# i = 10
# j = 10.522222222222222222222
# print(f"j의 값은 {j:.2f}") #소숫점 자리수를 지정할 수 있음. j값:은.을 넣어서 2번째자리까지 만들어서 출력해라

# money = 10000000000000000000000000000
# print(f"{money:,}") #3자리 수로 콤마를 찍어서 출력

# a = 36565465464865
# print(f"a의 값은 {a:.3f}")

# # a && b
# a  = True
# b = True
# c = a and b
# d = 10 > 5 and 10 < 5 # d = True and False.
# print(d)

# #논리합 : 하나라도 1이라면 True. 000 101 111 011. because it's or
# f = 10 >= 10 or False #It's already true, in front of "or"
# print(f)

# f = False and True and True #0 1 1 so it's false. There is one 0.
# print(f)

# f2 = (False or True) and True #Firstly, count (), so it's 1 and 1 = True
# print(f2)

# #Not : it's totally opposite with or & and
# f3 = not((False or True) and True)
# print(f3)

# a = 10
# b = 20
# c = a!=b #Are they differnt? Yes they are differnt. True
# c = not a!=b #False

# #항은 3개 이상 and , or는 마음대로 연결하여 결과 출력
# f = 33
# g = 34
# h = 20
# i = (f>g or f<=g) and g > h
# print(i)

# #할당연산, = 축약표현임
# a = 10
# a = a + 10 #capable to count, afterall, a is 20/ == a+= 10
# a += 10 #same as a = a + 10

# #멤버연산 : 어떤 값이 문자에 있는지 확인해 주는 것
# st = "modulabs is good" #good, you can ask, is this word in this sentence?
# sta = "good" in st #Is good is in that sentence(st)?

#split
# a = "123456-1122334"
# c,d = a.split("-") #blank: split by space.
# print(c)

# a = "123456-1122334-good"
# c,d,e = a.split("-")
# print(c)

#Examples
'''
정수 3개가 공백을 두고 입력된다.
1 2 3
합과 평균을 공백을 두고 출력한다.
평균은 소숫점 이하 셋째 자리 까지 보이게한다.
(f-string)
6 3.010
'''
# a = "1-2-3"
# b,c,d = a.split("-")
# print(b,c,d)

# b = int(b)
# c = int(c)
# d = int(d)
# f = (b+c+d)/3
# print(f"합계: {b+c+d}, 평균: {f:.3f}")

#조건문
# age = 20
# #if  = 10 you can't use 'if' as a valuation
# if age > 18:
#     print("성인입니다") #들여쓰기
# print("안녕하세요")
#there is red line after 18, because it's not ending
#Depand on True or False, result is different. 들여쓰기로 가는지 안가는지의 차이
#조건과 조건, 항과 항을 연결지을 수 있다? 없다? 있다. 
# age = 10
# height = 200
# if age > 18 and height >= 150:
#     print("성인입니다.") #If you want this coding being successful, you can change 'age' or 'and'.




# #if ~ else 구문 : if가 참이 아니면 else구문을 실행
# age = 20
# if age > 30:
#     print("30대 이상입니다.")
# else: #들여쓰기 필요!
#     print("30대가 아닙니다.") #구문 구조 : 모 아니면 도

# #if elif ~ else 구문 #원하는 결과가 3가지 이상일 때는, else if의 줄인말인 elif 사용
# age = 19
# if age <= 19:
#     print("청소년입니다.")
# elif age < 30:
#     prinnt("성인입니다.")
# else:
#     print("30대 이상입니다.'")

'''
#Examples
한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)
'''



#정답
yyyy,mm,dd = input().split()
yyyy,mm,dd = int(yyyy),int(mm).int(dd)
if yyyy % 2 == 0:
    print("짝수 년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")


