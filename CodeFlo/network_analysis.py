import networkx as nx
import community as community_louvain
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)


class MyGraph:
    def __init__(self, nodes=None, edges=None):
        self.graph = nx.Graph()
        self.df_nodes = nodes
        self.df_edges = edges
        self.df_nodes["color"] = ["yellow" for _ in range(self.df_nodes.shape[0])]
        self.createGraph()
        self.colors = []

    
    # Function To Build Graph
    def createGraph(self):
        self.graph.add_nodes_from(self.df_nodes['#BIOGRID ID'])
        self.graph = nx.from_pandas_edgelist(self.df_edges, 'BioGRID ID Interactor A','BioGRID ID Interactor B')
        dict_nodes = self.df_nodes.set_index('#BIOGRID ID').to_dict()
        for key in dict_nodes:
            nx.set_node_attributes(self.graph, dict_nodes[key], name=key)

    # Todo: Improve the Visualisation of the Graph
    def temp_visualization(self):
        plt.figure(figsize=(25, 20))
        plt.title('Protein Graph')
        pos1 = nx.spring_layout(self.graph, k=3, iterations=10)
        nx.draw_networkx_nodes(self.graph, pos1, alpha=0.5)
        nx.draw_networkx_edges(self.graph, pos1, alpha=0.3)
        nx.draw_networkx_labels(self.graph, pos1, font_size=10)
        plt.show()
    def setupcolors(self):
        df = pd.read_csv('color.csv', dtype=str)
        df = df.iloc[:,0]
        self.colors = df.to_numpy()
    def setupstylesheet(self):
        tab_colors = self.colors
        tab_stylesheet = []
        m = {'selector': 'node', 'style': {'label': 'data(label)'}}
        tab_stylesheet.append(m)
        for i in tab_colors:
            x = {'selector':'.'+i, 'style': {'background-color': i, 'line-color':i}}
            tab_stylesheet.append(x)
        return tab_stylesheet
            
    #compute number of nodes
    def numberofnodes(self):
        return self.graph.number_of_nodes()    
    
    #compute number of egdes
    def numberofedges(self):
        return self.graph.number_of_edges()
    
    #compute clustering coefficient
    def clustcoef(self):
        return nx.clustering(self.graph)
    
    #compute the assortativity degree
    def assortativitydegree(self):
        return nx.degree_assortativity_coefficient(self.graph)
    # compute density
    def density(self):
        return nx.density(self.graph)
    #compute the average connectivity
    def connectivity(self):
        return nx.average_node_connectivity(self.graph)
    # compute betweenness centrality
    def betweeness_centrality(self):
        return nx.betweenness_centrality(self.graph)
    def ncommunities(self):
        partition = community_louvain.best_partition(self.graph)
        print(type(partition))
        return max(partition.values()) + 1
    def communities_detection(self):
        return community_louvain.best_partition(self.graph)
    # the K-core decomposition
    def k_core_decomposition(self):
        k = 1
        graph = self.graph.copy()
        store_k_shell = {}
        nodes = [n for n in graph.nodes()]
        for node in nodes:
            if graph.degree(node) == 0:
                graph.remove_node(node)
        while graph.number_of_nodes() != 0:
            to_prune = [key1 for key1, v in {key: graph.degree(key) for key in graph.nodes()}.items() if v == k]
            k_shell = []
            while len(to_prune) > 0:
                i = to_prune.pop(0)
                neighbors = [l for l in graph.neighbors(i)]
                for j in neighbors:
                    if j in graph.nodes() and graph.degree(j) - 1 == k:
                        to_prune.append(j)
                k_shell.append(i)
                graph.remove_node(i)
            # store shell
            if len(k_shell) != 0: store_k_shell[k] = k_shell
            k += 1
        return store_k_shell
    def get_elem(self):
        nodes = []
        edges = []
        for node in self.graph.nodes:
            x = {'data': {'id': str(node), 'label': self.graph.nodes[node].get('OFFICIAL SYMBOL', 'Unknown')}}
            nodes.append(x)
        for source,target in self.graph.edges:
            y = {'data': {'source': str(source), 'target': str(target), 'label': self.graph.edges[(source, target)].get('Official Symbol', 'Unknown')}}
            edges.append(y)
        return nodes + edges 
    def get_elements(self, layout):
        pos = nx.random_layout(self.graph)
        if layout == 'circular':
            pos = nx.circular_layout(self.graph)
        if layout == 'spectral':
            pos = nx.spectral_layout(self.graph)
        if layout == 'spring':
            pos = nx.spring_layout(self.graph)
        if layout == "fruchterman":
            pos = nx.fruchterman_reingold_layout(self.graph)
        if layout == "spiral":
            pos = nx.spiral_layout(self.graph)
        if layout == "shell":
            pos = nx.shell_layout(self.graph)
        nodes = [
            {
                'data': {'id': str(node), 'label': self.graph.nodes[node].get('OFFICIAL SYMBOL', 'Unknown')},
                'position': {'x': pos[node][0]*1000 , 'y': pos[node][1]*1000}
            }
            for node in self.graph.nodes
        ]
        edges = [
            {
                'data': {'source': str(source), 'target': str(target), 'label': self.graph.edges[(source, target)].get('Official Symbol', 'Unknown')}
            }
            for source, target in self.graph.edges
        ]
        return nodes + edges
    def color_elems(self,partition,elements):
        elem = elements.copy()
        tab = [0]*(self.numberofnodes())
        tab_keys = partition.keys()
        count = 0
        for i in tab_keys:
                index = partition.get(i)
                if tab[index] == 0:
                    if index < 147:
#                   x = np.random.randint(0,863)
                        tab[index] = self.colors[index]
                        to_add = {'classes':tab[index]}
                        elem[count].update(to_add)
                        count = count + 1
                    else :
                        index = index % 147
                        tab[index] = self.colors[index]
                        to_add = {'classes':tab[index]}
                        elem[count].update(to_add)
                        count = count + 1                       
                else:
                    to_add = {'classes': tab[index]}
                    elem[count].update(to_add)
                    count = count + 1
        return elem