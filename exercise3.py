# 2.자료형
# 문자열 자료형

# 문자열 인덱싱과 슬라이싱
# 인덱싱(Indexing) : 무엇인가를 '가리킨다'
# 슬라이싱(Slicing) : 무엇인가를 '잘라낸다'

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3]) # a[3]은 a라는 문자열의 네 번째 문자인 e를 말한다

# 파이썬은 0부터 숫자를 센다
# a[번호]는 문자열 내 특정한 값을 뽑아내는 역할을 한다. 이러한 것을 인덱싱이라고 한다

# 문자열 인덱싱 활용
a = "Life is too short, You need Python"
print(a[0])
print(a[12])
print(a[13])
print(a[-1]) # a[-1]은 뒤에서부터 세어 첫 번째가 되는 문자를 말한다

print(a[-0]) # 0과 -0은 똑같은 것이기 때문에 a[-0]은 a[0]과 똑같은 값을 보여준다
print(a[-2])
print(a[-5])
print("=" * 50)

# "Life is too short, You need Python"이라는 문자열에서 'Life' 또는 'You' 같은 단어들을 뽑아내는 방법
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

# 문자열 슬라이싱
a = "Life is too short, You need Python"
print(a[0:4])
print(a[0:3])
a = "안녕하세요! 윤영입니다. 저는 멋진 풀스택 개발자가 되고 싶습니다."
print(a[0:5])

# a[시작번호:끝번호]를 지정하면 끝 번호에 해당하는 것은 포함되지 않는다
# a[0:3] 0 <= a < 3
a = "Life is too short, You need Python"
print(a[0:5])

# 슬라이싱할 때 항상 시작 번호가 '0'일 필요는 없다
print(a[0:2])
print(a[5:7])
print(a[12:17])

# a[시작번호:끝번호] 에서 끝 번호 부분을 생략하면 시작번호부터 그 문자열의 끝까지 뽑아낸다
print(a[19:])



