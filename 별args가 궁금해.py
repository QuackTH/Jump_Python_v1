
"""  * (아스테리스크): "지금부터 들어오는 인자들을 전부 하나로 묶어서 튜플(Tuple, 바구니)에 담아라!" 라는 마법의 기호입니다."""
""" *args는 가변 인자(Variable Arguments)라고 부르며, 인자의 개수를 제한하지 않고 다 받아내겠다는 뜻입니다. """

# 일반 함수
def add(a, b):
    return a + b

print(add(10, 4))
print(add(20, 49))



# *args 를 쓴 만능 함수
def add_all(*args):
    return sum(args)

print(add_all(100, 200, 300))
print(add_all(1, 3, 20, 500, 10))



# 문자도 다 받아내는 만능 함수로 바꿔보자
def add_alls(*args):
    return "".join(args)

print(add_alls("a", "b", "c", "d"))






# """*args가 순서대로 던지는 값들을 담는 '일반 바구니'였다면, 
# kwargs는 "이름표가 붙은 데이터(키워드 인자)들을 싹 다 받아먹는 '딕셔너리(Dictionary) 바구니'"입니다."""
# # (더블 아스테리스크): "지금부터 이름표를 달고 들어오는 값들(이름=값)을 전부 묶어서 딕셔너리(Dictionary, 사전형) 바구니에 담아라!" 라는 뜻입니다.
# def intro_user(**kwargs):
#     print(kwargs)
    
# intro_user(name="이영임", age=38, job="3D 환경 아티스트")