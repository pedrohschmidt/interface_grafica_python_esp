from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Atualizar_usuario(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 407)
        self.tbox_name = QtWidgets.QLineEdit(Dialog)
        self.tbox_name.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.tbox_name.setObjectName("tbox_name")
        self.tbox_email = QtWidgets.QLineEdit(Dialog)
        self.tbox_email.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.tbox_email.setObjectName("tbox_email")
        self.tbox_senha = QtWidgets.QLineEdit(Dialog)
        self.tbox_senha.setGeometry(QtCore.QRect(150, 155, 113, 20))
        self.tbox_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tbox_senha.setObjectName("tbox_senha")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 165, 47, 13))
        self.label_3.setObjectName("label_3")
        self.tbox_confirma_senha = QtWidgets.QLineEdit(Dialog)
        self.tbox_confirma_senha.setGeometry(QtCore.QRect(150, 195, 113, 20))
        self.tbox_confirma_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tbox_confirma_senha.setObjectName("tbox_confirma_senha")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 101, 21))
        self.label_4.setObjectName("label_4")
        self.btn_atualizar_usuario = QtWidgets.QPushButton(Dialog)
        self.btn_atualizar_usuario.setGeometry(QtCore.QRect(180, 290, 121, 41))
        self.btn_atualizar_usuario.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_atualizar_usuario.setObjectName("btn_atualizar_usuario")
        self.lbl_status = QtWidgets.QLabel(Dialog)
        self.lbl_status.setGeometry(QtCore.QRect(56, 260, 311, 20))
        self.lbl_status.setText("")
        self.lbl_status.setObjectName("lbl_status")
        self.btn_voltar = QtWidgets.QPushButton(Dialog)
        self.btn_voltar.setGeometry(QtCore.QRect(30, 290, 121, 41))
        self.btn_voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_voltar.setObjectName("btn_voltar")
        self.cbox_tipoAcesso = QtWidgets.QComboBox(Dialog)
        self.cbox_tipoAcesso.setGeometry(QtCore.QRect(150, 120, 111, 22))
        self.cbox_tipoAcesso.setObjectName("cbox_tipoAcesso")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 126, 81, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nome: "))
        self.label_2.setText(_translate("Dialog", "Email:"))
        self.label_3.setText(_translate("Dialog", "Senha:"))
        self.label_4.setText(_translate("Dialog", "Confirme a senha:"))
        self.btn_atualizar_usuario.setText(_translate("Dialog", "Atualizar usuário"))
        self.btn_voltar.setText(_translate("Dialog", "Voltar"))
        self.label_5.setText(_translate("Dialog", "Tipo de acesso:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Atualizar_usuario()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
