# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yutnori01.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


# 맨 처음 화면 Display
# Start 버튼을 누르면 플레이어의 정보를 입력받는 playerinfo.py의 클래스가 수행되고
# Exit을 누르면 게임 화면이 종료되게!
# @Yeomin

from PyQt5 import QtCore, QtGui, QtWidgets # PyqT5를 사용하기 위한 라이브러리
from PyQt5.QtCore import QCoreApplication #Pyqt에서 창을 종료하는 함수를 실행하기 위한 라이브러리
from PlayerInfoScreen import UI_Dialog_02 as pi     # 띄워진 창을 바꾸기 위해 두번째 씬인 PlayerInfoScreen을 임포트
import myres_rc
import sys

class UI_Dialog_01(object):

    def ChangeUI(self):                                     # 한 윈도우창에서 다른 윈도우창을 띄울 때 사용할 함수
        self.app = QtWidgets.QApplication(sys.argv)         #윈도우 창을 띄우기 위함
        self.Dialog = QtWidgets.QDialog()                   # Dialog(윈도우 창이라고 생각하면 됨)을 사용하기 위함
        t = pi()                                            # PlayerInfoScreen 객체 선언
        self.ui = t                                         # ui에 해당 클래스(PlayerInfoScreen의 UI_Dialog_02)를 연결
        self.ui.setupUi(self.Dialog) # 해당 ui의 setupUi함수를 실행 -
        #Dialog.hide()                                      # 현재 창을 지움 -> 이건 현재 클래스에서 프로그램을 돌릴 때는 실행되는데, 없으면 실행이 안되어서 막아둠(Controller에서 돌릴 것이기 때문)
        self.Dialog.show()                                  # 새로운 창을 띄움


    def setupUi(self, Dialog):
        Dialog.setObjectName("YutNori")                             # Dialog의 이름 , 변경시 해당 이름으로 접근 , Dialog는 우리가 보는 윈도우 창이라고 생각하면 됨
        Dialog.resize(1020, 800)                                    # 화면 크기 1020*800

        # 윷놀이 이름 쓰기 위한 label
        self.label = QtWidgets.QLabel(Dialog)                       # Qt위젯 중 label을 사용(Dialog에 붙여서)
        self.label.setGeometry(QtCore.QRect(360, 60, 291, 121))     # 해당 label 크기
        font = QtGui.QFont()                                        # 아래 세 줄은 폰트 변경 선언
        font.setFamily("배달의민족 주아")                            # 글씨체 설정
        font.setPointSize(72)                                       # 폰트 크기
        self.label.setFont(font)                                    # 변경 내용 적용
        self.label.setObjectName("YutNori_Sub")                     # 윷놀이 이름 넣기 위해 label 생성하여 dialog에 붙임

        # start 버튼
        self.start = QtWidgets.QPushButton(Dialog)                  # Start버튼
        self.start.setGeometry(QtCore.QRect(230, 600, 191, 71))     # Start버튼의 크기 조절 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        self.start.clicked.connect(self.ChangeUI)                   # Start버튼을 눌렀을 때 ChangeUI함수 실행 - PlayerInfoScreen으로 전환
        font = QtGui.QFont()                                        # 폰트 변경
        font.setFamily("배달의민족 주아")                            # 글씨체 설정
        font.setPointSize(28)                                       # 폰트 크기 설정
        self.start.setFont(font)                                    # 변경 내용 적용
        self.start.setObjectName("start")                           # 해당 버튼의 이름

        # Exit버튼
        self.Exit = QtWidgets.QPushButton(Dialog)                      # Exit버튼
        self.Exit.setGeometry(QtCore.QRect(580, 600, 191, 71))         # Exit버튼 크기 설정 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        self.Exit.clicked.connect(QCoreApplication.instance().quit)    # Exit버튼을 누르면 윈도우 창이 종료된다
        font = QtGui.QFont()                                           # 폰트 설정 선언
        font.setFamily("배달의민족 주아")                               # 글씨체 설정
        font.setPointSize(28)                                          # 폰트 크기
        self.Exit.setFont(font)                                        # 변경 내용 적용
        self.Exit.setObjectName("Exit")                                # 해당 버튼의 이름

        # 윷놀이 가족 그림
        self.label_2 = QtWidgets.QLabel(Dialog)                         # 윷놀이하는 가족 그림을 넣기 위한 lable
        self.label_2.setGeometry(QtCore.QRect(230, 200, 541, 381))      # 가족 그림 위치 및 크기 설정 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        self.label_2.setObjectName("label_2")                           # 해당 버튼의 이름

        # 그래픽 뷰 - 배경 화면 흰색으로 하기 위하여 (실은 배경화면 흰색으로 하는 코드를 몰라서 그래픽 뷰-디폴트 흰색-으로 배경을 덮음)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)                 # Qt위젯 중 그래픽뷰 사용을 선언
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1020, 800))        # 그래픽 뷰 위치 및 크기 설정 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        self.graphicsView.setObjectName("graphicsView")                     # 해당 뷰의 이름

        # 여태까지 만든 위젯들(버튼 , label, graphicsView)등을 위로 올림 , 뒤늦게 raise한 것이 맨 위에 있다
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.start.raise_()
        self.Exit.raise_()


        self.retranslateUi(Dialog)                                  # Dialog의 위젯들(label, 버튼 등)에 글씨 및 그림을 넣는 함수 실행
        QtCore.QMetaObject.connectSlotsByName(Dialog)               # 설정한 이름과 위젯들을 연결


    # Dialog의 위젯들(label, 버튼 등)에 글씨 및 그림을 넣음
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "YutNoriGame!!!"))
        self.label.setText(_translate("Dialog", "윷놀이"))
        self.start.setText(_translate("Dialog", "START"))
        self.Exit.setText(_translate("Dialog", "EXIT"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/yutnori_fam.jpg\"/></p></body></html>"))



if __name__ == "__main__":
    import sys                              # sys임포트 , 맨 위에 선언해줘도 문제 없음
    app = QtWidgets.QApplication(sys.argv)  # 윈도우 창을 띄우기 위한 함수
    Dialog = QtWidgets.QDialog()            # 그 중 Dialog를 쓴다
    ui = UI_Dialog_01()                     # ui에 ui 클래스를 붙인다 (여기에서는 FirstScreen의 클래스)
    ui.setupUi(Dialog)                      # 클래스의 setupUI를 Dialog를 넣어 실행한다
    Dialog.show()                           # Dialog를 화면에 띄운다
    sys.exit(app.exec_())