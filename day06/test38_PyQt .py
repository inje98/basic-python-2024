# date : 20240205
# file : test38_PyQt.py
# desc : Qt디자이너 만든 ui와 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# print(sys.argv) # 현재 파이썬파일의 경로

class qtwin_exam(QWidget):  # QWidget을 [상속] 받을거야. QWidget이 가진 모든것을 사용할 수 있다

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui', self) #Qt디자이너에서 만든 ui를 로드
        # 버튼에 대한 시그널처리

        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내에 있는 위젯접근은 VSCode 상에서 생상으로 표시X
        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblStatus.setText('상태 : 동작시작')
        QMessageBox.about(self, '동작', '***시스템이 시작되었습니다.')

    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblStatus.setText('상태 : 동작중지')



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

