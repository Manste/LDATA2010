import sys
import threading
from PyQt5 import QtCore
from dash import dcc, html, Dash
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

import plotly.figure_factory as ff


class QDash(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._app = Dash()
        self.app.layout = html.Div()

    def layout_network(self, layout, elements):
        self.app.layout = html.Div([
            html.Div([
                cyto.Cytoscape(
                    id='network',
                    elements=elements,
                    style={'width': '100%', 'height': '500px'},
                    layout={
                        'name': layout
                    }
                )
            ], className='network-graph'),
            html.Div([
                html.Div(id='empty-div', children='')
            ], className='one column'),
            html.Div([
                dcc.Graph(id='graph')
            ], className='network-graph')]
        )
        @self.app.callback(
            Output('graph', 'figure'),
            Input('network', 'tapNodeData'),
        )
        def update_nodes(data):
            print(data)

    @property
    def app(self):
        return self._app

    def update_graph(self, df):
        fig = ff.create_gantt(df)
        self.app.layout = html.Div([dcc.Graph(figure=fig)])

    def run(self, **kwargs):
        threading.Thread(target=self.app.run_server, kwargs=kwargs, daemon=True).start()