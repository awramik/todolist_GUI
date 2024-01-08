from PyQt5.QtWidgets import QTableView, QPushButton, QHeaderView
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QGridLayout


class Ui_Widget(object):

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")

        # tabelaryczny widok danych
        self.widok = QTableView()

        # przyciski Push ###
        self.logujBtn = QPushButton("&Zaloguj")
        self.koniecBtn = QPushButton("&Koniec")
        self.dodajBtn = QPushButton("&Dodaj")
        self.dodajBtn.setEnabled(False)
        self.zapiszBtn = QPushButton("&Zapisz")
        self.zapiszBtn.setEnabled(False)

        # układ przycisków Push ###
        uklad = QHBoxLayout()
        uklad.addWidget(self.logujBtn)
        uklad.addWidget(self.dodajBtn)
        uklad.addWidget(self.zapiszBtn)
        uklad.addWidget(self.koniecBtn)

        # zmiana kolorów przycisków
        self.logujBtn.setStyleSheet("background-color: #a39081; color: #292522;")
        self.koniecBtn.setStyleSheet("background-color: #a39081; color: #292522;")
        self.dodajBtn.setStyleSheet("background-color: #a39081; color: #292522;")
        self.zapiszBtn.setStyleSheet("background-color: #a39081; color: #292522;")

        # główny układ okna ###
        ukladV = QVBoxLayout(self)
        ukladV.addWidget(self.widok)
        ukladV.addLayout(uklad)

        # właściwości widżetu ###
        self.setStyleSheet("background-color: #4d6160")
        self.setWindowTitle("To Do List App")
        self.resize(800, 500)



class LoginDialog(QDialog):
    """ Okno dialogowe logowania """
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Login')
        hasloLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # zmiana koloru dialogu

        # zmiana kolorów etykiet, pól edycyjnych
        loginLbl.setStyleSheet("color: #292522;")
        hasloLbl.setStyleSheet("color: #292522;")
        self.login.setStyleSheet("background-color: #a39081; color: #292522;")
        self.haslo.setStyleSheet("background-color: #a39081; color: #292522;")

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Logowanie')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, haslo = dialog.loginHaslo()
        return (login, haslo, ok == QDialog.Accepted)
