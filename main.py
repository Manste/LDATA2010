import sys
from network.network_analysis import Graph
from network.display_network import QDash
import os

from PyQt5 import uic

# Import from Pyside
from PySide6.QtGui import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
import threading

# Import from PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from PyQt5.QtCore import *

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
        self.qdask = QDash()
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
        self.ui.network_web_engine.load(QUrl("http://127.0.0.1:8050"))
        self.qdask.run(debug=True, use_reloader=False)
        self.qdask.app.title = "Graph representation"

        graph_vis = Graph_visualization(self.graph)
        fig = graph_vis.set_dash_visualization()

        self.qdask.app.layout = html.Div([
            html.Div(dcc.Graph(id='Graph', figure=fig)),
            html.Div(className='row', children=[
                html.Div([html.H2('Overall Data'),
                          html.P('Num of nodes: ' + str(len(self.graph.nodes))),
                          html.P('Num of edges: ' + str(len(self.graph.edges)))],
                         className='three columns'),
                html.Div([
                    html.H2('Selected Data'),
                    html.Div(id='selected-data'),
                ], className='six columns')
            ])
        ])

        @app.callback(
            Output('selected-data', 'children'),
            [Input('Graph', 'selectedData')])
        def display_selected_data(selectedData):
            num_of_nodes = len(selectedData['points'])
            text = [html.P('Num of nodes selected: ' + str(num_of_nodes))]
            for x in selectedData['points']:
                material = int(x['text'].split('<br>')[0][10:])
                text.append(html.P(str(material)))
            return text
        self.ui.network_web_engine.reload()

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
        return extension == ".csv"


class Graph_visualization:
    def __init__(self, graph):
        self.graph = graph

    def set_dash_visualization(self):
        edge_trace = self.create_edges()
        node_trace = self.create_nodes()
        num_nodes = len(self.graph.nodes())
        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='<br>Network Graph of ' + str(num_nodes) + ' rules',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0.005, y=-0.002)],
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
        return fig

    def create_edges(self):
        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')
        for edge in self.graph.edges():
            x0, y0 = self.graph.node[edge[0]]['pos']
            x1, y1 = self.graph.node[edge[1]]['pos']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])
        return edge_trace

    def create_nodes(self):
        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))
        for node in self.graph.nodes():
            x, y = self.graph.node[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        # Adding color and hovertext
        for node, adjacencies in enumerate(self.graph.adjacency()):
            node_trace['marker']['color'] += tuple([len(adjacencies[1])])
            node_info = 'Name: ' + str(adjacencies[0]) + '<br># of connections: ' + str(len(adjacencies[1]))
            node_trace['text'] += tuple([node_info])
        return node_trace


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
