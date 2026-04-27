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

# # 입력값은 없지만 리턴값으로 "HI"라는 문자열을 리턴한다. 
# def say():
#     return "hi"
# a = say()
# print(a)
# # 이처럼 입력값이 없고 리턴값만 있는 함수는 다음과 같이 사용한다
# # 리턴 값을 받을 변수 = 함수_이름()




# # 리턴값이 없는 함수 역시 존재한다. 다음 예를 살펴보자.
# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    
# add(3 ,4)
# # 리턴 값이 없는 함수는 호출해도 리턴되는 값이 없기때문에, 다음과 같이 사용한다.
# #함수_이름(입력_인수1, 입력_인수2) 

# # 리턴값이 없음으로 None을 뱉는다.
# a = add(3,4)
# print(a)





# #입력값도 리턴값도 없는 함수
# def say():
#     print("Hi")

# say()
# # 입력값도 리턴값도 없는 함수는 다음과 같이 사용한다. 함수_이름()



# #매개변수를 지정하여 호출하기
# def sub(a, b):
#     return a - b
# result = sub(a = 7, b = 3) # result 변수를 통해 매개변수를 지정
# print(result)

# # 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
# result = sub(b=5, a=3) # b가 a보다 앞에 와있다.
# print(result)

# 입력값이 몇개가 될지 모를 때는 어떻게 해야할까?
# def 함수_이름 (*매개 변수): # 일반적으로 볼 수 있는 함수 형태에서 괄호 안의 매개변수 부분이 *매개변수
#     실행할 문장
#     ...

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# #위의 add_many() 함수는 입력값이 몇 개든 상관없다. 매개변수 이름 앞에 *를 붙이며 입력값을 전부 모아 튜플로 만들어주기 때문이다.

# # result = add_many(1, 2, 3)
# # print(result)

# result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)





# # 두 개 이상의 매개변수 사용도 가능하다
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("add", 1, 2, 3, 4, 5)
# print(result)

# result = add_mul("mul", 1, 2, 3, 4, 5)
# print(result)
        
        
        
# # 키워드 매개변수, kwargs 
# # 키워드 매개변수를 사용할 때는 매개변수 앞에 ** 2개를 붙인다.
# def print_kwargs(**kwargs):
#     print(kwargs)
    
# print_kwargs(a=1) # 함수의 입력값으로 a=1 이 되면, {"a": 1}이라는 딕셔너리가 된다.
# print_kwargs(name="foo", age=3) #{"age":3, name:"foo"}라는 딕셔너리가 된다.



# #함수의 리턴값은 언제나 하나이다.
# def add_and_mul(a, b):
#     return a+b, a*b
# result = add_and_mul(3,4) # 변수를 받아들이는 result 하나만 쓰였으므로 오류가 발생하지않을까?
# print(result)
# # 하지만 오류는 발생하지않았다. 이유는 함수의 리턴값은 2개가 아니라 언제나 1개라는 점에 있다. 튜플값인 (a+b, a*b)로 리턴된다.
# # (7, 12)   결과값으로 튜플 값이 출력되었다.

# # return문을 2개 사용하면 분리 된 값을 리턴받을 수 있지 않을까?
# def add_and_mul(a, b):
#     return a + b
#     return a * b
# result = add_and_mul(3, 4)
# print(result)
# 하지만 a * b는 출력되지않는다. 함수는 첫번째 return 문을 만나는 순간 함수를 빠져나간다.
# return을 통해 함수를 빠져나가고 싶을 때 단독으로 써서 즉시 빠져나갈 수 있다.
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick) # 문자열을 출력하는 것과 리턴값이 있다는 것은 전혀 다른 말이므로 혼동하지말자
    #함수의 return값은 오직 리턴문에 의해서만 생성 된다.
say_nick("야호")
say_nick("바보") # nick == "바보" 에 의해 return문이 실행되어 문자열 출력없이 함수를 빠져나왔다.

