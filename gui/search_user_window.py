from os import sep
import PyQt5
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QGridLayout,QTableView, QRadioButton, QGroupBox, QHBoxLayout, QLineEdit
from PyQt5.QtCore import QAbstractTableModel ,QModelIndex, Qt
from modules import database
from gui import initial_window

class table_model(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)

        #Dados do banco de dados
        self.data = data
        self.colunas = ['ID', 'Nome', 'CPF', "Telefone", "E-mail", "Região"]


    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def columnCount(self, parente=QModelIndex()):
        return len(self.colunas)

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.colunas[section].upper()
        else:
            return section

        return None

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            return self.data[row][column]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft


class window(QWidget):
    def __init__(self, mainwindow, data = None):
        super().__init__()
        self.mainwindow = mainwindow
        self.data = data

        self.grid = QGridLayout(self)

        if data == None: #Se não for passado nenhum dado ele mostra todos do banco de dados
            self.data = database.SQL().get_users()

        #COnfigura a Tabela
        self.table = QTableView()
        self.table.setModel(table_model(self.data))
        self.table.setColumnWidth(4, 200)
        self.table.setColumnWidth(5, 60)
        
        #cria os radiobutton
        self.box = QGroupBox("Tipo de pesquisa")
        self.boxlayout = QHBoxLayout(self.box)

        self.box_regiao = QRadioButton("Região")
        self.box_regiao.setChecked(True)
                        
        self.box_name = QRadioButton("Nome")
        
        self.box_cpf = QRadioButton("CPF")
        
        #Cria e configura a Linha para digitar
        self.data_box = QLineEdit()
        self.data_box.setPlaceholderText("Dados")
        self.data_box.returnPressed.connect(self.search)
        self.data_box.setMaxLength(2)
        

        #Ajudsta os radio buttons conforme clickados selecionados
        self.box_regiao.clicked.connect(lambda : self.data_box.setInputMask(""))
        self.box_regiao.clicked.connect(lambda : self.data_box.setMaxLength(2))
        self.box_regiao.clicked.connect(self.data_box.setFocus)
        self.box_name.clicked.connect(lambda: self.data_box.setInputMask(""))
        self.box_name.clicked.connect(lambda : self.data_box.setMaxLength(100))
        self.box_name.clicked.connect(self.data_box.setFocus)
        self.box_cpf.clicked.connect(lambda : self.data_box.setMaxLength(100))
        self.box_cpf.clicked.connect(lambda : self.data_box.setInputMask("999.999.999-99"))
        self.box_cpf.clicked.connect(self.data_box.setFocus)

        self.search_box = QPushButton("Pesquisar")
        self.search_box.clicked.connect(self.search)

        self.voltar = QPushButton("voltar")
        self.voltar.clicked.connect(lambda : self.mainwindow.setCentralWidget(initial_window.window(self.mainwindow)))

        #Mostra o total de usuarios que foram encontrados na pesquisa
        self.tot_line = QLabel()
        self.tot_line.setText(f"Total de usuarios encontrados: {len(self.data)}")
        
        #Adciona os items ao Qwidget
        self.boxlayout.addWidget(self.box_regiao)
        self.boxlayout.addWidget(self.box_name)
        self.boxlayout.addWidget(self.box_cpf)
        
        self.grid.addWidget(self.data_box, 0, 0, 1, 2)
        self.grid.addWidget(self.box, 0, 2)
        self.grid.addWidget(self.search_box, 0, 3, 1, 2)

        self.grid.addWidget(self.table, 1, 0, 1, 5)
        self.grid.addWidget(self.tot_line, 2, 0, 1, 5)
        self.grid.addWidget(self.voltar, 3, 0, 1, 5)

    def search(self): #Procura os usuarios
        if self.data_box.text() == "":
            self.mainwindow.setCentralWidget(window(self.mainwindow, database.SQL().get_users()))
        elif self.box_regiao.isChecked():
            self.data = database.SQL().get_user_regiao(self.data_box.text())
            self.mainwindow.setCentralWidget(window(self.mainwindow, self.data))
        elif self.box_name.isChecked():
            self.data = database.SQL().get_user_name(self.data_box.text())
            self.mainwindow.setCentralWidget(window(self.mainwindow, self.data))
        else:
            self.data = database.SQL().get_user_cpf(self.data_box.text())
            self.mainwindow.setCentralWidget(window(self.mainwindow, self.data))
