# # datetime.date
# """datetime.date는 연,월,일 날짜를 표현할 때 사용하는 함수"""
# import datetime
# day1 = datetime.date(2021, 12, 14)
# day2 = datetime.date(2023, 4, 5)

# diff = day2 - day1
# print(diff.days) # 477  둘이 만난지 477일 째

# """day2 에서 day1을 뺀 datetime 모듈의 timedelta 객체가 리턴된다.
# 요일은 datetime.date 객체의 weekday 함수를 사용하면 쉽게 구할 수 있다"""
# day = datetime.date(2021, 12, 14)
# print(day.weekday())   # 1 (2021년 12월 14일은 화요일), 월요일은 0 ~ 6은 일요일이 된다. 만약 월요일을 1로 시작해서 리턴하고 싶다면 isoweekday() 를 사용하면 된다.
# print(day.isoweekday()) # 2











# time
#시간과 관련된 time 모듈에는 함수가 매우 많다. 

# time.time
# time.time()는 UTC 세계 표준시를 사용하여, 현재 시간을 실수 형태로 리턴하는 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴해준다.
import time
print(time.time()) # 1778006533.4747453

# time.localtime
# time.localtime 은 time.time()이 리턴한 실숫값을 사용해서 년,월,일,시,분,초 의 형태로 바꾸어 주는 함수이다.
print(time.localtime(time.time())) # time.struct_time(tm_year=2026, tm_mon=5, tm_mday=6, tm_hour=3, tm_min=42, tm_sec=13, tm_wday=2, tm_yday=126, tm_isdst=0)


# time.asctime
# time.asctime은 time.localtime이 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알보기 쉬운 형태로 리턴한다. asctime은 ASCII time의 약자입니다.
print(time.asctime(time.localtime(time.time()))) # Wed May  6 03:42:13 2026


# time.ctime
# time.asctime(time.localtime(time.time()))은 간단하게 time.ctime 으로 표시할 수 있다. ctime이 asctime과 다른 점은 항상 현재 시간만을 리턴한다는 점이다.
print(time.ctime()) # Wed May  6 03:45:11 2026


# time.strftime
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.
# time.strftime("출력할_형식_포맷_코드", time.localtime(time.time()))
# strftime은 string format time의 약자입니다
"""str = string (문자열)
f = format (형식)
time = time (시간)"""
import time
print(time.strftime("%x", time.localtime(time.time()))) # 05/06/26
print(time.strftime("%c", time.localtime(time.time()))) # Wed May  6 03:55:30 2026
