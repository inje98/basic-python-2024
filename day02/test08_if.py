#desc : 홀/짝 구분

number = int(input('정수입력 > ')) # 입력 받은 후 정수로 변경

if number % 2 == 0:
    print('짝수')
else:
    print('홀수')


if number % 5 == 0:     # %는 홀짝, 배수때문에 꽤 쓰이는듯
    print('5의 배수')
else:
    pass   