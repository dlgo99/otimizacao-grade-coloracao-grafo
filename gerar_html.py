import csv
from collections import defaultdict

def read_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def group_by_unit_period(data):
    units = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for row in data:
        unit = row['unidade']
        period = int(row['periodo'])
        turno = row['turno']
        if turno == 'M':
            turno = 'Manhã'
        elif turno == 'T':
            turno = 'Tarde'
        elif turno == 'N':
            turno = 'Noite'
        units[unit][period][turno].append(row)
    return units

def generate_html_table(data):
    units = group_by_unit_period(data)
    html = '<html>\n<head>\n<title>Tabela de Aulas</title>\n<style>\n'
    html += 'table { border-collapse: collapse; width: 100%; }\n'
    html += 'th, td { border: 1px solid black; padding: 8px; text-align: left; }\n'
    html += '.hidden { display: none; }\n'
    html += '.clickable { cursor: pointer; }\n'  # Adiciona o estilo de cursor para elementos clicáveis
    html += '</style>\n</head>\n<body>\n'
    html += '<script>\n'
    html += 'function toggleVisibility(elementId) {\n'
    html += '    var element = document.getElementById(elementId);\n'
    html += '    element.classList.toggle("hidden");\n'
    html += '}\n'
    html += '</script>\n'
    
    sorted_units = sorted(units.keys())
    
    for unit in sorted_units:
        html += f'<h2 class="clickable" onclick="toggleVisibility(\'unit_{unit}\')">{unit}</h2>\n'
        html += f'<div id="unit_{unit}" class="hidden">\n'
        
        periods = units[unit]
        sorted_periods = sorted(periods.keys())
        
        for period in sorted_periods:
            html += f'<h3 class="clickable" onclick="toggleVisibility(\'period_{unit}_{period}\')">{period}º período</h3>\n'
            html += f'<div id="period_{unit}_{period}" class="hidden">\n'
            
            turnos = periods[period]
            sorted_turnos = sorted(turnos.keys(), key=lambda x: ("Manhã", "Tarde", "Noite").index(x))
            
            for turno in sorted_turnos:
                html += f'<h4 class="clickable" onclick="toggleVisibility(\'turno_{unit}_{period}_{turno}\')">{turno}</h4>\n'
                html += f'<div id="turno_{unit}_{period}_{turno}" class="hidden">\n'
                html += '<table>\n'
                html += '<tr>\n<th></th>\n'
                html += '<th>Segunda-feira</th>\n'
                html += '<th>Terça-feira</th>\n'
                html += '<th>Quarta-feira</th>\n'
                html += '<th>Quinta-feira</th>\n'
                html += '<th>Sexta-feira</th>\n'
                html += '</tr>\n'
                
                table = [['' for _ in range(5)] for _ in range(3)]
                for row in turnos[turno]:
                    dia_semana = int(row['dia']) - 2  # Ajuste para indexar corretamente a coluna
                    horario = int(row['horario'])
                    table[horario - 1][dia_semana] = f'{row["disciplina"]} ({row["professor"]})'
                
                for horario, row in enumerate(table, start=1):
                    html += f'<tr>\n<td>{horario}º horário</td>\n'
                    for cell in row:
                        html += f'<td>{cell}</td>\n'
                    html += '</tr>\n'
                
                html += '</table>\n'
                html += '</div>\n'
            
            html += '</div>\n'
        
        html += '</div>\n'
    
    html += '</body>\n</html>'
    return html

def save_html_file(html, file_name):
    with open(file_name, 'w') as file:
        file.write(html)

csv_file = 'aulas.csv'
data = read_csv(csv_file)
html = generate_html_table(data)
save_html_file(html, 'view.html')
