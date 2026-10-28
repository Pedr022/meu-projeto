import os
import os.path


lista = []
for e in os.listdir('.'):
    if os.path.splitext(e)[1] == '.png' or os.path.splitext(e)[1] == '.jpg':
        lista.append(e)

pagina = open('pagina-teste.html', 'w', encoding='utf-8')

pagina.write('''
<DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>fds o leo</title>
</head>
<body>
''')

for i in lista:
    pagina.write(f'<img src=\"{i}\">\n')

pagina.write('''
</body>
</html>      
''')
