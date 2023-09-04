
# converter ui para py:  pyuic5 -x tela_principal.ui -o tela_principal.py
# converter ui para py:  pyuic5 -x login.ui -o login.py
# converter ui para py:  pyuic5 -x criar_usuario.ui -o criar_usuario.py
# converter ui para py:  pyuic5 -x gerenciar_usuarios.ui -o gerenciar_usuarios.py
# converter ui para py: pyuic5 -x alterar_senha_adm.ui -o alterar_senha_adm.py
# converter ui para py: pyuic5 -x cadastrar_imovel.ui -o cadastrar_imovel.py
# converter ui para py: pyuic5 -x sobre.ui -o sobre.py
# converter ui para py:  pyuic5 -x procurarImoveis.ui -o procurar_imoveis.py

# pyrcc5 icons\\imagens.qrc -o imagens_rc.py
# para abrir o pyqt coloca 'designer' no terminal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow, QMessageBox
import sqlite3
from login import Ui_Dialog as tela_login
from tela_principal import Ui_MainWindow
from criar_usuario import Ui_Dialog
from atualizar_usuario import Ui_Atualizar_usuario
from gerenciar_usuarios import Ui_gerenciarUsuarios
from cadastrar_imovel import Ui_Cadastrar_Imovel
from procurar_imoveis import Ui_buscarImoveis
from sobre import Ui_Sobre
import os, sys
import pandas as pd
import brazilcep
from brazilcep.exceptions import CEPNotFound, BlockedByFlood
def conexao():
    conn = sqlite3.connect("PHSN_IMOBILIARIA.db")
    cursor = conn.cursor()
    return conn, cursor

