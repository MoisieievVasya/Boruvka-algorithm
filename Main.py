import time
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

def find_set(parent, i):
    if parent[i] == i:
        return i
    return find_set(parent, parent[i])

def union_set(parent, rank, x, y):
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def boruvka_algorithm_adj_list(graph):
    if not hasattr(graph, 'adj_list'):
        graph.to_adjacency_list()
    num_vertices = graph.num_vertices
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    mst_weight = 0
    num_components = num_vertices

    while num_components > 1:
        cheapest = [-1] * num_vertices
        edges_added = False

        for i in range(num_vertices):
            for (j, w) in graph.adj_list[i]:
                set_i = find_set(parent, i)
                set_j = find_set(parent, j)
                if set_i != set_j:
                    if cheapest[set_i] == -1 or cheapest[set_i][0] > w:
                        cheapest[set_i] = (w, i, j)

        # Add cheapest edges to the MST
        for i in range(num_vertices):
            if cheapest[i] != -1:
                w, u, v = cheapest[i]
                set_u = find_set(parent, u)
                set_v = find_set(parent, v)
                if set_u != set_v:
                    mst_weight += w
                    union_set(parent, rank, set_u, set_v)
                    num_components -= 1
                    edges_added = True

        if not edges_added:
            break

    return mst_weight

def boruvka_algorithm_adj_matrix(graph):
    if not hasattr(graph, 'adj_matrix'):
        graph.to_adjacency_matrix()
    num_vertices = graph.num_vertices
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    mst_weight = 0
    num_components = num_vertices

    while num_components > 1:
        cheapest = [-1] * num_vertices
        edges_added = False

        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph.adj_matrix[i][j] != 0:
                    set_i = find_set(parent, i)
                    set_j = find_set(parent, j)
                    if set_i != set_j:
                        if cheapest[set_i] == -1 or cheapest[set_i][0] > graph.adj_matrix[i][j]:
                            cheapest[set_i] = (graph.adj_matrix[i][j], i, j)

        # Add cheapest edges to the MST
        for i in range(num_vertices):
            if cheapest[i] != -1:
                w, u, v = cheapest[i]
                set_u = find_set(parent, u)
                set_v = find_set(parent, v)
                if set_u != set_v:
                    mst_weight += w
                    union_set(parent, rank, set_u, set_v)
                    num_components -= 1
                    edges_added = True

        if not edges_added:
            break

    return mst_weight

def measure_performance():
    vertices = [20, 50, 70, 90, 100, 120, 150, 180, 200]
    density = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    times_by_list = []
    times_by_matrix = []

    for _ in range(20):
        for v in vertices:
            time_for_v_by_list = []
            time_for_v_by_matrix = []
            for d in density:

                graph = generate_random_graph(v, d)
                start_time_list = time.time()
                mst_weight_list = boruvka_algorithm_adj_list(graph)
                end_time_list = time.time()

                graph.to_adjacency_matrix()
                start_time_matrix = time.time()
                mst_weight_matrix = boruvka_algorithm_adj_matrix(graph)
                end_time_matrix = time.time()

                time_for_v_by_list.append((d, v, end_time_list - start_time_list, mst_weight_list))
                time_for_v_by_matrix.append((d, v, end_time_matrix - start_time_matrix, mst_weight_matrix))
                # graph.visualize()

            times_by_list.append(time_for_v_by_list)
            times_by_matrix.append(time_for_v_by_matrix)

    with open('by_list.txt', 'w') as f:
        for mass in times_by_list:
            for d, v, t, w in mass:
                f.write(f"Density:{d}, Vertices: {v}, Time: {t:.4f} seconds, MST Weight by list: {w}\n")

    with open('by_matrix.txt', 'w') as f:
        for mass in times_by_matrix:
            for d, v, t, w in mass:
                f.write(f"Density:{d}, Vertices: {v}, Time: {t:.4f} seconds, MST Weight by matrix: {w}\n")

    with open('by_list_raw.txt', 'w') as f:
        for mass in times_by_list:
            for d, v, t, w in mass:
                f.write(f"{d} {v} {t:.4f} {w}\n")

    with open('by_matrix_raw.txt', 'w') as f:
        for mass in times_by_matrix:
            for d, v, t, w in mass:
                f.write(f"{d} {v} {t:.4f} {w}\n")

measure_performance()
