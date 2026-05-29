# # datetime.date
# """datetime.date는 연,월,일 날짜를 표현할 때 사용하는 함수"""
# import datetime
# day1 = datetime.date(2021, 12, 14)
# day2 = datetime.date(2023, 4, 5)

# diff = day2 - day1
# print(diff.days) # 477  둘이 만난지 477일 째

# """day2 에서 day1을 뺀 datetime 모듈의 timedelta 객체가 리턴된다.
# 요일은 datetime.date 객체의 weekday 함수를 사용하면 쉽게 구할 수 있다"""
# day = datetime.date(2021, 12, 14)
# print(day.weekday())   # 1 (2021년 12월 14일은 화요일), 월요일은 0 ~ 6은 일요일이 된다. 만약 월요일을 1로 시작해서 리턴하고 싶다면 isoweekday() 를 사용하면 된다.
# print(day.isoweekday()) # 2











# # time
# #시간과 관련된 time 모듈에는 함수가 매우 많다. 

# # time.time
# # time.time()는 UTC 세계 표준시를 사용하여, 현재 시간을 실수 형태로 리턴하는 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴해준다.
# import time
# print(time.time()) # 1778006533.4747453

# # time.localtime
# # time.localtime 은 time.time()이 리턴한 실숫값을 사용해서 년,월,일,시,분,초 의 형태로 바꾸어 주는 함수이다.
# print(time.localtime(time.time())) # time.struct_time(tm_year=2026, tm_mon=5, tm_mday=6, tm_hour=3, tm_min=42, tm_sec=13, tm_wday=2, tm_yday=126, tm_isdst=0)


# # time.asctime
# # time.asctime은 time.localtime이 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알보기 쉬운 형태로 리턴한다. asctime은 ASCII time의 약자입니다.
# print(time.asctime(time.localtime(time.time()))) # Wed May  6 03:42:13 2026


# # time.ctime
# # time.asctime(time.localtime(time.time()))은 간단하게 time.ctime 으로 표시할 수 있다. ctime이 asctime과 다른 점은 항상 현재 시간만을 리턴한다는 점이다.
# print(time.ctime()) # Wed May  6 03:45:11 2026


# # time.strftime
# # strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.
# # time.strftime("출력할_형식_포맷_코드", time.localtime(time.time()))
# # strftime은 string format time의 약자입니다
# """str = string (문자열)
# f = format (형식)
# time = time (시간)"""
# import time
# print(time.strftime("%x", time.localtime(time.time()))) # 05/06/26
# print(time.strftime("%c", time.localtime(time.time()))) # Wed May  6 03:55:30 2026



    
    
# # time sleep
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)
    
    
    
    
    
    
    
    
# # math.gcd
# # math.gcd 함수를 사용하면 최대 공약수를 쉽게 구할 수 있다.
# """사탕 60개, 초콜릿 100개, 젤리 80개는 최대 몇봉지까지 만들 수 있고, 몇개씩 담아야할까"""
# import math
# print(math.gcd(60, 100, 80))  # math.gcd 함수를 통해 최대공약수를 구한다. >>> 20
# print(60/20, 100/20, 80/20) # 3.0 5.0 4.0 / 최대 공약수 20을 각 갯수에 나눠 각 봉지에 들어가는 사탕,초콜릿,젤리의 개수를 구한다.






# # math.lcm
# # math.lcm은 최소 공배수를 구할 때 사용하는 함수이다. 최소 공배수란 두 수의 공통 배수 중 가장 작은 수를 말한다. lcm = least common multiple
# """버스 정류장, 시내버스는 15분, 마을 버스는 25분 마다 도착. 오후 1시에 두 버스가 동시 도착, 두 버스가 동시 도착할 다음 시간은?
# 이 문제는 15와 25의 공통 배수 중 가장 작은 최소 공배수를 구하면 바로 해결 된다."""
# import math
# print(math.lcm(15,25)) # 75, 두 버스가 동시에 도착 할 다음 시간은 75분 후인 오후 2시 15분.









# # random
# # random 은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈. random과 randint 함수에 대해 알아보자.
# import random
# print(random.randint(0, 100)) # 1~100 사이의 정수 중에서 난수값을 리턴
# print(random.random()) # 0.0 ~ 1.0 사이의 실수중에서 난수값을 리턴












