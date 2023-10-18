def check_vertex_degree(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            # Caso a aresta não seja ponderada
            if graph.weight[i][j] == 0:
                # Verifica se a aresta é não direcionada
                if graph.graph[i][j] == 1 and graph.graph[j][i] == 1:
                    # Se a aresta não for direcionada nem ponderada, incrementa 1 o primeiro vértice
                    graph.degree[i] += 1
                # Verifica se a aresta é direcionada i>j
                elif graph.graph[i][j] == 1 and graph.graph[j][i] == 0:
                    # Se a aresta for direcionada mas não for ponderada, incrementa 1 apenas no vértice de saída
                    graph.degree[i] += 1
            # Caso a aresta seja ponderada
            else:
                # Verifica se a aresta é não direcionada
                if graph.graph[i][j] == graph.graph[j][i]:
                    # Se a aresta for ponderada mas direcionada, incrementa o peso respectivo para o primeiro vértice
                    graph.degree[i] += graph.weight[i][j]
                # Verifica se a aresta é direcionada i>j
                else:
                    # Se a aresta for direcionada mas não for ponderada, incrementa 1 apenas no vértice de saída
                    graph.degree[i] += graph.weight[i][j]

    # Definição do grau do grafo
    for i in range(len(graph)):
        graph.graph_degree += graph.degree[i]