# Definição da classe Cor, onde no grafo é responsável por atribuir o horario
class Cor:
    def __init__(self, nome, dia, turno, horario):
        self.nome = nome
        self.dia = dia
        self.turno = turno
        self.horario = horario

    def __str__(self):
        return f"Objeto Cor:\nNome:\t\t{self.nome}\nDia:\t\t{self.dia}\nTurno:\t\t{self.turno}\nHorario:\t{self.horario}\n"

# Procurar uma cor pelo nome, na lista de obetos cores
def buscar(nome, lista):
    for cor in lista:
        if cor.nome == nome:
            return cor
    return None

# Definição das cores disponíveis
colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "gray", "cyan",
    "magenta", "lime", "teal", "lavender", "maroon", "navy", "olive", "silver", "aqua", "gold",
    "indigo", "violet", "turquoise", "tan", "salmon", "coral", "peru", "orchid", "plum", "khaki",
    "skyblue", "crimson", "chartreuse", "sandybrown", "thistle", "darkgreen", "steelblue", "indianred",
    "sienna", "mediumslateblue", "darkkhaki", "lightcoral", "mediumorchid", "mediumturquoise", "cornflowerblue",
    "darkorange", "limegreen"
]
available_colors = colors[:]

# Lista de objetos Cor
cores = [] 

# Variáveis disponíveis para o objeto cor
dias = [2, 3, 4, 5, 6]
turnos = ['M', 'T', 'N']
horarios = [1, 2, 3]

# Gerar objetos Cor para cada combinação
for turno in turnos:
    for dia in dias:
        for horario in horarios:
            cor = available_colors.pop(0)  # Remove a primeira cor da lista
            objeto_cor = Cor(cor, dia, turno, horario)
            cores.append(objeto_cor)

# Imprimir as cores
# for cor in cores:
#     print(cor)