# # random모듈을 이용하여 함수 제작
# import random
# def random_pop(data):
#     number = random.randint(0, len(data) - 1)
#     return data.pop(number)

# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5]
#     while data:
#         print(random_pop(data))
        
        

# # random_pop 함수는 random 모듈의 choice 함수를 사용해 좀 더 직관적으로 만들 수 있다.
# import random
# def random_pop(data):
#     number = random.choice(data) # radom.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다. 리스트의 항목을 무작위로 섞고싶을때는 random.sample 함수를 사용.
#     data.remove(number)
#     return number

# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5]
#     while data:
#         print(random_pop(data))

# import random
# data = [1, 2, 3, 4, 5]
# print(random.sample(data, len(data)))


# import random
# data = [1, 2, 3, 4, 5]
# print(random.sample(data, 3)) # >>>[2, 3, 4] random,sample(datam, 숫자값) 무작위의 3개의 숫자 출력




# # itertools.zip_longest
# """itertools.zop_longest 함수는 같은 개수의 자료형을 묶는 파이썬 내장함수인 zip 함수와 똑같이 작동한다. 하지만 itertools.zip_longest() 
# 함수는 전달한 반복 가능 객체(iterables) 의 길이가 서로 다르다면 긴 객체의 길이에 맞춰 fillvalue 에 설정 한 값을 짧은 객체에 채울 수 있다"""
# students = ["곽태헌", "이영임", "황지민", "이광수", "김승민"]
# snacks = ["사탕", "초콜렛", "젤리"]
# result = zip(students, snacks)
# print(list(result)) # [('곽태헌', '사탕'), ('이영임', '초콜렛'), ('황지민', '젤리')]
# """간식의 개수가 네임 리스트보다 적으므로 위와 같은 결과가 나온다.
# strudents != snacks 요소 개수가 다르므로, 더 적은 snacks 의 갯수만큼 zip()으로 묶이게 된다.
# students 의 요소갯수가 snacks보다 더 많을 때 그만큼을 "새우깡"으로 채우려면 어떻게 해야할까?
# 이럴 때 요소 개수가 많은 것을 기준으로 자료형을 묶는 itertools.zip_longest()를 사용하면 된다. 
# 부족한 항목은 None으로 채우는데, 다음처럼 fillvalue로 값을 지정하면 None 대신 다른 값으로 채울 수 있다."""
# import itertools
# students = ["곽태헌", "이영임", "황지민", "이광수", "김승민"]
# snacks = ["사탕", "초콜렛", "젤리"]
# result = itertools.zip_longest(students, snacks, fillvalue="새우깡")
# print(list(result)) # [('곽태헌', '사탕'), ('이영임', '초콜렛'), ('황지민', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]






# # itertools.permutation
# # Permutation 이란 수학/컴퓨터 분야에서 순열이라는 뜻입니다. 즉, 순서를 고려해서 나열하는 경우의 수를 의미합니다.
# # itertools.permutations()는 ("a", "b") 와 ("b", "a")를 다른 것으로 간주합니다. 즉, 순서가 다르면 다른 결과입니다.
# """itertools.permutation(iterable, r)은 반복 가능 객체 중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수이다.
# 1, 2, 3 이라는 숫자가 적힌 3장의 카드에서 2장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면 어떻게 해야 할까?
# """
# import itertools
# list(itertools.permutations(["1", "2", "3"], 2)) # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

# for a, b in itertools.permutations(["1", "2", "3"], 2):
#     print(a + b)
# """
# 12
# 13
# 21
# 23
# 31
# 32
# """

# from itertools import permutations
# data = ["a", "b", "c"]
# result = permutations(data)
# for item in result:
#     print(data)
# """
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# ['a', 'b', 'c']

# """









# # itertools.conbination
# # itertools.combinations(iterble, r)은 반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 리턴하는 함수
# """3장의 카드에서 순서에 상관없이 2장을 고르는 조합은 itertools.combinations()를 사용하면 된다."""
# """itertools.combinations()는 순서를 무시하는 조합으로, ("a", "b") 와 ("b", "a")를 같은 것으로 봅니다."""
# import itertools
# print(list(itertools.combinations(["1", "2", "3"], 2))) # [('1', '2'), ('1', '3'), ('2', '3')]
# # 수학적으로 길이 n 의 전체 순열 개수는: n!입니다. 예를 들어 3개 요소면 3! = 3 x 2 x 1 = 6 이라서 실제로 6개의 결과가 나옵니다.



