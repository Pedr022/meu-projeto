import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    campo_alerta = ft.Text('', color='red')

    def entrar(e):
        for element in [caixa_nome, caixa_email, caixa_senha]:
            if element.value == '':
                campo_alerta.value = ''
                campo_alerta.value = 'É obrigatório preencher todos os campos'
                page.update()
                break
            
        else:
            if '@' not in caixa_email.value:
                campo_alerta.value = ''
                campo_alerta.value = 'Email incorreto!'
                page.update()

            elif len(caixa_senha.value) < 4:
                campo_alerta.value = ''
                campo_alerta.value = 'Senha precisa ter mais de 4 caracteres!'
                page.update()
            
            else:
                campo_alerta.value = ''
                page.remove(titulo, coluna_entrada)
                page.add(ft.Text('Vai se foder administração!!!!!!!!!'))
                page.update()

    titulo = ft.Text('Entrar com o usuário')    
    caixa_nome = ft.TextField(label='Nome...')
    caixa_email = ft.TextField(label='Email...')
    caixa_senha = ft.TextField(label='Senha...')
    botao_entrar = ft.ElevatedButton('Entrar', width=150, height=35, on_click=entrar)
    coluna_entrada = ft.Column([caixa_nome, caixa_email, caixa_senha, botao_entrar, campo_alerta])

    page.add(titulo, coluna_entrada)

ft.app(target=main) #view=ft.AppView.WEB_BROWSER)