# # try - execpt 문

# try:
#     .....
# except[발생_오류[as 오류_변수]]:
#     ...
# """try 블록 수행 중 오류가 발생하면 except 블록이 수행 된다. 하지만 try 블록에서 오류가 발생하지 않는다면  except 블록은 수행되지 않는다"""

# except[발생_오류[as 오류_변수]]:
    
# """위 구문을 보면 []를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례적인 표기법이다. except 구문은 다음 3가지 방법으로 사용가능하다."""

# # try - except 만 쓰는 방법
# try:
#     ...
# except:
#     ...
    
    
# #발생 오류만 포함한 except문
# try:
#     ...
# except 발생_오류:
#     ...
# """이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류와 동일한 오류일 경우에만 except블록을 수행한다는 뜻이다."""

# # 발생 오류와 오류 변수까지 포함한 except문
# try:
#     ...
# except 발생_오류 as 오류_변수:
#     ...
# """이 경우는 두 번째 경우에서 오류의 내용까지 알고 싶을 때 사용하는 방법이다."""

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# """위 처럼 4를 0으로 나누려고하면 ZeroDivisionError 가 발생하여 except 블록이 실행되고 오류 변수를e에 담기는 오류 메세지를 출력할 수 있다."""


# #try-finally문
# """try문에는 finally절을 사용할 수 없다.
# finally 절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally절은 사용한 리소스를 close 할 때 많이 사용한다."""






# # ZeroDivisionError 와 IndexError 를 함께 처리
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)
    



# # 각각의 블록으로 처리해야 두 개의 출력을 볼 수 있다.
# try:
#     a = [1, 2]
#     print(a[3])
# except IndexError as e:
#     print(f"첫 번째 에러: {e}")
    
    
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(f"두 번째 에러: {e}")




# # try - else문
# """try문에는 다음처럼 else문을 사용할 수도 있다"""
# try:
#     ...
# except[발생_오류{as 오류_변수}]:
#     ...
# else:   #오류가 없을 경우에만 사용
#     ...

"""try문 수행 중 오류가 발생하면 except절, 오류가 발생하지 않으면 else절이 수행."""
# 예
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("Welcome to here! ")