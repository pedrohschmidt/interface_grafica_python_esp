'''
O sistema deverá permitir a seleção do Tipo de negociação para o imóvel: Venda, Locação, Venda/Locação
Deve haver um local para seleção do status: Disponível, Locado, Vendido, À liberar
O campo identificação deve ser preenchido automaticamente pelo sistema.
O endereço pode estar armazenado em um único campo ou separado em campos para armazenamento do número, complemento, CEP, Bairro e Estado
O sistema deve permitir o cadastro de uma descrição curta para o imóvel. Essa descrição será usada nos anúncios
Deve haver um campo para seleção do tipo do imovel: Apartamento, Casa, Terreno
O sistema deve possuir um campo de texto no qual armazenará as Características do Imóvel. Aqui devem constar os detalhes.
Deve haver armazenamento do Preço, porém você poderá optar por permitir que o usuário o armazene nas características do imóvel ou criar um campo exclusivo.
O mesmo caso acima serve para Condições. Você pode criar um campo de texto para preenchimento ou deixar que o usuário registre no campo das características do imóvel.
Deve existir um campo para registro das Observações.
'''


# converter ui para py:  pyuic5 -x tela_principal.ui -o tela_principal.py
# converter ui para py:  pyuic5 -x login.ui -o login.py
# converter ui para py:  pyuic5 -x criar_usuario.ui -o criar_usuario.py
# converter ui para py:  pyuic5 -x gerenciar_usuarios.ui -o gerenciar_usuarios.py
# converter ui para py: pyuic5 -x alterar_senha_adm.ui -o alterar_senha_adm.py
# pyrcc5 icons\\imagens.qrc -o imagens_rc.py
# para abrir o pyqt coloca 'designer' no terminal

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
import sqlite3
from login import Ui_Dialog as tela_login
from tela_principal import Ui_MainWindow
from criar_usuario import Ui_Dialog
from gerenciar_usuarios import Ui_gerenciarUsuarios
import os, sys


def conexao():
    conn = sqlite3.connect("PHSN_IMOBILIARIA.db")
    cursor = conn.cursor()
    return conn, cursor

def verificar_bd():
    # Conecta no banco de dados
    conn, cursor = conexao()

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

    # salva
    print("Banco de dados verificado com sucesso. Acessando informação!")
    conn.commit()
    conn.close()


