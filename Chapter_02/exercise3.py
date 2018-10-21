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
print(a[0:5])

# 슬라이싱할 때 항상 시작 번호가 '0'일 필요는 없다
print(a[0:2])
print(a[5:7])
print(a[12:17])

# a[시작번호:끝번호] 에서 끝 번호 부분을 생략하면 시작번호부터 그 문자열의 끝까지 뽑아낸다
print(a[19:])

# "Life is too short, You need Python"이라는 문자열에서 단순히 한 문자만을 뽑아내는 것이 아니라#
#'Life' 또는 'You' 같은 단어들을 뽑아내는 방법은?
x = "안녕하세요. 수지입니다!"
y = "Life is too short, You need Python"
z = y[0] + y[1] + y[2] + y[3]
print(z)
print(z[0:4])
print(z[0:3])

# a[시작 번호:끝 번호]를 지정하면 끝 번호에 해당하는 것은 포함X
# a[0:3] -> 0 <= a < 3

print(y[0:4])
print(y[0:5])

# a[4]는 공백 문자이기때문에 'Life '가 출력. 공백문자 역시 L, i, f, e 같은
# 문자와 동일하게 취급

# 슬라이싱할 때 항상 시작 번호가 0 일 필요는 X
print(y[0:2])
print(y[5:7])
print(y[12:17])

# a[시작 번호:끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터
# 그 문자열의 끝까지 뽑아낸다
print(y[19:])
print(x[7:])

# a[시작 번호:끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다
print(y[:17])
print(x[:2])

# a[시작 번호:끝 번호]에서 시작 번호와 끝 번호를 생략하면
# 문자열의 처음부터 끝까지를 뽑아낸다
print(y[:])
print(x[:])

# 슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-) 기호를 사용할 수 있다
print(y[19:-7])
print(x[0:-1])
# y[19:-7] 이 뜻하는 것은 y[19]에서 y[-8]까지를 말한다. y[-7]은 포함되지 않는다.

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20010331Rainy"
year = a[:4]    # 처음부터 a[3]까지
day = a[4:8]    # a[4]부터 a[7]까지
weather = a[8:] # a[8]부터 마지막까지

print("------------------------------")
print(year)
print(day)
print(weather)


# 'Pithon' 이라는 문자열을 'Python'으로 바꾸려면?

print("------------------------------")
a = "Pithon"
print(a[1])

# a[1] = 'y' # 문자열, 튜플 등의 자료형은 그 요소값을 변경할 수 없다. 그래서 immutable한 자료형이라고도 부른다.
# 'Pithon' 을 'Python' 으로 변경하려면 슬라이싱 기법을 이용한다.

a = "Pithon"
print(a[:1])
print(a[2:])

print(a[:1] + 'y' + a[2:])



## 문자열 포매팅


# 1) 숫자 바로 대입
print("I eat %d apples." %3)

# 2) 문자열 바로 대입
print("I eat %s apples." %"five")

# 3) 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." %number)