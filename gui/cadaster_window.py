import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QLineEdit
from modules import database
from validate_docbr import CPF
from gui import main_window, initial_window

class window(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.grid = QGridLayout(self)

        self.title_label = QLabel("Cadastrar Usuario")
        self.grid.addWidget(self.title_label)

        #Configurando linha de inserção de nome
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Nome")
        self.grid.addWidget(self.name_edit)

        #Configurando linha de inserção de cpf
        self.cpf_edit = QLineEdit()
        self.cpf_edit.setPlaceholderText("CPF")
        self.name_edit.returnPressed.connect(self.cpf_edit.setFocus)
        
        #Define o texto com padrao de cpf
        self.cpf_edit.textChanged.connect(lambda : self.cpf_edit.setInputMask("999.999.999-99") if self.cpf_edit.inputMask() == "" else self.cpf_edit)
        self.name_edit.returnPressed.connect(lambda : self.cpf_edit.setInputMask("999.999.999-99"))
        self.grid.addWidget(self.cpf_edit)

        #Configurando linha de inserção de telefone
        self.tel_edit = QLineEdit()
        self.tel_edit.setPlaceholderText("Telefone")
        self.cpf_edit.returnPressed.connect(self.tel_edit.setFocus)
        #Define a linha com o padrao de telefone
        self.tel_edit.textChanged.connect(lambda : self.tel_edit.setInputMask("(99) 99999-9999") if self.tel_edit.inputMask() == "" else self.tel_edit)
        self.cpf_edit.returnPressed.connect(lambda : self.tel_edit.setInputMask("(99) 99999-9999"))
        self.grid.addWidget(self.tel_edit)

        #Configurando linha de inserção de email
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("E-mail")
        self.tel_edit.returnPressed.connect(self.email_edit.setFocus)
        self.grid.addWidget(self.email_edit)

        #Configurando linha de inserção de regiao
        self.regiao_edit = QLineEdit()
        self.regiao_edit.setPlaceholderText("Região")
        self.regiao_edit.setMaxLength(2)
        self.regiao_edit.textChanged.connect(lambda : self.regiao_edit.setText(self.regiao_edit.text().upper()))
        self.email_edit.returnPressed.connect(self.regiao_edit.setFocus)
        self.regiao_edit.returnPressed.connect(self.register)
        self.grid.addWidget(self.regiao_edit)

        self.register_button = QPushButton("Registrar")
        self.register_button.clicked.connect(self.register)
        self.grid.addWidget(self.register_button)

        self.voltar = QPushButton("Voltar")
        self.voltar.clicked.connect(lambda : self.mainwindow.setCentralWidget(initial_window.window(self.mainwindow)))
        self.grid.addWidget(self.voltar)

        self.error_label = QLabel()
        self.grid.addWidget(self.error_label)

    def register(self):
        data = [self.name_edit.text(),  self.cpf_edit.text(), self.tel_edit.text(), self.email_edit.text(), self.regiao_edit.text()]
        if not '' in data and data[4][0].isnumeric() == False and data[4][1].isnumeric() == False:
            if CPF().validate(data[1]):
                try:
                    #Cadastra o usuario no banco de dados
                    db = database.SQL()                
                    db.cadaster_user(data)
                    db.connection_close()

                    #Configura as linhas apos o cadastro
                    self.name_edit.setText("")
                    self.cpf_edit.setText("")
                    self.tel_edit.setText("")
                    self.email_edit.setText("")
                    self.regiao_edit.setText("")
                    self.error_label.setText("Usuario cadastrado com sucesso!")
                    self.cpf_edit.setInputMask("")
                    self.tel_edit.setInputMask("")
                    
                except sqlite3.IntegrityError:
                    self.error_label.setText("Usuario já cadastrado!")
            else: self.error_label.setText("CPF invalido!")
        else: self.error_label.setText("Preencha todos os dados! ou verifique se a região está correta")