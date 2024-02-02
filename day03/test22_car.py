# file : test22_car.py
# desc : Car 클래스 만들기

class Car:
    wheel_num = 4
    color = 'white'
    __plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다.')

    def moveLeft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def moveBackRight(self):
        print(f'{self.__plate_num}이 우회전합니다.')

    def __init__(self, plate_num, company, color, gear_type) -> None:    # wheel_num은 4고정이니까 여기다 안적음
        self.__plate_num = plate_num
        self.company = company
        self.color = color
        self.gear_type = gear_type

    def __str__(self) -> str:
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다.'  # print(객체명) 딱 찍었을때 이상한 주소명 비스무리한거 안뜨고 이렇게 나오게끔

    def getPlateNumber(self):
        return self.__plate_num
    
    def setPlateNumber(self, new_plateNumber):
        self.__plate_num = new_plateNumber
        return self.__plate_num

sarah = Car('32더 0564', '기아', '검정', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차번호는 {sarah.getPlateNumber()}')
print(f'차색상은 {sarah.color}')

csuv = Car('경남88 1234', '현대', '흰색', '자동')
print(f'차번호는 {csuv.getPlateNumber()}')
print(csuv)

csuv.setPlateNumber('123러 1234')     # __plate_num 이렇게 __쓰는 이유가 클래스 밖에서 값 못바꾸게 하는거잖아
                                      # 클래스 안에서 setPlateNumber() 함수 만들어서 클래스 안에서 값 바꾸는거인듯
print(csuv)

