# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playerinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


# 플레이어의 정보를 입력받는 UI
# 플레이어 명수(2~4) , 말의 갯수 (2~5) , 플레이어 이름을 입력할 수 있게!
# @Yeomin

from PyQt5 import QtCore, QtGui, QtWidgets # PyqT5를 사용하기 위한 라이브러리
from PyQt5.QtCore import QCoreApplication # PyqT5를 사용하기 위한 라이브러리 2
from GamePlayingScreen import UI_Dialog_03 as gp # GamePlayingScreen을 임포트
import sys
import myres_rc

class UI_Dialog_02(object):

    def ChangeUI2(self):                                               # 한 UI에서 다른 UI띄울 때 사용할 함수
        self.app = QtWidgets.QApplication(sys.argv)                    #윈도우 창을 띄우기 위함
        self.Dialog = QtWidgets.QDialog()                              # Dialog(윈도우 창이라고 생각하면 됨)을 사용하기 위함
        a = gp(self.PlayerNum.value(), self.Player1_PieceNum.value(),self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text())                                                       # GamePlayingScreen 객체 선언
        self.ui = a                                                    # ui에 해당 클래스( GamePlayingScreend의 UI_Dialog_023)를 연결
        self.ui.setupUi(self.Dialog)                                   # 해당 ui의 setupUi함수를 실행 -
        #Dialog.hide()
        self.Dialog.show()             

    def setupUi(self, Dialog):
        Dialog.setObjectName("PlayerInfo")             #Dialog의 이름 , 변경시 해당 이름으로 접근 , Dialog는 우리가 보는 윈도우 창이라고 생각하면 됨
        Dialog.resize(1020, 800)                                                # 화면크기 1020*800

        # 플레이어01
        self.Playerinfo = QtWidgets.QLabel(Dialog)
        self.Playerinfo.setGeometry(QtCore.QRect(130, 330, 211, 51))         #해당 label 크기
        font = QtGui.QFont()                                                 # 아래 세 줄은 폰트 설정 변경 선언
        font.setFamily("배달의민족 주아")                                     #글씨체 설정
        font.setPointSize(28)                                                #글씨크키 설정
        self.Playerinfo.setFont(font)
        self.Playerinfo.setObjectName("Playerinfo")

        # 플레이어02
        self.Playerinfo_2 = QtWidgets.QLabel(Dialog)
        self.Playerinfo_2.setGeometry(QtCore.QRect(130, 420, 211, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.Playerinfo_2.setFont(font)
        self.Playerinfo_2.setObjectName("Playerinfo_2")

        # 플레이어03
        self.Playerinfo_3 = QtWidgets.QLabel(Dialog)
        self.Playerinfo_3.setGeometry(QtCore.QRect(130, 520, 211, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.Playerinfo_3.setFont(font)
        self.Playerinfo_3.setObjectName("Playerinfo_3")

        # 플레이어04
        self.Playerinfo_4 = QtWidgets.QLabel(Dialog)
        self.Playerinfo_4.setGeometry(QtCore.QRect(130, 610, 221, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.Playerinfo_4.setFont(font)
        self.Playerinfo_4.setObjectName("Playerinfo_4")

        # 플레이어 정보 입력
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 50, 561, 101))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 배경색 흰색으로 하기 위해 넣은 그래픽 뷰
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1021, 821))
        self.graphicsView.setObjectName("graphicsView")

        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(410, 330, 261, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.lineEdit.setFont(font)                                           # 첫번째 플레이어의 이름 입력하는 UI
        self.lineEdit.setObjectName("PlayerInfo01")


        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)                        #String 입력을 위한 LineEditer
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 420, 261, 51))         #String 입력을 위한 LineEditer 크기 설정
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.lineEdit_2.setFont(font)                                           # 두번째 플레이어의 이름 입력하는 UI
        self.lineEdit_2.setObjectName("PlayerInfo02")


        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 520, 261, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.lineEdit_3.setFont(font)                                         # 세번째 플레이어의 이름 입력하는 UI
        self.lineEdit_3.setObjectName("PlayerInfo03")


        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 610, 261, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.lineEdit_4.setFont(font)                                        # 세번째 플레이어의 이름 입력하는 UI
        self.lineEdit_4.setObjectName("PlayerInfo04")
        

        self.label_2 = QtWidgets.QLabel(Dialog)                # 그림02 - 오른쪽 아래의 윷놀이하는 가족 그림
        self.label_2.setGeometry(QtCore.QRect(530, 460, 521, 361))
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 341, 171))
        self.label_3.setMinimumSize(QtCore.QSize(341, 0))
        self.label_3.setMaximumSize(QtCore.QSize(341, 16777215))
        self.label_3.setObjectName("label_3")                          # 그림01 - 왼쪽 위의 윷놀이 그림


        self.GameStart = QtWidgets.QPushButton(Dialog)
        self.GameStart.setGeometry(QtCore.QRect(130, 700, 181, 61))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.GameStart.setFont(font)                                     # 게임 시작 버튼
        self.GameStart.setObjectName("GameStart")
        self.GameStart.clicked.connect(self.ChangeUI2)


        self.Player1_PieceNum = QtWidgets.QSpinBox(Dialog)              # 말의 갯수 선택할 수 있는 UI
        self.Player1_PieceNum.setGeometry(QtCore.QRect(720, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        self.Player1_PieceNum.setFont(font)
        self.Player1_PieceNum.setMinimum(2)
        self.Player1_PieceNum.setMaximum(5)
        self.Player1_PieceNum.setObjectName("Player1_PieceNum")
    


        self.ExitBtn = QtWidgets.QPushButton(Dialog)                   #게임 종료버튼
        self.ExitBtn.setGeometry(QtCore.QRect(370, 700, 181, 61))
        self.ExitBtn.clicked.connect(QCoreApplication.instance().quit)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.ExitBtn.setFont(font)
        self.ExitBtn.setObjectName("ExitBtn")


        self.PieceNum = QtWidgets.QLabel(Dialog)
        self.PieceNum.setGeometry(QtCore.QRect(520, 190, 141, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(24)
        self.PieceNum.setFont(font)                                 # "말의 갯수" - 글씨 -> 안건드려도 됨!
        self.PieceNum.setObjectName("PieceNum")


        self.PlayerNum = QtWidgets.QSpinBox(Dialog)
        self.PlayerNum.setGeometry(QtCore.QRect(370, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        self.PlayerNum.setFont(font)
        self.PlayerNum.setMinimum(2)
        self.PlayerNum.setMaximum(4)
        self.PlayerNum.setObjectName("PlayerNum")
        self.PlayerNum_Txt = QtWidgets.QLabel(Dialog)
        self.PlayerNum_Txt.setGeometry(QtCore.QRect(130, 190, 201, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(24)
        self.PlayerNum_Txt.setFont(font)                                      # 플레이어 명수 - 글씨 "플레이어 명수"
        self.PlayerNum_Txt.setObjectName("PlayerNum_Txt")


        # 여태까지 만든 위젯들(버튼 , label, graphicsView)등을 위로 올림 , 뒤늦게 raise한 것이 맨 위에 있다
        self.graphicsView.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.Playerinfo.raise_()
        self.Playerinfo_2.raise_()
        self.Playerinfo_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.Playerinfo_4.raise_()
        self.GameStart.raise_()
        self.Player1_PieceNum.raise_()
        self.ExitBtn.raise_()
        self.PieceNum.raise_()
        self.PlayerNum.raise_()
        self.PlayerNum_Txt.raise_()
        self.retranslateUi(Dialog)                                 #위젯들한테 글씨 붙여주는것
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):   # 각 UI별 텍스트 내용들
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Playerinfo.setText(_translate("Dialog", "플레이어 1 :"))
        self.Playerinfo_2.setText(_translate("Dialog", "플레이어 2 :"))
        self.Playerinfo_3.setText(_translate("Dialog", "플레이어 3 :"))
        self.Playerinfo_4.setText(_translate("Dialog", "플레이어 4 :"))
        self.label.setText(_translate("Dialog", "플레이어 정보 입력"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/yutnori_fam.jpg\"/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/yut001.jpg\"/></p></body></html>"))
        self.GameStart.setText(_translate("Dialog", "Game Start"))
        self.ExitBtn.setText(_translate("Dialog", "EXIT"))
        self.PieceNum.setText(_translate("Dialog", "말의 갯수"))
        self.PlayerNum_Txt.setText(_translate("Dialog", "플레이어 명수"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UI_Dialog_02()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

