# desc : 복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60

# 총 갯수가 10(n)이면 인덱스의 마지막 값은 9(n-1)
# index =   0   1   2    3   4   5   6   7   8   9
std =      [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]

print(std[5])

list_1 = [256, 3.5, '문자열', True, [1,2,3,4], (1,2,3,4), std] # 다 들어갈 수 있다
print(list_1)
print(list_1[5])

list_1[6] = '바꾼값'
print(list_1)

## 리스트 연산
print(list_1[2:4]) # :뒤의 수는 출력하고 싶은 인덱스 +1

print(list_1[-1])  # 마이너스 인덱스
print(list_1[-7:-5])

## 이중 리스트
print(list_1[4][2]) # [1,2,3,4] 중 3 가져오기

list_2 = [[1,2,3], [4,5,6], [7,8,9]]
print(list_2[1][2]) # 6


## 리스트 연산 + *만 사용가능
list_3 = [1,2,3]
list_4 = [7,8,9]
print(list_3 + list_4) # 리스트 연결
print(list_4 * 5) # 리스트 반복

## 리스트 길이
print(len(std))

## append() 리스트 마지막에 하나 추가
## insert(index, val) 리스트의 index 이후에 val 추가
print(list_1)
list_1.append('Hello!')
print(list_1)

list_1.insert(2, 100) # list_1[2]에 100 추가 (교체가 아님, 원래 값은 뒤로 밀림, 영어 뜻이 삽입이잖어)
print(list_1)

## extend() 기존 리스트 확장
list_3.extend(list_4)
print(list_3)

list_3.extend('4')
print(list_3)

list_3.extend([2,3])  # extend(4) 이렇게 숫자는 안들어가네..? 리스트, 문자열은 들어가는데
print(list_3)

## 리스트 삭제
del list_4[2] # 리스트 2번 인덱스 삭제
print(list_4)

del list_4 # 리스트 자체를 삭제

print(list_3)
val = list_3.pop() # 마지막 값을 꺼내오기
print(val)
print(list_3) # 끝에 값 없어졌다

val = list_3.pop(2) # list_3[2] 꺼내오기
print(val)
print(list_3)

## clear()
list_3.clear()  # del은 완전삭제 print도 안됨. clear()은 내용만 삭제
print(list_3) # 빈 리스트가 나온다

# sort() # 정렬
print(list_1)
# list_1.sort() # 문자열, 숫자, 불 섞여있는 리스트는 정렬 안됨

std.sort() # 오름차순 정렬
print(std)
std.sort(reverse = True) # 내림차순 정력
print(std)

# in, not in
print(99 in std) # True
print(98 in std) # False

# reverse(), copy(), count() ...
# *리스트 : 전개연산자
list_a = [1, 3, 5]
list_b = [2, 4, 8]
list_c = [*list_a, *list_b] # 리스트 안에 리스트 내용물을 넣는거지  # 거의 안쓰긴 하는듯
print(list_c)

list_d = [list_a, list_b] # 리스트 안에 리스트 넣기지
print(list_d)