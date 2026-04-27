# def add(a, b): # parametter
#     return a + b

# print(add(3, 4)) # arguments



# # add함수
# a = 3
# b = 4
# c = add(a, b)
# print(c)


# # 매개변수와 인수
# # 매개변수와 인수는 혼용해서 사용하는 용어이므로, 잘 기억해두자. 
# """매개변수는 함수에 입력으로 전달 된 값을 전달 받는 변수, 인수는 함수를 호출할 때 전달하는 입력갑을 의미한다"""



# 일반적인 함수
# 입력값이 있고 리턴값이 있는 함수가 일반적인 함수

# def add(a, b):
#     result = a + b
#     return result

# 입력값은 없지만 리턴값으로 "HI"라는 문자열을 리턴한다. 
def say():
    return "hi"
a = say()
print(a)
# 이처럼 입력값이 없고 리턴값만 있는 함수는 다음과 같이 사용한다
# 리턴 값을 받을 변수 = 함수_이름()