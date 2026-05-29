# # 마이너스 메소드 추가하기
# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val
        
# class UpgradeCalculator(Calculator): # Calculator 클래스에게 상속받아 마이너스 메소드 구현
#     def minus(self, val):
#         self.value -= val
    
        
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)







# # 클래스 상속받고 메서드 추가하기2
# # 객체 변수 value 가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자

# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val
        
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
        
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)





# # 참과 거짓 예측하기
# print(all([1, 2, abs(-3)-3])) # False
# """all()함수와 내부연산의 특성을 이해하면 쉽다
# abs(-3)은 -3의 절대값이므로 3이 되고, 여기에 -3 뺄셈이 이뤄져 0이 됩니다.
# 결과적으로 all([1, 2, 0]) 이 됩니다.
# all() 함수는 인자로 받은 리스트의 모든 요소가 참 일때만 Ture를 반환합니다.
# 0은 Boolean 컨텍스트에서 False 거짓으로 취급되므로 False를 반환합니다."""

# print(chr(ord("a")) == "a") # True
# """이 코드는 컴퓨터 내부의 유니코드(ASCII) 코드값 사이를 왕복하는 연산입니다.
# ord("a") 는 유니코드 정수 값 97(a의 유니코드 값) 을 반환합니다.
# chr(97) 정수 97에 해당하는 유니코드 문자를 반환합니다. 97은 다시 문자 "a" 가 됩니다. 
# 비교연산 == 결과적으로 chr(ord("a")) 는 자기자신인 "a"로 돌아오기 때문에, "a" == "a" 를 비교하는 형태가 됩니다.
# 고로 같으므로 True 를 반환합니다"""







# # filter 와 lambda 함수를 사용하여 리스트 [1, -2, 3, -5, 8, -3] 에서 음수를 모두 제거해보자
# # 1
# numbers = [1, -2, 3, -5,  8, -3]
# filtered_numbers = list(filter(lambda x: x >= 0, numbers))
# print(filtered_numbers)
# # 2
# print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))




# # 16 진수를 10진수로
# print(hex(234)) # 0xea
# print(int(0xea)) # 234




# # 리스트 항목마다 3 곱하여 리턴하기
# print(list(map(lambda x: x * 3, [1, 2, 3, 4])))
# """Python 3의 map() 함수는 메모리 효율성을 위해 연산 결과를 곧바로 리스트로 만들지 않고, 
# 값이 필요한 순간에만 하나씩 계산해서 꺼내주는 '마법 주머니(map 객체)' 상태로 리턴합니다.
# 현업이나 스크립트 자동화 환경에서는 map과 lambda 조합 대신, 가독성이 더 좋고 직관적인 
# 리스트 컴프리헨션(List Comprehension) 방식도 매우 애용됩니다. 참고 삼아 함께 기억해 두시면 좋습니다."""
# print([x * 3 for x in [1, 2, 3, 4]])




# # 최대값과 최소값의 합
# """제시해주신 리스트의 최댓값과 최솟값을 구하고, 이를 더하는 과정은 파이썬 내장 함수인 
# max()와 min()을 사용하면 아주 간결하게 해결할 수 있습니다."""

# numbers = [-8, 2, 7, 5, -3, 5, 0, 1]
# max_val = max(numbers)
# min_val = min(numbers)

# result = max_val + min_val

# print(f"최대값: {max_val}, 최소값: {min_val}")
# print(f"두 값의 합: {result}")







# # 소수점 반올림 하기
# print(17 / 3) # 5.666666666666667

# result = 17 / 3
# print(round(result,4)) # 5.6667

# print(f"{result:.4f}") # 5.6667

# import math
# result = 17 / 3
# print(math.ceil(result)) # 6
# print(math.floor(result)) # 5









# # 문자열 나열하기
# from itertools import permutations
# chars = "abcd"
# result = permutations(chars)

# for i, perm in enumerate(result, 1):
#     print(f"{i:2}. {"".join(perm)}")
    

# # 재귀함수로 직접 구현
# def get_permutations(chars, current="", result=[]):
#     if len(current) == len(chars):
#         result.append(current)
#         return
    
#     for char in chars:
#         if char not in current:
#             get_permutations(chars, current + char, result)
        
#     return result
    
# perms = get_permutations("abcd", "", [])
    
# for i, perm in enumerate(perms, 1):
#     print(f"{i:2}. {perm}")











# # 5명에게 할 일 부여하기
# import random

# people = ["이영임", "김진호", "강춘자", "이예준", "김현주"]
# tasks = ["청소", "빨래", "설거지"]

# random.shuffle(people)

# print("=" * 30)
# print("          오늘의 할일 배정표")
# print("=" * 30)

# assignments = {}
# for i, person in enumerate(people):
#     if i < len(tasks):
#         assignments[person] = tasks[i]
#         print(f"   {person:5s} ->    {tasks[i]}")
#     else:
#         assignments[person] = "휴식"
#         print(f"    {person:5s}  ->  휴식")

# print("=" * 30)
# print(f"총 {len(people)}명 중 {len(tasks)}명 근무, {len(people)-len(tasks)}명 휴식")
# """==============================
#           오늘의 할일 배정표
# ==============================
#    김진호   ->    청소
#    김현주   ->    빨래
#    이영임   ->    설거지
#     강춘자    ->  휴식
#     이예준    ->  휴식
# ==============================
# 총 5명 중 3명 근무, 2명 휴식"""








# # 벽에 타일 붙이기
# """가로의 길이는 200cm , 세로의 길이는 80cm 인 벽이 있다. 이 벽에 되도록 큰 정사각형 모양의 타일을 붙이려고 한다.
# 이때 붙이려는 타일 한 선의 길이와 붙이는 데 필요한 타일의 개수를 구하시오. (최대 공약수 구하는 함수 사용)"""

# import math

# # 벽의 크기 
# width_cm = 200
# height_cm = 80

# print("=" * 40)
# print("타일 계산 프로그램")
# print("=" * 40)
# print(f"벽의 가로 : {width_cm}cm")
# print(f"벽의 세로 : {height_cm}cm")
# print("=" * 40)


# # 최대 공약수로 타일 한 변의 길이 결정
# tile_side = math.gcd(width_cm, height_cm)

# # 필요한 타일 개수
# count_w = width_cm  //  tile_side
# count_h = height_cm // tile_side
# total = count_w * count_h

# print(f" GCD{width_cm}, {height_cm} = {tile_side}cm")
# print("-" * 40)
# print(f"타일 한 변의 길이 : {tile_side}cm")
# print(f"가로 방향 타일 수 : {count_w}개")
# print(f"세로 방향 타일 수 : {count_h}개")
# print(f"필요한 타일 개수 : {count_w} x {count_h} = {total}개")
# print("=" * 40)
# """========================================
# 타일 계산 프로그램
# ========================================
# 벽의 가로 : 200cm
# 벽의 세로 : 80cm
# ========================================
#  GCD200, 80 = 40cm
# ----------------------------------------
# 타일 한 변의 길이 : 40cm
# 가로 방향 타일 수 : 5개
# 세로 방향 타일 수 : 2개
# 필요한 타일 개수 : 5 x 2 = 10개
# ========================================"""