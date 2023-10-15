from graph import GraphMatrix, GraphAdjList

def main():
    # Crie uma instância da classe GraphMatrix e adicione arestas
    matrix_graph = GraphMatrix(5)
    matrix_graph.add_edge(0, 1)
    matrix_graph.add_edge(1, 2)
    matrix_graph.add_edge(2, 3)

    # Crie uma instância da classe GraphAdjList e adicione arestas
    adj_list_graph = GraphAdjList(5)
    adj_list_graph.add_edge(0, 1)
    adj_list_graph.add_edge(1, 2)
    adj_list_graph.add_edge(2, 3)

    # Imprima as representações dos grafos
    print("Matriz de Adjacência:")
    for row in matrix_graph.graph:
        print(row)

    print("Lista de Adjacência:")
    for i, neighbors in enumerate(adj_list_graph.graph):
        print(f"Vértice {i}: {neighbors}")

if __name__ == "__main__":
    main()
