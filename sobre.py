# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobre.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName("Sobre")
        Sobre.resize(1124, 504)
        self.btn_voltar = QtWidgets.QPushButton(Sobre)
        self.btn_voltar.setGeometry(QtCore.QRect(1020, 460, 81, 31))
        self.btn_voltar.setObjectName("btn_voltar")
        self.tbrowzer_Sobre = QtWidgets.QTextBrowser(Sobre)
        self.tbrowzer_Sobre.setGeometry(QtCore.QRect(40, 30, 1061, 411))
        self.tbrowzer_Sobre.setObjectName("tbrowzer_Sobre")

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        _translate = QtCore.QCoreApplication.translate
        Sobre.setWindowTitle(_translate("Sobre", "Dialog"))
        self.btn_voltar.setText(_translate("Sobre", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sobre = QtWidgets.QDialog()
    ui = Ui_Sobre()
    ui.setupUi(Sobre)
    Sobre.show()
    sys.exit(app.exec_())