# # abs
# # abs(x) 는 어떤 숫자를 입력받았을 때, 그 숫자의 절대값을 리턴하는 함수
# print(abs(3))
# """>>> 3"""
# print(abs(-3))
# """>>> 3"""
# print(abs(-1.2))
# """>>> 1.2"""

# #all
# #all(x) 는 반복 가능한 데이터 x를  입력값으로 받으며, 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False 를 리턴
# print(all([1, 2, 3])) # 참
# print(all([1, 2, 3, 0]))  # 0 은 거짓요소이므로 False 반환
# print(all([])) # 만약 all 의 입력 인수가 빈값인 경우에는 True 리턴


# #any
# #any(x)는 반복 가능한 데이터를 x를 입력받아 x 의 요소 중 하나라도 참이 있으면 True, x가 모두 거짓일 때만 false 를 리턴 즉, all의 반대로 작동
# print(any([1, 2, 3, 0]))
# print(any([0, ""])) # 0과 "" 둘다 거짓이므로 false 리턴
# print(any([])) # any의 입력 인수가 빈 값인 경우에는 False 리턴


# #chr
# #chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수이다
# print(chr(97)) # a
# print(chr(44032)) # 가


# #dir 
# #dir 는 객체가 지닌 변수나 함수를 보여주는 함수. dir 는 directory 의 약자
# print(dir([1, 2, 3]))
# print(dir({"1":"a"}))


# #divmod
# #divmod(a, b) 는 2개의 숫자 a,b 를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴한다.
# print(divmod(7, 3))

# #몫을 구하는 연산자 // 와 나머지를 구하는 연산자 %를 각각 사용한 결과와 비교
# print(7 // 3)
# print(7 % 3)

# #enumerate
# # enumerate 는 열거하다라는 뜻이다. 이 함수는 순서가 있는 데이터 (리스트,튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
# # 보통 for문과 함께 사용한다.
# for i, name in enumerate(["body", "foo", "bar"]):
#     print(i, name)
# # 인덱스 값과 함께 body, goo, bar 가 순서대로 출력되었다. 즉 enumerate 를 for문과 함께 사용하면 자료형의 현재 순서와 그 값을 쉽게 알 수 있다.
# """for문 처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할 때 enumerate 함수를 사용하면 매우 유용하다"""



# #eval
# """eval 은 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결과값을 리턴하는 함수이다"""
# print(eval("1 + 2"))
# print(eval("'hi' + 'a'"))
# print(eval("divmod(4, 3)"))


# #filter
# """filter란 무엇인가를 걸러낸다 라는 뜻으로 filter 함수도 이와 비슷한 기능을 한다."""
# # filter(함수, 반복 가능한 데이터)

# """filter 함수는 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다. 그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서
# (걸러 내서) 리턴한다."""
# def positive(l):
#     result = []
#     for i in l:
#         if i > 0:
#             result.append(i)
#     return result
# print(positive([1, -3, 2, 0, -5, 6])) # [1, 2, 6]

# # 위의 positive 함수는 리스트를 입력으로 받아 각각 요소를 판별하여 양수 값만 리턴하는 함수이다. filter 함수를 사용하면 위 내용을 더 간단히 작성할 수 있다.
# def positive(x):
#     return x > 0
# print(list(filter(positive, [1, -3, 2, 0, -5, 6])))  # [1, 2, 6] 위 for문과 리턴값이 같다.

# # 한번 더 복습
# def positive(x):
#     return x > 0

# print(list(filter(lambda X: X > 0, [1, -3, 2, 0, -5, 6])))
# #>> [1, 2, 6]




# # hex
# # hex(x)는 정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수이다.
# print(hex(234))
# #>>> 0xea
# print(hex(3))
# #>>> 0x3




# # id
# # id(object)는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)를 리턴하는 함수이다.
# a = 3
# print(id(3))

# print(id(a))

# b = a
# print(id(b))
# """위 예의 3, a, b 는 고유 주솟값이 모두 동일하다. 즉 3,a,b 가 모두 같은 객체를 가리키고있다."""

# print(id(4))
# """id 함수 안의 4는 변수를 통해 값을 할당받지않은 전혀 상관없는 개체이므로 가리키는 주솟값이 다름을 알 수 있다."""



# # input
# # 사용자의 입력을 받는 함수로, 입력 인수를 통해 문자열을 전달하면 그 문자열은 프롬프트가 된다.


# # int
# # int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수. 만약 정수가 입력되면 그대로 리턴.
# print(int("3")) # 3
# print(int(3.4)) # 3 (정수로 리턴하므로 float 타입이더라도 정수 3만 리턴)

# # int(x, radix) 는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴. 
# # 예를 들어 진수로 표현된 11의 10진수 값을 출력하는 표현식
# print(int("11", 2))
# # 3 출력
# print(int("1A", 16))
# # 26 출력


# # isinstance
# # isinstance(object, class) 함수는 첫번째 인수로 객체, 두 번째 인수로 클래스를 받는다. 입력으로 받은 객체가 그 클래스의 인스턴스인지 판단하여 참이면 True 거짓이면 Flase 리턴
# class  Person: pass
# a = Person()
# print(isinstance(a, Person))

# b = 3
# print(isinstance(b, Person))







# # len
# # len(s) 는 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수
# print(len("python")) # 6
# print(len([1, 2, 3])) # 3
# print(len((1, "a"))) # 2





# # list
# # list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수이다.
# print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
# print(list((1, 2, 3))) # [1, 2, 3]

# # list 함수에 리스트를 입력하면 똑같은 리스트를 복사하여 리턴한다.
# a = [1, 2, 3]
# b = list(a)
# print(b) # [1, 2, 3]







