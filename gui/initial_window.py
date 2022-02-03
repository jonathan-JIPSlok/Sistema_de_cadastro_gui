from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QGridLayout
from gui import cadaster_window, search_user_window

class window(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow

        self.grid_inicial = QGridLayout(self)

        #Configura os botões
        title_label = QLabel("Sistema de Cadastro de Usuarios")
        self.button_cadastro = QPushButton("Cadastrar Usuario")
        self.button_cadastro.clicked.connect(lambda : self.mainwindow.setCentralWidget(cadaster_window.window(self.mainwindow)))
        self.button_select = QPushButton("Selecionar Usuario")
        self.button_select.clicked.connect(lambda : self.mainwindow.setCentralWidget(search_user_window.window(self.mainwindow)))

        #Adiciona os item a tela
        self.grid_inicial.addWidget(title_label)
        self.grid_inicial.addWidget(self.button_cadastro)
        self.grid_inicial.addWidget(self.button_select)
