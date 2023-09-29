from main import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt
import sys


class TIC_TAC_TOE(QMainWindow):
     turn = 1
     wins = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
     player_1_moves = []
     player_2_moves = []
     total_moves = []
     player_1_name, player_2_name= "",""
     count1,count2 = 0,0
     def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.desktop = QDesktopWidget()
          self.screenSize = self.desktop.screenGeometry()
          self.height = self.screenSize.height()
          self.width = self.screenSize.width()
          self.setFixedSize(int(self.width/3),int(self.height/2))
          self.ui.setupUi(self)
          self.setDialog()
          self.setWindowTitle("TIC_TAC_TOE")
          self.buttons = [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4, self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]
          self.ui.button1.clicked.connect(lambda:self.mark(1))
          self.ui.button2.clicked.connect(lambda:self.mark(2))
          self.ui.button3.clicked.connect(lambda:self.mark(3))
          self.ui.button4.clicked.connect(lambda:self.mark(4))
          self.ui.button5.clicked.connect(lambda:self.mark(5))
          self.ui.button6.clicked.connect(lambda:self.mark(6))
          self.ui.button7.clicked.connect(lambda:self.mark(7))
          self.ui.button8.clicked.connect(lambda:self.mark(8))
          self.ui.button9.clicked.connect(lambda:self.mark(9))
          self.ui.actionReset.triggered.connect(self.resetGame)
          self.ui.actionExit.triggered.connect(lambda:exit())
          self.ui.actionFullScreen.triggered.connect(lambda:self.showFullScreen())
          self.ui.actionNormalScreen.triggered.connect(lambda:self.showNormal())
          self.setInputDialog1()
          
     def closeEvent(self, event):
          setInputDialog1.close()
          setInputDialog2.close()
          setDialog.close()

     def mark(self,position):
          if self.turn == 1:
               if position in self.total_moves:
                    self.turn = 1
               else:
                    self.buttons[position-1].setText("X")
                    self.player_1_moves.append(position)
                    self.total_moves.append(position)
                    for i in self.wins:
                         for j in i:
                              if j in self.player_1_moves:
                                   print(i,j)
                                   self.count1+=1
                              if self.count1==3:
                                   print("Player 1 Won")
                                   self.winmsg.setText(f"Congratulations, {self.player_1_name} Won")
                                   self.dialog.show()
                                   self.resetGame()
                                   self.count1=0
                         self.count1=0          
                    self.turn = 2
               

          elif self.turn==2:
               if position in self.total_moves:
                    self.turn = 2
                    
               else:
                    self.buttons[position-1].setText("O")
                    self.player_2_moves.append(position)
                    self.total_moves.append(position)
                    for i in self.wins:
                         for j in i:
                              if j in self.player_2_moves:
                                   print(i,j)
                                   self.count2+=1
                              if self.count2==3:
                                   print("Player 2 Won")
                                   self.winmsg.setText(f"Congratulations, {self.player_2_name} Won")
                                   self.dialog.show()
                                   self.resetGame()
                                   self.count2=0
                         self.count2=0
                         self.turn = 1


     def setDialog(self):
          self.dialog = QDialog()
          self.dialog.setWindowTitle("Congratulations!..")
          self.dialog.setFixedSize(int(self.width/3),int(self.height/5))
          self.dialogLayout = QVBoxLayout()
          self.dialog.setLayout(self.dialogLayout)
          self.winmsg = QLabel("",self.dialog)
          self.winmsg.setAlignment(Qt.AlignCenter)
          self.winmsg.setStyleSheet('QLabel {font-size: 30px; }')
          self.dialogLayout.addWidget(self.winmsg)

     def  setInputDialog1(self):
          self.dialog1 = QDialog()
          self.dialog1.setWindowTitle("P1 Name")
          self.dialog1.setFixedSize(int(self.width/3),int(self.height/5))
          self.dialogLayout1 = QVBoxLayout()
          self.dialog1.setLayout(self.dialogLayout1)
          self.inputName1 = QLineEdit()
          self.inputName1.setStyleSheet('QLineEdit {font-size: 20px; }')
          self.inputName1.setFixedSize(int(self.width/3.15), 50)
          self.inputName1.setPlaceholderText("Enter Player 1 Name")
          self.submitNamebtn1 = QPushButton("Enter")
          self.submitNamebtn1.setFixedSize(int(self.width/3.15), 50)
          self.submitNamebtn1.setStyleSheet('QPushButton {font-size: 15px; }')
          #self.winmsg.setStyleSheet('QLabel {font-size: 30px; }')
          self.dialogLayout1.addWidget(self.inputName1)
          self.dialogLayout1.addWidget(self.submitNamebtn1)
          self.submitNamebtn1.clicked.connect(self.getName1)
          self.inputName1.returnPressed.connect(self.getName1)
          self.dialog1.show()

     def getName1(self):
          while True:
               if self.inputName1.text()=="":
                  break  
               else:
                    self.player_1_name = self.inputName1.text()
                    self.dialog1.close()
                    self.setInputDialog2()
                    break


     def  setInputDialog2(self):
          self.dialog2 = QDialog()
          self.dialog2.setWindowTitle("P2 Name")
          self.dialog2.setFixedSize(int(self.width/3),int(self.height/5))
          self.dialogLayout2 = QVBoxLayout()
          self.dialog2.setLayout(self.dialogLayout2)
          self.inputName2 = QLineEdit()
          self.inputName2.setFixedSize(int(self.width/3.15), 50)
          self.inputName2.setStyleSheet('QLineEdit {font-size: 20px; }')
          self.inputName2.setPlaceholderText("Enter Player 2 Name")
          self.submitNamebtn2 = QPushButton("Enter")
          self.submitNamebtn2.setFixedSize(int(self.width/3.15), 50)
          #self.winmsg.setStyleSheet('QLabel {font-size: 30px; }')
          self.dialogLayout2.addWidget(self.inputName2)
          self.dialogLayout2.addWidget(self.submitNamebtn2)
          self.submitNamebtn2.clicked.connect(self.getName2)
          self.submitNamebtn2.setStyleSheet('QPushButton {font-size: 15px; }')
          self.inputName2.returnPressed.connect(self.getName2)
          self.dialog2.show()

     def getName2(self):
          while True:
               if self.inputName2.text()=="":
                    break
               else:
                    self.player_2_name = self.inputName2.text()
                    self.dialog2.close()
                    self.showNormal()
                    break
          

     def resetGame(self):
          for i in self.buttons:
               i.setText("")
          self.player_1_moves = []
          self.player_2_moves = []
          self.total_moves = []
          self.count1,self.count2 = 0,0
          self.turn = 1
          self.player_1_name,self.player_2_name = "",""
          self.setInputDialog1()

          
app = QApplication(sys.argv)
ttt = TIC_TAC_TOE()
#ttt.show()
sys.exit(app.exec_())
