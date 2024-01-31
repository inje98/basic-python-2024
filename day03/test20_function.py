# file : test20_function.py
# desc : 함수(계산기)

def add(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result

def multi(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y
    return result

def say_hello() -> None:
    print('Hello')
    # return None 은 생략된거임. 같은거임.

print('더하기 ->')
a, b = map(int, input('두 정수 입력 > ').split(' '))
결과 = add(a,b) # 리턴은 함수 결과값으로 바뀐다!
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a, b)}')
print(f'{a} x {b} = {multi(a, b)}')
print(f'{a} ÷ {b} = {divide(a, b)}')

say_hello()

# 객체를 나타내는 명사 = 변수
# 객체를 나타내는 동사 = 함수
# 변수 + 함수 = 클래스