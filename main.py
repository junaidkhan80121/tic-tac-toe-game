# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tic_tac_toe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button1.setFont(font)
        self.button1.setText("")
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 0, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button2.setFont(font)
        self.button2.setText("")
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 0, 1, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button3.setFont(font)
        self.button3.setText("")
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 0, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button4.setFont(font)
        self.button4.setText("")
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 1, 0, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button5.setFont(font)
        self.button5.setText("")
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 1, 1, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button6.setFont(font)
        self.button6.setText("")
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 1, 2, 1, 1)
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button7.setFont(font)
        self.button7.setText("")
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 2, 0, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button8.setFont(font)
        self.button8.setText("")
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 2, 1, 1, 1)
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button9.setFont(font)
        self.button9.setText("")
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 26))
        self.menubar.setObjectName("menubar")
        self.menuReset_Game = QtWidgets.QMenu(self.menubar)
        self.menuReset_Game.setObjectName("menuReset_Game")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFullScreen = QtWidgets.QAction(MainWindow)
        self.actionFullScreen.setObjectName("actionFullScreen")
        self.actionNormalScreen = QtWidgets.QAction(MainWindow)
        self.actionNormalScreen.setObjectName("actionNormalScreen")
        self.menuReset_Game.addAction(self.actionReset)
        self.menuReset_Game.addAction(self.actionExit)
        self.menuView.addAction(self.actionFullScreen)
        self.menuView.addAction(self.actionNormalScreen)
        self.menubar.addAction(self.menuReset_Game.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuReset_Game.setTitle(_translate("MainWindow", "Game Options"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionReset.setText(_translate("MainWindow", "Reset Game"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionFullScreen.setText(_translate("MainWindow", "Full Screen"))
        self.actionFullScreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionNormalScreen.setText(_translate("MainWindow", "Normal Screen"))
        self.actionNormalScreen.setShortcut(_translate("MainWindow", "F10"))
