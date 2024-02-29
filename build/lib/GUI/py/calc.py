# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(0, 0, 401, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.answer.setFont(font)
        self.answer.setStyleSheet("background-color: rgba(255, 253, 253, 45);")
        self.answer.setObjectName("answer")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(0, 250, 100, 50))
        self.btn_clear.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_1.setObjectName("btn_1")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 150, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_4.setObjectName("btn_4")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 100, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_7.setObjectName("btn_7")
        self.btn_umnowenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umnowenie.setGeometry(QtCore.QRect(300, 150, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_umnowenie.setFont(font)
        self.btn_umnowenie.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.btn_umnowenie.setObjectName("btn_nothing")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 250, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 100, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 100, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_9.setObjectName("btn_9")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 150, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 150, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_6.setObjectName("btn_6")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_2.setObjectName("btn_2")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(100, 250, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_0.setObjectName("btn_0")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("alternate-background-color: rgba(255, 253, 253, 45);")
        self.btn_3.setObjectName("btn_3")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(200, 250, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_mines = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mines.setGeometry(QtCore.QRect(300, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mines.setFont(font)
        self.btn_mines.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.btn_mines.setObjectName("btn_mines")
        self.btn_delenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delenie.setGeometry(QtCore.QRect(300, 100, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delenie.setFont(font)
        self.btn_delenie.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.btn_delenie.setObjectName("btn_mines_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.add_func()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculiator"))
        self.answer.setText(_translate("MainWindow", "0"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_umnowenie.setText(_translate("MainWindow", "*"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_mines.setText(_translate("MainWindow", "-"))
        self.btn_delenie.setText(_translate("MainWindow", "%"))

    def add_func(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_mines.clicked.connect(lambda: self.write_number(self.btn_mines.text()))
        self.btn_delenie.clicked.connect(lambda: self.write_number(self.btn_delenie.text()))
        self.btn_umnowenie.clicked.connect(lambda: self.write_number(self.btn_umnowenie.text()))
        
        self.btn_equal.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear)
        
        
    def write_number(self, number):
        if self.answer.text() == '0' or 'ans' in self.answer.text() or 'ОШИБКА' in self.answer.text():
            self.answer.setText(number)
        else:
            self.answer.setText(self.answer.text() + number)
    
    def clear(self):
        self.answer.setText('0')
        
    def result(self):
        try:
            res = eval(self.answer.text())
            self.answer.setText('ans = ' + str(res))
        except:
            self.answer.setText('ОШИБКА')
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
