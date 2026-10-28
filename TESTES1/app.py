import flet as ft
import string

def main(page: ft.Page):
    page.title = 'criar um usuario'

    titulo = ft.Text('Bem Vindo!')

    #1
    #entrar na pagina para criar um usuario
    def começar(e):
        page.remove(titulo, botao)
        page.add(lista1)
        page.update()

    #2
    #confirmar informações
    def confirmar(e):

        if any(char in string.punctuation for char in caixa_usuario.value) == True:

            if caixa_usuario.value.isspace() == True:
                caixa_usuario.value = ''

                if msg_erro.value != '':
                    msg_erro.value = ''
                    msg_erro.value = 'Escolha um nome válido'

                else:
                    msg_erro.value = 'Escolha um nome válido'

            elif caixa_usuario.value.isnumeric() == True:
                caixa_usuario.value = ''

                if msg_erro.value != '':
                    msg_erro.value = ''
                    msg_erro.value = 'O nome deve conter pelomenos uma letra'

                else:
                    msg_erro.value = 'O nome deve conter pelomenos uma letra'
            
            elif caixa_usuario.value.isalpha() == True:
                page.remove(lista1)
                page.update()

            elif caixa_usuario.value.isalnum() == True:
                page.remove(lista1)
                page.update()

            else:
                caixa_usuario.value = ''

                if msg_erro.value != '':
                    msg_erro.value = ''
                    msg_erro.value = 'nome escolhido é invalido'

                else:
                    msg_erro.value = 'nome escolhido é invalido'

    #1
    titulo2 = ft.Text('Crie seu usuário')
    caixa_usuario = ft.TextField(label='Usuário...', width=300)
    caixa_senha = ft.TextField(label='Senha...', width=300)
    conf_senha = ft.TextField(label='Confirmar senha...', width=300)
    botao_criar_usr = ft.ElevatedButton('Criar', width=200, on_click=confirmar)
    msg_erro = ft.Text('')
    lista1 = ft.Column([titulo2, caixa_usuario, caixa_senha, conf_senha, botao_criar_usr, msg_erro])

    botao = ft.ElevatedButton('Clique aqui', on_click=começar)

    page.add(titulo, botao)

ft.app(target=main)