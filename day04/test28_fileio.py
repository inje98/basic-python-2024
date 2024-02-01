# file : test28_fileio.py
# desc : 텍스트 파일 입출력

# mode = a(append : 내용추가), r(read : 파일읽기), w(write : 파일쓰기)
# encoding : cp949(euc-kr : 한글), utf-8(만국공통어)
# f = open(r'C:\sources\basic-python-2024\day04\sample.txt', mode = 'a', encoding = 'utf-8')
f = open(r'.\day04\sample.txt', mode = 'a', encoding = 'utf-8') # r : 원래 \는 \\써야 되는데 그 역할 해주는거임


f.write('안녕하세요. 우리는 IoT 개발자 과정입니다.\n') # mode = a, w 일때만 write
                                                       # 엔터 \n

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다.')