# # map
# # map(f, iterable)
# # 함수(f)와 반복 가능한 데이터를 입력으로 받는다. map은 입력받은 데이터를 가 요소에 함수 f를 적용한 결과를 리턴하는 함수
# def two_times(numberList):
#     result = []
#     for number in numberList:
#         result.append(number * 2)
#     return result

# result = two_times([1, 2, 3, 4])
# print(result) # [2, 4, 6, 8]

# # two_times는 리스트를 입력받아 리스트의 각 요소에 2를 곱해 리턴하는 함수이다. 위 예제는 map 함수를 사용해서 다음과 같이 바꿀 수 있다.
# def two_times(x):
#     return x * 2

# print(list(map(two_times, [1, 2, 3, 4]))) # [2, 4, 6, 8]
# # map 함수의 결과를 리스트로 출력하기 위해, list 함수 사용, map함수는 map객체를 리턴한다.

# # lambda 함수를 사용하여 더 간단하게 만들 수도 있다.
# print(list(map(lambda a: a*2, [1, 2, 3, 4]))) # [2, 4, 6, 8]







# # max
# # max(iterable)은 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수이다.
# print(max([1, 2, 3])) # 3
# print(max("Python")) # 문자열의 경우 유니코드 값이 가장 큰 문자를 리턴 : y리턴











# # min
# # min은 반대로 인수로 반복가능한 데이터를 입력받아 그 최솟값을 리턴하는 함수
# print(min([1, 2, 3])) # 1
# print(min("Python")) # 대문자P 반환
# print(min("python")) # h 반환









# # oct
# # oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수
# print(oct(34)) # 0o42
# print(oct(12345)) # 0o30071
















# # open
# # open(filename, [model]) 파일 이름과 읽기 방법을 입력 받아 파일 객체를 리턴하는 함수.
# # 읽기 방법을 생략할 경우, 기본값인 읽기 모드로(r) 파일 객체를 만들어 리턴한다.
# """w = 쓰기모드 / r = 읽기 모드 / a = 추가 모드 / b = 바이너리 모드"""
# # b는 w, r, a와 함께 사용한다. 예를 들어 rb 는 바이너리 읽기모드 라는 의미
# f = open("binary_file", "rb")









# #ord
# # ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수
# print(ord("a")) # 97
# print(ord("가")) # 44032
# """ord함수는 앞에서 배웠던 chr함수와 반대로 동작"""









# # pow
# # pow(x, y)는 x를 제곱한 결과값을 리턴한다.
# print(pow(2, 4)) # 16
# print(pow(3, 3)) # 27












# # range
# # range([start,])stop[,step])은 for문과 함께 자주 사용된다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.
# """인수가 하나일 경우"""
# #시작 숫자를 지정해주지 않으면 range함수는 0부터 시작한다. 끝 숫자는 미만으로 포함하지않는다.
# print(list(range(5))) # [0, 1, 2, 3, 4]

# """인수가 두개일 경우"""
# print(list(range(5, 10))) # [5, 6, 7, 8, 9]

# """인수가 세개일 경우"""
# print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9] 1부터 9까지 숫자간 거리는 2로 해석
# print(list(range(0, -10, -1))) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9] 0부터 -9까지, 간격은 -1

















# # round()
# # round(number, [,ndigits])는 숫자를 입력받아 반올림해 리턴하는 함수 (ndigits = number of digits)
# # [,ndigits]은 ndigits가 있을수도, 없을수도 있다는 의미
# print(round(4.6)) # 5
# print(round(4.2)) # 4
# """다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다"""
# print(round(5.678, 2)) # 5.68
# """round함수의 두번째 인수는 반올림하여 표시하고 샆은 소숫점의 자리수를 의미한다"""














# # sorted
# # sorted(iterable)는 입력 데이터를 정렬한 후, 그 결과를 리스트로 리턴하는 함수
# print(sorted([3, 1, 2])) # [1, 2, 3]
# print(sorted(["a", "c", "b"])) # ['a', 'b', 'c']
# print(sorted("zero")) # ['e', 'o', 'r', 'z']
# print(sorted((3, 2, 1))) # [1, 2, 3]












# # str
# # str(object)는 문자열 형태로 객체를 변환하여 리턴하는 함수
# print(str(3)) # 3
# print(str("hi")) # hi










# # sum
# # sum(iterable)은 입력 데이터의 합을 리턴하는 함수
# print(sum([1, 2, 3])) # 6
# print(sum([4, 5, 6])) # 15










# # tuple
# # tuple(iterable)은 반복가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다. 만약 입력이 튜플이라면 그대로 리턴
# print(tuple("abc")) # ('a', 'b', 'c')
# print(tuple([1, 2, 3])) # (1, 2, 3)
# print(tuple((1, 2, 3))) # (1, 2, 3)


















# # type
# # type(object)는 입력값의 자료형이 무엇인 알려 주는 함수이다.
# print(type("abc")) # <class 'str'>
# print(type([])) # <class 'list'>
# print(type(open("test", "w"))) # <class '_io.TextIOWrapper'>















# zip
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.
# 여기서 사용한 iterable은 반복 가능한 데이터를 여러 개 입력할 수 있다는 의미이다.
print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc", "def"))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]


#zip 함수의 쓰임새
"""zip함수가 없을 때"""
names = ["Point_A", "Point_B", "Point_C"]
positions = [10.5, 20.1, 5.4]

for i in range(len(names)):
    print(names[i], "의 위치는", positions[i])


"""zip함수를 사용할 때"""
for name, pos in zip(names, positions):
        print(f"{name}의 위치는 {pos}") # 인덱스 i를 관리 할 필요가 없어 코드가 훨씬 직관적이고 실수를 줄여줍니다.

""" 여러 속성 값을 가진 데이터를 하나의 튜플로 묶어서 처리하기 좋습니다.
"""


