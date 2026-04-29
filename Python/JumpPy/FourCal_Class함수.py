# # 사칙연산 프로그램 Class 함수 만들기

# class FourCal:
#     def setdata(self, first, second):  #setdata 에서 메서드를 수행해야 객체 a의 객체변수 first 와 second 가 생성된다.
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         reulst = self.first / self.second
#         return reulst
    
    
# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 8)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())
        
# # div 나눗셈은 실수로 표현됨










# # 생성자
# # 객체에 first, second 와 같이 초깃값을 설정해야 할 필요가 있을 초깃값을 설정하기보다 생성자를 구현하는 것이 안전한 방법이다.
# class FourCal:
#     def __init__(self, first, second):  # 생성자
#         self.first = first
#         self.second = second
#     # def setdata(self, first, second):  #setdata 에서 메서드를 수행해야 객체 a의 객체변수 first 와 second 가 생성된다. constuctor 가 있으면 자동으로 생성되면서 초기화(구성)
#     #     self.first = first
#     #     self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         reulst = self.first / self.second
#         return reulst



#     def __init__(self, first, second):  # 생성자
#        self.first = first
#        self.second = second
""" __init__은 setdata 메서드와 이름만 다르고 모든 게 동일하다. 단 메서드 이름을 __init__ 으로 했기때문에
 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이가 있다. """
 
# a = FourCal(10, 19)
# print(a.first)
# print(a.second)
# a = FourCal(4, 2)
# print(a.add())
# a = FourCal(18, 2)
# print(a.div())






# # 클래스의 상속
# # 생성자
# # 객체에 first, second 와 같이 초깃값을 설정해야 할 필요가 있을 초깃값을 설정하기보다 생성자를 구현하는 것이 안전한 방법이다.
# class FourCal:
#     def __init__(self, first, second):  # 생성자
#         self.first = first
#         self.second = second
#     # def setdata(self, first, second):  #setdata 에서 메서드를 수행해야 객체 a의 객체변수 first 와 second 가 생성된다. constuctor 가 있으면 자동으로 생성되면서 초기화(구성)
#     #     self.first = first
#     #     self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         reulst = self.first / self.second
#         return reulst


# class MoreFourCal(FourCal):   # 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속 할 클래스 이름을 넣어준다.
#     pass
# # MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있다.

# a = MoreFourCal(4, 2)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# #왜 굳이 상속받아야하는가?
# """기존 클래스가 라이브러리 형태로 제공되거나, 수정이 불가능하다면 상속을 사용해야 한다."""




# # 기능을 상속받은 새로운 클래스에 다른 계산 기능을 추가하기 
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second # 제곱 기능 추가
#         return result
    
# a = MoreFourCal(4, 2)
# print(a.pow()) # 새로 판 제곱 기능 테스트!
# print(a.add()) # 상속받은 기능은 더하기 기능도 잘 작동한다.
# # 이처럼 상속은 기존 클래스는 그대로 놔둔 체 클래스의 기능을 확장할 때 주로 사용한다.




# # # 메서드 오버라이딩
# # a = FourCal(4, 0)  # 0으로 나누면 에러를 뱉는다. 하지만 오류가 아닌 값 0을 리턴받고 싶다면 어떻게 해야할까?
# # print(a.div()) 


# # 0의 값을 리턴받는 클래스를 만들어보자
# class SafeFourCal(FourCal):
#     def div(self):    # 부모인 FourCal 함수에 이미 있는 div기능을 새로 작성한다. 이것을 메서드 오버라이딩 이라고 한다.
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
# # 이런식으로 부모 클래스의 메서드를 오버라이딩 하면 부모의 메서드 대신 오버라이딩 한 메서드가 호출 된다.

# a = SafeFourCal(4, 0)
# print(a.div())    # 메서드 오버라이딩을 통해 0 값이 리턴되는지 확인!!






# # 클래스 변수
# """ 객체 변수는 다른 객체들의 영향을 받지않고 독립적으로 그 값을 유지한다는 점을 알아보았다
# 이번에는 객체 변수와는 성격이 다른 클래스 변수에 대해 알아보자"""
# class Family:
#     lastname = "곽"
    
# """lastname 이 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성"""

# a = Family()
# b = Family()
# print(a.lastname)
# print(b.lastname)

# Family.lastname = "김" # 클래스 변수의 문자열을 다른 문자열로 치환
# print(a.lastname)
# print(b.lastname)
# """클래스 변수는 객체 변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있다.
# 클래스 변수를 제일 늦게 설명하는 이유는 객체 변수가 클래스 변수보다 훨씬 더 중요하기 때문이다. 실제 실무에서 객체 변수 사용빈도가 훨씬 높다"""

# # 클래스 변수와 동일한 이름의 객체변수를 생성하면?
# a.lastname = "최"
# print(a.lastname)
# """이렇게 하면 Family클래스의 lastname이 바뀌는게 아니라 a 객체에 lastname 이라는 객체 변수가 새롭게 생성된다.
# 즉, 객체 변수는 클래스 변수와 동일한 이름으로 생성할 수 있다."""

# print(Family.lastname) #박
# print(b.lastname) #박
# """Family클래스의 lastname값은 변하지 않았다. 즉 서로 상관없다."""