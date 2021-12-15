import networkx as nx
import community as community_louvain
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)


class MyGraph:
    def __init__(self, nodes=None, edges=None):
        self.graph = nx.Graph()
        self.graph_all = nx.Graph()
        self.mst = None
        self.df_nodes = nodes
        self.df_edges = edges
        self.df_nodes["color"] = ["yellow" for _ in range(self.df_nodes.shape[0])]
        self.createGraph()
        self.colors = []
        self.df_centrality = pd.DataFrame(columns=["nodes", "bet_centrality", "closeness_centrality", "eigen_centrality"])

    def betweenness_centrality(self):
        return nx.betweenness_centrality(self.graph)

    def closeness_centrality(self, node=None):
        if node:
            return nx.closeness_centrality(self.graph, node)
        else:
            return nx.closeness_centrality(self.graph)

    def eigenvector_centrality(self):
        return nx.eigenvector_centrality(self.graph)
    
    # Function To Build Graph
    def createGraph(self):
        self.graph.add_nodes_from(self.df_nodes['#BIOGRID ID'])
        self.graph_all = nx.from_pandas_edgelist(self.df_edges,'Official Symbol Interactor A','Official Symbol Interactor B')
        length = len(self.df_edges)
        tab = self.graph.nodes()
        for x in range(length):
            first = self.df_edges.iat[x,3]
            second = self.df_edges.iat[x,4]
            if first in tab and second in tab:
                self.graph.add_edge(first,second)

        dict_nodes = self.df_nodes.set_index('#BIOGRID ID').to_dict()
        self.mst = nx.minimum_spanning_tree(self.graph)
        for key in dict_nodes:
            nx.set_node_attributes(self.graph, dict_nodes[key], name=key)
            nx.set_node_attributes(self.mst, dict_nodes[key], name=key)

    def set_centrality_measures(self):
        print(len(self.df_centrality))
        betweeness_centrality = self.betweeness_centrality()
        g_closeness_centrality = self.closeness_centrality()
        eigen_centrality = self.eigenvector_centrality()
        self.df_centrality["nodes"] = list(betweeness_centrality.keys())
        self.df_centrality["bet_centrality"] = list(betweeness_centrality.values())
        self.df_centrality["closeness_centrality"] = list(g_closeness_centrality.values())
        self.df_centrality["eigen_centrality"] = list(eigen_centrality.values())

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
        return max(partition.values()) + 1
    def communities_detection(self):
        return community_louvain.best_partition(self.graph)
    # compute shortest path
    # DOIT RENVOYER UN TABLEAU DE DICO ET ELEMENTS EST UN TAB DE DICO DU GRAPH PRINCIPALE
    def shortestpath(self,source,target,elements):
        BioGRID_source = None ## BIOGRID ID (int)
        BioGRID_target = None##BIOGRID ID (int)
        for node in self.graph.nodes:### node c'est un int
            if source == self.graph.nodes[node].get('OFFICIAL SYMBOL'):
                BioGRID_source = node## biogrid id de la source
            elif target == self.graph.nodes[node].get('OFFICIAL SYMBOL'):
                BioGRID_target = node ##biogrid id de la target
        path = nx.shortest_path(self.graph,BioGRID_source,BioGRID_target)
        to_add = {'classes':'red'}
        nb = self.numberofnodes()
        for x in range(len(path)):
            for y in range(nb):
                if str(path[x]) == (elements[y]['data']['id']):
                    elements[y].update(to_add)
        nedges = self.numberofedges()
        for i in range(len(path)-1):
            for j in range(nedges):
                if (((elements[nb+j]['data']['source'] == str(path[i])) | (elements[nb+j]['data']['target'] == str(path[i]))) & ((elements[nb+j]['data']['source'] == str(path[i+1]))|(elements[nb+j]['data']['target']==str(path[i+1])))):
                    elements[nb+j].update(to_add)
        return elements
        ## colorier les nodes du chemin trouvédans le dico
        # renvoyer le dico
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
        pos2 = nx.random_layout(self.mst)
        if layout == 'circular':
            pos = nx.circular_layout(self.graph)
            pos2 = nx.circular_layout(self.mst)

        if layout == 'spectral':
            pos = nx.spectral_layout(self.graph)
            pos2 = nx.spectral_layout(self.mst)

        if layout == 'spring':
            pos = nx.spring_layout(self.graph)
            pos2 = nx.spring_layout(self.mst)

        if layout == "fruchterman":
            pos = nx.fruchterman_reingold_layout(self.graph)
            pos2 = nx.fruchterman_reingold_layout(self.mst)

        if layout == "spiral":
            pos = nx.spiral_layout(self.graph)
            pos2 = nx.spiral_layout(self.mst)
            
        if layout == "shell":
            pos = nx.shell_layout(self.graph)
            pos2 = nx.shell_layout(self.mst)
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
        nodes2 = [
            {
                'data': {'id': str(node), 'label': self.graph.nodes[node].get('OFFICIAL SYMBOL', 'Unknown')},
                'position': {'x': pos2[node][0]*1000 , 'y': pos2[node][1]*1000}
            }
            for node in self.graph.nodes
        ]
        edges2 = [
            {
                'data': {'source': str(source), 'target': str(target), 'label': self.mst.edges[(source, target)].get('Official Symbol', 'Unknown')}
            }
            for source, target in self.mst.edges       
        ]      
        return nodes + edges, nodes2 + edges2
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
    def alledges(self,node_data):
        ###dico info sur le nœud
        name = node_data['label']
        print(name)
        G = nx.Graph()
        for x in self.graph_all.adj[name]:
            G.add_edge(name,x)
        pos = nx.circular_layout(self.graph_all)
        elements= []
        nodes = []
        edges = []
        for node in G.nodes:
            nodes.append({'data':{'id' : node},'position':{'x': pos[node][0]*1000, 'y': pos[node][1]*1000}})
        for source,target in G.edges:
            edges.append({'data':{'source':source,'target':target}})
        return nodes + edges
        
