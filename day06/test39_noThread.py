# date : 20240205
# file : test39_noThread.py
# desc : Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# print(sys.argv) # 현재 파이썬파일의 경로

class qtwin_exam(QWidget):  # QWidget을 [상속] 받을거야. QWidget이 가진 모든것을 사용할 수 있다

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) #Qt디자이너에서 만든 ui를 로드
        # 버튼에 대한 시그널처리

        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내에 있는 위젯접근은 VSCode 상에서 생상으로 표시X

    def btnStartClicked(self):
        maxVal = 1000000
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) # 프로그래스바 0부터 시작
        self.pgbTask.setRange(1, maxVal-1) # 0~100까지
        for i in range(maxVal): #0~100까지
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txbLog.append(print_str)
            self.pgbTask.setValue(i)
    
    def closeEvent(self, QCloseEvent) -> None: # x버튼 종료확인
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성할거야
    instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
    instance.show()
    loop.exec_()

