def export_undirected_graph(graph, file_name):
    with open(file_name, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
        f.write('  <graph defaultedgetype="undirected">\n')

        f.write('    <nodes>\n')
        for i in range(len(graph)):
            f.write(f'      <node id="{i}" label="Node {i}" />\n')
        f.write('    </nodes>\n')

        f.write('    <edges>\n')
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                # Verifica se a aresta é ponderada
                if graph.weight[i][j] != 0:
                    if graph.weight[i][j] == graph.weight[j][i]:
                       f.write(f'      <edge source="{i}" target="{j}" weight="{graph.weight[i][j]}"/>\n')
                # Caso não seja ponderada verifica se é uma conexão bilateral
                elif graph.graph[i][j] == 1:
                    if graph.graph[j][i] == 1:      
                        f.write(f'      <edge source="{i}" target="{j}"/>\n')
        f.write('    </edges>\n')

        f.write('  </graph>\n')
        f.write('</gexf>\n')


def export_directed_graph(graph, file_name):
    with open(file_name, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
        f.write('  <graph defaultedgetype="directed">\n')

        f.write('    <nodes>\n')
        for i in range(len(graph)):
            f.write(f'      <node id="{i}" label="Node {i}" />\n')
        f.write('    </nodes>\n')

        f.write('    <edges>\n')
        for i in range(len(graph)):
            for j in range(len(graph)):
                # Verifica se a aresta não é ponderada e não vazia
                if graph.weight[i][j] == 0 and graph.graph[i][j] != 0:
                    f.write(f'      <edge source="{i}" target="{j}" type="directed"/>\n')
                # Verifica se a aresta é ponderada
                elif graph.weight[i][j] != 0:
                    f.write(f'      <edge source="{i}" target="{j}" type="directed" weight="{graph.weight[i][j]}"/>\n')
                   
        f.write('    </edges>\n')

        f.write('  </graph>\n')
        f.write('</gexf>\n')