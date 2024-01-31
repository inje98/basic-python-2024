# file : test24_lotto.py
# desc : 로또번호 생성

import random as rnd # 랜덤은 주로 rnd로 줄여서 많이 쓴다

# numbers = list(range(1,46)) # [i for i in range(1, 46)] 저번엔 이걸로 했었지
# lottery = list() # [] 이랑 같은거, 빈 리스트

# for i in range(6): # 0 ~ 5
#     lottery.append(rnd.choice(numbers)) # 1~45까지 숫자 중 하나를 랜덤 꺼내기


# lottery.sort() # 정렬
# print(lottery)

numbers = weight = list(range(1,46))
lottery = list()
rnd.shuffle(weight) # 가중치로 섞음

lottery = rnd.choices(numbers, weights = weight, k = 6) # 가중치로 한꺼번에 여섯개
lottery.sort()
print(lottery)