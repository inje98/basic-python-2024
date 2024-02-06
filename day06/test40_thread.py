# file : test40_Thread.py
# desc : Qt 스레드로 동작

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기 위한 변수객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent # BackWorker에서 사용할 멤버변수

    def run(self) -> None:  # 스레드 실행  # QThread에선 UI관련된 처리를 할 수 없음
        # 스레드로 동작할 내용
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        ### self.parent.pgbTask.setValue(0)
        ### self.parent.pgbTask.setRange(1, maxVal)
        for i in range(maxVal): #0~100까지
            print_str = f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            ### self.parent.txbLog.append(print_str)
            ### self.parent.pgbTask.setValue(i)

class qtwin_exam(QWidget):  # QWidget을 [상속] 받을거야. QWidget이 가진 모든것을 사용할 수 있다
                            # UI 쓰레드
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) #Qt디자이너에서 만든 ui를 로드
        # 버튼에 대한 시그널처리

        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내에 있는 위젯접근은 VSCode 상에서 생상으로 표시X

    def btnStartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxblog) # TextBrowser 위젯에 진행사항 출력

    # 부모의 CloseEvent는 그냥 닫히기 때문에 재정의
    # QWidget에 있는 CloseEvent를 그래도 쓰면 그냥 닫힘
    # 닫을지 말지를 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
    def closeEvent(self, QCloseEvent) -> None: # x버튼 종료확인
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 슬롯함수
    @pyqtSlot(int) # self.initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)

    @pyqtSlot(str) # self.setLog.emit() 동작해서 실행
    def setTxblog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int) # BackWorker 스레드에서 self.Setignalemit() 동작해서 실행
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

if __name__ == '__main__':
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성할거야
    instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
    instance.show()
    loop.exec_()
