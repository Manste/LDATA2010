import pandas as pd
import base64
import datetime
import io
from dash import dcc, html, Dash
from dash.dependencies import Input, Output, State
from network_analysis import MyGraph
import dash_cytoscape as cyto
import plotly.express as px

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
                    ],
                    style={"width": "20%"}),
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
                    ), style={'width': '80%'}),
                html.Div(
                    [
                        #html.Br(),
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
                            html.Div(id='numerical metrics output',children=''),
                            html.Button(children='Number of Communities',id = 'communities button',n_clicks=0),
                            html.Div(id='communities output',children='')                            
                        ])
                    ],style={'display': 'flex'}
                ),
                html.Div(
                cyto.Cytoscape(
                    id = 'communities network',
                    elements=[],
                    style = {'width':'100%', 'height': '800px'},
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

#        @self.app.callback(
#            [
#                Output('graph', 'figure'),
#                Output('graph', 'style')
#             ],
#            Input('network', 'tapNodeData'),
#        )
#        def update_nodes(data):
#            style= {"width": "100%", "display": "block"}
#            if self.graph is not None:
##                df_nodes = self.graph.df_nodes.copy()
 #               if data is None:
 #                   fig = px.bar(df_nodes, x="OFFICIAL SYMBOL", y="INTERACTION COUNT")
 #               else:
 #                   df_nodes.loc[df_nodes["OFFICIAL SYMBOL"] == data["label"], "color"] = "red"
 #                   fig = px.bar(df_nodes, x="OFFICIAL SYMBOL", y="INTERACTION COUNT")
 #               fig.update_traces(marker={'color': df_nodes['color']})
 #               return fig, style
 #           return {}, style

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
