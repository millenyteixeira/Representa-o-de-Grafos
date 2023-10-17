# Matriz de adjacência do grafo
class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

        # Criação da matriz peso para exportação
        self.weight = [[0] * num_vertices for _ in range(num_vertices)]

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