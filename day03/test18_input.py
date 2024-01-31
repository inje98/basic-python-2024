# file : test18_input.py
# desc : 다중입력...
# 원래는 튜플형(in_a, in_b)으로 데이터 받는게 정석 -> 생략


# input_a, input_b = input('값을 두개 입력 > ').split(' ')
# input_a = int(input_a)
# input_b = int(input_b)
input_a, input_b = map(int, input('값을 두개 입력(공백으로 구분) > ').split(' '))


print(f'입력값 {input_a}, {input_b}') # 2개 입력이면 2개 받아야됨. 1개만 받으면 오류남
print(f'더하기 결과 {input_a + input_b}')