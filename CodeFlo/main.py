import pandas as pd
import base64
import datetime
import io
import numpy as np
from dash import dcc, html, Dash
from dash.dependencies import Input, Output, State
from network_analysis import MyGraph
import dash_cytoscape as cyto
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


class InfoVis:
    def __init__(self):
        self.app = Dash(__name__, external_stylesheets=external_stylesheets)
        self.df_nodes = None
        self.df_edges = None
        self.graph = None
        self.temp = []
        self.layouts = ["circular", "random", "shell", "spring", "spectral", "spiral"]
        self.app.layout = html.Div([
            html.H1("Web application for network visualization"),
            html.Div([
                html.Div(
                    [
                        dcc.Upload(
                            id='upload-data-nodes',
                            children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Nodes Files')
                            ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            # Allow multiple files to be uploaded
                            multiple=True
                        ),
                        html.Div(id='output-data-upload-nodes'),
                        dcc.Upload(
                            id='upload-data-edges',
                            children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Edges Files')
                            ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            # Allow multiple files to be uploaded
                            multiple=True
                        ),
                        html.Div(id='output-data-upload-edges'),
                        dcc.Dropdown(
                            id="select-layout",
                            options=[
                                {"label": d, "value": d} for d in self.layouts
                            ],
                            placeholder = 'Select a view',
                            multi=False,
                            value="random",
                            style={
                                'width': '100%',
                                'margin': '6px'
                            }
                        ),
                        html.Div(
                            [   #html.Br(),
                                #html.Div([
                                #    dcc.Graph(
                                #        id='graph',
                                #        figure={}
                                #    )
                               # ], style={"width": "100%"}),
                                html.Br(),
                                html.Br(),
                                html.Div([
                                    html.Button(children='Numerical Metrics',id = 'numerical metrics button',n_clicks=0),
                                    html.Div(id='numerical metrics output',children='', style={"margin": "30px 0 30px 0"}),
                                    html.Button(children='Number of Communities',id = 'communities button',n_clicks=0),
                                    html.Div(id='communities output',children='', style={"margin": "30px 0 30px 0"})
                                ])
                            ],style={'display': 'flex', "margin": "30px 10px 0 10px"}
                        )
                    ],
                    style={"width": "20%"}),
                html.Div(
                    cyto.Cytoscape(
                        id='network',
                        elements=[],
                        style={'width': '100%', 'height': '500px'},
                        layout={
                            'name': "preset"
                        },
                        minZoom=0.2,
                        maxZoom=10
                    ), style={'width': '80%'}),
                html.Div(
                    [
                        html.Br(),
                        html.Div([
                            dcc.Graph(
                                id='graph',
                                figure={}
                            )
                        ], id="centrality-charts", style={"width": "100%"}),
                    ],
                    style={"width": "100%"}
                ),
                html.Div(
                cyto.Cytoscape(
                    id = 'communities network',
                    elements=[],
                    style = {'width':'100%', 'height': '500px'},
                    layout = {'name':'preset'},
                    minZoom = 0.2,
                    maxZoom = 10,
                    stylesheet=[],
                    ),style = {'width': '80%'}
                
                )
            ], style={
                "display": "flex",
                "justify-content": "space-between",
                "flexWrap": "wrap"
            })], style={}
        )
        @self.app.callback(Output('communities output','children'),
                           Output('communities network','elements'),
                           Input('communities button','n_clicks'),
                           State('network','elements'))
        def nbcommunities(n,elems):
            if (n%2 == 0):
                return '',[]
            else :
                new_elems = self.graph.color_elems(self.graph.communities_detection(),elems)
                print(new_elems)
                return 'Number of Communities : {}'.format(self.graph.ncommunities()), new_elems
        @self.app.callback(Output('numerical metrics output','children'),
        Input('numerical metrics button','n_clicks'))
        def numerical_metrics(n):
            if (n%2 == 0):
                return ''
            else :
                return 'Number of Nodes : {} Number of Edges : {} Assortativity Degree : {} Density : {}'.format(self.graph.numberofnodes(),self.graph.numberofedges(),self.graph.assortativitydegree(),self.graph.density())
        @self.app.callback(Output('output-data-upload-nodes', 'children'),
                           Input('upload-data-nodes', 'contents'),
                           State('upload-data-nodes', 'filename'),
                           State('upload-data-nodes', 'last_modified'))
        def update_output(list_of_contents, list_of_names, list_of_dates):
            if list_of_contents is not None:
                children = [
                    self.parse_contents_nodes(c, n, d) for c, n, d in
                    zip(list_of_contents, list_of_names, list_of_dates)]
                return children

        @self.app.callback(Output('output-data-upload-edges', 'children'),
                           Input('upload-data-edges', 'contents'),
                           State('upload-data-edges', 'filename'),
                           State('upload-data-edges', 'last_modified'))
        def update_output(list_of_contents, list_of_names, list_of_dates):
            if list_of_contents is not None:
                children = [
                    self.parse_contents_edges(c, n, d) for c, n, d in
                    zip(list_of_contents, list_of_names, list_of_dates)]
                return children

        @self.app.callback(
            Output(component_id="network", component_property="elements"),
            Output(component_id = "communities network", component_property ="stylesheet"),
            Input(component_id="select-layout", component_property="value")
        )
        def update_network(option_selected):
            if self.graph:
                x = {'name': option_selected }
                return self.graph.get_elements(option_selected), self.graph.setupstylesheet()
            return {},[]

        @self.app.callback(
            Output('graph', 'figure'),
            Input('network', 'tapNodeData')
        )
        def update_nodes(data):
            anchos = [0.2] * 5
            fig = go.Figure()
            if self.graph is not None:
                self.graph.set_centrality_measures()
                df = self.graph.df_centrality.copy()
                print(data)
                if data is None:
                    fig.add_trace(
                        go.Bar(x=df["nodes"].iloc[1:22], y=df["bet_centrality"].iloc[1:22], width=anchos, name="Betweeness centrality")
                    )
                    fig.add_trace(
                        go.Bar(x=df["nodes"].iloc[1:22], y=df["closeness_centrality"].iloc[1:22], width=anchos, name="Closeness centrality")
                    )
                    fig.add_trace(
                        go.Bar(x=df["nodes"].iloc[1:22], y=df["eigen_centrality"].iloc[1:22], width=anchos, name="Eigenvalue centrality")
                    )
                else:
                    index = np.where(df[["nodes"]] == data.id)[0][0]
                    start_idx = 11 - index
                    end_idx = 11 + index
                    fig.add_trace(
                        go.Bar(x=df["nodes"].iloc[start_idx:end_idx], y=df["bet_centrality"].iloc[start_idx:end_idx], width=anchos, name="Betweeness centrality", text=df["bet_centrality"].iloc[start_idx:end_idx])
                    )
                    fig.add_trace(
                        go.Bar(x=df["nodes"].iloc[start_idx:end_idx], y=df["closeness_centrality"].iloc[start_idx:end_idx], width=anchos, name="Closeness centrality", text=df["closeness_centrality"].iloc[start_idx:end_idx])
                    )
                    fig.add_trace(
                        go.Bar(x=df["nodes"].iloc[start_idx:end_idx], y=df["eigen_centrality"].iloc[start_idx:end_idx], width=anchos, name="Eigenvalue centrality", text=["eigen_centrality"].iloc[start_idx:end_idx])
                    )
                fig.update_layout(title="Centrality measurement",
                                  barmode='group', title_font_size=40,
                                  width=1000, height=500)
                fig.update_xaxes(title_text='Nodes',
                                 title_font=dict(size=30, family='Verdana', color='black'),
                                 tickfont=dict(family='Calibri', color='darkred', size=25))
                fig.update_yaxes(title_text="Values",
                                 title_font=dict(size=30, family='Verdana', color='black'),
                                 tickfont=dict(family='Calibri', color='darkred', size=25))
                return fig
            return {}

    def parse_contents_nodes(self, contents, filename, date):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                self.df_nodes = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                self.df_nodes = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
        return html.Div([
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date))
        ])

    def parse_contents_edges(self, contents, filename, date):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                self.df_edges = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                self.df_edges = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
        self.graph = MyGraph(self.df_nodes, self.df_edges)
        self.graph.setupcolors()
        return html.Div([
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date))
        ])


if __name__ == '__main__':
    project = InfoVis()
    project.app.run_server(debug=False)
