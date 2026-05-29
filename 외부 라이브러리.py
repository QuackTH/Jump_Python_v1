# # pip install
# """pip
# pip는 파이썬 모듈이나, 패키지를 쉽게 설치할 수 있도록 도와주는 도구. pip로 파이썬 프로그램을 설치하면 의존성 있는 모듈이나
# 퍄키지를 함께 설치해 주기 때문에 매우 편리하다
# 예를 들어 B라는 패키지를 설치하려면 먼저 A라는 패키지를 먼저 설치되어야 하는 규칙이 있다고 가정할 때,
# pip를 이용하면 B 패키지를 설치할 때 A 패키지도 자동으로 함께 설치된다."""

# # Faker 
# """Faker"""

# # [(이름1, 주소1), (이름2, 주소2),.....(이름30, 주소30)]
# from faker import Faker 
# fake = Faker("ko-KR")
# print(fake.address())

# test_data = [(fake.name(), fake.address()) for i in range(30)]
# print(test_data)

# test_data = [(fake.name(), fake.postcode()) for i in range(30)]
# print(test_data)


# sympy
from fractions import Fraction
import sympy
x = sympy.symbols("x") # 원래 가지고 있던 돈을 x라고 한다
x, y = sympy.symbols("x, y") 
f = sympy.Eq(x*Fraction("2/5"), 1760) # sympy.Eq(a, b)는 a 와 b가 같다는 방정식이다. 가지고 있던 돈의 2/5 가 1760원이므로 방정식은 x * (2/5) = 1760원이다.
result = sympy.solve(f)  # 결과값은 리스트
print(result) # [4400] 원래 가지고있던 돈은 4400원임을 알 수 있다.

remains = result[0] - 1760
print("남은 돈은 {}원 입니다.".format(remains)) # 남은 돈은 2640원 입니다.





# sympy 활용하기
"""x 2제곱 = 1 과 같은 2차 방정식의 해를 구해보자"""
import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
print(sympy.solve(f)) # [-1, 1]





# 연립 방정식의 해
import sympy
x, y = sympy.symbols("x, y")
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
print(sympy.solve([f1, f2])) # {x: 7, y: 3} 미지수가 2개 이상이라면 결과값은 리스트가 아닌 딕셔너리라는 것에 주의하자.