class MenuPrincipal(QMainWindow):
    def __init__(self, nome_bd, tipo_acesso, *args, **argvs):
        super(MenuPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.ui.lbl_userLogado.setText(f"Seja bem-vindo, {self.nome_bd}")
        self.ui.menu_Gerenciar_Usuarios.triggered.connect(self.gerenciar_usuarios)

    def gerenciar_usuarios(self):
        #self.hide()
        #gerenciar_dialog = gerenciarUsuarios()
        #gerenciar_dialog.exec_()

        self.hide()  # Hide the login window
        self.gerenciar_users = gerenciarUsuarios(self.nome_bd, self.tipo_acesso)
        self.gerenciar_users.show()



class gerenciarUsuarios(QDialog):
    def __init__(self, nome_bd, tipo_acesso, *args, **argvs):
        super(gerenciarUsuarios, self).__init__(*args, **argvs)
        self.ui = Ui_gerenciarUsuarios()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso

        self.ui.btn_addUsuario.clicked.connect(self.add_usuarios)

        if self.tipo_acesso != "administrador":
            #Bloqueia a deleção de usuários
            self.ui.lview_usuarios.setEnabled(False)

            # Bloqueia a criação de usuários
            self.ui.btn_addUsuario.setEnabled(False)

            #Bloqueia a remoção de usuários
            self.ui.btn_removerUsuario.setEnabled(False)

        else:
            #Se for adm, carrega a lista de usuarios
            lista_usuarios = cosultar_usuarios()
            for usuario in lista_usuarios:
                print(usuario[0])

    def add_usuarios(self):
        self.hide()  # Hide the login window
        self.menu_cadastro = cadastrarUsuario(self.nome_bd, self.tipo_acesso)
        self.menu_cadastro.show()







class cadastrarUsuario(QDialog):
    def __init__(self, nome_bd, tipo_acesso, *args, **argvs):
        super(cadastrarUsuario, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.nome_bd = nome_bd
        self.tipo_acesso = tipo_acesso
        self.ui.cbox_tipoAcesso.addItems(["administrador", "usuario"])

        #add uma funçãop ao botão
        self.ui.btn_criar_usuario.clicked.connect(self.criar_usuario)
        self.ui.btn_voltar.clicked.connect(self.voltar)

    def voltar(self):
        window = login()
        window.show()


    def criar_usuario(self):
        #coleta os dados do usuario
        input_nome = self.ui.tbox_name.text()
        input_senha = self.ui.tbox_senha.text()
        input_conf_senha = self.ui.tbox_confirma_senha.text()
        input_email = self.ui.tbox_email.text()
        input_acesso = self.ui.cbox_tipoAcesso.currentText()



        if not input_nome:
            self.ui.lbl_status.setText(
                "Você não pode criar um usuário sem nome")
        elif not input_senha:
            self.ui.lbl_status.setText(
                "Você não pode criar um usuário sem senha")
        elif not input_email:
            self.ui.lbl_status.setText(
                "Você não pode criar um usuário sem e-mail")
        elif input_senha != input_conf_senha:
            self.ui.lbl_status.setText(
                "A senha inserida no campo 'senha' e a senha inserida no campo \nde 'confirmação de senha' não coincidem")
            self.ui.lbl_status.adjustSize()
        else:

            conn, cursor = conexao()
            consulta = f"SELECT nome FROM tb_acessos WHERE email= '{input_email}' "
            cursor.execute(consulta)
            usuario_encontrado = cursor.fetchone()
            if usuario_encontrado:

                self.ui.lbl_status.setText(f'Já existe um usuário cadastrado para o email {input_email}')
                self.ui.lbl_status.adjustSize()

            else:


                cursor.execute("INSERT INTO tb_acessos (email, nome, tipo_acesso, senha) VALUES (?, ?, ?,?)",
                               (input_email, input_nome, input_acesso, input_senha))
                conn.commit()
                self.ui.lbl_status.setText(f"Usuário criado com sucesso. Permissão nível: {input_acesso}")
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
                self.ui.lbl_status_login.setText(f'Senha inválida.')

            else:
                # se a senha estiver ok, mostra a tela principal
                self.nome_bd = nome_bd
                self.tipo_acesso = tipo_acesso
                self.abrir_tela_principal()
        else:
            self.ui.lbl_status_login.setText(f'Não existe um usuário cadastrado para este e-mail.\nContacte o administrador.')
            print('Usuário não encontrado!')

    def abrir_tela_principal(self):
        self.hide()  # Hide the login window
        self.menu_inicial = MenuPrincipal(self.nome_bd, self.tipo_acesso)
        self.menu_inicial.show()




    def sair(self):
        print('Saindo da aplicação...')
        sys.exit()

def cosultar_usuarios():

    conn, cursor = conexao()
    consulta = f"SELECT * FROM tb_acessos"
    cursor.execute(consulta)
    lista_usuarios = cursor.fetchall()
    conn.commit()
    conn.close()

    return lista_usuarios


def apagar_tabela(nome_tabela):
    conn, cursor = conexao()
    consulta = f"DROP TABLE IF EXISTS {nome_tabela}"
    print(f'Tabela {nome_tabela} apagada com sucesso!')
    cursor.execute(consulta)
    conn.commit()
    conn.close()


def main():
    app = QApplication(sys.argv)
    window = login()
    #window = cadastrarUsuario()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    #apagar_tabela("tb_acessos")
    verificar_bd()
    #cosultar_usuarios("tb_acessos")
    main()

