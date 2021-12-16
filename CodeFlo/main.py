import pandas as pd
import base64
import datetime
import io
from dash import dcc, html, Dash
import numpy as np
from network_analysis import MyGraph
from dash.dependencies import Input, Output, State
import dash_cytoscape as cyto

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Transform .txt of dataset into .csv
df = pd.read_csv("BIOGRID-PROJECT-glioblastoma_project-GENES.projectindex.txt", sep="\t", dtype='unicode')
df.to_csv("node.csv", index=False)
df = pd.read_csv("BIOGRID-PROJECT-glioblastoma_project-INTERACTIONS.tab3.txt", sep="\t", dtype='unicode')
df.to_csv("edges.csv", index=False)


class InfoVis:
    def __init__(self):
        self.app = Dash(__name__, external_stylesheets=external_stylesheets)
        self.df_nodes = None
        self.df_edges = None
        self.graph = None
        self.temp = []
        self.layouts = ["circular", "random", "shell", "spring", "spiral"]
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
                            placeholder='Select a view',
                            multi=False,
                            value=None,
                            style={
                                'width': '100%',
                                'margin': '6px'
                            }
                        ),
                        html.Div(
                            [
                                html.Br(),
                                html.Br(),
                                html.Div([
                                    html.Button(children='Numerical Metrics', id='numerical metrics button', n_clicks=0),
                                    html.Div(id='number of nodes output', children='', style={"margin": "10px 0 10px 10px"}),
                                    html.Div(id='number of edges output', children='', style={"margin": "10px 0 10px 10px"}),
                                    html.Div(id='assortativity degree output', children='', style={"margin": "10px 0 10px 10px"}),
                                    html.Div(id='density output', children=''),

                                    html.Button(children='Number of Communities', id='communities button', n_clicks=0),
                                    html.Div(id='communities output', children='')
                                ])
                            ], style={"margin": "30px 0 30px 10px"}
                        ),
                        html.Div([
                            html.H5("Centrality measures: "),
                            html.Div(id='centrality-measures', children='', style={"margin": "10px 0 30px 10px"}),
                        ], style={"margin": "30px 10px 0 10px"}),
                        cyto.Cytoscape(
                            id='details network',
                            elements=[],
                            style={'width': '100%', 'height': '500px'},
                            layout={'name': 'preset'},
                            stylesheet=[{'selector': 'node', 'style': {'label': 'data(id)'}}],
                            minZoom=0.05,
                            maxZoom=0.5
                        )
                    ], style={"width": "40%"}),
                html.Div(
                    cyto.Cytoscape(
                        id='network',
                        elements=[],
                        style={'width': '100%', 'height': '800px'},
                        layout={
                            'name': "preset"
                        },
                        minZoom=0.2,
                        maxZoom=10
                    ), style={'width': '60%'}),
                html.Div(
                    cyto.Cytoscape(
                        id='communities network',
                        elements=[],
                        style={'width': '100%', 'height': '800px'},
                        layout={'name': 'preset'},
                        minZoom=0.2,
                        maxZoom=10,
                        stylesheet=[],
                    ), style={'width': '80%'}

                ),
                html.Div([
                    html.Div(id='mst title', children='Minimum Spanning Tree'),
                    cyto.Cytoscape(
                        id='mst',
                        elements=[],
                        style={'witdh': '100%', 'height': '800px'},
                        layout={'name': 'preset'},
                        minZoom=0.2,
                        maxZoom=10,
                        stylesheet=[],
                    )], style={'width': '100%'}

                ),
                html.Div([
                    html.Div(id='shortest path title', children='Shortest Path'),
                    dcc.Input(id='Source Input', type='text', placeholder='Source Official Symbol',
                              style={'width': '50%'}),
                    dcc.Input(id='Target Input', type='text', placeholder='Target Official Symbol',
                              style={'width': '50%'}),
                    html.Button(children='submit', id='submit button', n_clicks=0)
                ], style={'width': '30%'}),
                html.Div(
                    cyto.Cytoscape(
                        id='shortest path network',
                        elements=[],
                        layout={'name': 'preset'},
                        style={'width': '100%', 'height': '800px'},
                        minZoom=0.2,
                        maxZoom=10,
                        stylesheet=[{'selector': 'node', 'style': {'label': 'data(label)'}},
                                    {'selector': 'edge', 'style': {'alpha': '0.2'}},
                                    {'selector': '.red',
                                     'style': {'background-color': 'red', 'line-color': 'red', 'alpha': '0.1'}}]
                    ), style={'width': '70%'}
                )
            ], style={
                "display": "flex",
                "justify-content": "space-between",
                "flexWrap": "wrap"
            })], style={}
        )

        @self.app.callback(Output('details network', 'elements'),
                           Input('network', 'tapNodeData'))
        def detail_node(node_data):
            print(node_data)
            if self.graph:
                x = self.graph.alledges(node_data)
                print(x)
                return x
            else:
                return []

        @self.app.callback(Output('shortest path network', 'elements'),
                           Input('submit button', 'n_clicks'),
                           State('Source Input', 'value'),
                           State('Target Input', 'value'),
                           State('network', 'elements'),
                           )
        def shortest_path(n, source_name, target_name, elems):
            if n > 0:
                return self.graph.shortestpath(source_name, target_name, elems)
            else:
                return []

        @self.app.callback(Output('communities output', 'children'),
                           Output('communities network', 'elements'),
                           Input('communities button', 'n_clicks'),
                           State('network', 'elements'))
        def nbcommunities(n, elems):
            if (n % 2 == 0):
                return '', []
            else:
                new_elems = self.graph.color_elems(self.graph.communities_detection(), elems)
                return 'Number of Communities : {}'.format(self.graph.ncommunities()), new_elems

        @self.app.callback(
            Output('number of nodes output', 'children'),
            Output('number of edges output', 'children'),
            Output('assortativity degree output', 'children'),
            Output('density output', 'children'),
            Input('numerical metrics button', 'n_clicks'))
        def numerical_metrics(n):
            if (n % 2 == 0):
                return '', '', '', ''
            else:
                return ('Number of Nodes : {}'.format(self.graph.numberofnodes()),
                        ' Number of Edges : {}'.format(self.graph.numberofedges()),
                        ' Assortativity Degree : {}'.format(self.graph.assortativitydegree()),
                        'Density : {}'.format(self.graph.density()))

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
            Output('mst', 'elements'),
            Output(component_id="communities network", component_property="stylesheet"),
            Output(component_id="mst", component_property="stylesheet"),
            Input(component_id="select-layout", component_property="value")
        )
        def update_network(option_selected):
            if self.graph:
                x = self.graph.get_elements(option_selected)
                return x[0], x[1], self.graph.setupstylesheet(), self.graph.setupstylesheet()
            return [], [], [], []

        @self.app.callback(
            Output('centrality-measures', 'children'),
            Input('network', 'tapNodeData')
        )
        def update_centrality_measures(data):
            if self.graph is not None:
                self.graph.set_centrality_measures()
                df = self.graph.df_centrality.copy()
                if data is None:
                    return "Nodes not selected"
                else:
                    index = np.where(df[["nodes"]] == int(data['id']))[0][0]
                    bet_centrality = df["bet_centrality"][index]
                    closeness_centrality = df["closeness_centrality"][index]
                    eigen_centrality = df["eigen_centrality"][index]
                    return "The betweenness centrality: {} The closeness centrality: {} The eigenvetor centrality: {}".format(
                        round(bet_centrality, 5), round(closeness_centrality, 5), round(eigen_centrality, 5))
            return "Nodes not selected"

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
