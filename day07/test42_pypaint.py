# file : test42_pypaint.py
# desc : 그림판 만들기

import sys
from PyQt5 import uic  # QtDesigner 호출 시 필요
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self): # 화면 초기화
        # uic.loadUi('./day07/pyPaint.ui', self)  # 실행파일 생성시는 경로에 상대경로가 엇어져야 함
        uic.loadUi('C:/sources/basic-python-2024/day07/pyPaint.ui', self)     # pyinstaller --onefile .\test42_pypaint.py 터미널에 이거 쳐서 실행파일 생성 # dist파일에 있음
                                                                              # pyinstaller -w -F .\test42_pypaint.py 이게 더 나은 방법인듯
        # self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowIcon(QIcon('C:/sources/basic-python-2024/day07/iot.png'))

        self.setWindowTitle('Py그림판')
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')

        self.setCenter()
        self.show()

    def initSignal(self): # 동작 초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)

        
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)


    def btnLoadClicked(self):
        image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
        imagePath = image[0]
        # print(imagePath)
        pixmap = QPixmap(imagePath).scaledToHeight(381) # 파일 경로에 있는 이미지를 읽어서 pixmap객체에 담기
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 라벨 사이즈로 조정

    
    def btnSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
        # print(filePath)
        if filePath == '': return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)
    
    # 반복되는 부분이 있어서 함수 하나로
    def buttonClicked(self): # black red, blue 를 다 통일한 함수
        btn_val = self.sender().objectName()
        print(btn_val)
        if btn_val == 'btn_black': # 검은버튼 클릭
            self.brushColor = Qt.black

        elif btn_val == 'btn_red': # 빨간버튼 클릭
            self.brushColor = Qt.red

        elif btn_val == 'btn_blue': # 파란버튼 클릭
            self.brushColor = Qt.blue

        elif btn_val == 'btn_clear':
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)
            
    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap())
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap)) # RoundCap: 끝에 둥굴게
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 업데이트

    


    def setCenter(self): # 화면 정중앙에 위치
        gm = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center() 
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_()) # 종료시 리소스 반환 등 효율을 위해(sys.exit) 