from graph import GraphMatrix, GraphAdjList, GraphAlgorithms
from export import export_directed_graph, export_undirected_graph
from check_degree import check_vertex_degree


def main():
    # Crie uma instância da classe GraphMatrix e adicione arestas
    matrix_graph = GraphMatrix(4)
    matrix_graph.add_edge(0, 1, 2)
    matrix_graph.add_edge(0, 2, 3)
    matrix_graph.add_edge(1, 2, 4)
    matrix_graph.add_edge(2, 3, 1)
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
    
    check_vertex_degree(matrix_graph)
    print("Grau dos vértices:")
    print(matrix_graph.degree)

    print("Grau do grafo:")
    print(matrix_graph.graph_degree)

    print("Lista de Adjacência:")
    print("exemplo: [(vertice1, peso1),(vertice2, peso2)]")
    for i, neighbors in enumerate(adj_list_graph.graph):
        print(f"Vértice {i}: {neighbors}")

    graph_algorithms = GraphAlgorithms()

    vertex_to_check = 2
    num_vertices = len(adj_list_graph.graph)
    neighbors_matrix = graph_algorithms.get_neighbors(matrix_graph, vertex_to_check, num_vertices)

    print(f"Vizinhos do Vértice {vertex_to_check}: {neighbors_matrix}")

    print("O Grafo é Conexo:", graph_algorithms.is_connected(matrix_graph))

    print("O Grafo é Regular:", graph_algorithms.is_regular(matrix_graph))

    print("O Grafo Completo:", graph_algorithms.is_complete(matrix_graph.graph))

    # Funções de exportações para .gexf

    export_directed_graph(matrix_graph, "Directed_graph.gexf")
    export_undirected_graph(matrix_graph, "Undirected_graph.gexf")
    
    # Teste de busca em profundidade
    start_vertex = 0
    end_vertex = 3
    path = GraphAlgorithms.depth_first_search(matrix_graph, start_vertex, end_vertex)
    
    if path:
        print(f"Caminho entre {start_vertex} e {end_vertex}: {path}")
    else:
        print(f"Não há caminho entre {start_vertex} e {end_vertex}.")

    # Teste de verificação de existência de caminho
    has_path = GraphAlgorithms.has_path(matrix_graph, start_vertex, end_vertex)
    if has_path:
        print(f"Existe um caminho entre {start_vertex} e {end_vertex}.")
    else:
        print(f"Não existe um caminho entre {start_vertex} e {end_vertex}.")

if __name__ == "__main__":
    main()
