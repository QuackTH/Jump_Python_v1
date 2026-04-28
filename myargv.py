# 입력 값을 모두 더해 출력하는 프로그램
import sys
numbers = sys.argv[1:]
result = 0
for number in numbers:    # for 변수 in 리스트 구조에서 변수 자리에 오는 것이 곧 정의이므로 별도로 number = ... 같이 선언할 필요가 없습니다.
    result += int(number)
print(result)

