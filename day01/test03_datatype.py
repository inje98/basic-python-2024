# date : 20240129
# desc : 자료형

## 기본자료형 - 숫자형, 문자형, 불형, None형...
## 복함자료형 - 리스트형, 튜플형, 딕셔너리, 집합...

## None형 == null(C, C++, C#, Java, SQL)
## 값은 값인데 아무것도 지정할 수 없는 값 => None

apple = None
print(apple)

##숫자형 - 정수형 실수형 진수형
### 정수
ten = 10
hundred = 100
temp = -8

### 실수
pi = 3.141592
tax_rate = 10.0
emp_earn_rate = 3.3
test_val = 2e10 # 2의 10승
print(test_val)

### 진수
bit8 = 0b100001110  # 2진수
oct9 = 0o11         # 8진수
hex255 = 0xFF       #16진수
print(bit8)
print(oct9)
print(hex255)

##문자형 - 파이썬에는 문자, 문자열 차이가 없음
greeting = 'Hello!'
greeting = "Hello!"  # 둘 다 모두 문자열을 나타냄

multi_str = '''Hello
I am a programmer.
Have a good afternoon.'''    # 여러줄, 이것도 홑따옴표 쌍따옴표 같음
print(multi_str)

multi_str2 = ('Line1\n'
              'Line2\n'
              'Line3\n')
print(multi_str2)

multi_str3 = 'Line1\n' \
             'Line2\n' \
             'Line3'         #str2랑 완전 같은거임 편한걸로 하자
print(multi_str3)

## 불형(Bool, Boolean)
isCheck = False
print(isCheck)

answer = (3 == 7)
print(answer)
answer = (3.0 == 3)
print(answer)

## 자료형이 어떤 타입인지 체크
print(type(apple))
print(type(hundred))
print(type(test_val))
print(type(hex255))
print(type(greeting))
print(type(isCheck))
