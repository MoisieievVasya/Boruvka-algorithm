import networkx as nx
import matplotlib.pyplot as plt
import random
class Graph:
    def __init__(self, vertices, representation='adjacency_list'):
        self.num_vertices = vertices
        if representation == 'adjacency_list':
            self.adj_list = [[] for _ in range(vertices)]
            self.adj_matrix = None
        elif representation == 'adjacency_matrix':
            self.adj_matrix = [[0] * vertices for _ in range(vertices)]
            self.adj_list = None

    def add_edge(self, u, v, weight):
        if self.adj_list is not None:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        if self.adj_matrix is not None:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def to_adjacency_matrix(self):
        if self.adj_list is not None and self.adj_matrix is None:
            self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
            for i in range(len(self.adj_list)):
                for (j, w) in self.adj_list[i]:
                    self.adj_matrix[i][j] = w
                    self.adj_matrix[j][i] = w
        self.adj_list = None

    def to_adjacency_list(self):
        if self.adj_matrix is not None and self.adj_list is None:
            self.adj_list = [[] for _ in range(self.num_vertices)]
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if self.adj_matrix[i][j] != 0:
                        self.adj_list[i].append((j, self.adj_matrix[i][j]))
        self.adj_matrix = None

    def visualize(self):
        G = nx.Graph()
        if self.adj_list is not None:
            for i in range(len(self.adj_list)):
                for (j, weight) in self.adj_list[i]:
                    G.add_edge(i, j, weight=weight)
        elif self.adj_matrix is not None:
            for i in range(self.num_vertices):
                for j in range(i + 1, self.num_vertices):
                    if self.adj_matrix[i][j] != 0:
                        G.add_edge(i, j, weight=self.adj_matrix[i][j])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='#FF5733', width=2, edge_cmap=plt.cm.Blues, node_size=700)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def __str__(self):
        if self.adj_list is not None:
            return str(self.adj_list)
        elif self.adj_matrix is not None:
            return str(self.adj_matrix)
        return "Graph not initialized properly"



def generate_random_graph(vertices, density, representation='adjacency_list'):
    graph = Graph(vertices, representation)
    for i in range(vertices):
        for j in range(i + 1, vertices):
            if random.random() < density:
                weight = random.randint(1, 10)
                graph.add_edge(i, j, weight)
    return graph