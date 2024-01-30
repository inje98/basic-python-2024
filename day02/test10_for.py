# file : test10_for.py
# desc : for 반복문

std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]
kor_sum = 0
for i in std:
    kor_sum = kor_sum + i

print(kor_sum)
print(kor_sum / len(std)) # 리스트의 길이로 처리하면 소스를 다시 수정할 필요X

list_a = [[1,3,5], [2,4,8],[10,15,20]]

for in_list in list_a:
    print(in_list)

for in_list in list_a:
    for item in in_list:
        print(item)