from collections import deque
import sys

# Matriz de adjacência do grafo
class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

        # Criação da matriz peso para exportação
        self.weight = [[0] * num_vertices for _ in range(num_vertices)]

        # Criação da lista de graus do vértice para consulta
        self.degree = [0 for _ in range(num_vertices)]

        # Criação da variável de grau do grafo
        self.graph_degree = 0
        
    # Método que retornará o número de vértices
    def __len__(self):
        return self.num_vertices
    
    # Adicionar aresta simples
    def add_edge(self, v1, v2, wght=0):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            # Caso o peso seja 0 (padrão) a aresta não sera ponderada
            if wght == 0:
                self.graph[v1][v2] = 1
                self.graph[v2][v1] = 1
            else:
                # Salvar o peso inserido pelo usuário na matriz de peso
                self.weight[v1][v2] = wght
                self.weight[v2][v1] = wght
                self.graph[v1][v2] = wght
                self.graph[v2][v1] = wght

    # Adicionar aresta direcionada de v1 para v2
    def add_directed_edge(self, v1, v2, wght=0):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            # Caso o peso seja 0 (padrão) a aresta não sera ponderada
            if wght == 0:
                self.graph[v1][v2] = 1
                # self.graph[v2][v1] = 0        # Remove a aresta de v2>v1 ao adicionar v1>v2
            else:
                # Salvar o peso inserido pelo usuário na matriz de peso
                self.weight[v1][v2] = wght
                self.graph[v1][v2] = wght
                # self.graph[v2][v1] = 0        # Remove a aresta de v2>v1 ao adicionar v1>v2

    # Remover aresta
    def remove_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.graph[v1][v2] = 0
            self.graph[v2][v1] = 0

# Lista de adjacência do grafo
class GraphAdjList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

        # Criação da lista peso para consulta de grau
        # self.weight = [[] for _ in range(num_vertices)]

    # Adicionar aresta simples
    def add_edge(self, v1, v2, wght = 0):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            # Caso o peso seja 0 (padrão) a aresta não sera ponderada
            if wght == 0:
                self.graph[v1].append(v2)
                self.graph[v2].append(v1)
            else:
                temp1 = (v2, wght)
                temp2 = (v1, wght)
                # self.weight[v1].append(wght) # Salva o peso da lista de adjacência em uma lista peso
                # self.weight[v2].append(wght)
                self.graph[v1].append(temp1)
                self.graph[v2].append(temp2)

    # Adicionar aresta direcionada de v1 para v2
    def add_directed_edge(self, v1, v2, wght = 0):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            # Caso o peso seja 0 (padrão) a aresta não sera ponderada
            if wght == 0:
                self.graph[v1].append(v2)
                # if v1 in self.graph[v2]:
                #     self.graph[v2].remove(v1)  # Remove a aresta de v2>v1 ao adicionar v1>v2 
            else:
                temp1 = (v2, wght)
                #temp2 = (v1, wght)
                # self.weight[v1].append(wght) # Salva o peso da lista de adjacência em uma lista peso
                self.graph[v1].append(temp1)
                # if temp2 in self.graph[v2]:
                #     self.graph[v2].remove(temp2) # Remove a aresta de v2>v1 ao adicionar v1>v2
            
    # Remover aresta
    def remove_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
            if v1 in self.graph[v2]:
                self.graph[v2].remove(v1)

