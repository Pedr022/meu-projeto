import flet as ft

def main(page: ft.Page):

    def clicar(e):
        print('clicou')

        page.remove(botao)
        page.add(pagina_inicial, coluna)
        page.update()


    def confirmar(e):
        print('clicou para confirmar')

        if caixa_usuario.value == '' or caixa_senha.value == '':
            coluna.controls.append(msg_info_falt)
            page.update()
            exit

        else:
            if msg_info_falt in coluna.controls:
                coluna.controls.remove(msg_info_falt)
                page.remove(pagina_inicial, coluna)
                page.add(pagina_acesso, coluna2)
                page.update()
                exit
            
            else:
                page.remove(pagina_inicial, coluna)
                page.add(pagina_acesso, coluna2)
                page.update()
                exit

            exit
    
    msg_info_falt = ft.Text('preencha todas as caixas')
    coluna = ft.Column()

    def acessar(e):
        print('clicou para acessar a conta')

        if usuario.value != caixa_usuario.value or senha.value != caixa_senha.value:
            coluna2.controls.append(msg_info_incorr)
            page.update()
            exit

        else:
            if msg_info_incorr in coluna2.controls:
                coluna2.controls.remove(msg_info_incorr)
                page.remove(pagina_acesso)
                page.add(ft.Text('bem vindo!'))
                page.update()
                exit

            else:
                page.remove(pagina_acesso)
                page.add(ft.Text('bem vindo!'))
                page.update()
                exit

            exit

    msg_info_incorr = ft.Text('Usuário ou senha incorretos')
    coluna2 = ft.Column()
    
    usuario = ft.TextField(label='nome de usuário', width=300)
    senha = ft.TextField(label='senha', width=300)
    botao_entrar = ft.ElevatedButton('entrar', on_click=acessar)
    pagina_acesso = ft.Column([usuario, senha, botao_entrar])

    
    caixa_usuario = ft.TextField(label='usuário', width=300, on_submit=confirmar)
    caixa_senha = ft.TextField(label='senha', width=300, on_submit=confirmar)
    caixa_conf_senha = ft.TextField(label='confirmar', width=300, on_submit=confirmar)
    botao_confirmar = ft.ElevatedButton('confirmar', width=150, on_click=confirmar)
    pagina_inicial = ft.Column([caixa_usuario, caixa_senha, caixa_conf_senha, botao_confirmar])


    botao = ft.ElevatedButton('clique aqui!!!', on_click=clicar)
    page.add(botao)

ft.app(target=main)