
# # 일반 리스트
# for a in [1, 2, 3]:
#     print(a)


# # 일반 리스트에 next함수 사용 시 타입에러 출력 확인해보기
# a = [1, 2, 3]
# next(a)


# # 일반 리스트를 이터레이터 타입으로 전환하기
# a = [1, 2, 3]
# ia = iter(a)
# print(type(ia)) # <class 'list_iterator'>
# # 이터레이터 타입으로 전환되었으니 출력해보기
# print(next(ia)) # 1
# print(next(ia)) # 2
# print(next(ia)) # 3
# print(next(ia)) # stopiteration 예외

# # 이터레이터의 값을 가져오는 가장 일반적인 방법은 for문을 이용하는 것
# a = [1, 2, 3]
# ia = iter(a)
# for i in ia:
#     print(i)
    
    
# """for문을 사용하면 자동으로 값을 호출하므로 next함수를 따로 쓸 필요도 없고 stopiteration 예외에 신경 쓸 필요도 없다."""

# """이터레이터는 for문으로 반복하고 난 후에는 다시 반복하더라도 더는 그 값을 가져오지못한다. 
# 즉 그 값을 한번 읽으면 다시 읽을 수 없다는 특징이 있다."""



# # 클래스 이터레이터 만들기

# """for문을 통해 인덱스를 0부터 1씩 올리며 데이터를 꺼내다가 범위를 벗어나면 멈추는 코드로
# 파이썬 표준 메소드 __iter__, __next__ 로 어떻게 구현되는지 보여주는 정석적인 코드"""
# class myiterator: # class myiterator 생성
#     def __init__(self, data):
#         self.data = data # 우리가 넘겨준 리스트 [1,2,3]을 저장
#         self.position = 0 # 현재 몇 번째 데이터를 읽고 있는지 가리키는 포인터(인덱스) 입니다
    
#     def __iter__(self):
#         return self # 나 자신을 반복할 준비가 된 객체로 자기 자신을 반환. for 문을 시작할 때 가장 먼저 이 메소드를 실행

#     def __next__(self): # 핵심 로직, for문이 돌때마다 내부적이 이것을 계속 호출
#         if self.position >= len(self.data): # 조건확인. 가리 키는 위치(position)가 데이터 전체길이보다 크기가 크거나 같이지면?
#             raise StopIteration # 이제 더 이상 꺼낼 데이터가 없으면 에러신호를 발생시켜 반복문을 정지시킴
#         result = self.data[self.position] # 아직 데이터가 남아있다면 현재 위치의 값을 가져옵니다.
#         self.position += 1 # 위치 이동. 다음번에는 그 다음 칸의 데이터를 꺼낼 수 있도록 posotion 을 1 증가시킴
#         return result # 가져온 값을 반환


# if __name__ == "__main__":
#     i = myiterator([1, 2, 3]) # self.data = [1, 2, 3], self.position = 0 상대로 시작
#     for item in i: 
#         print(item)
        
        
        
        
# class ReverseIterator:
#     def __init__(self, data):
#         self.data = data
#         self.position = len(self.data) -1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.position < 0:
#             raise StopIteration
#         result = self.data[self.position]
#         self.position -= 1
#         return result
    
# if __name__ == "__main__":
#     i = ReverseIterator([1, 2, 3])
#     for item in i:
#         print(item)
            
            
# def mygen():
#     yield "a"
#     yield "b"
#     yield "c"
    
# g = mygen()

# print(type(g)) # <class 'generator'>
# print(next(g)) # a
# print(next(g)) # b
# print(next(g)) # c


# # 제너레이터 표현식
# def mygen():
#     for i in range(1, 1000):
#         result = i * i
#         yield result
# gen = mygen()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# # 튜플 표현식으로 좀 더 간단하게 만들 수 있다
# gen = (i * i for i in range(1, 1000))

# print(next(gen))
# print(next(gen))
# print(next(gen))




# 제네레이터 활용하기
# 비교를 위해 리스트 컴프리헨션을 이용한 출력부터 살펴보자
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job[0])
"""job start
job start
job start
job start
job start
done"""


# 제네레이터 활용하기
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))
"""job start
done"""
"""이러한 결과가 나오는 이유는 제네레이터 익스프레션에 의해 함수가 5회가 아닌 1회만 호출되기 때문이다
이러한 방식을 lazy evaluation 이라고 부른다.
작업을 한꺼번에 처리하기보다는 필요한 경우에만 호출하여 사용할 때 제네레이터는 유용하다"""