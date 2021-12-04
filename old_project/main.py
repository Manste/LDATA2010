import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from old_project.gui.interface import *
from network.network_analysis import MyGraph
from network.display_network import QDash
import os

shadow_elements = {
    "left_menu_widget",
    "frame_3",
    "frame_5",
    "header_frame",
    "frame_7"
}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.qdash = QDash()
        # set the minimum size of the window
        self.setMinimumSize(850, 600)
        self.nodes_file = None
        self.edges_file = None
        self.graph_net = None
        self.graph = None
        self.qdash.run(debug=True, use_reloader=False)

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
        self.ui.load_data_button.clicked.connect(self.upload_data)
        self.ui.graph_represent_button.clicked.connect(self.graph_representation_action)
        self.ui.network_overview_button.clicked.connect(self.network_overview_action)
        self.ui.upload_edges_button.clicked.connect(self.upload_edges_csv_action)
        self.ui.upload_nodes_button.clicked.connect(self.upload_nodes_csv_action)
        self.ui.nodes_overview_button.clicked.connect(self.nodes_overview_action)
        self.ui.edges_overview_button.clicked.connect(self.edges_overview_action)
        self.ui.random_button.clicked.connect(lambda x: self.set_layout('preset', 'random'))
        self.ui.circular_button.clicked.connect(lambda x: self.set_layout('preset', 'circular'))
        self.show()

    def set_layout(self, dash_layout, networkx_layout):
        self.qdash.layout_network(dash_layout, networkx_layout)
        self.ui.network_web_engine.reload()

    def graph_representation_action(self):
        self.ui.label_7.setText("Graph representation")
        self.ui.stackedWidget.setCurrentWidget(self.ui.graph_representation)
        if not self.graph_net:
            return
        elif self.qdash.graph_net:
            self.ui.network_web_engine.reload()
        else:
            self.qdash.set_graph_net(self.graph_net)
            self.qdash.layout_network('preset', 'circular')
            self.ui.network_web_engine.load(QtCore.QUrl("http://127.0.0.1:8050"))

    def network_overview_action(self):
        self.ui.label_7.setText("Network overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.network_overview)

    def upload_csv_action(self):
        self.ui.label_7.setText("Upload csv files")
        self.ui.stackedWidget.setCurrentWidget(self.ui.csv_content)
        csv_file = self.open_csv_file()
        if not self.is_csv(csv_file) and csv_file != "":
            self.show_popup("Error", "CSV file: Wrong datatype", QMessageBox.Critical)
            return None
        return csv_file

    def upload_nodes_csv_action(self):
        self.nodes_file = self.upload_csv_action()
        if self.nodes_file:
            self.ui.nodes_path.setText(self.nodes_file)

    def upload_edges_csv_action(self):
        self.edges_file = self.upload_csv_action()
        if self.edges_file:
            self.ui.edges_path.setText(self.edges_file)

    def upload_data(self):
        if self.nodes_file and self.edges_file:
            self.graph_net = MyGraph(self.nodes_file, self.edges_file)
            self.graph = self.graph_net.graph
            self.show_popup("Succeed", "Network created", QMessageBox.Information)

    def show_popup(self, title, text, icon_type):
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
        return extension == ".csv"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
