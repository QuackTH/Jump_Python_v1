# -*- coding:ecu-kr -*-
# # 인코딩 하기
# # 유니코드를 바이트 문자열로 인코딩 하기
# a = "Life is too short"
# b = a.encode("UTF-8")
# print(b) # b'Life is too short'
# print(type(b)) # <class 'bytes'>

# """한글 문자열을 아스키 코드로 인코딩 하려고 하면, 아스키 코드로는 한글을 표현할 수 없으므로
# 에러가 난다"""

# # 유니코드 문자열을 eus-kr 방식으로 인코딩
# a = "한글"
# print(a.encode("euc-kr")) # b'\xc7\xd1\xb1\xdb'
# print(a.encode("utf-8")) # b'\xed\x95\x9c\xea\xb8\x80'


# # 반대로 인코딩 한 문자열을 유니코드 문자열로 변환하는 디코딩
# # euc-kr 로 인코딩한 바이트 문자열은 euc-kr 로만 디코딩 해야한다.
# a = "한글"
# b = a.encode("euc-kr")
# print(b.decode("euc-kr")) # 한글




a = "똠방각하"
b = a.encode("euc-kr")
print(b) # b'\xa4\xd4\xa4\xa8\xa4\xc7\xa4\xb1\xb9\xe6\xb0\xa2\xc7\xcf'
# print(b.decode("euc-kr")) # 한글


a = "똠방각하"
b = a.encode("cp949") 
print(b) # b'\x8cc\xb9\xe6\xb0\xa2\xc7\xcf'