# # 1~45 중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)을 구하고, 그 개수를 출력하려면 어떻게 해야할까?
# #다음과 같이 itertools.combinations()를 사용하면 45개의 숫자 중 6개를 선택하는 경우의 수를 구할 수 있다.
# import itertools
# it = itertools.combinations(range(1, 46), 6) # 1 ~ 45 까지의 숫자중 6개를 뽑는 경우의 수를 이터레이터로 리턴.
# # for num in it:
# #     print(num) # 이터레이터 객체를 루프를 이용해서 출력하면 끝없이 출력된다.

# # 하지만 순환하여 출력하지 않고, 이터레이터 갯수만 세려면 다음과 같이 하면 된다.
# print(len(list(itertools.combinations(range(1, 46), 6)))) # 8145060 즉, 로또에 당첨되려면 서로 다른 번호의 814만5천장의 로또를 사야한다.
# print(len(list(itertools.combinations_with_replacement(range(1, 46), 6)))) # 15890700 같은 숫자의 중복을 허용하는 함수. ex)1,1,1,1,1,1 / 1,2,3,4,5,5









# # functools.reduce
# """fuctools.reduce(function, iterable)은 함수(function)을 반복 가능한 객체(iterable)의 요소를 차례대로 (왼쪽에서 오른쪽으로)
# 누적 적용하여, 이 객체를 하나의 값으로 줄이는 함수이다."""
# def add(data):
#     result = 0
#     for i in data:
#         result += i
#     return result

# data = [1, 2, 3, 4, 5]
# result = add(data)
# print(result) # 15


# # 위의 함수를 functools.reduce 함수를 사용하여 작성해보자
# import functools

# data = [1, 2, 3, 4, 5]
# result = functools.reduce(lambda x, y: x + y, data)
# print(result) # 15 ((((1+2)+3)+4)+5) reduce()함수가 람다 함수를 data 요소에 누적 적용하는 방식
# #따라서 앞서 본 add함수와 동일한 역할을 하게 된다.



# # functools.reduce()로 최댓값 구하기
# num_list = [3, 2, 8, 1, 6, 7]
# max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
# print(max_num)


# # operator itemgetter
# # operator.itemgetter는 주로 sorted 와 같은 함수의 key 매개변수에 적용하여, 다양한 기준으로 정렬할 수 있도록 도와주는 모듈이다.

# # operator.itemgatter()
# # python의 operator 모듈에 있는 함수로, 인덱스나 키로 항목을 가져오는 callable 객체를 만들어 줍니다.

# # 람다와의 비교
# from operator import itemgetter
# lambda x: x[1] # 이것과
# itemgetter(1) # 이것은 동일한 역할

# # 1. 리스트/튜플에서 인덱스로 가져오기
# from operator import itemgetter

# data = [10, 20, 30, 40]

# get_second = itemgetter(1)
# print(get_second(data)) # 20 (데이터의 인덱스 1을 가리키므로)
# get_multi = itemgetter(0, 2, 3)
# print(get_multi(data)) # (10, 30, 40) 





# # 2. 딕셔너리에서 키로 가져오기
# from operator import itemgetter

# person = {"name":"Alice", "age":"30", "city":"seoul"}

# get_name = itemgetter("name")
# print(get_name(person)) # Alice

# # 여러 키 동시에
# get_info = itemgetter("name", "age")
# print(get_info(person)) # ('Alice', '30')

# get_live = itemgetter("name", "age", "city")
# print(get_live(person)) # ('Alice', '30', 'seoul')







# # 3. 정렬에서 가장 많이 쓰임
# from operator import itemgetter
# students = [
#     {"name": "Bob", "grade": 85, "age": 20},
#     {"name": "Alice", "grade": 92, "age": 24},
#     {"name": "Tom", "grade": 85, "age": 19},
# ]
# #grade 기준 정렬
# print(sorted(students, key=itemgetter("grade"))) # [{'name': 'Bob', 'grade': 85, 'age': 20}, {'name': 'Tom', 'grade': 85, 'age': 19}, {'name': 'Alice', 'grade': 92, 'age': 24}]
# #grade -> age 다중 정렬
# print(sorted(students, key=itemgetter("grade", "age"))) # [{'name': 'Tom', 'grade': 85, 'age': 19}, {'name': 'Bob', 'grade': 85, 'age': 20}, {'name': 'Alice', 'grade': 92, 'age': 24}]




