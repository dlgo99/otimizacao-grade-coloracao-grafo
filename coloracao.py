import networkx as nx
import matplotlib.pyplot as plt
import csv
import cor
import disciplina
import vertice

# Procurar uma cor pelo nome, na lista de obetos cores
def checarRestricao(node1, node2):
    restricao = False

    # Não pode haver aulas do mesmo periodo e da mesma unidade no mesmo horario
    if (node1.disciplina.periodo == node2.disciplina.periodo and node1.disciplina.unidade == node2.disciplina.unidade):
        restricao = True
    # Não pode haver aulas do mesmo professor no mesmo horario
    if (node1.professor == node2.professor):
        restricao = True

    return restricao

# Criação do grafo
G = nx.Graph()

# Adicionar vários nós ao grafo
for node in vertice.vertices:
    G.add_node(node.id)

# Atribuir cores aos nós usando o algoritmo greedy_color
# color_map = nx.greedy_color(G, strategy="largest_first")

# Mapear os códigos de cor para os nomes de cor
# color_names = {i: cor.colors[color] for i, color in enumerate(set(color_map.values()))}

# ------------------------------------------------------------------------
while True: # do while
    novaRestricao = False

    # Atribuir cores aos nós usando o algoritmo greedy_color
    color_map = nx.greedy_color(G, strategy="largest_first")

    # Mapear os códigos de cor para os nomes de cor
    color_names = {i: cor.colors[color] for i, color in enumerate(set(color_map.values()))}

    # Atribuir os objetos cores aos objetos vertices
    for node, color in color_map.items():
        node_color = cor.buscar(color_names[color], cor.cores)
        vertice.vertices[node-1].cor = node_color
        # print(f"No: {node} Cor: {color_names[color]}")

    # Checar se existem restrições entre vertices e adicionar aresta se sim
    for node1 in range(len(vertice.vertices)):
        for node2 in range(node1+1, len(vertice.vertices)):
            if (checarRestricao(vertice.vertices[node1], vertice.vertices[node2])):
                if not G.has_edge(node1+1, node2+1):
                    G.add_edge(node1+1, node2+1)
                    novaRestricao = True
    
    if not novaRestricao:
        break  # Sai do loop
# ------------------------------------------------------------------------

# PRINTAR APENAS (REMOVER)
for node, color in sorted(color_map.items(), key=lambda x: x[0]):
    print(vertice.vertices[node-1])

# Salvar em aulas.csv
with open('aulas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Escrever o cabeçalho do arquivo CSV
    writer.writerow(['id', 'professor', 'disciplina', 'periodo', 'unidade', 'turno', 'dia', 'horario', 'cor'])

    # Escrever os dados no arquivo CSV
    for aula in vertice.vertices:
        writer.writerow([aula.id, aula.professor, aula.disciplina.nome, aula.disciplina.periodo, aula.disciplina.unidade, aula.disciplina.turno, aula.cor.dia, aula.cor.horario, aula.cor.nome])

# Plotar o grafo com as cores atribuídas aos nós
nx.draw(G, with_labels=True, node_color=[vertice.vertices[node-1].cor.nome for node in G.nodes])
plt.show()