def verificar_bd():
    # Conecta no banco de dados
    conn, cursor = conexao()
    # Os códigos abaixo são para criar o bd no primeiro acesso, caso ele não exista. Não precisaria manter no código depois de colocar em produção

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tb_acessos'")
    tabela_existe = cursor.fetchone()
    if tabela_existe:
        print("A tabela de acessos já existe no banco de dados, proseguindo com as demais rotinas.")
    else:
        # se não existe a tb com os dados de acesso, cria e add um usuário admin para teste
        cursor.execute('''CREATE TABLE IF NOT EXISTS tb_acessos (
                             email TEXT PRIMARY KEY,
                             nome TEXT NOT NULL,
                             tipo_acesso TEXT NOT NULL,
                             senha TEXT NOT NULL
                         )''')


        # cria dois usuários iniciais para poder testar a aplicação
        # usuario adm
        admin_email = "admin@phsn.com.br"
        admin_password = "admin1234"
        admin_nome = "Administrador"
        tipo_acesso = "administrador"

        cursor.execute("INSERT OR REPLACE INTO tb_acessos (email, nome, tipo_acesso, senha) VALUES (?, ?, ?,?)", (admin_email, admin_nome, tipo_acesso, admin_password))
        # usuario padrao
        admin_email = "user@phsn.com.br"
        admin_password = "user1234"
        admin_nome = "Usuário Padrão"
        tipo_acesso = "usuario"

        cursor.execute("INSERT OR REPLACE INTO tb_acessos (email, nome, tipo_acesso, senha) VALUES (?, ?, ?,?)",
                       (admin_email, admin_nome, tipo_acesso, admin_password))


    # Cria a tabela de imoveis se ela não existir no bd
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tb_imoveis'")
    tabela_existe = cursor.fetchone()
    if tabela_existe:
        print("A tabela de imóveis já existe no banco de dados, proseguindo com as demais rotinas.")
    else:
        cursor.execute('''CREATE TABLE IF NOT EXISTS tb_imoveis (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TIPO_NEGOCIACAO TEXT NOT NULL,
                        ESTADO TEXT,
                        CIDADE TEXT,
                        BAIRRO TEXT,
                        CEP TEXT,
                        ENDERECO TEXT NOT NULL,
                        COMPLEMENTO TEXT,
                        DESCRICAO TEXT NOT NULL,
                        TIPO_IMOVEL TEXT NOT NULL,
                        DETALHES TEXT,
                        VALOR_VENDA REAL,
                        VALOR_ALUGUEL REAL,
                        VAGAS_GARAGEM INTEGER,
                        QUARTOS INTEGER,
                        OBSERVACAO TEXT,
                        IDADE_IMOVEL TEXT,
                        SEGURANCA INTEGER,
                        ELEVADOR INTEGER,
                        CHURRASQUEIRA INTEGER,
                        QUADRA INTEGER,
                        PORTARIA INTEGER,
                        GARAGEM_COBERTA INTEGER,
                        ACEITA_PET INTEGER,
                        DATA_REGISTRO DATETIME DEFAULT CURRENT_TIMESTAMP
                         )''')

        #Add três imóveis para teste
        cursor.execute("""
            INSERT INTO tb_imoveis (TIPO_NEGOCIACAO, ESTADO, CIDADE, BAIRRO, CEP, ENDERECO, COMPLEMENTO, DESCRICAO, TIPO_IMOVEL, DETALHES, VALOR_VENDA, VALOR_ALUGUEL, VAGAS_GARAGEM, QUARTOS, OBSERVACAO, IDADE_IMOVEL, SEGURANCA, ELEVADOR, CHURRASQUEIRA, QUADRA, PORTARIA, GARAGEM_COBERTA, ACEITA_PET)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
        'VENDA/LOCAÇÃO', 'PR', 'CURITIBA', 'XAXIM', '01234-567', 'Rua Teste 123', 'Apto 101', 'Apartamento amplo',
        'CASA', 'Com varanda', 300000.00, None, 1, 2, 'Nenhum', 'ATÉ 5 ANOS',1,1,0,0,0,0,1))

        # Inserir o segundo registro
        cursor.execute("""
            INSERT INTO tb_imoveis (TIPO_NEGOCIACAO, ESTADO, CIDADE, BAIRRO, CEP, ENDERECO, COMPLEMENTO, DESCRICAO, TIPO_IMOVEL, DETALHES, VALOR_VENDA, VALOR_ALUGUEL, VAGAS_GARAGEM, QUARTOS, OBSERVACAO, IDADE_IMOVEL, SEGURANCA, ELEVADOR, CHURRASQUEIRA, QUADRA, PORTARIA, GARAGEM_COBERTA, ACEITA_PET)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ('LOCAÇÃO', 'PR', 'CURITIBA', 'SANTA QUITERIA', '04567-890', 'Avenida Principal 456', None,
              'Apartamento com vista para o mar', 'APARTAMENTO', 'Mobiliado', None, 2500.00, 1, 1,
              'Aceita animais de estimação', 'ATÉ 20 ANOS',0,0,0,1,0,1,1))

        # Inserir o terceiro registro
        cursor.execute("""
            INSERT INTO tb_imoveis (TIPO_NEGOCIACAO, ESTADO, CIDADE, BAIRRO, CEP, ENDERECO, COMPLEMENTO, DESCRICAO, TIPO_IMOVEL, DETALHES, VALOR_VENDA, VALOR_ALUGUEL, VAGAS_GARAGEM, QUARTOS, OBSERVACAO, IDADE_IMOVEL, SEGURANCA, ELEVADOR, CHURRASQUEIRA, QUADRA, PORTARIA, GARAGEM_COBERTA, ACEITA_PET)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ('VENDA', 'PR', 'CURITIBA', 'BAIRRO NOVO', '09876-543', 'Rua Principal 789', 'Apto 205',
              'Casa espaçosa com quintal', 'CASA', 'Quintal grande', 500000.00, None, None, 3, 'Próximo ao metrô', 'BREVE LANÇAMENTO',0,1,1,0,0,1,0))


    # salva
    print("Banco de dados verificado com sucesso. Acessando informação!")
    conn.commit()
    conn.close()


class MenuPrincipal(QMainWindow):
    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(MenuPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.email_acesso = email_acesso
        self.tipo_acesso = tipo_acesso
        self.ui.lbl_userLogado.setText(f"Seja bem-vindo, {self.nome_bd}")
        self.ui.menu_Gerenciar_Usuarios.triggered.connect(self.gerenciar_usuarios)
        self.ui.actionCadastrar_Imovel.triggered.connect(self.cadastrar_imovel)
        self.ui.actionSobre.triggered.connect(self.sobre)
        self.ui.actionBuscar_Imovel.triggered.connect(self.filtrar_imovel)

    def filtrar_imovel(self):

        self.hide()  # Hide the login window
        self.busca = procurarImoveis(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.busca.show()
    def sobre(self):
        self.hide()  # Hide the login window
        self.menu_sobre = sobre(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_sobre.show()
    def cadastrar_imovel(self):
        self.hide()  # Hide the login window
        self.cadastrar_imoveis = cadastrarImovel(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.cadastrar_imoveis.show()

    def gerenciar_usuarios(self):
        self.hide()  # Hide the login window
        self.gerenciar_users = gerenciarUsuarios(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.gerenciar_users.show()

class gerenciarUsuarios(QDialog):
    def connect_buttons(self):
        self.ui.btn_addUsuario.clicked.connect(self.add_usuarios)
        self.ui.btn_removerUsuario.clicked.connect(self.remover_usuario_selecionado)
        self.ui.btn_voltar.clicked.connect(self.voltar_gerenciar_usuarios)
        self.ui.btn_atualizarUsuario.clicked.connect(self.atualizar_usuario)
    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(gerenciarUsuarios, self).__init__(*args, **argvs)
        self.ui = Ui_gerenciarUsuarios()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.email_acesso = email_acesso
        self.tipo_acesso = tipo_acesso
        self.list_model = QtGui.QStandardItemModel()
        self.ui.lview_usuarios.setModel(self.list_model)
        self.connect_buttons()

        if self.tipo_acesso != "administrador":
            #Bloqueia a deleção de usuários
            self.ui.lview_usuarios.setEnabled(False)

            # Bloqueia a criação de usuários
            self.ui.btn_addUsuario.setEnabled(False)

            #Bloqueia a remoção de usuários
            self.ui.btn_removerUsuario.setEnabled(False)

        else:
            #Se for adm, carrega a lista de usuarios
            lista_usuarios = consultar_usuarios()
            for usuario in lista_usuarios:
                email = usuario[0]
                item = QtGui.QStandardItem(email)
                self.list_model.appendRow(item)

    def atualizar_usuario(self):
        selected_indexes = self.ui.lview_usuarios.selectedIndexes()
        # Verifica se algum item foi selecionado
        if self.tipo_acesso == "administrador":
            selected_index = selected_indexes[0]
            item_selecionado = self.list_model.itemFromIndex(selected_index)
            email_selecionado = item_selecionado.text()
        else:

            email_selecionado = self.email_acesso
        email, nome, senha, tipo_acesso = consultar_usuario_especifico(email_selecionado)

        self.form_cadastro = atualizarUsuario(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.form_cadastro.preencher_campos(email, nome, senha, tipo_acesso)  # Preenche os campos
        self.form_cadastro.show()
        self.hide()

    def voltar_gerenciar_usuarios(self):
        #volta para o menu anterior
        self.hide()
        self.menu_inicial = MenuPrincipal(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_inicial.show()

    def remover_usuario_selecionado(self):
        selected_indexes = self.ui.lview_usuarios.selectedIndexes()
        # Verifica se algum item foi selecionado
        if selected_indexes:
            selected_index = selected_indexes[0]
            item_selecionado = self.list_model.itemFromIndex(selected_index)
            if item_selecionado:
                #Verificar se a pessoa tem certeza
                resposta = QtWidgets.QMessageBox.question(
                    self,
                    'Remover Usuário',
                    'Você tem certeza que deseja remover este usuário? \nNão será possível desfazer esta ação!',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No
                )
                if resposta ==QtWidgets.QMessageBox.Yes:
                    # Se a respsota for sim, verifica a quantidade de usuarios adm ficariam
                    # Não permite se o bd não tiver pelo menos um usuario adm depois da exclusao
                    email = str(item_selecionado.text())
                    if consultar_usuario_especifico(email)[3] == 'administrador':
                        contador = contar_adm()
                        if contador == 1:
                            QMessageBox.warning(self, "Aviso", "Você precisa de ao menos um usuário adm na aplicação, portanto \nnão podemos remover este usuário.", QMessageBox.Ok)
                        else:
                            deletar_usuario_especifico(email)
                            self.list_model.removeRow(self.ui.lview_usuarios.currentIndex().row())
                            QMessageBox.warning(self, "Aviso", f"Usuário {email} removido com sucesso!", QMessageBox.Ok)

                    else:
                        deletar_usuario_especifico(email)
                        self.list_model.removeRow(self.ui.lview_usuarios.currentIndex().row())
                        QMessageBox.warning(self, "Aviso", f"Usuário {email} removido com sucesso!..", QMessageBox.Ok)

                else:
                    # Se a resposta for não, cancela
                    print(f'Remoção cancelada!')

    def add_usuarios(self):
        self.hide()  # Hide the login window
        self.menu_cadastro = cadastrarUsuario(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_cadastro.show()

class sobre(QDialog):
    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(sobre, self).__init__(*args, **argvs)
        self.ui = Ui_Sobre()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.email_acesso = email_acesso
        self.ui.btn_voltar.clicked.connect(self.voltar)

        with open('README.md', 'r', encoding='utf-8') as file:
            readme_content = file.read()
            self.ui.tbrowzer_Sobre.setHtml(readme_content)


    def voltar(self):
        self.hide()  # Hide the login window
        self.menu_inicial = MenuPrincipal(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_inicial.show()

class cadastrarImovel(QDialog):
    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(cadastrarImovel, self).__init__(*args, **argvs)
        self.ui = Ui_Cadastrar_Imovel()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.email_acesso = email_acesso
        self.ui.cbox_negociacao.addItems(["VENDA","LOCAÇÃO", "VENDA/LOCAÇÃO"])
        self.ui.cbox_tipo_imovel.addItems(["APARTAMENTO", "CASA", "TERRENO"])
        self.ui.cbox_idade_imovel.addItems(["EM CONSTRUÇÃO", "BREVE LANÇAMENTO", "ATÉ 5 ANOS", "ATÉ 10 ANOS", "ATÉ 20 ANOS", "ATÉ 50 ANOS", "MAIS DE 50 ANOS"])
        self.ui.btn_cadastrar.clicked.connect(self.inserir_imovel)
        self.ui.btn_buscarCEP.clicked.connect(self.buscar_cep)
        self.ui.btn_voltar.clicked.connect(self.voltar)
    def voltar(self):
        self.hide()  # Hide the login window
        self.menu_inicial = MenuPrincipal(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_inicial.show()
    def buscar_cep(self):
        cep = self.ui.tbox_cep.text()

        try:
            endereco = brazilcep.get_address_from_cep(cep)
            # Se o cep for encontrado, preenche as textbox de endereco com os dados do endereco
            bairro = endereco['district']
            cidade = endereco['city']
            rua = endereco['street']
            estado = endereco['uf']

            self.ui.tbox_bairro.setText(bairro)
            self.ui.tbox_cidade.setText(cidade)
            self.ui.tbox_estado.setText(estado)
            self.ui.tbox_endereco.setText(rua)

            QMessageBox.warning(self, "Aviso", f"CEP encontrado, verifique o número do endereço do imóvel.", QMessageBox.Ok)

        except CEPNotFound:
            # Se não for encontrado, libera o campo para que seja preenchido manualmente
            QMessageBox.warning(self, "Aviso", f"CEP não encontrado. Inclua o endereço manualmente.", QMessageBox.Ok)
            self.ui.tbox_bairro.setEnabled(True)
            self.ui.tbox_cidade.setEnabled(True)
            self.ui.tbox_estado.setEnabled(True)

        except BlockedByFlood:
            # Se não for encontrado, libera o campo para que seja preenchido manualmente
            QMessageBox.warning(self, "Aviso", "Muitas consultas de CEP em um curto período. Preencha o endereço manualmente.", QMessageBox.Ok)
            self.ui.tbox_bairro.setEnabled(True)
            self.ui.tbox_cidade.setEnabled(True)
            self.ui.tbox_estado.setEnabled(True)
    def inserir_imovel(self):



        tipo_negociacao = self.ui.cbox_negociacao.currentText()
        estado = self.ui.tbox_estado.text().upper()
        cidade = self.ui.tbox_cidade.text()
        bairro = self.ui.tbox_bairro.text()
        cep = self.ui.tbox_cep.text()
        endereco = self.ui.tbox_endereco.text()
        complemento = self.ui.tbox_complemento.text()
        descricao = self.ui.tbox_descricao.toPlainText()
        tipo_imovel = self.ui.cbox_tipo_imovel.currentText()
        detalhes = self.ui.tbox_detalhes.toPlainText()
        valor_venda = converter_para_zero(self.ui.tbox_valor_venda.text())
        valor_locacao = converter_para_zero(self.ui.tbox_valor_locacao.text())
        vagas = int(self.ui.spin_vagas.value())
        quartos = int(self.ui.spin_quartos.value())
        observacao = self.ui.tbox_observacao.toPlainText()
        idade_imovel = self.ui.cbox_idade_imovel.currentText()
        seguranca = self.ui.chbox_seguranca.isChecked()
        elevador = self.ui.chbox_elevador.isChecked()
        churrasqueira = self.ui.chbox_churrasqueira.isChecked()
        quadra = self.ui.chbox_quadra.isChecked()
        portaria = self.ui.chbox_portaria.isChecked()
        garagem_coberta = self.ui.chbox_garagem.isChecked()
        aceita_pet = self.ui.chbox_aceita_pet.isChecked()



        # Em vez de fazer a validação com if/elif, achei que ficava mais organizado fazer dentro de outra função, diferente do que fiz no login
        def validar_dados(estado, cidade, endereco, descricao, quartos, valor_venda, valor_locacao, tipo_negociacao, tipo_imovel):
            if endereco == '':
                QMessageBox.warning(self, "Aviso", "O campo de ENDEREÇO não pode estar vazio.", QMessageBox.Ok)
                return False

            if cidade == '':
                QMessageBox.warning(self, "Aviso", "O campo de CIDADE não pode estar vazio.", QMessageBox.Ok)
                return False

            if estado == '':
                QMessageBox.warning(self, "Aviso", "O campo de ESTADO não pode estar vazio.", QMessageBox.Ok)
                return False
            if descricao == '':
                QMessageBox.warning(self, "Aviso", "O campo de DESCRIÇÃO não pode estar vazio.", QMessageBox.Ok)
                return False
            if tipo_imovel != 'TERRENO' and quartos == 0:
                QMessageBox.warning(self, "Aviso", f"Você não pode ter um imóvel do tipo {tipo_imovel} com zero quartos. Por favor, verifique.", QMessageBox.Ok)
                return False
            if 'VENDA' in tipo_negociacao and valor_venda == 0:
                QMessageBox.warning(self, "Aviso", f"Você não pode ter um valor de VENDA vazio/zerado para uma negociação do tipo {tipo_negociacao}.\nInsira um valor de venda e tente novamente.", QMessageBox.Ok)
                return False
            if 'LOCAÇÃO' in tipo_negociacao and valor_locacao == 0:
                QMessageBox.warning(self, "Aviso", f"Você não pode ter um valor de LOCAÇÃO vazio/zerado para uma negociação do tipo {tipo_negociacao}.\nInsira um valor de locação e tente novamente.", QMessageBox.Ok)
                return False
            return True

        # Se a validação passar em todos os campos, insere os dados
        if validar_dados(estado, cidade, endereco, descricao, quartos, valor_venda, valor_locacao, tipo_negociacao, tipo_imovel):
            # Ajuste do campo de quartos
            if tipo_imovel == 'TERRENO':
                quartos = 0

            # Faz a inserção do registro
            conn, cursor = conexao()
            cursor.execute("""
                INSERT INTO tb_imoveis (TIPO_NEGOCIACAO, ESTADO, CIDADE, BAIRRO, CEP, ENDERECO, COMPLEMENTO, DESCRICAO, TIPO_IMOVEL, DETALHES, VALOR_VENDA, VALOR_ALUGUEL, VAGAS_GARAGEM, QUARTOS, OBSERVACAO, IDADE_IMOVEL, SEGURANCA, ELEVADOR, CHURRASQUEIRA, QUADRA, PORTARIA, GARAGEM_COBERTA, ACEITA_PET)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (tipo_negociacao, estado, cidade, bairro, cep, endereco, complemento,
                  descricao, tipo_imovel, detalhes, valor_venda, valor_locacao, vagas, quartos, observacao,
                  idade_imovel, seguranca, elevador, churrasqueira, quadra, portaria, garagem_coberta, aceita_pet))


            #Avisa que o registro foi inserido com sucesso
            QMessageBox.warning(self, "Aviso","Imóvel cadastrado com sucesso!.", QMessageBox.Ok)