# # 4.튜플 리스트 정렬
# from operator import itemgetter
# pairs = [(1, "banana"), (3, "apple"), (2, "cherry")]
# print(sorted(pairs, key=itemgetter(1))) # [(3, 'apple'), (1, 'banana'), (2, 'cherry')] / index 1 = 알파벳 순서 정렬
# print(sorted(pairs, key=itemgetter(0))) # [(1, 'banana'), (2, 'cherry'), (3, 'apple')] / index 2 = 숫자 정렬




# # 5.groupby 와 함께 사용
# from itertools import groupby
# from operator import itemgetter

# data = [
#     {"dept": "개발", "name": "Alice"},
#     {"dept": "개발", "name": "Bob"},
#     {"dept": "디자인", "name": "Carol"},
# ]

# data.sort(key=itemgetter("dept")) #groupby 전에 반드시 정렬

# for dept, members in groupby(data, key=itemgetter("dept")):
#     print(dept, list(members))
# """개발 [{'dept': '개발', 'name': 'Alice'}, {'dept': '개발', 'name': 'Bob'}]
# 디자인 [{'dept': '디자인', 'name': 'Carol'}]""" # >>> 같은 결과값이 연속되는 구간을 하나의 그룹으로 묶는다.








# # 6.점프 투 파이썬 예제
# # 튜플 - 나이 순으로 데이터 정렬하기
# from operator import itemgetter
# students = [
#     ("jane", 22, "A"),
#     ("dave", 32, "B"),
#     ("Sally", 17, "B"),
# ]
# result = sorted(students, key=itemgetter(1)) # 튜플의 2번 째 요소를 기준으로 정렬
# print(result) # [('Sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]




# # 딕셔너리 데이터를 age 기준으로 정렬하기
# from operator import itemgetter
# students = [
#     {"name": "jane", "age": 22, "grade": "A"},
#     {"name": "dave", "age": 32, "grade": "B"},
#     {"name": "slley", "age": 17, "grade": "B"},
# ]

# result = sorted(students, key=itemgetter("age"))
# print(result) # [{'name': 'slley', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]















# # operator.attrgetter()
# # 1. 기본 사용법

# from operator import attrgetter

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __repr__(self):
#         return f"Person({self.name}, {self.age})"
    
# people = [
#     Person("철수", 30),
#     Person("태헌", 38),
#     Person("영임", 34),
#     Person("Alice", 19),
#     Person("Bob", 60),
# ]

# # 나이 기준 정렬
# sorted_by_age = sorted(people, key=attrgetter("age"))
# print(sorted_by_age) # [Person(Alice, 19), Person(철수, 30), Person(영임, 34), Person(태헌, 38), Person(Bob, 60)]

# # 이름의 유니코드 기준 정렬
# sorted_by_name = sorted(people, key=attrgetter("name"))
# print(sorted_by_name) # [Person(Alice, 19), Person(Bob, 60), Person(영임, 34), Person(철수, 30), Person(태헌, 38)]

# for p in people:
#     print(f"{p.name[0]} -> U+{ord(p.name[0]):04x} ({ord(p.name[0])})") # 각 이름의 첫글자 유니코드 확인
# """철 -> U+cca0 (52384)
# 태 -> U+d0dc (53468)
# 영 -> U+c601 (50689)
# A -> U+0041 (65)
# B -> U+0042 (66)"""







# # 2.중첩 속성(점 표기법)
# from operator import attrgetter
# class address:
#     def __init__(self, city):
#         self.city = city
        
# class employee:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
        
# employee = [
#     employee("Alice", address("busan")),
#     employee("bob", address("seoul")),
#     employee("carol", address("daegu")),
# ]

# # address.city 기준 정렬
# sorted_by_city = sorted(employee, key=attrgetter("address.city"))
# for e in sorted_by_city:
#     print(e.name, e.address.city) 
# """Alice busan
# carol daegu
# bob seoul"""














