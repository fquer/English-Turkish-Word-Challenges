# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ingtrsoru.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from math import fabs
from tkinter import E
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
import random
from openpyxl import load_workbook

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.soruLabel = QtWidgets.QLabel(self.centralwidget)
        self.soruLabel.setGeometry(QtCore.QRect(160, 40, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.soruLabel.setFont(font)
        self.soruLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.soruLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.soruLabel.setObjectName("soruLabel")
        self.aButton = QtWidgets.QPushButton(self.centralwidget)
        self.aButton.setGeometry(QtCore.QRect(170, 110, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.aButton.setFont(font)
        self.aButton.setObjectName("aButton")
        self.bButton = QtWidgets.QPushButton(self.centralwidget)
        self.bButton.setGeometry(QtCore.QRect(170, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bButton.setFont(font)
        self.bButton.setObjectName("bButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget)
        self.cButton.setGeometry(QtCore.QRect(170, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.dButton = QtWidgets.QPushButton(self.centralwidget)
        self.dButton.setGeometry(QtCore.QRect(170, 230, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dButton.setFont(font)
        self.dButton.setObjectName("dButton")
        self.eButton = QtWidgets.QPushButton(self.centralwidget)
        self.eButton.setGeometry(QtCore.QRect(170, 270, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eButton.setFont(font)
        self.eButton.setObjectName("eButton")
        self.fButton = QtWidgets.QPushButton(self.centralwidget)
        self.fButton.setGeometry(QtCore.QRect(170, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fButton.setFont(font)
        self.fButton.setObjectName("fButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(394, 360, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.trButton = QtWidgets.QPushButton(self.centralwidget)
        self.trButton.setGeometry(QtCore.QRect(20, 360, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trButton.setFont(font)
        self.trButton.setObjectName("trButton")
        self.enButton = QtWidgets.QPushButton(self.centralwidget)
        self.enButton.setGeometry(QtCore.QRect(90, 360, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enButton.setFont(font)
        self.enButton.setObjectName("enButton")
        self.kalanLabel = QtWidgets.QLabel(self.centralwidget)
        self.kalanLabel.setGeometry(QtCore.QRect(325, 30, 250, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.kalanLabel.setFont(font)
        self.kalanLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.kalanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kalanLabel.setObjectName("kalanLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        

        self.enButton.clicked.connect(self.enButtonWork)
        self.trButton.clicked.connect(self.trButtonWork)
        self.nextButton.clicked.connect(self.nextButtonWork)
        self.aButton.clicked.connect(lambda:self.answerButtonWork(self.aButton))
        self.bButton.clicked.connect(lambda:self.answerButtonWork(self.bButton))
        self.cButton.clicked.connect(lambda:self.answerButtonWork(self.cButton))
        self.dButton.clicked.connect(lambda:self.answerButtonWork(self.dButton))
        self.eButton.clicked.connect(lambda:self.answerButtonWork(self.eButton))
        self.fButton.clicked.connect(lambda:self.answerButtonWork(self.fButton))

        self.answerButtons = [self.aButton, self.bButton, self.cButton, self.dButton, self.eButton, self.fButton]

        self.readExcel()
        self.trQuestions()
        self.enQuestions()
        self.enButtonWork()
        self.setQuestion()

        self.enQuestion = True

        self.excel = load_workbook(filename = 'kelimeler.xlsx')
        self.sayfa = self.excel['Yanlışlar']
        for cell in range(2,len(self.enWords)):
            print(self.sayfa['B' + str(cell)].value)
            if self.sayfa['B' + str(cell)].value == None:
                self.savePoint = str(cell)
                break

        print(self.savePoint)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İngilizce-Türkçe Kelimeler"))
        self.soruLabel.setText(_translate("MainWindow", "simply dummy text"))
        self.aButton.setText(_translate("MainWindow", ""))
        self.bButton.setText(_translate("MainWindow", ""))
        self.cButton.setText(_translate("MainWindow", ""))
        self.dButton.setText(_translate("MainWindow", ""))
        self.nextButton.setText(_translate("MainWindow", "Sonraki Soru"))
        self.trButton.setText(_translate("MainWindow", "TR"))
        self.enButton.setText(_translate("MainWindow", "EN"))
        self.kalanLabel.setText(_translate("MainWindow", "Kalan Soru: 500"))

    def readExcel(self):
        self.data = pd.read_excel('kelimeler.xlsx', usecols=['İngilizce','Türkçe'], sheet_name=0)
        self.data = self.data.dropna()

    def enQuestions(self):
        self.enWords = self.data['İngilizce'].tolist()
        self.enQuestion = True
        print(len(self.enWords))

    def trQuestions(self):
        self.trWords = self.data['Türkçe'].tolist()
        self.enQuestion = False
        print(len(self.trWords))

    def setQuestion(self):
        if self.enQuestion == True:
            self.kalanLabel.setText("Kalan Soru: " + str(len(self.enWords)))
        else:
            self.kalanLabel.setText("Kalan Soru: " + str(len(self.trWords)))

        if len(self.enWords) == 0 or len(self.trWords) == 0 :
                self.soruLabel.setText('Sorular Bitti')
                for button in self.answerButtons:
                    button.setText('')
                    button.setEnabled(False)
                self.nextButton.setEnabled(False)

        else:

            if self.enQuestion == True:
                self.randomQuestion(self.enWords)
            else:
                self.randomQuestion(self.trWords)

            self.answerButtonFill()

    def randomQuestion(self,words): 
        secim = random.choice(words)
        print(type(secim))
        try:
            words.remove(True)
            print('Silindi true')
            words.remove(False)
            print('Silindi false')
        except:
            pass
        
        words.remove(secim)
        self.soruLabel.setText(str(secim))
        

    def trButtonWork(self):
        self.enQuestions()
        self.trQuestions()
        self.nextButtonWork()
        self.nextButton.setEnabled(True)
        self.trButton.setEnabled(False)
        self.enButton.setEnabled(True)
        self.trButton.setStyleSheet("background-color : #373333; color:white;")
        self.enButton.setStyleSheet("")

    def enButtonWork(self):
        self.trQuestions()
        self.enQuestions()
        self.nextButtonWork()
        self.nextButton.setEnabled(True)
        self.trButton.setEnabled(True)
        self.enButton.setEnabled(False)
        self.trButton.setStyleSheet("")
        self.enButton.setStyleSheet("background-color : #373333; color:white;")

    def nextButtonWork(self):
        for button in self.answerButtons:
            button.setStyleSheet("background-color : none")
            button.setEnabled(True)
        self.setQuestion()

    def answerButtonFill(self):
        print(self.soruLabel.text())
        if self.enQuestion == True:
            self.trueAnswer = self.data.loc[self.data['İngilizce'] == self.soruLabel.text(), 'Türkçe'].values[0]
        else:
            self.trueAnswer = self.data.loc[self.data['Türkçe'] == self.soruLabel.text(), 'İngilizce'].values[0]

        trueButton = random.choice(self.answerButtons)

        answers = self.randomAnswer() 
        
        say = 0
        for button in self.answerButtons:
            if button == trueButton:
                button.setText(str(self.trueAnswer))
            else:
                button.setText(str(answers[say]))
                say += 1
    
    def randomAnswer(self):
        if self.enQuestion == True:
            return random.sample(self.trWords,len(self.answerButtons)-1)
        else:
            return random.sample(self.enWords,len(self.answerButtons)-1)

    def answerButtonWork(self,button):
        for fbutton in self.answerButtons:
                fbutton.setEnabled(False)
                fbutton.setStyleSheet("background-color : #373333; color:white;")

        if button.text() == self.trueAnswer:
            button.setStyleSheet("background-color : green; color:white;")

        else:
            for fbutton in self.answerButtons:

                if fbutton.text() == self.trueAnswer:
                    fbutton.setStyleSheet("background-color : green; color:white;")

                if fbutton == button:
                    button.setStyleSheet("background-color : red; color:white;")
                    if self.enQuestion == True:
                        self.sayfa['B' + self.savePoint] = self.soruLabel.text()
                        self.sayfa['C' + self.savePoint] = self.trueAnswer
                    else:
                        self.sayfa['B' + self.savePoint] = self.trueAnswer 
                        self.sayfa['C' + self.savePoint] = self.soruLabel.text()
                    self.savePoint = str(int(self.savePoint) + 1)
                    


            self.excel.save(filename = 'kelimeler.xlsx')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())