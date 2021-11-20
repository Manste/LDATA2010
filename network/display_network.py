import sys
import threading
from PyQt5 import QtCore
from dash import dcc, html, Dash

import plotly.figure_factory as ff


class QDash(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._app = Dash()
        self.app.layout = html.Div()

    @property
    def app(self):
        return self._app

    def update_graph(self, df):
        fig = ff.create_gantt(df)
        self.app.layout = html.Div([dcc.Graph(figure=fig)])

    def run(self, **kwargs):
        threading.Thread(target=self.app.run_server, kwargs=kwargs, daemon=True).start()