# # shutil
# # shutil은 파일을 복사하거나 이동할때 사용하는 모듈, shutil 은 shell utilities 의 약자
# """작업중인 파일을 자동으로 백업하는 기능을 구현하고자 c:\doit\a.txt를 c:\temp\a.txt.bak 이라는 이름으로 복사하는 프로그램을 만들고자 한다.
# c:\doit 디렉토리에 a.txt 를 만드는 중이며, 백업용 c:\temp 디렉토리는 이미 만들었다고 가정한다."""
# import shutil
# shutil.copy("c:\doit\a.txt", "c:\temp\a.txt.bak")

# # shutil.move 로 삭제기능 만들기
# # 휴지통으로 삭제하는 기능을 구현하고자 c:\doit\a.txt 파일을 c:\temp\a.txt 로 이동하려면?
# import shutil
# shutil.move("c:\doit\a.txt", "c:\temp\a.txt") 















# # glob
# # glob은 과거 유닉스 운영체제에서 여러 파일을 묶어 처리할 때, 사용하던 global의 약자에서 유래
# # 특정 디텍토리에 있는 파일 이름 모두를 알아야 할 때 사용
# # glob 모듈은 디레토리 안의 파일들을 읽어서 리턴한다. *,? 등의 메타 문자를 사용하여원하는 파일만 읽어들일 수도 있다.
# # 아래는 mark 로 시작하는 파일을 모두 찾아서 읽어들이는 예이다.
# import glob
# glob.glob("c:\doit\mark*")













# # pickle
# # pickle은 객체의 형태를 유지하면서 파일에 저장하고, 불러올 수 있게 하는 모듈
# # pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data 를 그대로 파일에 저장하는 방법 
# # 딕셔너리가 아닌 어떤 자료형이든 저장하고 불러올 수 있다.
# import pickle
# f = open("testt.txt", "wb")
# data = {1: "python", 2: "you need"}
# pickle.dump(data, f)
# f.close()

# # pickle.dump 로 저장한 파일을 pickle.load 를 사용해서 원래 있던 딕셔너리를 객체(data)상태 그대로 불러오는 예
# import pickle
# f = open("test.txt", "rb")
# data = pickle.load(f)
# print(data)










# # OS
# # os 모듈은 환경변수나, 디렉토리 ,파일 등의 os 자원을 제어할 수 있게 해주는 모듈

# # 내 시스템의 변수값을 알고 싶을 때,
# """시스템은 제각기 다른 환경 변수값을 가지고 있는데. os.environ은 현재 시스템의 환경 변숫값을 리턴한다."""
# import os
# print(os.environ)
# """ environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\cheat\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME':.....(생략)"""
# # 위 결과값은 시스템 정보이다. os.environ 은 환경 변수에 대한 정보를 딕셔너리 형태로 구성된 environ 객체로 리턴한다.
# # 리턴 받은 객체는 다음과 같이 호출해서 사용할 수 있다. 다음은 시스템의 PATH 환경 변수의 내용.
# print(os.environ("PATH"))

# # 디렉토리 위치 변경하기 - OS.chdir
# # os.chdir를 사용하면  다음과 같이 현재 디렉토리의 위치를 변경할 수 있다.
# import os
# os.chdir("c:\WINDOW")


# # 디렉토리 위치 돌려받기 - os.getcwd
# # Get Current Working Directory
# # os.getcwd는 현재 자신의 디렉토리 위치를 리턴한다.
# import os
# print(os.getcwd())


# # os.system
# # 시스템의 자체의 프로그램이나, 기타 명령어를 파이썬에서 호출할 수도 있다. 
# # os.system("명령어")처럼 사용한다. 다음은 현재 디렉토리에소 시스템 명령어 dir을 실행한다.
# import os
# print(os.system("dir"))


# # 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# # popen = pipe open 약자
# # 최신 파이썬 프로젝트에서는 subprocess 모듈 사용 권장
# import os
# f = os.popen("dir")
# print(f.read())  # 읽어들인 파일 객체의 내용을 보기 위해서는 다음과 같이 하면 된다.

