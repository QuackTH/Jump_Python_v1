"""파이썬 버전 3.5 부터 변수와 함수에 타입을 지정할 수 있는 타입 어노테이션 기능이 추가 됨"""


#동적 언어와 정적 언어
a = 1
print(type(a)) # <class 'int'>

a = "Python"
print(type(a)) # <class 'str'>

a = "1"
print(type(a)) # <class 'str'>

"""프로그램 수행 중에 변수의 타입을 동적으로 바꿀 수 있으므로 파이썬을 동적 프로그래밍 언어라고 부른다
자바는 정수형 변수 a에 숫자 1을 대입하고 다시 문자열 1을 대입하려 할 때 컴파일 오류가 발생한다. """


def greeting(name: str) -> str:
    return "Hello, " + name

print(greeting("Quack")) # Hello, Quack


# 일반 변수 어노테이션
age: int = 38
user_name: str = "곽태헌"
is_active: bool = True 

#빈 리스트를 만들 대 내부에 무엇이 담길지 힌트 추가
from typing import List
node_names: List[str] = []



# 파이썬은 타입 어노테이션으로 매개변수의 타입을 명시하더라도 다음과 같이 다른 타입의 인수를 입력 가능
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 3.4)
print(result) # 6.4
"""float 타입의 인자를 받았지만 문제없이 코드는 돌아간다. 파이썬 어노테이션은 체크가 아닌 힌트이기 때문"""



# 더 적극적으로 어노테이션을 활용하려면 mypy 를 사용하는 것이 좋다
# 다만 mypy 는 표준 라이브러리가 아니므로 설치가 필요하다
