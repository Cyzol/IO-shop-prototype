import pkg_resources.py2_warn
from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

client = pymongo.MongoClient("mongodb://root:root@cluster0-shard-00-00-iguvt.mongodb.net:27017,cluster0-shard-00-01-iguvt.mongodb.net:27017,cluster0-shard-00-02-iguvt.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client["Sklep"]
col_zam = db["Zamowienia"]
col_pro = db["Produkty"]
class Ui_Form(object):
    def __init__(self,lista):
        self.lista = lista
        list = []
        self.lista_id = []
        self.lista_cen = []
        for index in range(lista.count()):
            list.append(lista.item(index).text())
            mydoc = col_pro.find_one({"Nazwa": list[index]})
            self.lista_id.append(mydoc["_id"])
            self.lista_cen.append(mydoc["Cena"])
        # print(self.lista_id)
        # print(self.lista_cen)


    def max_id(self):
        max_id = db.col_zam.find().sort({"_id":-1}).limit(1)
        print(max_id)


    def wypisz(self):
        imie = self.editimie.text()
        nazwisko = self.editnazwisko.text()
        ulica = self.ulicaedit.text()
        telefon = self.telefonedit.text()
        email = self.emailedit.text()
        kodpocztowy = self.editkodpocztowy.text()
        miasto = self.miastoedit.text()

        new_id = 0
        for x in col_zam.find({}, {"_id": 1}):
            new_id = x['_id']
        new_id = new_id + 1

        if (len(imie) <= 0 or imie[0:len(imie)].isalpha() == False):
            self.warning("Uzupelnij poprawnie Imie")
        else:
            if (len(nazwisko) <= 0 or nazwisko[0:len(nazwisko)].isalpha() == False):
                self.warning("Uzupelnij poprawnie Nazwisko")
            else:
                if (len(ulica) < 0):
                    self.warning("Uzupelnij poprawnie Ulice")
                else:
                    if (len(telefon) != 9 or telefon.isdigit() == False):
                        self.warning("Uzupelnij poprawnie numer telefonu( 9 cyfr)")
                    else:
                        if (len(email) < 0):
                            self.warning("Uzupelnij poprawnie Email")
                        else:
                            if (len(kodpocztowy) != 5 or kodpocztowy.isdigit() == False):
                                self.warning("Uzupelnij poprawnie Kod Pocztowy( 5 cyfr)")
                            else:
                                if (len(miasto) <= 0 or miasto[0:len(miasto)].isalpha() == False):
                                    self.warning("Uzupelnij poprawnie Miasto")
                                else:
                                    zamowienie = {"_id": new_id, "Imie": imie, "Nazwisko": nazwisko,
                                                  "Ulica": ulica, "Telefon": telefon, "Email": email,
                                                  "KodPocztowy": kodpocztowy, "Miasto": miasto,
                                                  "Produkty ": self.lista_id, "Kwota": round(sum(self.lista_cen),2)}
                                    col_zam.insert_one(zamowienie)
                                    self.warning("Zamówienie zostało złożone poprawnie, możesz wyjść z aplikacji")

    def warning(self,item):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(item)
        msg.exec_()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 695)
        Form.setStyleSheet("color: black;font-weight: bold;")

        self.email = QtWidgets.QLabel(Form)
        self.email.setGeometry(QtCore.QRect(40, 520, 51, 16))
        self.email.setObjectName("email")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(133, 20, 201, 21))
        self.title.setObjectName("title")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 640, 231, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: #fff;background-color: #FF8C00;border: none;border-radius: 15px;")
        self.pushButton.clicked.connect(self.wypisz)

        self.editnazwisko = QtWidgets.QLineEdit(Form)
        self.editnazwisko.setGeometry(QtCore.QRect(40, 390, 331, 20))
        self.editnazwisko.setObjectName("editnazwisko")

        self.editkodpocztowy = QtWidgets.QLineEdit(Form)
        self.editkodpocztowy.setGeometry(QtCore.QRect(40, 590, 121, 21))
        self.editkodpocztowy.setObjectName("editkodpocztowy")

        self.emailedit = QtWidgets.QLineEdit(Form)
        self.emailedit.setGeometry(QtCore.QRect(40, 540, 331, 20))
        self.emailedit.setObjectName("emailedit")

        self.kodPocztowy = QtWidgets.QLabel(Form)
        self.kodPocztowy.setGeometry(QtCore.QRect(40, 570, 81, 16))
        self.kodPocztowy.setObjectName("kodPocztowy")

        self.editimie = QtWidgets.QLineEdit(Form)
        self.editimie.setGeometry(QtCore.QRect(40, 330, 331, 20))
        self.editimie.setObjectName("editimie")

        self.Imie = QtWidgets.QLabel(Form)
        self.Imie.setGeometry(QtCore.QRect(40, 300, 131, 21))
        self.Imie.setObjectName("Imie")

        self.Ulica = QtWidgets.QLabel(Form)
        self.Ulica.setGeometry(QtCore.QRect(40, 420, 151, 16))
        self.Ulica.setObjectName("Ulica")

        self.Miasto = QtWidgets.QLabel(Form)
        self.Miasto.setGeometry(QtCore.QRect(180, 570, 71, 16))
        self.Miasto.setObjectName("Miasto")
        self.telefonedit = QtWidgets.QLineEdit(Form)
        self.telefonedit.setGeometry(QtCore.QRect(40, 490, 331, 20))
        self.telefonedit.setObjectName("telefonedit")
        self.Nazwisko = QtWidgets.QLabel(Form)
        self.Nazwisko.setGeometry(QtCore.QRect(40, 360, 141, 16))
        self.Nazwisko.setObjectName("Nazwisko")
        self.telefon = QtWidgets.QLabel(Form)
        self.telefon.setGeometry(QtCore.QRect(40, 470, 131, 16))
        self.telefon.setObjectName("telefon")
        self.ulicaedit = QtWidgets.QLineEdit(Form)
        self.ulicaedit.setGeometry(QtCore.QRect(40, 440, 331, 20))
        self.ulicaedit.setObjectName("ulicaedit")
        self.miastoedit = QtWidgets.QLineEdit(Form)
        self.miastoedit.setGeometry(QtCore.QRect(180, 590, 191, 21))
        self.miastoedit.setObjectName("miastoedit")
        self.label = QtWidgets.QLabel(Form)

        self.label.setGeometry(QtCore.QRect(103, 60, 200, 201))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-image: url(fruit2.png)")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(63, 70, 300, 200))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-image: url(logo.png)")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Konrad & Karol Shop"))
        self.email.setText(_translate("Form", "E-mail"))
        self.title.setText(_translate("Form", "SKŁADANIE ZAMÓWIENIA"))
        self.pushButton.setText(_translate("Form", "Złóż zamówienie"))
        self.kodPocztowy.setText(_translate("Form", "Kod pocztowy"))
        self.Imie.setText(_translate("Form", "Imie"))
        self.Ulica.setText(_translate("Form", "Ulica"))
        self.Miasto.setText(_translate("Form", "Miasto"))
        self.Nazwisko.setText(_translate("Form", "Nazwisko"))
        self.telefon.setText(_translate("Form", "Telefon"))
        # self.max_id()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form([])
    ui.setupUi(Form)
    Form.show()
    app.exec_()