# 이밖에도 유용한 os관련 함수
# os.mkdir(디렉토리) - 디렉토리를 생성한다. make directory
# os.rmdir(디렉토리) - 디렉토리를 삭제한다. 단 디렉토리가 비어 있어야 삭제할 수 있다.
# os.remove(파일) - 파일을 지운다.
# os.rename(src, dst) - src라는 이름의 파일을 dst라는 이름으로 바꾼다. (바꿀파일, 바뀔파일)





# # zipfile
# # zipfile은 여러개의 파일을 zp형식으로 합치거나, 이를 해제할 때 사용하는 모듈이다.
# """a.txt
# b.txt
# c.txt"""

# """이 3개의 파일을 하나로 합쳐 mytext.zip 이라는 파일을 만들고 이 파일을 원래의 텍스트 파일 3개로 해체하는 프로그램을 만드려면 어떻게해야할까?"""

# import zipfile

# #파일 합치기
# with zipfile.ZipFile("mytext.zip", "w") as myzip:
#     myzip.write("a.txt")
#     myzip.write("b.txt")
#     myzip.write("c.txt")
    
# #해제하기
# with zipfile.ZipFile("mytext.zip") as myzip:
#     myzip.extractall()


# """ZipFile객체의 write()함수로 개별 파일을 추가할 수도 있고 extractall()함수를 사용하면 모든 파일을 해제할 수 있다.
# 합친 파일에서 특정 파일만 해제하고 싶다면 다음과같이 extract() 함수를 사용하면 된다"""
# with zipfile.ZipFile("mytext.zip") as myzip:
#     myzip.extract("a.txt")
    
# """만약 파일을 압축하여 묶고 싶은 경우에는 compression, compresslevel 옵션을 사용할 수 있다.
# """
# # 압축하여 묶기
# with zipfile.ZipFile("mytext.zip", "w", compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:

# # compression에는 4가지 종류가 있다
# """ZIP_STORED - 압축하지 않고 파일을 ZIP으로만 묶는다. 속도가 빠르다."""
# """ZIP_DEFLATED - 일반적인 ZIP 압축으로 속도가 빠르고 압축률은 낮다. (호환성 좋음)"""
# """ZIP_BZIP2 - bzip2 압축으로 압축률이 높고 속도가 느리다."""
# """ZIP_LZMA - lzma 압축으로 압축률이 높고 속도가 느리다. (7zip과 동일한 알고리즘으로 알려져 있다.)"""
# # compressionlevel은 압축 수준을 의미하는 숫자값으로 1~9 를 사용. 1은 속도가 가장 빠르지만 압축률은 낮고, 9는 속도가 가장 느리나, 압축률은 가장 높다













# # threading
# """스레드 프로그래밍은 초보 프로그래머가 구현하기에는 매우 어려운 기술이다. 여기에 잠시 소개했으므로 눈으로만 살펴보고 넘어가자

# 컴퓨터에서 동작하고 있는 프로그램을 프로세스라고 한다.
# 보통 1개의 프로세스가 1가지 일만 하지만 스레드를 사용하면, 한 프로세스가 2가지 또는 그 이상의 일을 동시에 수행할 수 있다."""
# import time

# def long_task():
#     for i in range(5):   # 5초의 시간이 걸리는 함수
#         time.sleep(1) # 1초 대기
#         print("working:%s\n" % i)
        
# print("Start")
# for i in range(5):
#     long_task

# print("End")


# """long_task는 수행하는 데 5초의 시간이 걸리는 함수이다. 위 프로그램은 이 함수를 총 5번 반복해서 수행하는 프로그램이다.
# 이 프로그램은 5초가 5번 반복되므로 총 25초의 시간이 걸린다.
# 하지만 앞에서 설명했듯이 스레드를 사용하면 5초의 시간이 걸리는 long_task 함수를 동시에 실행할 수 있으므로 시간을 줄일 수 있다."""

# """아래와 같이 프로그램을 수정하고 실행해 보면 25초 걸리던 작업이 5초 정도에 수행되는 것을 확인할 수 있다. threading.Thread를 
# 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해주기 때문이다."""

# import time
# import threading
# def long_tesk():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("Start")

# threads = []
# for i in range(5):
#     #long_task()
#     t = threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     t.start()
    
# print("End")

