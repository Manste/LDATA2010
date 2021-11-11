import sys
from network.network_analysis import Graph
import os

from PyQt5 import uic

# Import from Pyside
from PySide6.QtGui import *
from PySide6.QtCharts import *
from  PySide6.QtCore import *

# Import from PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
        self.nodes_file = None
        self.edges_file = None
        self.graph = None

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
        self.ui.graph_represent_button.clicked.connect(self.graph_representation_action)
        self.ui.network_overview_button.clicked.connect(self.network_overview_action)
        self.ui.upload_edges_button.clicked.connect(self.upload_edges_csv_action)
        self.ui.upload_nodes_button.clicked.connect(self.upload_nodes_csv_action)
        self.ui.nodes_overview_button.clicked.connect(self.nodes_overview_action)
        self.ui.edges_overview_button.clicked.connect(self.edges_overview_action)
        self.show()

    def graph_representation_action(self):
        self.ui.label_7.setText("Graph representation")
        self.ui.stackedWidget.setCurrentWidget(self.ui.graph_representation)

    def network_overview_action(self):
        self.ui.label_7.setText("Network overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.network_overview)

    def upload_csv_action(self):
        self.ui.label_7.setText("Upload csv files")
        self.ui.stackedWidget.setCurrentWidget(self.ui.csv_content)
        csv_file = self.open_csv_file()
        if not self.is_csv(csv_file):
            self.show_error_popup("Error", "CSV file: Wrong datatype", QMessageBox.Critical)
        return csv_file

    def upload_nodes_csv_action(self):
        self.nodes_file = self.upload_csv_action()
        self.ui.nodes_path.setText(self.nodes_file)
        if self.nodes_file and self.edges_file:
            self.graph = Graph(self.nodes_file, self.edges_file)

    def upload_edges_csv_action(self):
        self.edges_file = self.upload_csv_action()
        self.ui.edges_path.setText(self.edges_file)
        if self.nodes_file and self.edges_file:
            self.graph = Graph(nodes_csv=self.nodes_file, edges_csv=self.edges_file)


    def show_error_popup(self, title, text, icon_type):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon_type)
        x = msg.exec_()

    def open_csv_file(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        return path

    def nodes_overview_action(self):
        self.ui.label_7.setText("Nodes overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.nodes_overview)

    def edges_overview_action(self):
        self.ui.label_7.setText("Edges overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.edges_overview)

    def is_csv(self, path):
        name, extension = os.path.splitext(path)
        return extension == ".csv" or extension == '.txt'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())    
