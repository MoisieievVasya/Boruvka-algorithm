from set_operations import find_set, union_set


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