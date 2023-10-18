from graph import GraphMatrix, GraphAdjList
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

    # Funções de exportações para .gexf

    export_directed_graph(matrix_graph, "Directed_graph.gexf")
    export_undirected_graph(matrix_graph, "Undirected_graph.gexf")

if __name__ == "__main__":
    main()
