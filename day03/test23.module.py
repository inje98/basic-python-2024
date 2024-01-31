# file : test23.module.py
# desc : 모듈 사용

import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')
# print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'cos(0) = {math.cos(0)}')

print(2 ** 10)
print(math.pow(2,10))

print(math.ceil(3.1))  # 올림
print(math.floor(3.1)) # 내림
print(round(3.5)) # 반올림(너무 많이 사용하니까 기본함수, math가 아님)

import math as m # 별명짓기
print(m.sin(1))


from math import pow, sin  # 조심해서 사용해야 함 # 굳이 쓰는 이유는 최적화때문
print(sin(0))
print(pow(2,10))