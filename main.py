from graph import GraphMatrix, GraphAdjList, GraphAlgorithms
from export import export_directed_graph, export_undirected_graph

def main():
    # Crie uma instância da classe GraphMatrix e adicione arestas
    matrix_graph = GraphMatrix(6)
    matrix_graph.add_edge(0, 1, 2)
    matrix_graph.add_edge(0, 2, 5)
    matrix_graph.add_edge(0, 3, 5)
    matrix_graph.add_edge(0, 5, 7)
    matrix_graph.add_edge(1, 2, 1)
    matrix_graph.add_edge(1, 3, 4)
    matrix_graph.add_edge(1, 4, 1)
    matrix_graph.add_edge(1, 5, 3)
    matrix_graph.add_edge(2, 5, 1)
    matrix_graph.add_edge(3, 4, 1)
    matrix_graph.add_edge(4, 5, 1)
    #matrix_graph.add_edge(1, 2)
    #matrix_graph.add_edge(2, 3)
    # matrix_graph.add_directed_edge(0, 1, 2)
    # matrix_graph.add_directed_edge(0, 2, 3)
    # matrix_graph.add_directed_edge(1, 2, 4)
    # matrix_graph.add_directed_edge(2, 3, 1)
  

    # Crie uma instância da classe GraphAdjList e adicione arestas
    adj_list_graph = GraphAdjList(4)
    adj_list_graph.add_edge(0, 1, 2)
    adj_list_graph.add_edge(0, 2, 3)
    adj_list_graph.add_edge(1, 2, 4)
    adj_list_graph.add_edge(2, 3, 1)
    # adj_list_graph.add_directed_edge(0, 1, 2)
    # adj_list_graph.add_directed_edge(0, 2, 3)
    # adj_list_graph.add_directed_edge(1, 2, 4)
    # adj_list_graph.add_directed_edge(2, 3, 1)

    # Imprima as representações dos grafos
    print("Matriz de Adjacência:")
    for row in matrix_graph.graph:
        print(row)
    
    print("\nLista de Adjacência:")
    for i, neighbors in enumerate(adj_list_graph.graph):
        print(f"Vértice {i}: {neighbors}")

    GraphAlgorithms.check_vertex_degree(matrix_graph)
    print("\nGrau dos vértices:")
    print(matrix_graph.degree)

    print("Grau do grafo:")
    print(matrix_graph.graph_degree)


    graph_algorithms = GraphAlgorithms()

    vertex_to_check = 2
    num_vertices = len(adj_list_graph.graph)
    neighbors_matrix = graph_algorithms.get_neighbors(matrix_graph, vertex_to_check, num_vertices)

    print(f"\nVizinhos do Vértice {vertex_to_check}: {neighbors_matrix}")

    print("O Grafo é Conexo:", graph_algorithms.is_connected(matrix_graph))

    print("O Grafo é Regular:", graph_algorithms.is_regular(matrix_graph))

    print("O Grafo Completo:", graph_algorithms.is_complete(matrix_graph.graph))

    print("Busca em Profundidade")
    # Teste de busca em profundidade
    print("\nbusca em profundidade:")
    start_vertex = 0
    end_vertex = 3
    path = GraphAlgorithms.depth_first_search(matrix_graph, start_vertex, end_vertex)
    
    if path:
        print(f"\nCaminho entre {start_vertex} e {end_vertex}: {path}")
    else:
        print(f"\nNão há caminho entre {start_vertex} e {end_vertex}.")

    print("Busca em Largura")
    # Teste de busca em largura
    path_2 = GraphAlgorithms.breadth_first_search(matrix_graph, start_vertex, end_vertex)
    if path_2:
        print(f"\nCaminho entre {start_vertex} e {end_vertex}: {path_2}")
    else:
        print(f"\nNão há caminho entre {start_vertex} e {end_vertex}.")


    # Teste de verificação de existência de caminho
    print(f"\nVerifica se existe caminho:")
    has_path = GraphAlgorithms.has_path(matrix_graph, start_vertex, end_vertex)
    if has_path:
        print(f"Existe um caminho entre {start_vertex} e {end_vertex}.")
    else:
        print(f"Não existe um caminho entre {start_vertex} e {end_vertex}.")

 

    # Funções de exportações para .gexf
    export_directed_graph(matrix_graph, "Directed_graph.gexf")
    export_undirected_graph(matrix_graph, "Undirected_graph.gexf")

    # Teste do algoritmo de Bellman-Ford para calcular a menor distância de uma origem para todos os outros vértices
    print("\nAlgoritmo de Bellman-Ford para uma origem:")
    start_vertex_bellman_ford = 0
    distances_from_source = graph_algorithms.bellman_ford(matrix_graph, start_vertex_bellman_ford)

    for i, distance in enumerate(distances_from_source):
        print(f"A distância mais curta de {start_vertex_bellman_ford} para {i} é {distance}")

    # Teste do algoritmo de Bellman-Ford para calcular a menor distância de todos para todos
    print("\nAlgoritmo de Bellman-Ford para todos os pares de vértices:")
    all_distances = []
    for v in range(len(matrix_graph)):
        distances_from_v = graph_algorithms.bellman_ford(matrix_graph, v)
        all_distances.append(distances_from_v)

    for i, distances_from_i in enumerate(all_distances):
        for j, distance in enumerate(distances_from_i):
            print(f"A distância mais curta de {i} para {j} é {distance}")
    # Dentro da função main


    # Teste do algoritmo de Dijkstra
    print("\nAlgoritmo de Dijkstra:")
    start_vertex_dijkstra = 0
    dijkstra_result = graph_algorithms.dijkstra(matrix_graph, start_vertex_dijkstra)

    # Imprimir a menor distância de uma origem para todos os outros vértices
    for i, distance in enumerate(distances_from_source):
        print(f"A distância mais curta de {start_vertex_dijkstra} para {i} é {distance}")

    # Imprimir a menor distância de todos para todos
    print("\nAlgoritmo de Dijkstra para todos os pares de vértices:")
    all_distances = []
    for v in range(len(matrix_graph)):
        distances_from_v = graph_algorithms.dijkstra(matrix_graph, v)
        all_distances.append(distances_from_v)

    for i, distances_from_i in enumerate(all_distances):
        for j, distance in enumerate(distances_from_i):
            print(f"A distância mais curta de {i} para {j} é {distance}")
            
if __name__ == "__main__":
    main()
