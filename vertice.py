import csv
import disciplina

# Definição da classe Vertice que representa o professor com suas informacoes
class Vertice:
    id = 1

    def __init__(self, professor, disciplina):
        self.id = Vertice.id
        Vertice.id += 1
        self.professor = professor
        self.disciplina = disciplina
        self.cor = None

    def __str__(self):
        return f"----------------------------------------\nObjeto Vertice:\t\t{self.id}\nProfessor:\t\t{self.professor}\n\t\t\n{self.disciplina}\n{self.cor}----------------------------------------\n"

# Lista de objetos Vertice
vertices = [] 

# Criar os vertices
with open('professores.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # pular o cabeçalho do arquivo CSV

    for row in reader:
        professor = row[0] # Nome do professor
        lecionadas = eval(row[1]) # Disciplinas lecionadas pelo professor
        for lecionada in lecionadas:
            objeto_disciplina = disciplina.buscar(lecionada, disciplina.disciplinas)
            if (objeto_disciplina):
                for _ in range(objeto_disciplina.aulas):
                    vertice = Vertice(professor, objeto_disciplina)
                    vertices.append(vertice)

# Imprimir os vertices
# for vertice in vertices:
#     print(vertice)