class procurarImoveis(QDialog):
    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(procurarImoveis, self).__init__(*args, **argvs)
        self.ui = Ui_buscarImoveis()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.email_acesso = email_acesso
        #pegando todos os imoveis para usar no filtro
        self.df_imoveis = None
        todos_imoveis = get_imoveis()
        colunas = ['ID', 'TIPO_NEGOCIACAO', 'ESTADO', 'CIDADE', 'BAIRRO', 'CEP', 'ENDERECO', 'COMPLEMENTO', 'DESCRICAO',
                   'TIPO_IMOVEL',
                   'DETALHES', 'VALOR_VENDA', 'VALOR_ALUGUEL', 'VAGAS_GARAGEM', 'QUARTOS', 'OBSERVACAO', 'IDADE_IMOVEL',
                   'SEGURANCA', 'ELEVADOR', 'CHURRASQUEIRA',
                   'QUADRA', 'PORTARIA', 'GARAGEM_COBERTA', 'ACEITA_PET', 'DATA REGISTRO']

        self.df_imoveis = pd.DataFrame(todos_imoveis, columns=colunas)
        #self.ui.btn_procurar.clicked.connect(self.filtrar_imoveis)
        self.ui.cbox_tipoImovel.addItems(["APARTAMENTO", "CASA", "TERRENO"])
        self.ui.cbox_vendaLocacao.addItems(["VENDA", "LOCAÇÃO"])
        #define que cada vez que um cbox mudar o status, a consulta é refeita, pra não precisar ter um botão
        #comboboxes
        self.ui.cbox_tipoImovel.currentIndexChanged.connect(self.filtrar_imoveis)
        self.ui.cbox_vendaLocacao.currentIndexChanged.connect(self.filtrar_imoveis)
        #Textboxes
        self.ui.tbox_valorAteAluguel.textChanged.connect(self.filtrar_imoveis)
        self.ui.tbox_valorDeAluguel.textChanged.connect(self.filtrar_imoveis)
        self.ui.tbox_valorDeVenda.textChanged.connect(self.filtrar_imoveis)
        self.ui.tbox_valorAteVenda.textChanged.connect(self.filtrar_imoveis)
        #Checkboxes
        self.ui.chbox_quadra.stateChanged.connect(self.filtrar_imoveis)
        self.ui.chbox_garagem.stateChanged.connect(self.filtrar_imoveis)
        self.ui.chbox_elevador.stateChanged.connect(self.filtrar_imoveis)
        self.ui.chbox_aceitaPets.stateChanged.connect(self.filtrar_imoveis)
        self.ui.chbox_portaria.stateChanged.connect(self.filtrar_imoveis)
        self.ui.chbox_churrasqueira.stateChanged.connect(self.filtrar_imoveis)
        self.ui.chbox_seguranca.stateChanged.connect(self.filtrar_imoveis)
        self.ui.spin_quartos.valueChanged.connect(self.filtrar_imoveis)
        self.ui.btn_voltar.clicked.connect(self.voltar)

        #define rotina para quando clicar duas vezes em um item
        self.ui.tb_resultados.doubleClicked.connect(self.mostrar_detalhes)

    def mostrar_detalhes(self, index):
        selected_row = index.row()
        print(self.model.data(self.model.index(selected_row, 0)))
    def voltar(self):
        self.hide()  # Hide the login window
        self.menu_inicial = MenuPrincipal(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_inicial.show()

    def filtrar_imoveis(self):

        # atribuindo campos a variáveis e definindo quais os filtros. f1 = filtro1
        tipo_imovel = self.ui.cbox_tipoImovel.currentText()
        tipo_negociacao = self.ui.cbox_vendaLocacao.currentText()
        min_venda = converter_para_zero(self.ui.tbox_valorDeVenda.text())
        max_venda = converter_para_zero(self.ui.tbox_valorAteVenda.text())
        min_aluguel = converter_para_zero(self.ui.tbox_valorDeAluguel.text())
        max_aluguel = converter_para_zero(self.ui.tbox_valorAteAluguel.text())
        min_quartos = converter_para_zero(self.ui.spin_quartos.value())

        #Esses filtros são feitos sempre, independente de qualquerr coisa

        df_filtro = self.df_imoveis.loc[(self.df_imoveis['QUARTOS'] >= min_quartos) & (self.df_imoveis['TIPO_NEGOCIACAO'].str.contains(tipo_negociacao, case=False, na=False)) & (self.df_imoveis['TIPO_IMOVEL'] == tipo_imovel)]
        df_filtro = df_filtro.loc[df_filtro['ID'].notna()]
        # Verifica quais filtros secundários serão feitos e atualiza o filtro
        if 'VENDA' in tipo_negociacao:

            if min_venda > 0:
                df_filtro = df_filtro.loc[(df_filtro['VALOR_VENDA'] >= min_venda)]
            if max_venda > 0:
                df_filtro = df_filtro.loc[(df_filtro['VALOR_VENDA'] <= max_venda)]

        if 'LOCAÇÃO' in tipo_negociacao:

            if min_aluguel > 0:
                df_filtro = df_filtro.loc[(df_filtro['VALOR_ALUGUEL'] >= min_aluguel)]
            if max_venda > 0:
                df_filtro = df_filtro.loc[(df_filtro['VALOR_ALUGUEL'] <= max_aluguel)]


        if self.ui.chbox_seguranca.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['SEGURANCA'] == 1)]

        if self.ui.chbox_churrasqueira.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['CHURRASQUEIRA'] == 1)]

        if self.ui.chbox_portaria.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['PORTARIA'] == 1)]

        if self.ui.chbox_aceitaPets.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['ACEITA_PET'] == 1)]

        if self.ui.chbox_elevador.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['ELEVADOR'] == 1)]

        if self.ui.chbox_quadra.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['QUADRA'] == 1)]

        if self.ui.chbox_garagem.isChecked():
            df_filtro = df_filtro.loc[(df_filtro['GARAGEM_COBERTA'] == 1)]

        if df_filtro is None:
            print("Nenhum imóvel encontrado com estes parâmetros. Experimente mexer nos filtros!")
        else:
            # se encontrar resultados com o filtro desejado, exibe na tabela
            #colunas_resumidas = ['ID', 'TIPO_IMOVEL', 'QUARTOS', 'TIPO_NEGOCIACAO','IDADE_IMOVEL', 'ESTADO', 'CIDADE', 'BAIRRO', 'ENDERECO']

            #df_resumido = df_filtro[colunas_resumidas]
            df_resumido = df_filtro
            model = QStandardItemModel(self)
            model.setHorizontalHeaderLabels(df_resumido.columns)
            # Preencher a tabela com os dados do DataFrame
            for row_index, row_data in df_resumido.iterrows():
                for col_index, col_value in enumerate(row_data):
                    item = QStandardItem(str(col_value))  # Correção aqui
                    model.setItem(row_index, col_index, item)
            self.ui.tb_resultados.setModel(model)
            # corrige o tamanho das colunas de acordo com o conteúdo
            self.ui.tb_resultados.resizeColumnsToContents()


