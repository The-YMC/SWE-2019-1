# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yutnori01.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1021, 763)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 60, 291, 121))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(230, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.Exit = QtWidgets.QPushButton(Dialog)
        self.Exit.setGeometry(QtCore.QRect(580, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 170, 541, 381))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1021, 771))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.start.raise_()
        self.Exit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "윷놀이"))
        self.start.setText(_translate("Dialog", "START"))
        self.Exit.setText(_translate("Dialog", "Exit"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/imgs/yutnori_fam.jpg\"/></p></body></html>"))


        """import myres_rc"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