# """실행해보면 "Start"와 "End"가 먼저 출력되고 그 이후에 스레드의 결과가 출력된다.
# 그리고 프로그램이 정상 종료되지않는다. 우리가 기대하는 것은 "Start"가 출력되고 그 다음에 스레드의 결과가 출력된 후, 마무리에서 "End"가 출력되는 것이다
# 이 문제를 해결하려면 함수를 수정해야 한다."""
# import time
# import threading # 스레드를 생성하기 위해서는 threading모듈이 필요
# def long_task():
#     for i in range(5):
#         time.sleep(1) #  time.sleep()함수는 "프로그램의 실행을 지정된 시간만큼 일시 정지"시키는 아주 직관적인 함수
#         print("working:%s\n" % i) # 문자열 포맷팅 / working이라는 문자 뒤에 변수 i의 값을 넣어 출력하되, 출력이 끝나면 줄바꿈을 한번 더 하라는 뜻
#                                   # %는 나머지 연산자가 아니라 앞의 양식 %s에 뒤의 값(i)를 대입해라 라는 연결고리  
        
# print("Start") # 일꾼들 업무 시작을 스타트를 통해 알림 (멀티스레딩 프로세스 및 작업 모니터링 시작)

# threads = [] # 고용된 일꾼들의 이름을 적어둘 빈 명단
# for i in range(5): # 다섯명의 일꾼 준비
#     t = threading.Thread(target=long_task) # threading 모듈을 사용하여, 새로운 일꾼 "Thread"를 생성하고, 그 일꾼이 해야 할 업무를 배정하는 단계
#     threads.append(t) # 생성된 일꾼(객체)ㄹ,ㄹ 나중에 한꺼번에 관리하기 위해 명단(thread리스트)에 추가
    
# for t in threads: 
#     t.start() # 업무 스타트
    
# for t in threads:
#     t.join() # 메인 프로그램이 일꾼들에게 너희 일이 다 끝날때까지 대기할게 라고 말하는 단계
    
# print("End") # 일꾼들이 long_task 를 무사히 마친 것을 확인한 후, 비로소 마지막 인사를 건넴
# """스레드의 join함수는 해당 스레드가 종료될때까지 기다리게 한다. 
# 따라서 위와 같이 수정하면 우리가 원하던 출력을 보게 된다."""


















# # tempfile
# # 파일을 임시로 만들어서 사용할 때, 유용한 모듈
# # make secure temporary 의 약자
# # tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴
# import tempfile
# filename = tempfile.mkstemp()
# print(filename) # >>> (3, 'C:\\Users\\cheat\\AppData\\Local\\Temp\\tmpwwjmv8o4')
# """tmepfile.temporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 리턴한다.
# 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일은 자동으로 삭제된다."""

# import tempfile
# f = tempfile.TemporaryFile()
# f.close() # 임시 파일 삭제







# # traceback
# # traceback은 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈
# def a():
#     return 1 / 0

# def b():
#     a()
    
# def main():
#     try:
#         b()
#     except:
#         print("오류가 발생하였습니다.")
        
# main()
"""main()함수가 시작되면 b()함수를 호출하고, b()함수에서 다시 a()함수를 호출하여 1을 0으로 나누므로
오류가 발생.
이때 이 코드에서 오류가 발생한 위치와 원인을 정확히 판단할 수 있도록 코드를 업그레이드 하려면 어떡해야할까?"""
import traceback

def a():
    return 1 / 0

def b():
    a()
    
def main():
    try:
        b()
    except:
        print("오류 발생")
        print(traceback.format_exc())
        
main()    
"""오류 발생
Traceback (most recent call last):
  File "D:\Project\Python\Jump_Python_v1\Python\JumpPy\표준 라이브러리.py", line 805, in main
    b()
  File "D:\Project\Python\Jump_Python_v1\Python\JumpPy\표준 라이브러리.py", line 801, in b
    a()
  File "D:\Project\Python\Jump_Python_v1\Python\JumpPy\표준 라이브러리.py", line 798, in a
    return 1 / 0
           ~~^~~
ZeroDivisionError: division by zero"""
# 오류 추적을 통해 main()함수에서 b()함수를 호출하고 b()함수에서 다시 a()함수를 호출하여 1 / 0 을 실행하려하므로 0으로 나눌 수 없다는 ZeroDivisonError가 발생 로그 출력






    












