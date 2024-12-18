import networkx as nx
import matplotlib.pyplot as plt
#from graphviz import Digraph

def readingFile(file_name): 
    G = nx.Graph()
    with open(file_name, 'r') as f:
        f.readline()  
        for line in f:
            if line.strip():
                try:
                    a, b = map(int, line.strip().split())
                    G.add_edge(a, b)
                except ValueError:
                    continue  
    return G

def sum_graus(graph):
    return 2*graph.number_of_edges()

def calc_grau(graph):
    return dict(graph.degree())

def max_grau(graph):
    graus = calc_grau(graph)
    return max(graus.values())

def min_grau(graph):
    graus = calc_grau(graph)
    return min(graus.values())

def draw_graph(graph):
    nx.draw(graph, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    plt.show()

def conex_components(graph):
    return list(nx.connected_components(graph))

def max_min_component(graph):
    components = conex_components(graph)
    sizes = [len(component) for component in components]

    max_c = max(sizes)
    min_c = min(sizes)

    return max_c, min_c

def bfs(graph, root):
    bfs_tree = nx.bfs_tree(graph, source=root)
    distances = nx.single_source_shortest_path_length(bfs_tree, root)
    greatest_dist = max(distances.values())
    return greatest_dist

def diameter_bfs(graph):
    greatest_d = 0
    for vertex in graph.nodes:
        distances = nx.single_source_shortest_path_length(graph, vertex)
        greatest_d_vertex = max(distances.values())
        greatest_d = max(greatest_d, greatest_d_vertex)

        return greatest_d

def main(file_name):
    G = readingFile(file_name)
    sumG = sum_graus(G)
    maxG = max_grau(G)
    minG = min_grau(G)
    count_comp_con = conex_components(G)
    size_max_c, size_min_c = max_min_component(G)
    grt_dist_1 = bfs(G, root=1)
    grt_dist_2 = bfs(G, root=2)
    grt_dist_3 = bfs(G, root=3)
    grt_dist_4 = bfs(G, root=4)
    grt_dist_5 = bfs(G, root=5)
    grt_dist_6 = bfs(G, root=6)
    grt_dist_7 = bfs(G, root=7)
    grt_dist_8 = bfs(G, root=8)
    grt_dist_9 = bfs(G, root=9)
    grt_dist_10 = bfs(G, root=10)
    grt_dist_11 = bfs(G, root=11)
    grt_dist_12 = bfs(G, root=12)
    grt_dist_13 = bfs(G, root=13)
    grt_dist_14 = bfs(G, root=14)
    grt_dist_15 = bfs(G, root=15)
    grt_dist_16 = bfs(G, root=16)
    grt_dist_17 = bfs(G, root=17)
    grt_dist_18 = bfs(G, root=18)
    grt_dist_19 = bfs(G, root=19)
    grt_dist_20 = bfs(G, root=20)
    grt_min_dist = diameter_bfs(G)

    print(f"soma total dos graus: {sumG}")
    print(f"maior grau: {maxG}")
    print(f"menor grau: {minG}")
    print(f"número de componentes conexos: {len(count_comp_con)}")
    print(f"tamanho do maior componente conexo: {size_max_c}")
    print(f"tamanho do menor componente conexo: {size_min_c}")
    print(f"maior distância a partir do vértice 1: {grt_dist_1}")
    print(f"maior distância a partir do vértice 2: {grt_dist_2}")
    print(f"maior distância a partir do vértice 3: {grt_dist_3}")
    print(f"maior distância a partir do vértice 4: {grt_dist_4}")
    print(f"maior distância a partir do vértice 5: {grt_dist_5}")
    print(f"maior distância a partir do vértice 6: {grt_dist_6}")
    print(f"maior distância a partir do vértice 7: {grt_dist_7}")
    print(f"maior distância a partir do vértice 8: {grt_dist_8}")
    print(f"maior distância a partir do vértice 9: {grt_dist_9}")
    print(f"maior distância a partir do vértice 10: {grt_dist_10}")
    print(f"maior distância a partir do vértice 11: {grt_dist_11}")
    print(f"maior distância a partir do vértice 12: {grt_dist_12}")
    print(f"maior distância a partir do vértice 13: {grt_dist_13}")
    print(f"maior distância a partir do vértice 14: {grt_dist_14}")
    print(f"maior distância a partir do vértice 15: {grt_dist_15}")
    print(f"maior distância a partir do vértice 16: {grt_dist_16}")
    print(f"maior distância a partir do vértice 17: {grt_dist_17}")
    print(f"maior distância a partir do vértice 18: {grt_dist_18}")
    print(f"maior distância a partir do vértice 19: {grt_dist_19}")
    print(f"maior distância a partir do vértice 20: {grt_dist_20}")
    print(f"maior caminho mínimo: {grt_min_dist}")
    draw_graph(G)

if __name__ == "__main__":
    file_name = 'as_graph.txt' 
    main(file_name)
