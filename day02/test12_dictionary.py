# file : test12_dictionary.py
# desc : 복합자료형 딕셔너리

## 사전형 key와 value 쌍을 나열해 놓은 자료형
## {key : vlaue, key : value, key : value }

dict_movie = {'name' : '어벤져스 엔드게임', 'type' : '히어로 무비', 'year' : 2019, 'director' : ['안소니 루소', '조 루소'], 
              'cast' : ['아이언맨', '타노스', '헐크', '토르', '닥터스트레인지']}

# 조회
print(dict_movie['name'])
print(dict_movie['type'])
print(dict_movie['cast'])

# 추가, 조회
dict_movie['year'] = 2020
print(dict_movie)

dict_movie['producer'] = '케빈 파이기'
print(dict_movie)

if 'musician' in dict_movie:       # 딕셔너리에 키가 있는지 확인할 때 if문 이렇게 쓰면 됨 musician 없으니까 else로 가지
    print(dict_movie['musician'])
else:
    print('제작자 없음')

musician = dict_movie.get('musician')
print(musician) # musician 키 없으니까 None이 나온다. 오류가 나오진 않네
# print(dict_movie['musician']) # 이건 오류임
print('반복문 출력 --------------------------------------------------')
# 반복문으로 출력
for key in dict_movie:
    print(key, ':', dict_movie[key])

print('반복문 다른방법-----------------------------------------------')
for key, value in dict_movie.items():
    print(key, ':', value)
    