class atualizarUsuario(QDialog):

    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(atualizarUsuario, self).__init__(*args, **argvs)
        self.ui = Ui_Atualizar_usuario()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.email_acesso = email_acesso
        self.ui.cbox_tipoAcesso.addItems(["administrador", "usuario"])
        self.ui.btn_atualizar_usuario.clicked.connect(self.atualizar_usuario)
        self.ui.btn_voltar.clicked.connect(self.voltar)
        self.ui.tbox_email.setEnabled(False)
        if tipo_acesso == 'administrador':
            self.ui.cbox_tipoAcesso.setEnabled(True)
        else:
            self.ui.cbox_tipoAcesso.setEnabled(False)
    def atualizar_usuario(self):
        input_nome = self.ui.tbox_name.text()
        input_senha = self.ui.tbox_senha.text()
        input_conf_senha = self.ui.tbox_confirma_senha.text()
        input_tipo_acesso = self.ui.cbox_tipoAcesso.currentText()
        input_email = self.ui.tbox_email.text()


        if not input_nome:
            QMessageBox.warning(self, "Aviso", "Você não pode deixar um usuário sem nome", QMessageBox.Ok)
        elif not input_senha:
            QMessageBox.warning(self, "Aviso", "Você não pode deixar um usuário sem senha", QMessageBox.Ok)
        elif input_senha != input_conf_senha:
            QMessageBox.warning(self, "Aviso", "A senha inserida no campo 'senha' e a senha inserida no campo \nde 'confirmação de senha' não coincidem", QMessageBox.Ok)
        else:
            atualizar_usuario_especifico(input_email, input_nome, input_senha, input_tipo_acesso)
            QMessageBox.warning(self, "Aviso", "Usuário atualizado com sucesso", QMessageBox.Ok)

    def voltar(self):
        self.hide()  # Hide the login window
        self.gerenciar_users = gerenciarUsuarios(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.gerenciar_users.show()


    def preencher_campos(self, email, nome, senha, tipo_acesso):
        #caso o usuário já exista, para podermos usar o mesmo form para atualização/criação
        self.ui.tbox_name.setText(nome)
        self.ui.tbox_email.setText(email)
        self.ui.tbox_senha.setText(senha)
        self.ui.tbox_confirma_senha.setText(senha)
        self.ui.cbox_tipoAcesso.setCurrentText(tipo_acesso)


class cadastrarUsuario(QDialog):
    def __init__(self, nome_bd, tipo_acesso, email_acesso, *args, **argvs):
        super(cadastrarUsuario, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.email_acesso = email_acesso
        self.ui.cbox_tipoAcesso.addItems(["administrador", "usuario"])

        #add uma funçãop ao botão
        self.ui.btn_criar_usuario.clicked.connect(self.criar_usuario)
        self.ui.btn_voltar.clicked.connect(self.voltar)

    def voltar(self):
        self.hide()  # Hide the login window
        self.gerenciar_users = gerenciarUsuarios(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.gerenciar_users.show()


    def criar_usuario(self):
        #coleta os dados do usuario
        input_nome = self.ui.tbox_name.text()
        input_senha = self.ui.tbox_senha.text()
        input_conf_senha = self.ui.tbox_confirma_senha.text()
        input_email = self.ui.tbox_email.text()
        input_acesso = self.ui.cbox_tipoAcesso.currentText()

        # Faz a validação dos campos preenchidos

        if not input_nome:
            QMessageBox.warning(self, "Aviso",
                                f"Você não pode criar um usuário sem nome",
                                QMessageBox.Ok)
        elif not input_senha:
            QMessageBox.warning(self, "Aviso",
                                f"Você não pode criar um usuário sem senha",
                                QMessageBox.Ok)
        elif not input_email:
            QMessageBox.warning(self, "Aviso",
                                f"Você não pode criar um usuário sem e-mail",
                                QMessageBox.Ok)
        elif input_senha != input_conf_senha:
            QMessageBox.warning(self, "Aviso",
                                f"A senha inserida no campo 'senha' e a senha inserida no campo \nde 'confirmação de senha' não coincidem",
                                QMessageBox.Ok)
        else:

            conn, cursor = conexao()
            consulta = f"SELECT nome FROM tb_acessos WHERE email= '{input_email}' "
            cursor.execute(consulta)
            usuario_encontrado = cursor.fetchone()
            if usuario_encontrado:

                QMessageBox.warning(self, "Aviso",
                                    f"Já existe um usuário cadastrado para o email {input_email}",
                                    QMessageBox.Ok)


            else:


                cursor.execute("INSERT INTO tb_acessos (email, nome, tipo_acesso, senha) VALUES (?, ?, ?,?)",
                               (input_email, input_nome, input_acesso, input_senha))
                conn.commit()
                QMessageBox.warning(self, "Aviso",
                                    f"Usuário criado com sucesso. Permissão nível: {input_acesso}",
                                    QMessageBox.Ok)

                #Limpa os campos para uma nova insercao

                self.ui.tbox_name.clear()
                self.ui.tbox_email.clear()
                self.ui.tbox_senha.clear()
                self.ui.tbox_confirma_senha.clear()



class login(QDialog):
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        self.ui = tela_login()
        self.ui.setupUi(self)
        self.nome_bd = None
        self.tipo_acesso = None
        self.email_acesso = None
        #add uma funçãop ao botão
        self.ui.btn_login.clicked.connect(self.validar_usuario)
        self.ui.btn_sair.clicked.connect(self.sair)
        self.ui.btn_login.setDefault(True)

    # verifica se o bd já existe, e a tabela de acessos já foi criada

    def validar_usuario(self):

        #coleta os dados do usuario
        input_email = self.ui.tbox_login_email.text()
        input_senha = self.ui.tbox_login_senha.text()

        #verifica se email e senha estão ok

        conn, cursor = conexao()
        consulta = f"SELECT * FROM tb_acessos WHERE email= '{input_email}' "
        cursor.execute(consulta)
        usuario_encontrado = cursor.fetchone()


        if usuario_encontrado:

            email_bd = usuario_encontrado[0]
            nome_bd = usuario_encontrado[1]
            tipo_acesso = usuario_encontrado[2]
            senha_bd = usuario_encontrado[3]


            if input_senha != senha_bd:
                QMessageBox.warning(self, "Aviso",
                                    f"Senha inválida.",
                                    QMessageBox.Ok)

            else:
                # se a senha estiver ok, mostra a tela principal
                self.nome_bd = nome_bd
                self.tipo_acesso = tipo_acesso
                self.email_acesso = email_bd
                self.abrir_tela_principal()
        else:
            QMessageBox.warning(self, "Aviso", f"Não existe um usuário cadastrado para este e-mail.\nContacte o administrador.", QMessageBox.Ok)


    def abrir_tela_principal(self):
        self.hide()  # Hide the login window
        self.menu_inicial = MenuPrincipal(self.nome_bd, self.tipo_acesso, self.email_acesso)
        self.menu_inicial.show()




    def sair(self):
        print('Saindo da aplicação...')
        sys.exit()

def converter_para_zero(valor):
    if not valor:
        valor = 0
    return float(valor)
def atualizar_usuario_especifico(email,novo_nome, nova_senha, novo_tipo_acesso):
    conn, cursor = conexao()
    consulta = "UPDATE tb_acessos SET nome=?, senha=?, tipo_acesso=? WHERE email=?"
    cursor.execute(consulta, (novo_nome, nova_senha, novo_tipo_acesso, email))
    conn.commit()


def deletar_usuario_especifico(email):
    conn, cursor = conexao()
    consulta = f"DELETE FROM tb_acessos WHERE email= '{email}'"
    cursor.execute(consulta)
    conn.commit()
    conn.close()
    print(f'Usuário {email} removido com sucesso!')
def consultar_usuario_especifico(email):
    conn, cursor = conexao()
    consulta = f"SELECT email, nome, senha, tipo_acesso FROM tb_acessos WHERE email= '{email}' "
    dados = cursor.execute(consulta)
    usuario_encontrado = cursor.fetchone()
    conn.close()
    return usuario_encontrado

def contar_adm():
    conn, cursor = conexao()
    consulta = "SELECT COUNT(*) FROM tb_acessos WHERE tipo_acesso = 'administrador'"
    cursor.execute(consulta)
    quantidade_administradores = cursor.fetchone()[0]
    conn.close()

    return quantidade_administradores
def consultar_usuarios():

    conn, cursor = conexao()
    consulta = f"SELECT * FROM tb_acessos"
    cursor.execute(consulta)
    lista_usuarios = cursor.fetchall()
    conn.commit()
    conn.close()

    return lista_usuarios

def get_imoveis():


    conn, cursor = conexao()
    consulta = f"SELECT * FROM tb_imoveis;"
    cursor.execute(consulta)
    imoveis_encontrados = cursor.fetchall()

    return imoveis_encontrados

def apagar_tabela(nome_tabela):
    conn, cursor = conexao()
    consulta = f"DELETE FROM {nome_tabela}"
    print(f'Tabela {nome_tabela} apagada com sucesso!')
    cursor.execute(consulta)
    conn.commit()
    conn.close()


def main():
    app = QApplication(sys.argv)
    #window = login()
    #window = cadastrarUsuario('admin@phsn.com.br', 'administrador','admin@phsn.com.br')
    window = MenuPrincipal('admin@phsn.com.br', 'administrador', 'admin@phsn.com.br')

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    verificar_bd()
    #consultar_usuarios()
    main()

