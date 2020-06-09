import pkg_resources.py2_warn
from PyQt5 import QtCore, QtGui, QtWidgets
from Formularz import Ui_Form
from Zamowienia import Ui_Form2
import pymongo
import numpy as np



client = pymongo.MongoClient("mongodb://root:root@cluster0-shard-00-00-iguvt.mongodb.net:27017,cluster0-shard-00-01-iguvt.mongodb.net:27017,cluster0-shard-00-02-iguvt.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["Sklep"]
collection = db["Produkty"]


global koszyk,suma,cena_do_usuniecia
koszyk = []
suma = 0.0
cena_do_usuniecia = 0.0

class Ui_MainWindow(object):

    def dodaj(self):
        item =self.listWidget.currentItem().text()
        if item != "" and item[0].isalpha():
            self.listWidget_2.addItem((item))
            mydoc = collection.find_one({"Nazwa":item})
            koszyk.append(float(mydoc["Cena"]))
            self.suma_koszyka()

    def suma_koszyka(self):
        suma = round(sum(koszyk),2)
        self.cena.setText(str(suma))

    def usun_z_koszyka(self):
        item = self.listWidget_2.currentItem()
        item2 = self.listWidget_2.currentItem().text()
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        mydoc2 = collection.find_one({"Nazwa": item2})
        cena_do_usuniecia = mydoc2["Cena"]
        koszyk.remove(cena_do_usuniecia)
        suma = round(sum(koszyk), 2)
        self.cena.setText(str(suma))

    def dodaj_kategorie(self):
        lista= []
        for x in collection.find({}):
            lista.append(x["Kategoria"])
        unikalne = np.unique(lista)
        for element in unikalne:
            self.combobox.addItem(element)

    def filtruj(self):
        filtr = self.combobox.currentText()
        self.listWidget.clear()
        for x in collection.find({"Kategoria" : filtr}):
            self.listWidget.addItem(x["Nazwa"])
            self.listWidget.addItem(str(x["Cena"]))

    def wszystko(self):
        self.listWidget.clear()
        self.refresh()

    def refresh(self):
        for x in collection.find({}):
            self.listWidget.addItem(x["Nazwa"])
            self.listWidget.addItem(str(x["Cena"]))

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form(self.listWidget_2)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def openWindow_zamowienia(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window)
        self.window.exec_()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("color: black;font-weight: bold;")

        self.Koszyk = QtWidgets.QLabel(self.centralwidget)
        self.Koszyk.setGeometry(QtCore.QRect(515,265, 131, 31))
        self.Koszyk.setObjectName("Koszyk")
        self.Koszyk.setStyleSheet("font-size : 20px")

        self.Produkty = QtWidgets.QLabel(self.centralwidget)
        self.Produkty.setGeometry(QtCore.QRect(150, 220, 131, 31))
        self.Produkty.setObjectName("Koszyk")
        self.Produkty.setStyleSheet("font-size : 20px")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 300, 351, 311))
        self.listWidget.setObjectName("listWidget")

        self.combobox = QtWidgets.QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(20,270,100,20))
        self.combobox.setObjectName("comboBox")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(420, 300, 256, 192))
        self.listWidget_2.setObjectName("listWidget_2")

        self.razemza = QtWidgets.QLabel(self.centralwidget)
        self.razemza.setGeometry(QtCore.QRect(420, 520, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.razemza.setFont(font)
        self.razemza.setObjectName("razemza")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 580, 231, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton.clicked.connect(self.openWindow)

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(35, 635, 150, 31))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton1.clicked.connect(self.dodaj)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(200, 635, 150, 31))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton2.clicked.connect(self.usun_z_koszyka)

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(220, 265, 70, 31))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton3.clicked.connect(self.filtruj)

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(300, 265, 70, 31))
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton4.clicked.connect(self.wszystko)

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(30, 30, 100, 31))
        self.pushButton5.setObjectName("pushButton")
        self.pushButton5.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton5.clicked.connect(self.openWindow_zamowienia)

        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(250, 20, 201, 201))
        self.img.setText("")
        self.img.setObjectName("img")
        self.img.setStyleSheet("background-image: url(fruit2.png);")

        self.cena = QtWidgets.QLabel(self.centralwidget)
        self.cena.setGeometry(QtCore.QRect(560, 520, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cena.setFont(font)
        self.cena.setObjectName("cena")


        self.img_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_2.setGeometry(QtCore.QRect(210, 20, 301, 201))
        self.img_2.setText("")
        self.img_2.setObjectName("img_2")
        self.img_2.setStyleSheet("background-image: url(logo.png);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.razemza.setText(_translate("MainWindow", "Razem za zakupy :"))
        self.pushButton.setText(_translate("MainWindow", "Przejdz do skladania zamowienia"))
        self.pushButton1.setText(_translate("MainWindow", "Dodaj do koszyka"))
        self.pushButton2.setText(_translate("MainWindow", "Usuń z koszyka"))
        self.pushButton3.setText(_translate("MainWindow", "Filtruj"))
        self.pushButton4.setText(_translate("MainWindow", "Wszystko"))
        self.pushButton5.setText(_translate("MainWindow", "Zamówienia"))
        self.cena.setText(_translate("MainWindow", ""))
        self.Koszyk.setText(_translate("MainWindow", "Koszyk"))
        self.Produkty.setText(_translate("MainWindow", "Produkty"))
        self.refresh()
        self.dodaj_kategorie()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
