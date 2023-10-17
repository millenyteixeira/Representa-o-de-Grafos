def export_directed_graph(graph, file_name):
    with open(file_name, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
        f.write('  <graph defaultedgetype="mixed">\n')

        # Escreva os nós
        f.write('    <nodes>\n')
        for i in range(len(graph)):
            f.write(f'      <node id="{i}" label="Node {i}" />\n')
        f.write('    </nodes>\n')

        # Escreva as arestas
        f.write('    <edges>\n')
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                if graph.graph[i][j] == 1:
                    if graph.graph[j][i] == 0:
                        f.write(f'      <edge source="{i}" target="{j}" type="directed"/>\n')
                    else:
                        f.write(f'      <edge source="{i}" target="{j}"/>\n')
        f.write('    </edges>\n')

        f.write('  </graph>\n')
        f.write('</gexf>\n')

def export_weighted_graph(graph, file_name):
    with open(file_name, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
        f.write('  <graph defaultedgetype="directed">\n')

        # Escreva os nós
        f.write('    <nodes>\n')
        for i in range(len(graph)):
            f.write(f'      <node id="{i}" label="Node {i}" />\n')
        f.write('    </nodes>\n')

        # Escreva as arestas
        f.write('    <edges>\n')
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                if graph.graph[i][j] > 0:
                    weight = graph.graph[i][j]
                    f.write(f'      <edge source="{i}" target="{j}" weight="{weight}"/>\n')
        f.write('    </edges>\n')

        f.write('  </graph>\n')
        f.write('</gexf>\n')