# def mul(a):
#     def wrapper(n):
#         return a * n
#     return wrapper

# if __name__ == "__main__":
#     mul3 = mul(3)
#     mul5 = mul(5)
    
#     print(mul3(10)) # 30
#     print(mul5(10)) # 50
    
    
    
    
# import time
# def myfunc():
#     start = time.time()
#     print("함수가 실행됩니다.")
#     end = time.time()
#     print("함수의 수행시간: %f 초" % (end - start))
    
# myfunc()
# """함수가 실행됩니다.
# 함수의 수행시간: 0.000068 초"""

# """하지만 실행 시간을 측정해야 하는 함수가 myfunc 말고도 많다면 이런 코드를 모든 함수에 마찬가지로 적용하는 것은
# 너무 비효율적이다. 이 때 클로저를 사용하면 좀 더 효율적인 방법을 찾을 수 있다"""


import time
def elapsed(original_func): # 기존 함수를 인수로 받는다.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs) # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f초" % (end - start)) # 기존 함수의 수행 시간을 출력
        return result #기존 함수의 수행 결과를 리턴
    return wrapper

# def func():
#     print("함수가 실행됩니다.")


# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()


@elapsed
def myfunc(msg):
    print("'%s'를 출력합니다." % msg)
    
myfunc("You need Pyhton")