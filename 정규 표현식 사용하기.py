# """주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의
# 뒷자리를 * 문자로 변경해보자"""

# # 전체 텍스트를 공백 문자로 나눈다
# # 나뉜 단어가 주민등록번호 형식인지 조사한다
# # 단어가 주민등록번호 형식이라면 뒷자리를 *로 변환한다
# # 나뉜 단어를 다시 조립한다

# data = """Quack 881105-1041311 
# youngim 930112-2041311"""

# result = []
# for line in data.split("\n"):
#     word_result = []
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print("\n".join(result))

# import re

# data = """Quack 881105-1041311 
# youngim 930112-2041311"""

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))


# # 제미나이 추천식 (조금 더 직관적인 표현 방식)
# import re

# data = """Quack 881105-1041311
# youngim 930112 2041311"""

# pat = re.compile(r"(\d{6})-\d{7}")
# print(pat.sub(r"\1-*******", data))


# import re

# p = re.compile("[a-z]+")

# m = p.match("python")
# print(m) # <re.Match object; span=(0, 6), match='python'>

# m = p.match("3 Python")
# print(m) # None

# import re

# p = re.compile("[a-z]+")

# result = p.findall("life is too short")
# print(result) # ['life', 'is', 'too', 'short']

# m = p.match("python")
# print(m) # <re.Match object; span=(0, 6), match='python'>

# m = p.match("3 python")
# print(m) # None











# # 문자열 소비가 없는 메타 문자
"""문자열 소비가 없다는 것은 커서가 글자 위를 지나가지않으며, 그저 조건만 체크함을 의미합니다"""

# """메타 문자는 or 과 동일한 의미로 사용된다. A|B 라는 정규식이 있다면 A 또는 B 라는 의미가 된다."""
# import re

# p = re.compile("Crow|Servo")
# m = p.match("CrowHello")
# print(m) # <re.Match object; span=(0, 4), match='Crow'>




# """  ^ 메타 문자는 맨 처음과 일치한다는 것을 의미한다. re.MULTILINE 을 사용할 경우에는 여러 줄의 문자열일 때
# 각 줄의 처음과 일치하게 된다."""
# print(re.search("^Life", "Life is too short")) # <re.Match object; span=(0, 4), match='Life'>
# print(re.search("^Life", "My Life")) # None
# """Life 정규식은 Life 문자열이 처음에 온 경우에는 매치하지만, 처음 위치가 아닌 경우에는 매치
# 되지않는다는 것을 알 수 있다."""






# # $
# """  $ 메타 문자는 ^ 메타 문자와 반대의 경우이다. 
# 즉 $ 메타 문자는 문자열의 끝과 매치한다는 것을 의미한다."""
# print(re.search("short$", "Life is too short")) # <re.Match object; span=(12, 17), match='short'>
# print(re.search("short$", "Life is too short, you need python")) # None
# """ short$ 정규식은 검색 할 문자열이 short으로 끝난 경우에는 매치. 이외의 경우에는 매치X"""




# # \A
# """\A 는 문자열의 처음과 매치한다는 것을 의미
# ^ 문자와 동일한 의미이지만, Re.MULTILINE 옵션을 사용할 경우에는 다르게 해석된다.
# RE.MULTILINE 옵션을 사용할 경우 ^ 은 각 줄의 문자열의 처음과 매치되지만
# \A 는 줄과 상관없이 전체 문자열의 처음하고만 매치된다."""



# # \Z
# """ \Z 는 문자열의 끝과 매치된다는 것을 의미한다. 이것 역시 \A와 동일하게 re.MULTILINE 옵션을 사용할 경우
# $ 메타 문자와는 달리 전체 문자열의 끝과 매치 된다."""


# # \b
# """\b 는 단어 구분자이다
# 보통 단어는 화이트 스페이스에 의해 두분된다.
# 문자를 소비하지않으며 커서가 글자 위를 지나가지않습니다.(소비X) 그저, 조건만 체크합니다"""
# import re
# p = re.compile(r"\bclass\b")
# print(p.search("no class at all")) # <re.Match object; span=(3, 8), match='class'>
# print(p.search("the declassfied algorithm")) # None   # class문자열이 포함되있긴하지만, whitespace로 구분된 문자 아니므로 X
# print(p.search("one subclass is")) # None  # 앞에 sub 문자열이 더해져있어 매치X
# """\b 메타 문자를 사용할 때 주의해야 할 점은 \b는 파이썬 리터럴 규칙에 따르면 백스페이스를 의미하므로
# 백스페이스가 아닌 단어 구분자라는 것을 알려주기 위해 r\bclass\b 처럼 raw string이라는 것을 알려주는 r 을 반드시 붙여야한다"""


