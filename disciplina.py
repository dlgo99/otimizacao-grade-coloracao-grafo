import csv

class Disciplina:
    def __init__(self, nome, periodo, unidade, aulas):
        self.nome = nome
        self.periodo = periodo
        self.unidade = unidade
        self.aulas = aulas

    def __str__(self):
        return f"Objeto Disciplina:\nNome:\t\t\t{self.nome}\nPeriodo:\t\t{self.periodo}\nUnidade:\t\t{self.unidade}\nAulas por semana:\t{self.aulas}\n"

# Procurar uma disciplina pelo nome, na lista de disciplinas
def buscar(nome, lista):
    for disciplina in lista:
        if disciplina.nome == nome:
            return disciplina
    return None

# Lista de objetos Disciplina
disciplinas = [] 

# Criar as disciplinas
with open('disciplinas.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # pular o cabeçalho do arquivo CSV

    for row in reader:
        disciplina = Disciplina(row[0], row[1], row[2], int(row[3]))
        disciplinas.append(disciplina)

# Imprimir as disciplinas
# for disciplina in disciplinas:
#     print(disciplina)
