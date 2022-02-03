import sys
from modules.database import *
from gui.main_window import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())