import time
import analise
from graph import generate_random_graph
from boruvka_algorithm import boruvka_algorithm_adj_list, boruvka_algorithm_adj_matrix

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

    with open('output_files/by_list.txt', 'w') as f:
        for mass in times_by_list:
            for d, v, t, w in mass:
                f.write(f"Density:{d}, Vertices: {v}, Time: {t:.4f} seconds, MST Weight by list: {w}\n")

    with open('output_files/by_matrix.txt', 'w') as f:
        for mass in times_by_matrix:
            for d, v, t, w in mass:
                f.write(f"Density:{d}, Vertices: {v}, Time: {t:.4f} seconds, MST Weight by matrix: {w}\n")

    with open('output_files/by_list_raw.txt', 'w') as f:
        for mass in times_by_list:
            for d, v, t, w in mass:
                f.write(f"{d} {v} {t:.4f} {w}\n")

    with open('output_files/by_matrix_raw.txt', 'w') as f:
        for mass in times_by_matrix:
            for d, v, t, w in mass:
                f.write(f"{d} {v} {t:.4f} {w}\n")

measure_performance()
analise.analise()