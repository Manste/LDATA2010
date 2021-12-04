import sys
import threading
from PyQt5 import QtCore
from dash import dcc, html, Dash
import dash_cytoscape as cyto
from dash.dependencies import Input, Output
import networkx as nx

import plotly.express as px


class QDash(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._app = Dash()
        self.graph_net = None
        self.app.layout = html.Div()

    def set_graph_net(self, graph_net):
        self.graph_net = graph_net

    def layout_network(self, dash_layout, network_layout='spring'):
        self.app.layout = html.Div([
            html.Div([
                cyto.Cytoscape(
                    id='network',
                    elements=self.graph_net.get_elements(network_layout),
                    style={'width': '100%', 'height': '500px'},
                    layout={
                        'name': dash_layout
                    },
                    minZoom = 0.2,
                    maxZoom=1
                )
            ], className='six columns'),
            html.Div([
                dcc.Graph(id='graph')
            ], className='six columns'),
        ], className='row')

        @self.app.callback(
            Output('graph', 'figure'),
            Input('network', 'tapNodeData'),
        )
        def update_nodes(data):
            df_nodes = self.graph_net.df_nodes.copy()
            if data is None:
                fig = px.bar(df_nodes, x="OFFICIAL SYMBOL", y="INTERACTION COUNT")
            else:
                df_nodes.loc[df_nodes["OFFICIAL SYMBOL"] == data["label"], "color"] = "red"
                fig = px.bar(df_nodes, x="OFFICIAL SYMBOL", y="INTERACTION COUNT")
            fig.update_traces(marker={'color': df_nodes['color']})
            return fig

    @property
    def app(self):
        return self._app

    def run(self, **kwargs):
        threading.Thread(target=self.app.run_server, kwargs=kwargs, daemon=True).start()