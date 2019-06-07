# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GamePlaying.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# 게임 진행 Display
# @Yeomin

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QCoreApplication
import Controller
import sys

class UI_Dialog_03(object):


    # 이 아래의 함수 3개와 temp_list는 만들다가 못 만든 것...T^T 지우셔도 됩니다
    
    # UI 설정
    def __init__(self):
        self.controller = Controller.Contoller()
        self.current_turn = 0
        self.next_turn = 0
        self.remainedpiece = [5,5,5,5]
        self.action = 0
    def map_clicked(self, map_index):
        if self.action == 1:
            self.current_turn = self.next_turn
            self.viewmapinfo, self.remainedpiece, self.next_turn, self.in_goal =self.controller.map_clicked(map_index)
            print(self.viewmapinfo, self.remainedpiece)
            self.action = 2
            self.update_ui()
            string = str(self.next_turn + 1) + "의 턴 입니다."
            self.turn.setText(string)
            
    def update_ui(self):
        btn_list = [self.Btn0, self.Btn1, self.Btn2, self.Btn3, self.Btn4, self.Btn5, self.Btn6, self.Btn7, self.Btn8, self.Btn9, self.Btn10, self.Btn11, self.Btn12, self.Btn13, self.Btn14, self.Btn15, self.Btn16,
                    self.Btn17, self.Btn18, self.Btn19, self.Btn20, self.Btn21, self.Btn22, self.Btn23, self.Btn24, self.Btn25, self.Btn26, self.Btn27, self.Btn28]
        
        self.Player01.setGeometry(QtCore.QRect(690, 40, 141, 151))
        self.Player01_2.setGeometry(QtCore.QRect(750, 40, 141, 151))
        self.Player01_3.setGeometry(QtCore.QRect(780, 40, 141, 151))
        self.Player01_4.setGeometry(QtCore.QRect(810, 40, 141, 151))
        self.Player01_5.setGeometry(QtCore.QRect(850, 40, 141, 151))
        self.Player02.setGeometry(QtCore.QRect(690, 140, 141, 151))
        self.Player02_2.setGeometry(QtCore.QRect(750, 140, 141, 151))
        self.Player02_3.setGeometry(QtCore.QRect(780, 140, 141, 151))
        self.Player02_4.setGeometry(QtCore.QRect(810, 140, 141, 151))
        self.Player02_5.setGeometry(QtCore.QRect(850, 140, 141, 151))
        self.Player03.setGeometry(QtCore.QRect(690, 240, 141, 151))
        self.Player03_2.setGeometry(QtCore.QRect(750, 240, 141, 151))
        self.Player03_3.setGeometry(QtCore.QRect(780, 240, 141, 151))
        self.Player03_4.setGeometry(QtCore.QRect(810, 240, 141, 151))
        self.Player03_5.setGeometry(QtCore.QRect(850, 240, 141, 151))
        self.Player04.setGeometry(QtCore.QRect(690, 340, 141, 151))
        self.Player04_2.setGeometry(QtCore.QRect(750, 340, 141, 151))
        self.Player04_3.setGeometry(QtCore.QRect(780, 340, 141, 151))
        self.Player04_4.setGeometry(QtCore.QRect(810, 340, 141, 151))
        self.Player04_5.setGeometry(QtCore.QRect(850, 340, 141, 151))
        
        if self.remainedpiece[0] == 0:
            self.Player01.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[0] == 1:
            self.Player01.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[0] == 2:
            self.Player01.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[0] == 3:
            self.Player01.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player01_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[0] == 4:
            self.Player01.setGeometry(QtCore.QRect(0, 0, 0, 0))
        
        
        if self.remainedpiece[1] == 0:
            self.Player02.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[1] == 1:
            self.Player02.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[1] == 2:
            self.Player02.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[1] == 3:
            self.Player02.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player02_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[1] == 4:
            self.Player02.setGeometry(QtCore.QRect(0, 0, 0, 0))
        
        if self.remainedpiece[2] == 0:
            self.Player03.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[2] == 1:
            self.Player03.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[2] == 2:
            self.Player03.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[2] == 3:
            self.Player03.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player03_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[2] == 4:
            self.Player03.setGeometry(QtCore.QRect(0, 0, 0, 0))
        
        if self.remainedpiece[3] == 0:
            self.Player04.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[3] == 1:
            self.Player04.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[3] == 2:
            self.Player04.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[3] == 3:
            self.Player04.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.Player04_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        if self.remainedpiece[3] == 4:
            self.Player04.setGeometry(QtCore.QRect(0, 0, 0, 0))
        
            
        if self.action == 2:
            for j in range(29):
                
                if self.viewmapinfo[j][2] == -1:
                    opacity_effect = QGraphicsOpacityEffect(btn_list[j])          
                    opacity_effect.setOpacity(0)
                    temp = btn_list[j]                              
                    temp.setGraphicsEffect(opacity_effect)
                elif self.viewmapinfo[j][2] == 0:
                    opacity_effect = QGraphicsOpacityEffect(btn_list[j])          
                    opacity_effect.setOpacity(1)
                    temp = btn_list[j]                              
                    temp.setGraphicsEffect(opacity_effect)
                    if self.viewmapinfo[j][3] == 1:
                        temp.setIcon(QtGui.QIcon("1.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 2:
                        temp.setIcon(QtGui.QIcon("1-2.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 3:
                        temp.setIcon(QtGui.QIcon("1-3.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 4:
                        temp.setIcon(QtGui.QIcon("1-4.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 5:
                        temp.setIcon(QtGui.QIcon("1-5.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    
                elif self.viewmapinfo[j][2] == 1:
                    opacity_effect = QGraphicsOpacityEffect(btn_list[j])          
                    opacity_effect.setOpacity(1)
                    temp = btn_list[j]                              
                    temp.setGraphicsEffect(opacity_effect)
                    if self.viewmapinfo[j][3] == 1:
                        temp.setIcon(QtGui.QIcon("2.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 2:
                        temp.setIcon(QtGui.QIcon("2-2.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 3:
                        temp.setIcon(QtGui.QIcon("2-3.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 4:
                        temp.setIcon(QtGui.QIcon("2-4.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 5:
                        temp.setIcon(QtGui.QIcon("2-5.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    
                
                elif self.viewmapinfo[j][2] == 2:
                    opacity_effect = QGraphicsOpacityEffect(btn_list[j])          
                    opacity_effect.setOpacity(1)
                    temp = btn_list[j]                              
                    temp.setGraphicsEffect(opacity_effect)
                    if self.viewmapinfo[j][3] == 1:
                        temp.setIcon(QtGui.QIcon("3.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 2:
                        temp.setIcon(QtGui.QIcon("3-2.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 3:
                        temp.setIcon(QtGui.QIcon("3-3.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 4:
                        temp.setIcon(QtGui.QIcon("3-4.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 5:
                        temp.setIcon(QtGui.QIcon("3-5.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    
                elif self.viewmapinfo[j][2] == 3:
                    opacity_effect = QGraphicsOpacityEffect(btn_list[j])          
                    opacity_effect.setOpacity(1)
                    temp = btn_list[j]                              
                    temp.setGraphicsEffect(opacity_effect)
                    if self.viewmapinfo[j][3] == 1:
                        temp.setIcon(QtGui.QIcon("4.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 2:
                        temp.setIcon(QtGui.QIcon("4-2.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 3:
                        temp.setIcon(QtGui.QIcon("4-3.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 4:
                        temp.setIcon(QtGui.QIcon("4-4.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    if self.viewmapinfo[j][3] == 5:
                        temp.setIcon(QtGui.QIcon("4-5.PNG"))
                        temp.setIconSize(QtCore.QSize(200,200))
                    
                    
            self.action = 0
              
                   
    def roll(self):
        if self.action == 0:
            self.controller.roll()
            self.action = 1
    def button_Click00(self):
        self.map_clicked(0)
    def button_Click01(self):
        self.map_clicked(1)
    def button_Click02(self):
        self.map_clicked(2)
    def button_Click03(self):
        self.map_clicked(3)
    def button_Click04(self):
        self.map_clicked(4)
    def button_Click05(self):
        self.map_clicked(5)
    def button_Click06(self):
        self.map_clicked(6)
    def button_Click07(self):
        self.map_clicked(7)
    def button_Click08(self):
        self.map_clicked(8)
    def button_Click09(self):
        self.map_clicked(9)
    def button_Click10(self):
        self.map_clicked(10)
    def button_Click11(self):
        self.map_clicked(11)
    def button_Click12(self):
        self.map_clicked(12)
    def button_Click13(self):
        self.map_clicked(13)
    def button_Click14(self):
        self.map_clicked(14)
    def button_Click15(self):
        self.map_clicked(15)
    def button_Click16(self):
        self.map_clicked(16)
    def button_Click17(self):
        self.map_clicked(17)
    def button_Click18(self):
        self.map_clicked(18)
    def button_Click19(self):
        self.map_clicked(19)
    def button_Click20(self):
        self.map_clicked(20)
    def button_Click21(self):
        self.map_clicked(21)
    def button_Click22(self):
        self.map_clicked(22)
    def button_Click23(self):
        self.map_clicked(23)
    def button_Click24(self):
        self.map_clicked(24)
    def button_Click25(self):
        self.map_clicked(25)
    def button_Click26(self):
        self.map_clicked(26)
    def button_Click27(self):
        self.map_clicked(27)
    def button_Click28(self):
        self.map_clicked(28)
        
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        _translate = QtCore.QCoreApplication.translate
        Dialog.setObjectName("Dialog")                              # Dialog의 이름 , 변경시 해당 이름으로 접근 , Dialog는 우리가 보는 윈도우 창이라고 생각하면 됨
        Dialog.resize(1020, 800)                                    # 화면 크기 1020*800

        # 그래픽 뷰 - 배경 화면 흰색으로 하기 위하여 (실은 배경화면 흰색으로 하는 코드를 몰라서 그래픽 뷰-디폴트 흰색-으로 배경을 덮음)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)             # Qt위젯 중 그래픽뷰 사용을 선언
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1021, 801))    # 그래픽 뷰 위치 및 크기 설정 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        self.graphicsView.setObjectName("graphicsView")                 # 해당 뷰의 이름

        # 말 추가 기능 버튼 - 누르면 말이 추가되도록
        self.AddPiece = QtWidgets.QPushButton(Dialog)                   # AddPiece라는 버튼을 Dialog에 띄움
        self.AddPiece.setGeometry(QtCore.QRect(720, 590, 121, 71))      # Dialog의 크기 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        font = QtGui.QFont()                                            # 폰트 설정
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.AddPiece.setFont(font)
        self.AddPiece.setObjectName("AddPiece")                         # 해당 버튼의 이름
        self.AddPiece.clicked.connect(self.button_Click00)
        # 윷 던지기 버튼 - 누르면 랜덤으로 윷이 도~모까지 나온다
        self.Roll = QtWidgets.QPushButton(Dialog)                       # Roll이라는 버튼을 Dialog에 띄움
        self.Roll.setGeometry(QtCore.QRect(850, 590, 121, 71))          # 버튼의 크기 (시작점의 x좌표, 시작점의 y좌표, 가로 크기, 세로 크기)
        self.Roll.clicked.connect(self.roll)               
        font = QtGui.QFont()                                            # 폰트 설정
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Roll.setFont(font)
        self.Roll.setObjectName("Roll")                                 # 해당 버튼의 이름

        # 지정 윷 던지기 글씨
        self.Rolling_Yut = QtWidgets.QLabel(Dialog)
        self.Rolling_Yut.setGeometry(QtCore.QRect(10, 720, 191, 61))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Rolling_Yut.setFont(font)
        self.Rolling_Yut.setAlignment(QtCore.Qt.AlignCenter)
        self.Rolling_Yut.setObjectName("Rolling_Yut")

        # 지정 윷 던지기 - 도
        self.Do_Btn = QtWidgets.QPushButton(Dialog)
        self.Do_Btn.setGeometry(QtCore.QRect(210, 730, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Do_Btn.setFont(font)
        self.Do_Btn.setObjectName("Do_Btn")

        # 지정 윷 던지기 - 개
        self.Ge_btn = QtWidgets.QPushButton(Dialog)
        self.Ge_btn.setGeometry(QtCore.QRect(300, 730, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Ge_btn.setFont(font)
        self.Ge_btn.setObjectName("Ge_btn")

        # 지정 윷 던지기 - 걸
        self.Gul_btn = QtWidgets.QPushButton(Dialog)
        self.Gul_btn.setGeometry(QtCore.QRect(390, 730, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Gul_btn.setFont(font)
        self.Gul_btn.setObjectName("Gul_btn")

        # 지정 윷 던지기 - 윷
        self.Yut_btn = QtWidgets.QPushButton(Dialog)
        self.Yut_btn.setGeometry(QtCore.QRect(480, 730, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Yut_btn.setFont(font)
        self.Yut_btn.setObjectName("Yut_btn")

        # 지정 윷 던지기 - 모
        self.Mo_btn = QtWidgets.QPushButton(Dialog)
        self.Mo_btn.setGeometry(QtCore.QRect(570, 730, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.Mo_btn.setFont(font)
        self.Mo_btn.setObjectName("Mo_btn")

        # 지정 윷 던지기 - 빽도
        self.BackDo_btn = QtWidgets.QPushButton(Dialog)
        self.BackDo_btn.setGeometry(QtCore.QRect(660, 730, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.BackDo_btn.setFont(font)
        self.BackDo_btn.setObjectName("BackDo_btn")

        # 윷놀이 보드판
        self.Yut_Board = QtWidgets.QLabel(Dialog)
        self.Yut_Board.setGeometry(QtCore.QRect(70, 60, 611, 611))
        self.Yut_Board.setObjectName("Yut_Board")
        
        self.turn = QtWidgets.QLabel(Dialog)
        self.turn.setGeometry(QtCore.QRect(900, 60, 611, 611))
        self.turn.setObjectName("turn")
        self.turn.resize(200,20)

        self.Do = QtWidgets.QLabel(Dialog)                          # 그림 - 도
        self.Do.setGeometry(QtCore.QRect(780, 480, 131, 101))
        self.Do.setObjectName("Do")

        self.BackDo = QtWidgets.QLabel(Dialog)                      # 그림 - 빽도
        self.BackDo.setGeometry(QtCore.QRect(780, 480, 141, 101))
        self.BackDo.setObjectName("BackDo")

        self.Ge = QtWidgets.QLabel(Dialog)                          # 그림 - 개
        self.Ge.setGeometry(QtCore.QRect(780, 480, 141, 101))
        self.Ge.setObjectName("Ge")

        self.Gul = QtWidgets.QLabel(Dialog)                         # 걸 그림 - 각 단계별 그림이 있으니 if문 같은것으로 조절하면  될듯
        self.Gul.setGeometry(QtCore.QRect(780, 480, 141, 101))
        self.Gul.setObjectName("Gul")

        self.Yut = QtWidgets.QLabel(Dialog)                          # 윷 그림
        self.Yut.setGeometry(QtCore.QRect(780, 480, 141, 101))
        self.Yut.setObjectName("Yut")

        self.Mo = QtWidgets.QLabel(Dialog)                           # 모 그림
        self.Mo.setGeometry(QtCore.QRect(780, 480, 141, 101))
        self.Mo.setObjectName("Mo")

        

        
        if self.remainedpiece[0] > 0:
            self.Player01 = QtWidgets.QLabel(Dialog)
            self.Player01.setGeometry(QtCore.QRect(690, 40, 141, 151))
            self.Player01.setObjectName("Player01")
            self.Player01.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player01_1.png\"/></p></body></html>"))
        if self.remainedpiece[0] > 1:
            self.Player01_2 = QtWidgets.QLabel(Dialog)
            self.Player01_2.setGeometry(QtCore.QRect(750, 40, 141, 151))
            self.Player01_2.setObjectName("Player01_2")
            self.Player01_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player01_1.png\"/></p></body></html>"))
        if self.remainedpiece[0] > 2:
            self.Player01_3 = QtWidgets.QLabel(Dialog)
            self.Player01_3.setGeometry(QtCore.QRect(780, 40, 141, 151))
            self.Player01_3.setObjectName("Player01_3")
            self.Player01_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player01_1.png\"/></p></body></html>"))
        if self.remainedpiece[0] > 3:
            self.Player01_4 = QtWidgets.QLabel(Dialog)
            self.Player01_4.setGeometry(QtCore.QRect(810, 40, 141, 151))
            self.Player01_4.setObjectName("Player01_4")
            self.Player01_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player01_1.png\"/></p></body></html>"))
        
        if self.remainedpiece[0] > 4:
            self.Player01_5 = QtWidgets.QLabel(Dialog)
            self.Player01_5.setGeometry(QtCore.QRect(850, 40, 141, 151))
            self.Player01_5.setObjectName("Player01_5")
            self.Player01_5.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player01_1.png\"/></p></body></html>"))
    

        # 두 번째 플레이어 - 말 5개
        if self.remainedpiece[1] > 0:
            self.Player02 = QtWidgets.QLabel(Dialog)
            self.Player02.setGeometry(QtCore.QRect(690, 140, 141, 151))
            self.Player02.setObjectName("Player02")
            self.Player02.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player02_1.png\"/></p></body></html>"))
      
        if self.remainedpiece[1] > 1:
            self.Player02_2 = QtWidgets.QLabel(Dialog)
            self.Player02_2.setGeometry(QtCore.QRect(750, 140, 141, 151))
            self.Player02_2.setObjectName("Player02_2")
            self.Player02_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player02_1.png\"/></p></body></html>"))
        if self.remainedpiece[1] > 2:
            self.Player02_3 = QtWidgets.QLabel(Dialog)
            self.Player02_3.setGeometry(QtCore.QRect(780, 140, 141, 151))
            self.Player02_3.setObjectName("Player02_3")
            self.Player02_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player02_1.png\"/></p></body></html>"))
        if self.remainedpiece[1] > 3:    
            self.Player02_4 = QtWidgets.QLabel(Dialog)
            self.Player02_4.setGeometry(QtCore.QRect(810, 140, 141, 151))
            self.Player02_4.setObjectName("Player02_4")
            self.Player02_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player02_1.png\"/></p></body></html>"))
        if self.remainedpiece[1] > 4:    
            self.Player02_5 = QtWidgets.QLabel(Dialog)
            self.Player02_5.setGeometry(QtCore.QRect(850, 140, 141, 151))
            self.Player02_5.setObjectName("Player02_5")
            self.Player02_5.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player02_1.png\"/></p></body></html>"))

        # 세 번째 플레이어 - 말 5개
        if self.remainedpiece[2] > 0:
            self.Player03 = QtWidgets.QLabel(Dialog)
            self.Player03.setGeometry(QtCore.QRect(690, 240, 141, 151))
            self.Player03.setObjectName("Player03")
            self.Player03.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player03_1.png\"/></p></body></html>"))
        if self.remainedpiece[2] > 1:
            self.Player03_2 = QtWidgets.QLabel(Dialog)
            self.Player03_2.setGeometry(QtCore.QRect(750, 240, 141, 151))
            self.Player03_2.setObjectName("Player03_2")     
            self.Player03_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player03_1.png\"/></p></body></html>"))
        
        if self.remainedpiece[2] > 2:
            self.Player03_3 = QtWidgets.QLabel(Dialog)
            self.Player03_3.setGeometry(QtCore.QRect(780, 240, 141, 151))
            self.Player03_3.setObjectName("Player03_3")
            self.Player03_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player03_1.png\"/></p></body></html>"))

        if self.remainedpiece[2] > 3:
            self.Player03_4 = QtWidgets.QLabel(Dialog)
            self.Player03_4.setGeometry(QtCore.QRect(810, 240, 141, 151))
            self.Player03_4.setObjectName("Player03_4")
            self.Player03_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player03_1.png\"/></p></body></html>"))
    
        if self.remainedpiece[2] > 4:
            self.Player03_5 = QtWidgets.QLabel(Dialog)
            self.Player03_5.setGeometry(QtCore.QRect(850, 240, 141, 151))
            self.Player03_5.setObjectName("Player03_5")
            self.Player03_5.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player03_1.png\"/></p></body></html>"))

        # 네 번째 플레이어 - 말 5개
        if self.remainedpiece[3] > 0:
            self.Player04 = QtWidgets.QLabel(Dialog)
            self.Player04.setGeometry(QtCore.QRect(690, 340, 141, 151))
            self.Player04.setObjectName("Player04")
            self.Player04.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player04_1.png\"/></p></body></html>"))

        if self.remainedpiece[3] > 1:
            self.Player04_2 = QtWidgets.QLabel(Dialog)
            self.Player04_2.setGeometry(QtCore.QRect(750, 340, 141, 151))
            self.Player04_2.setObjectName("Player04_2")
            self.Player04_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player04_1.png\"/></p></body></html>"))
      

        if self.remainedpiece[3] > 2:
            self.Player04_3 = QtWidgets.QLabel(Dialog)
            self.Player04_3.setGeometry(QtCore.QRect(780, 340, 141, 151))
            self.Player04_3.setObjectName("Player04_3")
            self.Player04_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player04_1.png\"/></p></body></html>"))

        if self.remainedpiece[3] > 3:
            self.Player04_4 = QtWidgets.QLabel(Dialog)
            self.Player04_4.setGeometry(QtCore.QRect(810, 340, 141, 151))
            self.Player04_4.setObjectName("Player04_4")
            self.Player04_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player04_1.png\"/></p></body></html>"))
        
        if self.remainedpiece[3] > 4:
            self.Player04_5 = QtWidgets.QLabel(Dialog)
            self.Player04_5.setGeometry(QtCore.QRect(850, 340, 141, 151))
            self.Player04_5.setObjectName("Player04_5")
            self.Player04_5.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/player04_1.png\"/></p></body></html>"))

        # 여기에서부터는 각 보드의 버튼 0 ~ 28까지 있으며, 그 순서는 yutnori_map의 보드판과 일치
        self.Btn0 = QtWidgets.QPushButton(Dialog)                # 버튼 생성
        self.Btn0.setGeometry(QtCore.QRect(560, 550, 93, 101))     # 버튼 위치 및 사이즈
        self.Btn0.setObjectName("Btn0")                             # 버튼 이름
        opacity_effect = QGraphicsOpacityEffect(self.Btn0)          
        opacity_effect.setOpacity(0.1)                              
        self.Btn0.setGraphicsEffect(opacity_effect)                 
        self.Btn0.clicked.connect(self.button_Click00)

        ## 버튼 0 ~ 28까지 생성
        self.Btn1 = QtWidgets.QPushButton(Dialog)
        self.Btn1.setGeometry(QtCore.QRect(570, 460, 71, 81))
        self.Btn1.setObjectName("0.1")
        opacity_effect = QGraphicsOpacityEffect(self.Btn1)
        opacity_effect.setOpacity(0.1)
        self.Btn1.setGraphicsEffect(opacity_effect)
        self.Btn1.clicked.connect(self.button_Click01)

        
        self.Btn2 = QtWidgets.QPushButton(Dialog)
        self.Btn2.setGeometry(QtCore.QRect(570, 370, 71, 71))
        self.Btn2.setObjectName("Btn2")
        opacity_effect = QGraphicsOpacityEffect(self.Btn2)
        opacity_effect.setOpacity(0.1)
        self.Btn2.setGraphicsEffect(opacity_effect)
        self.Btn2.clicked.connect(self.button_Click02)

        self.Btn3 = QtWidgets.QPushButton(Dialog)
        self.Btn3.setGeometry(QtCore.QRect(570, 280, 71, 71))
        self.Btn3.setObjectName("Btn3")
        opacity_effect = QGraphicsOpacityEffect(self.Btn3)
        opacity_effect.setOpacity(0.1)
        self.Btn3.setGraphicsEffect(opacity_effect)
        self.Btn3.clicked.connect(self.button_Click03)

        self.Btn4 = QtWidgets.QPushButton(Dialog)
        self.Btn4.setGeometry(QtCore.QRect(570, 200, 71, 71))
        self.Btn4.setObjectName("Btn4")
        opacity_effect = QGraphicsOpacityEffect(self.Btn4)
        opacity_effect.setOpacity(0.1)
        self.Btn4.setGraphicsEffect(opacity_effect)
        self.Btn4.clicked.connect(self.button_Click04)

        self.Btn5 = QtWidgets.QPushButton(Dialog)
        self.Btn5.setGeometry(QtCore.QRect(560, 80, 93, 101))
        self.Btn5.setObjectName("Btn5")
        opacity_effect = QGraphicsOpacityEffect(self.Btn5)
        opacity_effect.setOpacity(0.1)
        self.Btn5.setGraphicsEffect(opacity_effect)
        self.Btn5.clicked.connect(self.button_Click05)

        self.Btn6 = QtWidgets.QPushButton(Dialog)
        self.Btn6.setGeometry(QtCore.QRect(470, 90, 71, 71))
        self.Btn6.setObjectName("Btn6")
        opacity_effect = QGraphicsOpacityEffect(self.Btn6)
        opacity_effect.setOpacity(0.1)
        self.Btn6.setGraphicsEffect(opacity_effect)
        self.Btn6.clicked.connect(self.button_Click06)

        self.Btn7 = QtWidgets.QPushButton(Dialog)
        self.Btn7.setGeometry(QtCore.QRect(380, 90, 71, 71))
        self.Btn7.setObjectName("Btn7")
        opacity_effect = QGraphicsOpacityEffect(self.Btn7)
        opacity_effect.setOpacity(0.1)
        self.Btn7.setGraphicsEffect(opacity_effect)
        self.Btn7.clicked.connect(self.button_Click07)

        self.Btn8 = QtWidgets.QPushButton(Dialog)
        self.Btn8.setGeometry(QtCore.QRect(290, 90, 71, 71))
        self.Btn8.setObjectName("Btn8")
        opacity_effect = QGraphicsOpacityEffect(self.Btn8)
        opacity_effect.setOpacity(0.1)
        self.Btn8.setGraphicsEffect(opacity_effect)
        self.Btn8.clicked.connect(self.button_Click08)

        self.Btn9 = QtWidgets.QPushButton(Dialog)
        self.Btn9.setGeometry(QtCore.QRect(200, 90, 71, 71))
        self.Btn9.setObjectName("Btn9")
        opacity_effect = QGraphicsOpacityEffect(self.Btn9)
        opacity_effect.setOpacity(0.1)
        self.Btn9.setGraphicsEffect(opacity_effect)
        self.Btn9.clicked.connect(self.button_Click09)

        self.Btn10 = QtWidgets.QPushButton(Dialog)
        self.Btn10.setGeometry(QtCore.QRect(90, 80, 93, 101))
        self.Btn10.setObjectName("Btn10")
        opacity_effect = QGraphicsOpacityEffect(self.Btn10)
        opacity_effect.setOpacity(0.1)
        self.Btn10.setGraphicsEffect(opacity_effect)
        self.Btn10.clicked.connect(self.button_Click10)

        self.Btn11 = QtWidgets.QPushButton(Dialog)
        self.Btn11.setGeometry(QtCore.QRect(100, 200, 71, 71))
        self.Btn11.setObjectName("Btn11")
        opacity_effect = QGraphicsOpacityEffect(self.Btn11)
        opacity_effect.setOpacity(0.1)
        self.Btn11.setGraphicsEffect(opacity_effect)
        self.Btn11.clicked.connect(self.button_Click11)

        self.Btn12 = QtWidgets.QPushButton(Dialog)
        self.Btn12.setGeometry(QtCore.QRect(100, 290, 71, 71))
        self.Btn12.setObjectName("Btn12")
        opacity_effect = QGraphicsOpacityEffect(self.Btn12)
        opacity_effect.setOpacity(0.1)
        self.Btn12.setGraphicsEffect(opacity_effect)
        self.Btn12.clicked.connect(self.button_Click12)

        self.Btn13 = QtWidgets.QPushButton(Dialog)
        self.Btn13.setGeometry(QtCore.QRect(100, 370, 71, 71))
        self.Btn13.setObjectName("Btn13")
        opacity_effect = QGraphicsOpacityEffect(self.Btn13)
        opacity_effect.setOpacity(0.1)
        self.Btn13.setGraphicsEffect(opacity_effect)
        self.Btn13.clicked.connect(self.button_Click13)

        self.Btn14 = QtWidgets.QPushButton(Dialog)
        self.Btn14.setGeometry(QtCore.QRect(100, 460, 71, 71))
        self.Btn14.setObjectName("Btn14")
        opacity_effect = QGraphicsOpacityEffect(self.Btn14)
        opacity_effect.setOpacity(0.1)
        self.Btn14.setGraphicsEffect(opacity_effect)
        self.Btn14.clicked.connect(self.button_Click14)

        self.Btn15 = QtWidgets.QPushButton(Dialog)
        self.Btn15.setGeometry(QtCore.QRect(90, 550, 93, 101))
        self.Btn15.setObjectName("Btn15")
        opacity_effect = QGraphicsOpacityEffect(self.Btn15)
        opacity_effect.setOpacity(0.1)
        self.Btn15.setGraphicsEffect(opacity_effect)
        self.Btn15.clicked.connect(self.button_Click15)

        self.Btn16 = QtWidgets.QPushButton(Dialog)
        self.Btn16.setGeometry(QtCore.QRect(200, 560, 71, 71))
        self.Btn16.setObjectName("Btn16")
        opacity_effect = QGraphicsOpacityEffect(self.Btn16)
        opacity_effect.setOpacity(0.1)
        self.Btn16.setGraphicsEffect(opacity_effect)
        self.Btn16.clicked.connect(self.button_Click16)

        self.Btn17 = QtWidgets.QPushButton(Dialog)
        self.Btn17.setGeometry(QtCore.QRect(290, 560, 71, 71))
        self.Btn17.setObjectName("Btn17")
        opacity_effect = QGraphicsOpacityEffect(self.Btn17)
        opacity_effect.setOpacity(0.1)
        self.Btn17.setGraphicsEffect(opacity_effect)
        self.Btn17.clicked.connect(self.button_Click17)

        self.Btn18 = QtWidgets.QPushButton(Dialog)
        self.Btn18.setGeometry(QtCore.QRect(380, 560, 71, 71))
        self.Btn18.setObjectName("Btn18")
        opacity_effect = QGraphicsOpacityEffect(self.Btn18)
        opacity_effect.setOpacity(0.1)
        self.Btn18.setGraphicsEffect(opacity_effect)
        self.Btn18.clicked.connect(self.button_Click18)

        self.Btn19 = QtWidgets.QPushButton(Dialog)
        self.Btn19.setGeometry(QtCore.QRect(470, 560, 71, 71))
        self.Btn19.setObjectName("Btn19")
        opacity_effect = QGraphicsOpacityEffect(self.Btn19)
        opacity_effect.setOpacity(0.1)
        self.Btn19.setGraphicsEffect(opacity_effect)
        self.Btn19.clicked.connect(self.button_Click19)

        self.Btn20 = QtWidgets.QPushButton(Dialog)
        self.Btn20.setGeometry(QtCore.QRect(490, 180, 71, 71))
        self.Btn20.setObjectName("Btn20")
        opacity_effect = QGraphicsOpacityEffect(self.Btn20)
        opacity_effect.setOpacity(0.1)
        self.Btn20.setGraphicsEffect(opacity_effect)
        self.Btn20.clicked.connect(self.button_Click20)

        self.Btn21 = QtWidgets.QPushButton(Dialog)
        self.Btn21.setGeometry(QtCore.QRect(420, 240, 71, 71))
        self.Btn21.setObjectName("Btn21")
        opacity_effect = QGraphicsOpacityEffect(self.Btn21)
        opacity_effect.setOpacity(0.1)
        self.Btn21.setGraphicsEffect(opacity_effect)
        self.Btn21.clicked.connect(self.button_Click21)

        self.Btn22 = QtWidgets.QPushButton(Dialog)
        self.Btn22.setGeometry(QtCore.QRect(250, 410, 71, 71))
        self.Btn22.setObjectName("Btn22")
        opacity_effect = QGraphicsOpacityEffect(self.Btn22)
        opacity_effect.setOpacity(0.1)
        self.Btn22.setGraphicsEffect(opacity_effect)
        self.Btn22.clicked.connect(self.button_Click22)

        self.Btn23 = QtWidgets.QPushButton(Dialog)
        self.Btn23.setGeometry(QtCore.QRect(180, 480, 71, 71))
        self.Btn23.setObjectName("Btn23")
        opacity_effect = QGraphicsOpacityEffect(self.Btn23)
        opacity_effect.setOpacity(0.1)
        self.Btn23.setGraphicsEffect(opacity_effect)
        self.Btn23.clicked.connect(self.button_Click23)

        self.Btn24 = QtWidgets.QPushButton(Dialog)
        self.Btn24.setGeometry(QtCore.QRect(190, 180, 71, 71))
        self.Btn24.setObjectName("Btn24")
        opacity_effect = QGraphicsOpacityEffect(self.Btn24)
        opacity_effect.setOpacity(0.1)
        self.Btn24.setGraphicsEffect(opacity_effect)
        self.Btn24.clicked.connect(self.button_Click24)

        self.Btn25 = QtWidgets.QPushButton(Dialog)
        self.Btn25.setGeometry(QtCore.QRect(260, 240, 71, 71))
        self.Btn25.setObjectName("Btn25")
        opacity_effect = QGraphicsOpacityEffect(self.Btn25)
        opacity_effect.setOpacity(0.1)
        self.Btn25.setGraphicsEffect(opacity_effect)
        self.Btn25.clicked.connect(self.button_Click25)

        self.Btn26 = QtWidgets.QPushButton(Dialog)
        self.Btn26.setGeometry(QtCore.QRect(420, 410, 71, 71))
        self.Btn26.setObjectName("Btn26")
        opacity_effect = QGraphicsOpacityEffect(self.Btn26)
        opacity_effect.setOpacity(0.1)
        self.Btn26.setGraphicsEffect(opacity_effect)
        self.Btn26.clicked.connect(self.button_Click26)

        self.Btn27 = QtWidgets.QPushButton(Dialog)
        self.Btn27.setGeometry(QtCore.QRect(480, 480, 71, 71))
        self.Btn27.setObjectName("Btn27")
        opacity_effect = QGraphicsOpacityEffect(self.Btn27)
        opacity_effect.setOpacity(0.1)
        self.Btn27.setGraphicsEffect(opacity_effect)
        self.Btn27.clicked.connect(self.button_Click27)

        self.Btn28 = QtWidgets.QPushButton(Dialog)
        self.Btn28.setGeometry(QtCore.QRect(322, 310, 101, 101))
        self.Btn28.setObjectName("Btn28")
        opacity_effect = QGraphicsOpacityEffect(self.Btn28)
        opacity_effect.setOpacity(0.1)
        self.Btn28.setGraphicsEffect(opacity_effect)
        self.Btn28.clicked.connect(self.button_Click28)
        

        self.retranslateUi(Dialog)                      # Dialog의 위젯들(label, 버튼 등)에 글씨 및 그림을 넣는 함수 실행
        QtCore.QMetaObject.connectSlotsByName(Dialog)   # 설정한 이름과 위젯들을 연결
        return  True
        
    
# 각 버튼 및 레이블의 글자
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AddPiece.setText(_translate("Dialog", "말 추가"))
        self.Roll.setText(_translate("Dialog", "윷 던지기"))
        self.Rolling_Yut.setText(_translate("Dialog", "지정 윷 던지기"))
        self.Do_Btn.setText(_translate("Dialog", "도"))
        self.Ge_btn.setText(_translate("Dialog", "개"))
        self.Gul_btn.setText(_translate("Dialog", "걸"))
        self.Yut_btn.setText(_translate("Dialog", "윷"))
        self.Mo_btn.setText(_translate("Dialog", "모"))
        self.Yut_Board.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/Yut_Board2.jpg\"/></p></body></html>"))
        self.Do.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/DO.png\"/></p></body></html>"))
        self.BackDo.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/BackDO.png\"/></p></body></html>"))
        self.Ge.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/GE.png\"/></p></body></html>"))
        self.BackDo_btn.setText(_translate("Dialog", "빽도"))
        self.Gul.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/GUL.png\"/></p></body></html>"))
        self.Yut.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/YUT.png\"/></p></body></html>"))
        self.Mo.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/MO.png\"/></p></body></html>"))
        
        
        

 # 여기에서부터는 각 버튼의 글씨
 # 단, 글씨가 있으면 투명도를 낮춰도 지저분하기 때문에 글씨는 제거함

import myres_rc





def UI_Display(Dialog00):  # 한 UI에서 다른 UI띄울 때 사용할 함수
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Dialog00()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

import myres_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UI_Dialog_03()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



