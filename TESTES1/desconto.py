#interface de USUÁRIO

print("-" * 50)
titulo = "CRIAÇÃO DE USUÁRIO"
print(f"{titulo:=^50}")
print("-" * 50)

import time
import string

verificar = True

while verificar:

        nome = input("crie um nome de usuário:")

        if any(char in string.punctuation for char in nome) == True:

                nome_limpo = nome.translate(str.maketrans('', '', string.punctuation))

                if nome_limpo.isspace() == True:
                        print ("escreva algo!")

                elif nome_limpo.isnumeric() == True:
                    print ("nome precisa conter pelomenos uma letra!")
                
                elif nome_limpo.isalpha() == True:
                        verificar = False

                elif nome_limpo.isalnum() == True:
                        verificar = False

                else:
                        print ("escolha um nome válido!")

        else:

                if nome.isspace() == True:
                        print ("escreva algo!")

                elif nome.isnumeric() == True:
                        print ("nome precisa conter pelomenos uma letra!")

                elif nome.isalpha() == True:
                        verificar = False

                elif nome.isalnum() == True:
                        verificar = False

                else:
                        print ("escolha um nome válido!")

nome1 = nome


verif_senha = True

while verif_senha:

        senha = input("crie uma senha:")

        if sum(1 for char in senha if char.isalnum()) >= 4:

                if any(char in string.ascii_uppercase for char in senha) == True and any(char in string.ascii_lowercase for char in senha) == True and any(char in string.digits for char in senha) == True:
                        verif_senha = False

                else:
                        print ("a senha deve conter obrigatoriamente:")
                        print ("uma letra maiúscula")
                        print ("uma letra minúscula")
                        print ("um número")


        else:
                print ("a senha deve conter pelomenos 4 digitos!")

senha1 = senha


conf_senha = True
while conf_senha:

        psswd = input("confirme sua senha:")

        if psswd == senha1:
                conf_senha = False

        else:
                print ("senha não corresponde com a primeira!")

print ("carregando...%")

time.sleep(2)

verif_acesso = True

while verif_acesso:

        user = input("usuário:")
        senha2 = input("senha:")

        if user == nome1 and senha2 == senha1:
                verif_acesso = False

        else:
                print ("usuário ou senha incorretos!")

print ("carregando...%")

time.sleep(3)
print ("bem vindo", nome1,"!")