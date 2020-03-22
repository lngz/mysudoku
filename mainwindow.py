# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 562)
        self.block = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 440, 113, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 440, 113, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 410, 101, 81))
        self.label.setObjectName("label")
        x = 80
        y = 80
        orgx = x
        stepx = 0
        stepy = 0
        for i in range(81):
            stepx = 30 * (i % 9 )
            stepy = 30 * (i //9 ) 
            lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            lineEdit.setGeometry(QtCore.QRect(x+stepx, y+stepy, 30, 30))
            lineEdit.setObjectName("lineEdit")
           


            self.block.append(lineEdit)
        
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_2.setGeometry(QtCore.QRect(240, 80, 113, 21))
        # self.lineEdit_2.setObjectName("lineEdit_2")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Reset"))
        self.pushButton_2.setText(_translate("MainWindow", "Resolve"))
        self.label.setText(_translate("MainWindow", "数独"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
