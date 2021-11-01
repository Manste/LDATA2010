import networkx as nx
import community as community_louvain
import pandas as pd
import matplotlib.pyplot as plt


class Net_analysis:
    def __init__(self, nodes_csv=None, edges_csv=None):
        assert nodes_csv is None or edges_csv is None, "Impossible to work with empty dataset"
        self.df_nodes = pd.read_table(nodes_csv)
        self.df_edges = pd.read_table(edges_csv)
        self.graph = self.createGraph()

    # Function To Build Graph
    def createGraph(self):
        nb_nodes = len(self.df_nodes.index)
        self.graph = nx.Graph()
        count = 0
        while count < nb_nodes:
            first = self.df_nodes.iat[count, 3]
            self.graph.add_node(first)
            count += 1
        label = {}
        for i in self.graph.nodes():
            label[i] = i
        count2 = 0
        tab = self.graph.nodes()
        nb_edges = len(self.df_edges.index)
        while count2 < nb_edges:
            first = self.df_edges.iat[count2, 7]
            second = self.df_edges.iat[count2, 8]
            if first in tab and second in tab:
                self.graph.add_edge(first, second)
            count2 += 1
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

