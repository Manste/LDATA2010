import networkx as nx
import community as community_louvain
import pandas as pd
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, nodes_csv=None, edges_csv=None, separator=','):
        self.graph = nx.Graph()
        self.df_nodes = pd.read_csv(nodes_csv, sep=',')
        self.df_edges = pd.read_csv(edges_csv, sep=',')
        self.createGraph()
        self.pos = nx.layout.spring_layout(self.graph)

    # Function To Build Graph
    def createGraph(self):
        self.graph.add_nodes_from(self.df_nodes['#BIOGRID ID'])
        self.graph.add_edges_from(self.df_edges[['BioGRID Gene ID', 'Related BioGRID Gene ID']].values.tolist())
        dict_nodes = self.df_nodes.set_index('#BIOGRID ID').to_dict()
        for key in dict_nodes:
            nx.set_node_attributes(self.graph, dict_nodes[key], name=key)
        dict_edges = self.df_edges.set_index(['BioGRID Gene ID', 'Related BioGRID Gene ID']).to_dict()
        for key in dict_edges:
            nx.set_edge_attributes(self.graph, dict_edges[key], name=key)
        self.graph.remove_node('-')
        return self.graph

    # Todo: Improve the Visualisation of the Graph
    def temp_visualization(self):
        plt.figure(figsize=(25, 20))
        plt.title('Protein Graph')
        pos1 = nx.spring_layout(self.graph, k=3, iterations=10)
        nx.draw_networkx_nodes(self.graph, pos1, alpha=0.5)
        nx.draw_networkx_edges(self.graph, pos1, alpha=0.3)
        nx.draw_networkx_labels(self.graph, pos1, font_size=10)
        plt.show()

    # compute the best partition
    def communities_detection(self):
        partition = community_louvain.best_partition(self.graph)
        pos = nx.spring_layout(self.graph, seed=4321, k=3)
        fig = plt.figure(figsize=(20, 10))
        communities_colors = ["#ff0000", "#02f51b", "#fc8505", "#d3fc05", "#00a1f2", "#ce00f2", "#6a5d7a", "#113832",
                              "#421408"]
        nb_communities = max(partition.values()) + 1
        for i in range(nb_communities):
            nb_community = 0
            for key, value in partition.items():
                if value == i:
                    nb_community += 1
            percentage = nb_community * 100 / len(partition)
            nx.draw_networkx_nodes(self.graph, pos, [k for k, v in partition.items() if v == i], cmap=plt.cm.RdYlBu,
                                   label="{} ({})%".format(nb_community, round(percentage, 3)),
                                   node_color=communities_colors[i])
        nx.draw_networkx_edges(self.graph, pos, alpha=0.1)
        nx.draw_networkx_labels(self.graph, pos)
        plt.legend(title="Per community")
        plt.show()

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

