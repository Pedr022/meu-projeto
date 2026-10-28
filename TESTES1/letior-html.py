arquivo = open('arquivo.html', 'w', encoding='utf-8')

arquivo.write('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">     
    <title>site legal</title>
    <style>
              img{
              border-radius: 100px;
              height: 200px;
              width: 200px;
              }

              h1{
              color: yellow;
              height: 100px;
              }

              body{
              display: flex;
              justify-content: center;
              background-color: gray;
              }
    </style>
</head>
<body>
    <div>
        <h1>EU TE AMO MARISANDRA</h1>
        <div>
            <img src="Captura de tela 2026-07-22 221609.jpg">
        </div>
    </div>
</body>
</html>
''')

arquivo.close()