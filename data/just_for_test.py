import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from dash import html, dcc
from dash.dependencies import Input, Output
from network.display_network import QDash
from network.network_analysis import MyGraph

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.graph_net = MyGraph('nodes.csv', 'edges.csv')
        self.graph = self.graph_net.graph

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.button = QtWidgets.QPushButton("Press me")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addWidget(self.browser, stretch=1)

        self.qdask = QDash()
        self.qdask.set_graph_net(self.graph_net)
        self.qdask.layout_network('preset', 'circular')

        self.qdask.run(debug=True, use_reloader=False)
        self.browser.load(QtCore.QUrl("http://127.0.0.1:8050"))

        #self.button.clicked.connect(self.update_figure)
        #self.update_figure()

    @QtCore.pyqtSlot()
    def update_figure(self):
        self.browser.reload()


if __name__ == "__main__":
    test = QtWidgets.QApplication(sys.argv)
    test.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    w = Mainwindow()
    w.show()

    sys.exit(test.exec_())
