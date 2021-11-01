import sys

# Import the GUI file
from gui.ui_interface import *

# Import from PyQt5
from PyQt5.QtWidgets import *

# Import from Pyside
from PySide6.QtGui import QPainter
from PySide6.QtCharts import QChart

# Import for Math Modularity
# from random import randrange
# from functools import partial

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())    
