# a = (
#     (1900, 170),
#     (1901, 160),
# )  # 년도, 키를 가진 학생이 있다. 이걸 튜플로 하는게 맞을까, 리스트로 하는게 맞을까의 기준을 가지고 있으면 됨.
# a = (1, 10, 1, 2, 3)  # 1,2,3만 가져오고 싶다면?
# # 슬라이싱 기법을쓰자!
# b = a[2:5]  # (1,2,3)
# #10만 가져오려면?
# c = a[1]
# #기눙
# c = a.count(1) #2가 나온다.
# d = a.index(1) #찾는 것, 값을 기반으로 . 결과는: 0 이유: 1이 2개여도 처음 위치를 담아낸다.

# # set 자료구조
# a = {1, 2, 3, 1}  # 결과적으로 데이터는 3개가 된다.
# print(a)
# print(len(a))  # 3

# # list와 set도 형변환이 가능할까? 가능하다.
# a = [1, 1, 1, 2, 2, 3] #중복값을 제거해야 한다면?
# b = set(a)
# print(b)
# #그 반대는?
# c = list(b)

# #set의 특징
# a = {1,2,3}
# print(a[0]) #set은 인덱스 기능이 안먹힘. 얘는 중복을 제거하느 역할
# #set 활용법? 수학 집합을 생각하면 됨

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8} #set1,2 는 데이터가 각각 5개 들어있다. 또한 각각 중복된 데이터가 없다.
# #교집합, 차집합, 합집합을 set을 통해 구할 수 있다.

# print(f"합집합: {set1 | set2}")
# print(f"교집합: {set1 & set2}")
# print(f"차집합: A의 차집합 - {set1 - set2}, B의 차집합 - {set2 - set1}")
# print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
# print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")

# # set 수정하기
# fruits = {'apple', 'banana', 'cherry'}
# fruits.add('orange')
# print(fruits)
# fruits.remove('apple')
# print(fruits) #여기서, 지울 값을 이 변수가 가지고 있지 않다면? 에러가 뜬다.

# #딕셔너리, 선언법: dict()*****매우 중요*****
# #사전에서 단어를 찾을 때, 우리는 특정 키를 통해서(가나다순) 값을 찾는다.
# #key와 value(데이터와 값)으로 이루어 진 것을 딕셔너리라고 한다.(자료구조의 이름)
# my_dict = {"me":"길동"} #키:벨류,처음부터 선언하는 경우도 있고
# my_dict2 = dict() #이후 코드에서 데이터를 추가하게 됨
# my_dict3 = {'me':[1,2,3],"me2":"good"} #벨류에는 여러 타입이 들어갈 수 있다. 키만 알면 여러 타입에 접근할 수 있다.
# #왜 딕셔너리를 많이 쓸까?
# #수많은 데이터가 존재한다. 내가 1억개 있는데, 9천만번을 찾는다면, 나는 9천만번을 찾아야 함.
# #딕셔너리 기준 : 방이 1부터 1억까지 있는데, 9천만번 키만 알면 9천만번에 바로 접근 가능. 9천만번 반복할 필요 없음
# #컴퓨터 상에서, 비용적으로 효율적임
# print(my_dict)
# #핵심적인 것: 키, 키는 중복이 되지 않음
# #딕셔너리에 데이터를 어떻게 추가할까?

# #데이터 추가
# dict4 = dict() #데이터가 없는 상태
# dict4["max"] = "노잼" #max가 키, "노잼" 이라는 문자열이 벨류가 됨
# #dict4["mac"] = [1,2,3,4] 이렇게도 된다.
# print(dict4)

# 벨류에는 딕셔너리 안에 딕셔너리를 넣을 수 있고, 또 그 안에 딕셔너리를 넣을 수 있다.

# '''
# dict() 를통해 빈 딕셔너리를 만든 후

# 데이터 삽입 키가 4개 , 각각의 밸류에는 다른 타입의 데이터를 넣어서

# 그 딕셔너리를 출력
# '''
# dict = dict()
# dict["1"] = "참 잘했어요"
# dict["2"] = "대단해요"
# dict["3"] = "노력이 필요해요"
# dict["4"] = "분발하세요"
# print(dict)

# #데이터 읽기
# a = person = {'name': 'licat', 'age' : 25, 'height' : 65}
# print(f"이름은 : {person["name"]} 입니다.")
# print(f"이름은 : {person["age"]} 입니다.")

