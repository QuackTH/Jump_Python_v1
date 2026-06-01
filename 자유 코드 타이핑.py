# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num * 3)
# print(result)



# b = [1, 2, 3, 4]
# result2 = [num * 5 for num in b]
# print(result2)



# x = 1
# y = eval("x + 1")
# print(y)


# def gugu(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i = i + 1
#     return result
# print(gugu(2))

# def guguL(n):
#     result = []
#     i = 1
#     for i in range(1, 10):
#         result.append(n * i)
#         i = i + 1
#     return result
# print(guguL(3))




# # 1000 미만의 자연수에서 3과 5의 배수의 총합을 구하라
# """다음 문제를 어떻게 풀면 좋을지 생각해 보자."""

# result = 0
# for n in range(0, 1000):
#     if n % 3 == 0 or n % 5 == 0:
#         result += n
# print(result) # 233168


# # 잘못된 예
# """3과 5의 겹치는 중복 배수를 고려하지않는 식"""
# result = 0
# for n in range(0, 1000):
#     if n % 3 == 0:
#         result += n
#     if n % 5 == 0:
#         result += n
# print(result) # 266333







# class Mul:
#     def __init__(self, m):
#         self = m
    
#     def mul(self, n):
#         return self * n
    
# if __name__ == "__main__":
#     mul3 = Mul(3)
#     mul5 = Mul(5)

#     print(mul3.mul(10))
#     print(mul5.mul(10))



