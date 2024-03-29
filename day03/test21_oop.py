# file : test21_oop.py
# desc : 객체지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person: # 사람 클래스 선언
    name = '' # 멤버변수
    age = 0
    gender = ''


    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할때 동작.
    # init == initialization 초기화
    def __init__(self) -> None:
        self.name = '홍길동'
        self.age = 29
        self.gender = '남자'
    

    # 클래스를 호출할때 원하는 형태로 변환해서 보여줄때
    def __str__(self) -> str:                                   # <__main__.Person object at 0x000001242B397B10> 원래는 이랬잖아
        strs = f'커스텀 출력, 이름: {self.name} 객체 생성!'     # 커스텀 출력, 이름: 홍길동 객체 생성! # 내가 원하는대로 출력
        return strs


    def walk(self): #멤버함수 # 매개변수 self는 필수
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    
# 사람 객체 생성, Instance(사례, 예제)
ij = Person()  # 함수호출처럼 작성하면 됨
es = Person()

# print(type(ij))
# print(type(1))

# print(id(ij)) # 다른 객체인지 확인
# print(id(1))
# print(id(es))

ij.name = '김인제'    # 객체명.멤버변수 = ...
ij.age = 27
ij.gender = '남자'

es.name = '에슐리'
es.age = 40
es.gender = '여자'

print(f'{ij} => 이름:{ij.name} / 나이{ij.age} / 성별:{ij.gender}')
print(f'{ij} => 이름:{es.name} / 나이{es.age} / 성별:{es.gender}')

ij.walk()
print('1분동안 걷는다')
ij.stop()

es.walk()
print('걷기 싫어함')
es.stop()

print('생성자 함수 추가 ------------------------------------------>')
gd = Person()
print(f'gd => 이름:{gd.name} / 나이{gd.age} / 성별:{gd.gender}')
print(gd)