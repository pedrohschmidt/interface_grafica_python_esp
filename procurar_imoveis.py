# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'procurarImoveis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buscarImoveis(object):
    def setupUi(self, buscarImoveis):
        buscarImoveis.setObjectName("buscarImoveis")
        buscarImoveis.resize(1122, 877)
        self.spin_quartos = QtWidgets.QSpinBox(buscarImoveis)
        self.spin_quartos.setGeometry(QtCore.QRect(90, 90, 42, 22))
        self.spin_quartos.setObjectName("spin_quartos")
        self.label = QtWidgets.QLabel(buscarImoveis)
        self.label.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(buscarImoveis)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(buscarImoveis)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 71, 31))
        self.label_3.setObjectName("label_3")
        self.tbox_valorDeVenda = QtWidgets.QLineEdit(buscarImoveis)
        self.tbox_valorDeVenda.setGeometry(QtCore.QRect(550, 40, 71, 20))
        self.tbox_valorDeVenda.setObjectName("tbox_valorDeVenda")
        self.label_4 = QtWidgets.QLabel(buscarImoveis)
        self.label_4.setGeometry(QtCore.QRect(520, 40, 21, 16))
        self.label_4.setObjectName("label_4")
        self.cbox_tipoImovel = QtWidgets.QComboBox(buscarImoveis)
        self.cbox_tipoImovel.setGeometry(QtCore.QRect(110, 50, 131, 22))
        self.cbox_tipoImovel.setObjectName("cbox_tipoImovel")
        self.label_5 = QtWidgets.QLabel(buscarImoveis)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_5.setObjectName("label_5")
        self.cbox_vendaLocacao = QtWidgets.QComboBox(buscarImoveis)
        self.cbox_vendaLocacao.setGeometry(QtCore.QRect(370, 50, 121, 22))
        self.cbox_vendaLocacao.setObjectName("cbox_vendaLocacao")
        self.label_6 = QtWidgets.QLabel(buscarImoveis)
        self.label_6.setGeometry(QtCore.QRect(270, 50, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(buscarImoveis)
        self.label_7.setGeometry(QtCore.QRect(520, 70, 21, 16))
        self.label_7.setObjectName("label_7")
        self.tbox_valorAteVenda = QtWidgets.QLineEdit(buscarImoveis)
        self.tbox_valorAteVenda.setGeometry(QtCore.QRect(550, 70, 71, 20))
        self.tbox_valorAteVenda.setObjectName("tbox_valorAteVenda")
        self.label_8 = QtWidgets.QLabel(buscarImoveis)
        self.label_8.setGeometry(QtCore.QRect(560, 20, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(buscarImoveis)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 111, 31))
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(buscarImoveis)
        self.line.setGeometry(QtCore.QRect(20, 160, 1091, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tbox_valorAteAluguel = QtWidgets.QLineEdit(buscarImoveis)
        self.tbox_valorAteAluguel.setGeometry(QtCore.QRect(660, 70, 71, 20))
        self.tbox_valorAteAluguel.setObjectName("tbox_valorAteAluguel")
        self.tbox_valorDeAluguel = QtWidgets.QLineEdit(buscarImoveis)
        self.tbox_valorDeAluguel.setGeometry(QtCore.QRect(660, 40, 71, 20))
        self.tbox_valorDeAluguel.setObjectName("tbox_valorDeAluguel")
        self.label_10 = QtWidgets.QLabel(buscarImoveis)
        self.label_10.setGeometry(QtCore.QRect(670, 20, 101, 16))
        self.label_10.setObjectName("label_10")
        self.chbox_seguranca = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_seguranca.setGeometry(QtCore.QRect(200, 100, 131, 17))
        self.chbox_seguranca.setObjectName("chbox_seguranca")
        self.chbox_elevador = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_elevador.setGeometry(QtCore.QRect(200, 130, 131, 17))
        self.chbox_elevador.setObjectName("chbox_elevador")
        self.chbox_churrasqueira = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_churrasqueira.setGeometry(QtCore.QRect(340, 100, 131, 17))
        self.chbox_churrasqueira.setObjectName("chbox_churrasqueira")
        self.chbox_quadra = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_quadra.setGeometry(QtCore.QRect(340, 130, 131, 17))
        self.chbox_quadra.setObjectName("chbox_quadra")
        self.chbox_portaria = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_portaria.setGeometry(QtCore.QRect(440, 100, 101, 17))
        self.chbox_portaria.setObjectName("chbox_portaria")
        self.chbox_garagem = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_garagem.setGeometry(QtCore.QRect(440, 130, 101, 17))
        self.chbox_garagem.setObjectName("chbox_garagem")
        self.chbox_aceitaPets = QtWidgets.QCheckBox(buscarImoveis)
        self.chbox_aceitaPets.setGeometry(QtCore.QRect(110, 130, 81, 17))
        self.chbox_aceitaPets.setObjectName("chbox_aceitaPets")
        self.tb_resultados = QtWidgets.QTableView(buscarImoveis)
        self.tb_resultados.setGeometry(QtCore.QRect(20, 200, 1081, 631))
        self.tb_resultados.setObjectName("tb_resultados")
        self.btn_voltar = QtWidgets.QPushButton(buscarImoveis)
        self.btn_voltar.setGeometry(QtCore.QRect(1030, 840, 75, 23))
        self.btn_voltar.setObjectName("btn_voltar")

        self.retranslateUi(buscarImoveis)
        QtCore.QMetaObject.connectSlotsByName(buscarImoveis)

    def retranslateUi(self, buscarImoveis):
        _translate = QtCore.QCoreApplication.translate
        buscarImoveis.setWindowTitle(_translate("buscarImoveis", "Dialog"))
        self.label.setText(_translate("buscarImoveis", "Mais de "))
        self.label_2.setText(_translate("buscarImoveis", "quartos"))
        self.label_3.setText(_translate("buscarImoveis", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#363636;\">Filtros</span></p></body></html>"))
        self.label_4.setText(_translate("buscarImoveis", "De:"))
        self.label_5.setText(_translate("buscarImoveis", "Tipo de imóvel:"))
        self.label_6.setText(_translate("buscarImoveis", "Venda/Locação:"))
        self.label_7.setText(_translate("buscarImoveis", "Até:"))
        self.label_8.setText(_translate("buscarImoveis", "R$ Venda:"))
        self.label_9.setText(_translate("buscarImoveis", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#363636;\">Resultados</span></p><p><br/></p></body></html>"))
        self.label_10.setText(_translate("buscarImoveis", "R$ Aluguel:"))
        self.chbox_seguranca.setText(_translate("buscarImoveis", "Segurança / Vigilância"))
        self.chbox_elevador.setText(_translate("buscarImoveis", "Elevador"))
        self.chbox_churrasqueira.setText(_translate("buscarImoveis", "Churrasqueira"))
        self.chbox_quadra.setText(_translate("buscarImoveis", "Quadra"))
        self.chbox_portaria.setText(_translate("buscarImoveis", "Portaria 24h"))
        self.chbox_garagem.setText(_translate("buscarImoveis", "Garagem coberta"))
        self.chbox_aceitaPets.setText(_translate("buscarImoveis", "Aceita PETs"))
        self.btn_voltar.setText(_translate("buscarImoveis", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    buscarImoveis = QtWidgets.QDialog()
    ui = Ui_buscarImoveis()
    ui.setupUi(buscarImoveis)
    buscarImoveis.show()
    sys.exit(app.exec_())