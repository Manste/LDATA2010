import sys
import os
import platform

from PyQt5 import uic

# Import from Pyside
from PySide6.QtGui import *
from PySide6.QtCharts import *
from  PySide6.QtCore import *

# Import from PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Import for Math Modules
# from random import randrange
# from functools import partial

shadow_elements = {
    "left_menu_widget",
    "frame_3",
    "frame_5",
    "header_frame",
    "frame_7"
}

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("gui\MainWindow.ui", self)
        # set the minimum size of the window
        self.setMinimumSize(850, 600)

        # apply shadow to widgets on shadow_elements list
        for x in shadow_elements:
            # Shadow effect style
            effect = QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0))
            getattr(self.ui, x).setGraphicsEffect(effect)

        # Navigation between pages
        self.ui.stackedWidget.setCurrentWidget(self.ui.frame_home)
        self.ui.csv_content_button.clicked.connect(self.csv_content_action)
        self.ui.graph_represent_button.clicked.connect(self.graph_representation_action)
        self.ui.network_overview_button.clicked.connect(self.network_overview_action)
        self.ui.upload_csv_button.clicked.connect(self.upload_csv_action)
        self.ui.nodes_overview_button.clicked.connect(self.nodes_overview_action)
        self.ui.edges_overview_button.clicked.connect(self.edges_overview_action)
        self.show()

    def csv_content_action(self):
        self.ui.label_7.setText("CSV content")
        self.ui.stackedWidget.setCurrentWidget(self.ui.csv_content)

    def graph_representation_action(self):
        self.ui.label_7.setText("Graph representation")
        self.ui.stackedWidget.setCurrentWidget(self.ui.graph_representation)

    def network_overview_action(self):
        self.ui.label_7.setText("Network overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.network_overview)

    def upload_csv_action(self):
        pass

    def nodes_overview_action(self):
        self.ui.label_7.setText("Nodes overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.nodes_overview)

    def edges_overview_action(self):
        self.ui.label_7.setText("Edges overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.edges_overview)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())    