# # B
# """\B 메타 문자는 \b 메타 문자와 반대의 경우이다
# 즉 화이트스페이스로 구분된 단어가 아닌 경우에만 매칭 된다"""
# import re
# p = re.compile(r"\Bclass\B")
# print(p.search("no class at all")) # None  # 앞 뒤 화이트스페이스
# print(p.search("the declassified algorithm")) # <re.Match object; span=(6, 11), match='class'>
# print(p.search("one subclass is")) # None   # 앞 뒤에 화이트스페이스가 하나라도 있으면 매치X





# # 그루핑
# """ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다고 가정해보자
# 이 때 필요한 것이 바로 그루핑이다"""
# # (ABC)+
# #그룹을 만들어 주는 메타 문자는 바로 ()이다
# import re

# p = re.compile("(ABC)+")
# m = p.search("ABCABCABC OK?")
# print(m) # <re.Match object; span=(0, 9), match='ABCABCABC'>



# # 이름 + " " + 전화번호 형태의 문자열을 찾는 정규식
# p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
# m = p.search("Quack 010-5135-0630")
# print(m) # <re.Match object; span=(0, 19), match='Quack 010-5135-0630'>


# import re
# p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
# m = p.search("Quack 010-5135-0630")
# print(m.group(1))

# # group(2)에 해당하는 그룹(전화번호) 만들어 출력하기
# import re

# p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
# m = p.search("Quack 010-5135-0630")
# print(m.group(2)) # 010-5135-0630
# """group(index)
# # group(0) 매치 된 전체 문자열
# # group(1) 첫 번째 그룹에 해당되는 문자열
# # group(2) 두 번째 그룹에 해당되는 문자열
# # group(3) n 번째 그룹에 해당되는 문자열"""


# # 지역번호만 출력하도록 그루핑 하기
# import re

# p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("Quack 010-5135-0630")
# print(m.group(3)) # 010




# # 그루핑 된 문자열 재참조하기
# import re
# p = re.compile(r"(\b\w+)\s+\1")
# p.search("Paris in the the spring").group()

# """정규식 (\b\w+)\s+\1 은 (그룹) + " " + 그룹
# 과 동일한 단어와 매치된다는 것을 의미
# 이렇게 정규식을 만들면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다
# 이를 가능하게 하는 것이 재참조 메타 문자인 \1 이다.
# \1 은 정규식 그룹 중 첫 번째 그룹을 가리킨다.두 번째 그룹을 참조하려면 \2를 사용하면 된다"""





# # 그루핑 된 문자열에 이름 붙이기
# """정규식 안에 그룹이 10개 이상이라면, 이에 더해 정규식이 수정되면서 그룹이 추가, 삭제 되면
# 그 그룹을 인덱스로 참조한 프로그램도 모두 변경해 주어야 하는 위험도 갖게 된다

# 만약 그 그룹을 인덱스가 아닌 이름으로 참조할 수 있다면 어떨까?

# 이러한 이유로 정규식은 그룹을 만들 때 그룹 이름을 지정할 수 있게 했다"""

# # (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
# """위 정규식은 앞에서 본 이름과 전화번호를 추출하는 정규식이다. 
# (\w+)라는 그룹 앞에 name 이라는 이름을 붙인 것이다.
# ? 표현식은 정규 표현식의 확장 구문이다.
# 이 확장 구문을 사용하면 가독성이 떨어지긴하지만, 강력함을 가지게 된다.
# 즉 그룹에 이름을 지어주려면 (?P<그룹명>...) """
# # name 이라는 그룹 이름으로 참조
# import re

# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("Quack 010-5135-0630")
# print(m.group("name")) # Quack

# # 그룹 이름을 사용하여 정규식 안에서 재참조
# import re

# p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
# print(p.search("Paris in the the spring").group()) # the the
# # 재참조할 때는 (?P=그룹이름)이라는 확장 구문을 사용해야 한다.







# 전방 탐색
"""정규식에서 사람들이 가장 어려하는 것이 바로 전방탐색이다.
전방 탐색 확장구문. 이 확장 구문을 사용하면 암호문처럼 알아보기 어렵게 바뀌기 때문
꼭 필요한 경우가 있으므로 습득해두자"""
import re

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group()) # http:

"""http: 가 출력되었다. 만약 http 만 출력하고 싶다면? 예는 간단하지만
훨씬 복잡한 정규식이여서 그루핑은 따로 추가할 수 없다는 조건이라고 가정하자"""

# 긍정형 전방 탐색 ((?=...)):...  해당하는 정규식과 매치되어야 하며, 조건이 통과되어도 문자열이 소비X
# 부정형 전방 탐색((?!....)):...  해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열 소비 X

#긍정형 전방 탐색 예
import re

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group()) # http








# 문자열 바꾸기
# blue|white|red 를 Colour 문자열로 치환하기
import re

p = re.compile("(blue|white|red)")
print(p.sub("colour", "blue socks and red shoes")) # colour socks and colour shoes

# 딱 한번만 바꾸고 싶을 땐?
print(p.sub("color", "blue socks and red shoes", count=1)) # color socks and red shoes
"""처음 일치하는 blue만 color 문자열로 치환되었다"""