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

            for neighbor in GraphAlgorithms.get_neighbors(graph, vertex):
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