# person["age"] = 30 #수정하는 방법
# print(person)


# person = {'name': 'licat', 'age': 25, 'height': 165.5}
# #데이터수정
# #몸무게 (데이터 추가)

# person["name"] = "이동진"
# person["age"] = 30
# person["height"] = 184
# person["weight"] = 88
# print(person)

# #데이터 삭제
# del person["height"]
# print(person)
# #키를 지우지 않고 데이터 삭제하는 법 person["age"] = None


# a = {"good": ["a", "b", "c"]}
# # 일단 키로 접근한다
# # a["good"]. #리스트에 있던 기능들이 주루룩 나옴
# a["good"].remove("c")
# print(a)

# b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
# # b = {"good1" : {"good2" : [1,2,3,[1,2,3,4]]}} 이렇게 만들려면? 벨류에 어떻게 접근할 것인가? **모르겠다**
# b["good1"]["good2"][3].append(4)
# # 이것의 타입은 뭘까? 리스트. 그 안에서 또 이중리스트에 있는 인덱스를 찾아줘야 한다.
# print(b)
# # 리스트 처럼 딕셔너리에도 여러가지 기능이 있다!
# person = {"name": "licat", "age": 25, "city": "seoul"}
# city = person.get("city", "없는뎅")
# print(city)
# # get : 키, 키가 없을 경우의 value
# city2 = person.get(
#     "city2", "없는뎅"
# )  # get은 내가 찾는 키가 없을때 대체값으로 무엇을 정하는 기능
# print(city2)

# # 만약, 키만 가져오고 싶다면?
# person_keys = person.keys()
# print(person_keys)  # dict_keys가 앞에 붙음
# # 변수 안 데이터가 특정 자료형을 가지고 있도록 형변환
# a = list(person_keys)
# print(a)

# # value만 추출할 수도 있다.
# person_values = person.values()  # value값들만 추출
# print(person_values)  # dict_values가 앞에 붙음
# b = list(person_values)
# print(b)

# # 전체를 추출할 수도 있다.
# person_items = person.items()
# print(person_items)
# c = list(person_items)
# print(c)
# print(type(person_items))
# #del person['age'] 권장 x
# a = person.pop("age") # age라는 키에 있는 값을 a에 저장
# print(a)

# # person.pop = del person['age']
# # 지운 값을 알아야 할 때 : pop. 그래서 del person['age']는 권장되지 않음

# s = 'hello'
# for i in s:
#     print(i) #for로 시작하면, 반복문을 의미함. s는 변수
# #순회할때 첫번째 값은 h, h 값을 가져와서 i라는 변수에 담는다.
# #들여쓰기 안의 블록에서은 우리가 지정한 i를 가지고 사용할 수 있다.
# # 이걸 j로 바꾸면 에러가 날까? 난다. 내가 지정한 j가 들여쓰기 안에 있는 코드에 i가 없으니까 에러가 남
# # print(j)로도 바꿔줘야 함 

# # for i in range(5000): #0부터 4999까지의 어떤 순회 가능한 데이터(리스트)를 만든다.
# #     print(i)    
# # #range(숫자) 0부터 숫자-1 까지의 범위를 만든다.
# # #만약 10부터 50까지 하고싶다면?
# # #RANGE(10,51) #10부터 50까지의 범위를 만든다.
# # for i in range(10,51):
# #     print(i)
# #1,3,5,7,9는?
# range(1,11,2)
# for i in range(1,11,2):
#     print(i)

# #range(5000) == range(0:5000:1)
# #음수로 내려가려면? 내림차순으로 만들어주면 된다.
# for i in range(10,1,-1):
#     pirnt(i)

# """
# 1 부터 100까지 출력
# 2 부터 50까지 짝수만 출력
# 10 부터 -1까지 출력력
# """

# #반복문에 조건문 추가 가능?
# for i in range(1,100): #1부터 99까지 반복한다.
#     if i % 3 ==0:
#         print(i) #3의 배수이면?

# #중첩반복문
# #이 구조에서 
# #구구단을 만들어보자, #외부내부관계, 부모자식관계
# for i in range(2,10):

#     for j in range(1,10):
#             print(f"{i} * {j} = {i * j}")
#             if i * j == 9:
#                   print(9)





