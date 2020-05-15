import json
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QInputDialog, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Gui(QMainWindow):

    def __init__(self,parent=None):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("Ouvrir",self)
        openAct.triggered.connect(self.open)
        openAct.setShortcut('ctrl+O')
        openAct.setStatusTip('Ouvrir un fichier')

        recAct = QAction("Enregistrer",self)
        recAct.triggered.connect(self.rec)
        recAct.setShortcut('ctrl+S')
        recAct.setStatusTip('Enregistrer un fichier')


        quitAct = QAction("Quitter",self)
        quitAct.triggered.connect(self.exit)
        quitAct.setShortcut('ctrl+Q')
        quitAct.setStatusTip('Quitter')



        fichierMenu.addAction(openAct)
        fichierMenu.addAction(recAct)
        fichierMenu.addSeparator()
        fichierMenu.addAction(quitAct)

        self.setMinimumSize(1280, 720)

        self.setWindowTitle('Ravi Example')

        self.myWidget = MyTableWidget(self)

        self.setCentralWidget(self.myWidget)

        self.show()

    def open(self):
        print("open")

    def rec(self):
        print("rec")

    def exit(self):
        print("exit")
        self.quit


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()


        # Add tabs
        self.tabs.addTab(self.tab1, "Onglet 1")
        self.tabs.addTab(self.tab2, "Onglet 2")

        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("Nom ?")
        openButton.clicked.connect(self.openClick)

        self.tab1.layout.addWidget(openButton)
        self.tab1.setLayout(self.tab1.layout)


        #Tab 2:
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)

        self.tab2.layout = QHBoxLayout(self)
        self.tab2.layout.addWidget(self.tableWidget)
        self.tab1.setStyleSheet(_fromUtf8("background-image: url(./download.png); background-attachment: fixed"))

#(nom, prenom, date de naissance, sexe, taille, poid)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("nom ?"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Prenom ?"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Date de naissance ?"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Sexe ?"))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("Taille ?"))
        self.tableWidget.setItem(5, 0, QTableWidgetItem("Poid ?"))

        saveButton = QPushButton("Sauvegarde ?")
        saveButton.clicked.connect(self.saveClick)
        self.tab2.layout.addWidget(saveButton)

        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def saveClick(self):
        print("save")
        dictionnaire = {}

        if self.tableWidget.item(0,1):
            dictionnaire["nom"] = self.tableWidget.item(0,1).text()
        if self.tableWidget.item(1, 1):
            dictionnaire["Prenom"] = self.tableWidget.item(1, 1).text()
        if self.tableWidget.item(2, 1):
            dictionnaire["Date"] = self.tableWidget.item(2, 1).text()
        if self.tableWidget.item(3, 1):
            dictionnaire["Sexe"] = self.tableWidget.item(3, 1).text()
        if self.tableWidget.item(4, 1):
            dictionnaire["Taille"] = self.tableWidget.item(4, 1).text()
        if self.tableWidget.item(5, 1):
            dictionnaire["Poids"] = self.tableWidget.item(5, 1).text()

        print(dictionnaire)
        with open('data.json', 'w') as file:
            json.dump(dictionnaire, file)

    def openClick(self):
        print("click")
        nom,type = QInputDialog.getText(self,"input dialog","Votre Nom ?",QLineEdit.Normal,"")
        print(nom)