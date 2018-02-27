## 2.자료형

# 문자열 자료형: 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합
# 파이썬에서 문자열을 만드는 방법은 총 4 가지

# 1.큰 따옴표(")로 양쪽 둘러싸기
print("Hello World")
print("Python Programming")

# 2.작은 따옴표(')로 양쪽 둘러싸기
print('Python is fun')
print('My name is Yun Young')

# 3.큰 따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")
print("""2020년 동계올림픽은 일본 도쿄에서 보자""")

# 4.작은 따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')
print('''파이썬에서 문자열을 만드는 방법은 4가지가 있습니다''')


## 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 때
# 1. 문자열 안에 작은 따옴표(') 포함시키기
food = "Python's favorite food is perl"
print(food)

str = "우리집 강아지가 짖었다 '멍멍'"
print(str)

# 2. 문자열에 큰 따옴표(") 포함시키기
say = '"Python is very easy." he says.'
print(say)
say = '"안녕하세요!" 그는 나의 어머니에게 인사를 했다'
print(say)

# 3. \(백슬래시)를 이용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
print(food)
say = "\"Python is very easy.\" he says."
print(say)

book = 'This is Yun Young\'s book'
print(book)
say = "\"안녕하세요\""
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1.줄을 바꾸기 위한 이스케이프 코드 '＼n' 삽입하기
multiline1 = "Life is too short\nYou need python"
print(multiline1)

multilne2 = "안녕하세요\n저는 한국에서 왔습니다."
print(multilne2)

# 2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용
multiline3 = '''
Life is too short
You need python 
hello world
'''
print(multiline3)
multiline4 = '''
올해 여행가고 싶은 국가
유럽
대만
중국 베이징
일본 도쿄
'''
print(multiline4)
multilne5 = """
Life is too short
You need python
"""
print(multilne5)
multiline6 = """
국내여행지
1.경주
2.전주
3.강원도
4.제주도
"""
print(multiline6)

# 문자열 연산하기
# 파이썬에서는 문자열을 더하거나 곱할 수 있다

# 1. 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)

head = "주미야"
tail = " 사랑해"
print(head + tail)

# 2. 문자열 곱하기
a = "python"
print(a * 2)

b = "사랑해"
print(b * 3)

# 3. 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)