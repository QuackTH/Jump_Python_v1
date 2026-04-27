# a = ["a", "c", "b"]    
# a.reverse()
# print(a)


# # 딕셔너리 쌍 추가하기 / 삭제하기
# a = {1: "a"}
# a[2] = "b"
# a[3] = "c"
# a["name"] = "pey"
# a[4] = [1, 2, 3]
# del a[4]


# print(a)

# # 딕셔너리에서 key 를 사용하여 value 얻기
# grade = {"pey" : 10, "Juliet": 99}
# print(grade["pey"])
# print(grade["Juliet"])

# a = {1:"a", 2:"b"}
# print(a[1])
# print(a[2])

# b = {"a": 1, "b": 2}
# print(b["a"])
# print(b["b"])

# a = 3
# if a > 1:
#     print("a는 1보다 큽니다")
# else:
#     print("a는 1보다 작습니다.")

    
# # for 반복문
# for a in [1, 2, 3]:
#     print(a)

# # 반복문 while
# i = 0
# while i < 5:
#     i = i + 1
#     print(i)

# # 함수
# import random

# def randomize():
#     a = random.randint(0, 100)
#     print(a)

# randomize()

# a = {"name": "pey", "phone": "010-0000-9999", "birth": "1105" }   
# print(dic["name"])
# print(dic["phone"])
# print(dic["birth"])




# # # 딕셔너리 관련 함수
# a = {"name": "pey", "phone": "010-5135-0630", "birth": 1105}
# # print(a.keys())
# print(list(a.keys()))
# print(list(a.values()))
# print(list(a.items()))
# # print(a.clear())
# print(a.get("name"))
# print(a.get("phone"))
# print(a.get("birth"))
# print(a.get("Nokey"))
# print(a.get("Nokey, foo"))
# print("name" in a)
# print("Nokey" in a)


# # 리스트를 사용하는 것과 별 차이는 없지만, 리스트 고유의 append, insert, pop, insert, sort 

# for k in a.keys():
#     print(k)

# tasks = ["Houdini_sim", "MAYA_Render", "Python_Script"]
# while tasks:
#     current_task = tasks.pop(0)
#     print(current_task)
#     break


# # 집합 자료형
# s1 = set([1, 2, 3])
# print(s1)

# s2 = set("Hello Python!")
# print(s2) # 중복을 허용하지 않는다. , 순서가 없다 - 집합 자료형의 특징

# a = [1, 2, 3]
# b = a.copy()
# print(b is a)

# a, b = ("Python", "Life")
# print(a, b)

# (a, b) = ("Python", "Life")
# print(a, b)

# [a, b] = ("Python", "Life") 
# print([a, b])

# a = b = "Python"
# print(a, b)


# #변수의 값 바꾸기
# a = 3
# b = 5
# a, b = b, a
# print(a)

# # a 와 b 는 서로 메모리 주소가 같지않으므로 flase
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)


## 평균 구하기
# 국어 = 80
# 영어 = 75
# 수학 = 55
# print((국어 + 영어 + 수학) / 3)



# score = {"국어": 80, "영어": 75, "수학": 55}
# average = sum(score.values()) / len(score)
# print(f"평균 점수: {average:2f}")



# # 자연수 13이 홀수인지 짝수인지 판별하기
# number = 13
# if number % 2 == 1:
#     print(f"{number}는 홀수 입니다.")
    
# else:
#     print(f"{number}는 짝수 입니다.")


# def check_odd_even(n):
#     return "홀수" if n % 2 != 0 else "짝수"

# result = check_odd_even(13)
# print(f"결과 : {result}")


# # 주민등록번호에 슬라이싱을 사용하여 나누어 출력하기, 성별 정보 인덱싱 사용하여 출력하기
# pin = "881105-1041311"
# yyyymmdd = pin[:6]
# num = pin[7:]
# print(f"생년월일: {yyyymmdd}")
# print(f"나머지 고유식별번호: {num}")
# print(f"성별 정보 : {pin[7]}")

# #문자열 바꾸기
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b)

# a = "total^gemini"
# b = a.replace("^", "$")
# print(b)


# # 리스트를 문자열로 출력하기
# a = ["Life", "is", "too", "short"]
# result = " ".join(a)
# print(result)

# # 튜플에 추가 숫자 튜플 덪붙이기
# a = (1, 2, 3)
# a = a + (4,)
# print(a)

# # 튜플을 리스트로 변환
# a = (1, 2, 3)
# a = list(a)
# a.append(4)
# a = tuple(a)

# print(a)



# # 딕셔너리의 키
# a = {"name": "Coody", "age": 38}
# print(a)

# b = dict()
# b["job"] = "3D Artist"
# b["tool"] = "Houdini sim"
# print(b)

# # pop 함수 이용하여 딕셔너리 values 값 추출
# a = {"A": 90, "B": 80, "C": 55}
# result = a.pop("B")
# print(a)
# print(result)

# 리스트의 중복 제거하기
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)
# b = list(aSet)
# print(aSet)
# print(b)


# Python 변수 (여러개의 변수 선언)
a = b =[1, 2, 3]
a[1] = 4
print(b)
