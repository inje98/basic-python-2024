# file : test15_output.py
# desc : 콘솔 출력 포맷양식
    
# print(10)
# print('10')  # 둘 다 출력되는건 문자임

string_1 = '{}'.format(10) # {} 위치에 함수 뒤에 값을 치환, 원하는 양식으로 표현
print(type(string_1))
print(string_1)

name = '김인제' # name = input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다.!'. format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000, '만', '빌려주세요')
print(string_3)

# 정수를 문자열 포맷
string_4 = '_____{:05d}_____'.format(100)  ##### 빈자리 0으로 채우기 # 이런 경우는 정말 많이 쓰인다. ######
print(string_4)

string_4 = '_____{:d}_____'.format(100)
print(string_4)

string_4 = '_____{:5d}_____'.format(1000)
print(string_4)

string_4 = '_____{:5d}_____'.format(100)
print(string_4)

string_4 = '_____{:+05d}_____'.format(-100)
print(string_4)

# = : 기호와 숫자를 분리, 05 : 다섯자리 만들때 빈자리 0으로 채우기, d : 정수

string_4 = '_____{:=10d}_____'.format(-100)
print(string_4)


print('\n\n\n\n ------------------- 실수 포맷 --------------------------\n\n\n\n')
# 실수 문자열포맷
string_5 = '_____{}_____'.format(78.33333333333333)
print(string_5)

string_5 = '_____{:.2f}_____'.format(78.33333333333333)
print(string_5)

string_5 = '_____{:7.2f}_____'.format(78.33333333333333) # 7은 총 자릿수 2는 소숫점 자릿수        #### 이것도 많이 쓰임 ####
print(string_5)

string_5 = '_____{:15f}_____'.format(78.33333333333333)
print(string_5)


print('\n\n\n')


# 파이썬 3.6이후에 도입. format() 함수를 아예 사용안함
val = 78.3333333
string_6 = f'_____{val:7.2f}_____'
print(string_6)


string_7 = 'Hello, World'
print(string_7.upper()) # upper case 대문자변환
print(string_7.lower()) # lower 모두 소문자변환
print(string_7.lower().capitalize()) # 첫글자만 대문자

print(string_7.split(' ')) # 특정한 단어로 자르는 함수, 리스트로


string_8 = 'Hello, I am IJ Kim. I am a student. Good Luck for tour day.'
words = string_8.split(' ')
print(words)
print(f'문장의 단어 갯수는 {len(words)}개 입니다.')


## is 시리즈 : isalnum이면 알파벳숫자로 돼있니? isupper면 다 대문자로 돼있니? 이런 느낌임.ok?
string_9 = 'A10'
print(string_9.isalnum()) # True     

string_9 = '+A10'
print(string_9.isalnum()) # True 

print(string_9.isnumeric()) # False 숫자만 있지 않으니까

print('안냥' in '안녕하세요') # False # 문장안에 단어가 있는지 확인






