"""mypy 인스톨 후, 테스트를 위한 텍스트 파일"""


def add(a: int, b: int) -> int:
    return a + b

result = add(3, 4.5)
print(result)