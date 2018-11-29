### 문자열 관련 함수들

# 복소수에 관련된 내장 함수가 있는 것과 마찬가지로 문자열 자료형 역시
# 자체적으로 가지고 있는 관련 함수들이 몇 개 있다.
# 그것들을 사용하려면 문자열 변수 이름 뒤에 '.'를 붙인 다음에 함수 이름을 써주면 된다.

# 문자 개수 세기(count)
a = "hobby"
print(a.count('b')) # 문자열 중 문자 b의 개수를 반환

# 위치 알려주기1 (find)
a = "Python is best choice"
print(a.find('b'))  # 파이썬은 숫자를 0부터 세기 떄문에 b의 위치는 11 이 아닌 10 이 된다
print(a.find('k'))

# 위치 알려주기2 (index)
a = "Life is too short"
print(a.index('t'))
# print(a.index('k'))  # 앞의 find 함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다는 점이다

# 문자열 삽입 (join)
a = ","
print(a.join('abcd'))

b = ","
print(b.join('사랑해'))


# 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())
b = "HI"
print(b.upper())
c = "i love girls"
print(c.upper())


# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())

b = "OH MY GOD"
print(b.lower())


# 왼쪽 공백 지우기 (lstrip)

a = "  hi"
print(a.lstrip())

b = "   안녕하세요!"
print(b.lstrip())


# 오른쪽 공백 지우기
a = "hi  "
print(a.rstrip())

b = "반갑습네다!   "
print(b.rstrip())


# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())
b = "  양쪽 공백 지우기  "
print(b.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

