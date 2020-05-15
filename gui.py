import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QInputDialog, QLineEdit, QHBoxLayout, QHeaderView
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.uic.properties import QtGui

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
        self.tab1.setStyleSheet(_fromUtf8("background-image: url(./download.png); background-attachment: fixed"))

        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(6)
        self.table.setItem(0, 0, QTableWidgetItem("Nom"))
        self.table.setItem(1, 0, QTableWidgetItem("Prénom"))
        self.table.setItem(2, 0, QTableWidgetItem("Date de naissance"))
        self.table.setItem(3, 0, QTableWidgetItem("Sexe"))
        self.table.setItem(4, 0, QTableWidgetItem("Taille"))
        self.table.setItem(5, 0, QTableWidgetItem("Poids"))

        # QWidget Layout
        self.tab2.layout = QVBoxLayout()

        #self.table_view.setSizePolicy(size)
        self.tab2.layout.addWidget(self.table)

        # Set the layout to the QWidget
        self.tab2.setLayout(self.tab2.layout)

        saveButton = QPushButton("Sauvegarder")
        saveButton.clicked.connect(self.save)

        self.tab2.layout.addWidget(saveButton)


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openClick(self):
        print("click")
        nom,type = QInputDialog.getText(self,"input dialog","Votre Nom ?",QLineEdit.Normal,"")
        print(nom)

    def save(self):
        print("Save")