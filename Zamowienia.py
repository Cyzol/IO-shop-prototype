import pkg_resources.py2_warn
from PyQt5 import QtCore, QtGui, QtWidgets

import pymongo
import numpy as np
client = pymongo.MongoClient("mongodb://root:root@cluster0-shard-00-00-iguvt.mongodb.net:27017,cluster0-shard-00-01-iguvt.mongodb.net:27017,cluster0-shard-00-02-iguvt.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["Sklep"]
collection = db["Zamowienia"]

class Ui_Form2(object):

    def dodaj_id(self):
        lista = []
        for x in collection.find({}):
            lista.append(x["_id"])
        unikalne = np.unique(lista)
        for element in unikalne:
            self.comboBox.addItem(str(element))


    def wyswietl(self):
        filtr = int(self.comboBox.currentText())

        for x in collection.find({"_id" : filtr}):
            self.Imieedit.setText(x["Imie"])
            self.Nazwiskoedit.setText(x["Nazwisko"])
            self.ulicaedit.setText(x["Ulica"])
            self.telefonedit.setText(x["Telefon"])
            self.emailedit.setText(x["Email"])
            self.kodpocztowyedit.setText(x["KodPocztowy"])
            self.miastoedit.setText(x["Miasto"])
            self.kwotaedit.setText(str(x["Kwota"]))



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 356)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 69, 22))
        self.comboBox.setObjectName("comboBox")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton.clicked.connect(self.wyswietl)

        self.idzamowienia = QtWidgets.QLabel(Form)
        self.idzamowienia.setGeometry(QtCore.QRect(10,10, 71, 21))
        self.idzamowienia.setObjectName("idzamowienia")

        self.Imie = QtWidgets.QLabel(Form)
        self.Imie.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.Imie.setObjectName("Imie")

        self.Nazwisko = QtWidgets.QLabel(Form)
        self.Nazwisko.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.Nazwisko.setObjectName("Nazwisko")

        self.Ulica = QtWidgets.QLabel(Form)
        self.Ulica.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.Ulica.setObjectName("Ulica")

        self.Telefon = QtWidgets.QLabel(Form)
        self.Telefon.setGeometry(QtCore.QRect(20, 180, 71, 21))
        self.Telefon.setObjectName("Telefon")

        self.Email = QtWidgets.QLabel(Form)
        self.Email.setGeometry(QtCore.QRect(20, 210, 71, 21))
        self.Email.setObjectName("Email")

        self.KodPocztowy = QtWidgets.QLabel(Form)
        self.KodPocztowy.setGeometry(QtCore.QRect(20, 240, 71, 21))
        self.KodPocztowy.setObjectName("KodPocztowy")

        self.Miasto = QtWidgets.QLabel(Form)
        self.Miasto.setGeometry(QtCore.QRect(20, 270, 71, 21))
        self.Miasto.setObjectName("Miasto")

        self.Kwota = QtWidgets.QLabel(Form)
        self.Kwota.setGeometry(QtCore.QRect(20, 300, 71, 21))
        self.Kwota.setObjectName("Kwota")


        self.Imieedit = QtWidgets.QLabel(Form)
        self.Imieedit.setGeometry(QtCore.QRect(150, 90, 181, 21))
        self.Imieedit.setObjectName("Imieedit")

        self.Nazwiskoedit = QtWidgets.QLabel(Form)
        self.Nazwiskoedit.setGeometry(QtCore.QRect(150, 120, 181, 21))
        self.Nazwiskoedit.setText("")
        self.Nazwiskoedit.setObjectName("Nazwiskoedit")

        self.ulicaedit = QtWidgets.QLabel(Form)
        self.ulicaedit.setGeometry(QtCore.QRect(150, 150, 181, 21))
        self.ulicaedit.setText("")
        self.ulicaedit.setObjectName("ulicaedit")

        self.telefonedit = QtWidgets.QLabel(Form)
        self.telefonedit.setGeometry(QtCore.QRect(150, 180, 181, 21))
        self.telefonedit.setText("")
        self.telefonedit.setObjectName("telefonedit")

        self.kodpocztowyedit = QtWidgets.QLabel(Form)
        self.kodpocztowyedit.setGeometry(QtCore.QRect(150, 240, 181, 21))
        self.kodpocztowyedit.setText("")
        self.kodpocztowyedit.setObjectName("kodpocztowyedit")

        self.miastoedit = QtWidgets.QLabel(Form)
        self.miastoedit.setGeometry(QtCore.QRect(150, 270, 181, 21))
        self.miastoedit.setText("")
        self.miastoedit.setObjectName("miastoedit")

        self.emailedit = QtWidgets.QLabel(Form)
        self.emailedit.setGeometry(QtCore.QRect(150, 210, 181, 21))
        self.emailedit.setText("")
        self.emailedit.setObjectName("emailedit")

        self.kwotaedit = QtWidgets.QLabel(Form)
        self.kwotaedit.setGeometry(QtCore.QRect(150, 300, 181, 21))
        self.kwotaedit.setText("")
        self.kwotaedit.setObjectName("kwotaedit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Znajdz"))
        self.Imie.setText(_translate("Form", "Imie : "))
        self.Nazwisko.setText(_translate("Form", "Nazwisko : "))
        self.Ulica.setText(_translate("Form", "Ulica : "))
        self.Telefon.setText(_translate("Form", "Telefon :"))
        self.Email.setText(_translate("Form", "E-mail : "))
        self.KodPocztowy.setText(_translate("Form", "Kod Pocztowy : "))
        self.Miasto.setText(_translate("Form", "Miasto : "))
        self.Kwota.setText(_translate("Form", "Kwota : "))
        self.idzamowienia.setText(_translate("Form", "ID Zamówienia"))
        self.dodaj_id()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