class GraphAlgorithms:

    @staticmethod
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

    @staticmethod
    def get_neighbors(graph, vertex, num_vertices):
        neighbors = []  # Inicializa neighbors como uma lista vazia
        if 0 <= vertex < num_vertices:
            if isinstance(graph, GraphMatrix):
                # Se o grafo for representado como matriz de adjacência
                # Encontra os vizinhos verificando as entradas na linha correspondente ao vértice
                neighbors = [i for i in range(num_vertices) if graph.graph[vertex][i] == 1]
            elif isinstance(graph, GraphAdjList):
                # Se o grafo for representado como lista de adjacência
                # Os vizinhos estão diretamente armazenados na lista de adjacência do vértice
                neighbors = graph.graph[vertex]
        return neighbors

    @staticmethod
    def is_connected(graph):
        num_vertices = len(graph)
        visited = [False] * num_vertices

        def dfs(vertex):
            visited[vertex] = True
            for neighbor in GraphAlgorithms.get_neighbors(graph, vertex, num_vertices):
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(num_vertices):
            if not visited[i]:
                # Realiza uma busca em profundidade para verificar a conectividade do grafo
                dfs(i)

        return all(visited)

    @staticmethod
    def is_regular(graph):
        if isinstance(graph, GraphMatrix):
            degree = sum(graph.graph[0])
            for i in range(1, len(graph)):
                # Verifica se todos os vértices têm o mesmo grau no grafo representado como matriz de adjacência
                if sum(graph.graph[i]) != degree:
                    return False
        elif isinstance(graph, GraphAdjList):
            degree = len(graph.graph[0])
            for i in range(1, len(graph.graph)):
                # Verifica se todos os vértices têm o mesmo grau no grafo representado como lista de adjacência
                if len(graph.graph[i]) != degree:
                    return False
        return True

    @staticmethod
    def is_complete(graph):
        num_vertices = len(graph)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if i != j and j not in graph[i]:
                    # Verifica se cada vértice está conectado a todos os outros vértices
                    return False
        return True
    
    #busca em profundidade
    @staticmethod
    def depth_first_search(graph, start_vertex, end_vertex):
        num_vertices = len(graph)
        visited = [False] * len(graph)
        path = []

        def dfs(vertex):
            #marca o vértice como visitado
            visited[vertex] = True
            path.append(vertex)
            if vertex == end_vertex:
                return True
            for neighbor in GraphAlgorithms.get_neighbors(graph, vertex, len(graph)):
                #se nao tiver sido visitado fazer a dfs
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            #desfazer a inclusão do vértice atual no caminho quando nenhum caminho válido é encontrado a partir dele
            path.pop()
            return False

        if dfs(start_vertex):
            return path
        else:
            return []

    @staticmethod
    def breadth_first_search(graph, start_vertex, end_vertex):
        #rastrear quais vértices foram visitados
        visited = [False] * len(graph)
        queue = deque()
        path = [-1] * len(graph)

        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            if vertex == end_vertex:
                break

            for neighbor in GraphAlgorithms.get_neighbors(graph, vertex, len(graph)):
                #adiciona os vizinhos não visitados à fila e  marca como visitados
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    path[neighbor] = vertex

        #Se não for possível encontrar um caminho, a função retorna uma lista vazia
        if path[end_vertex] == -1:
            return []
        else:
            path_list = []
            while end_vertex != -1:
                path_list.append(end_vertex)
                end_vertex = path[end_vertex]
            return path_list[::-1]

    @staticmethod
    def has_path(graph, start_vertex, end_vertex):
        #se a busca em profundidade retornar uma lista maior que 0, existe caminho
        return len(GraphAlgorithms.depth_first_search(graph, start_vertex, end_vertex)) > 0

    @staticmethod
    def find_path(graph, start_vertex, end_vertex):
        #retorna a busca em largura
        return GraphAlgorithms.breadth_first_search(graph, start_vertex, end_vertex)
    
    

    @staticmethod
    def bellman_ford(graph, source):
        distance = [float("Inf")] * len(graph.graph)
        distance[source] = 0

        # Passo 2: Relaxa as arestas |V| - 1 vezes
        for _ in range(len(graph.graph) - 1):
            for u in range(len(graph.graph)):
                for v in range(len(graph.graph)):
                    if graph.graph[u][v] != 0:  # Verifica se há uma aresta entre u e v
                        if distance[u] != float("Inf") and distance[u] + graph.graph[u][v] < distance[v]:
                            distance[v] = distance[u] + graph.graph[u][v]

        # Passo 3: Verifica ciclos negativos
        for u in range(len(graph.graph)):
            for v in range(len(graph.graph)):
                if graph.graph[u][v] != 0:  # Verifica se há uma aresta entre u e v
                    if distance[u] != float("Inf") and distance[u] + graph.graph[u][v] < distance[v]:
                        print("O grafo contém um ciclo de peso negativo")
                        return

     
        # retorna as distâncias mais curtas
        return distance
    
    # Dentro da classe GraphAlgorithms
    @staticmethod
    def floyd_warshall(graph):
        num_vertices = len(graph)
        distance_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

        for i in range(num_vertices):
            for j in range(num_vertices):
                if i == j:
                    distance_matrix[i][j] = 0
                elif graph[i][j] != 0:
                    distance_matrix[i][j] = graph[i][j]

        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if distance_matrix[i][k] != float('inf') and distance_matrix[k][j] != float('inf'):
                        distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

        return distance_matrix

    @staticmethod
    def dijkstra(graph, start):

        # Inicializa todos os vértices com infinito e a origem com 0
        distance = [float("Inf")] * len(graph.graph)
        distance[start] = 0

        # Relaxa as arestas
        for _ in range(len(graph.graph) - 1):
            for i in range(len(graph.graph)):
                for j in range(len(graph.graph)):
                    if graph.graph[i][j] != 0:  # Verifica se há uma aresta entre os dois vértices
                        if distance[i] != float("inf") and distance[i] + graph.graph[i][j] < distance[j]:
                            distance[j] = distance[i] + graph.graph[i][j]

        # Retorna as distâncias mais curtas a partir da origem
        return distance
'''    
        # Algoritmo de Dijkstra
    def dijkstra(graph, start):

        # Inicializa a distância para o vértice de origem como 0
        graph.distances[start] = 0

        # Usa uma fila de prioridade (heap) para manter os vértices a serem explorados
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Ignora vértices já processados
            if current_distance > graph.distances[current_vertex]:
                continue

            # Atualiza as distâncias dos vizinhos
            for neighbor in range(graph.num_vertices):
                if graph.graph[current_vertex][neighbor] > 0:
                    distance = current_distance + graph.weight[current_vertex][neighbor]

                    # Se encontrar um caminho mais curto, atualiza a distância
                    if distance < graph.distances[neighbor]:
                        graph.distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

        # Retorna as distâncias calculadas
        return graph.distances

    def dijkstra(graph, start):
        if start < 0 or start >= graph.num_vertices:
            raise ValueError("O vértice inicial está fora do intervalo válido.")

        # Inicializa as distâncias a partir do vértice de origem como infinito para todos os vértices
        distances = [float('inf')] * graph.num_vertices
        distances[start] = 0

        # Inicializa um conjunto para acompanhar os vértices já visitados
        visited = set()

        # Loop para encontrar o caminho mais curto para todos os vértices
        while len(visited) < graph.num_vertices:
            # Escolhe o vértice não visitado mais próximo
            min_distance = float('inf')
            min_vertex = -1
            for v in range(graph.num_vertices):
                if distances[v] < min_distance and v not in visited:
                    min_distance = distances[v]
                    min_vertex = v

            # Adiciona o vértice escolhido ao conjunto de visitados
            visited.add(min_vertex)

            # Atualiza as distâncias dos vizinhos do vértice escolhido
            for neighbor in GraphAlgorithms.get_neighbors(graph, min_vertex, graph.num_vertices):
                weight = graph.graph[min_vertex][neighbor]
                if weight != "-" and distances[min_vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[min_vertex] + weight

        return distances
'''   


