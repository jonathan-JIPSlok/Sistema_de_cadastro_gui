from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QGridLayout
from gui import cadaster_window, initial_window

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #Janela principal

        self.setWindowTitle("Sistema de Cadastro")

        self.setCentralWidget(initial_window.window(self))
        self.setGeometry(250, 100, 700, 500)
        self.setStyleSheet(self.style())
        self.show()

    def style(self) -> str:
        style = """ QMainWindow {
                        background-color: rgb(60, 180, 255);
                        
                    }
                    QTableView {
                        font-size: 12px;
                        font: bold;
                    }
                    QLabel {
                        font-size: 20px;
                        padding-left: 200px;
                        padding-right: 200px;
                        font: bold;
                    }
                    QLineEdit {
                        font-size: 15px;
                        border: 1px solid black;
                        border-radius: 10px;
                        font: bold;
                    }
                    QPushButton {
                        font-size: 15px;
                        padding: 4px;
                        border: 1px solid black;
                        border-radius: 10px;
                        font: bold;
                        color: rgba(0, 255, 0, 1);
                        background-color: rgba(50, 90, 255, 1);
                    }
                    QPushButton:hover{
                        font-size: 17px;
                        color: rgba(0, 255, 0, 1);
                        background-color: rgba(0, 0, 100, 0.6);
                    }
        """
        return style
