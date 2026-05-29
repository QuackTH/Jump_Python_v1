# def gugu(n):
#     result = []
#     result.append(n * 1)
#     result.append(n * 2)
#     return(result)
# print(gugu(2))
# """반복이 너무 많다 반복문을 사용하자"""

# #해당 반복문을 gugu 함수에 적용해보자
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1
    

def gugu(n):                    # 함수 선언
    result = []                 # 결과값은 리스트로 받겠다 선언 / 참고로 튜플은 요소를 추가, 삭제, 수정 할 수 없으므로 append()라는 메서드 자체가 정의되어있지않음. 고로 에러 발생
    i = 1                       # 변수 선언, 초기화 / 1로 초기화 하지않으면 컴퓨터는 메모리 어딘가에 저장된 i라는 이름의 상자를 찾아서 그 안에 든 값을 꺼내려고 
                                # 하는데 초기화 하지않을 경우 i가 대체 뭔데? 상태에 빠집니다. 컴퓨터에게 변수의 존재를 알리고, 공정한 레이스를 시작할 출발선을 그어주는 
                                # 작업"입니다. 이 출발선이 없으면 컴퓨터는 레이스 자체를 거부합니다.

    while i < 10:               # while문과 조건식
        result.append(n*i)      # 실행문 1 (명령문)/ 입력받은 n 에 i 의 곱연산이 끝난 최종 결과값을 리스트 맨 뒤에 추가한다 
        i += 1               # 실행문 2 / - 할당문
    return result               # 반환문
print(gugu(2))                  # 출력문
    
    
# def gugu(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu(2))


# 연습 - 구구단 3의 배수 while문 / for문 / 리스트 -> 튜플
# while문 리스트
def gugu3(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result
print(gugu3(3))

# for문 리스트
def gugu3(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result
print(gugu3(3))

# wile문 튜플
def gugu3(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return tuple(result)
print(gugu3(3))

# for문 튜플
def gugu3(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return tuple(result)
print(gugu3(3))
    



# # 연습 - 구구단 4의 배수
# def gugu4(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result

# print(gugu4(4))

# def gugu4(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu4(4))



# # 연습 - 구구단 5의 배수 - for문 사용
# def gugu5(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu5(5))



# # 연습 - 구구단 6의 배수 for문 / while문
# def gugu6(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu6(6))


# def gugu6(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result
# print(gugu6(6))



# # 연습 - 구구단 7의 배수 for문 / while문
# def gugu7(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result
# print(gugu7(7))

# def gugu7(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu7(7))


# # 연습 - 구구단 8의 배수 for문 / while문
# def gugu8(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#     return result
# print(gugu(8))

# def gugu8(n):
#     reuslt = []
#     for i in range(1, 10):
#         reuslt.append(n * i)
#     return reuslt
# print(gugu(8))



# # 연습 - 구구단 9의 배수 for문 / while문
# def gugu9(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result
# print(gugu9(9))

# def gugu9(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu9(9))



# # 연습 - 구구단 10의 배수 for문 / while문
# def gugu10(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result
# print(gugu10(10))

# def gugu10(n):
#     result = []
#     for i in range(1, 10):
#         result.append(n * i)
#     return result
# print(gugu10(10))