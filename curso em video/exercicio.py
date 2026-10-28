# Lista de Exercícios Práticos 01
# Disciplina: Programação Estruturada
# Curso: Sistemas de Informação - UNEMAT


# 1. Calcular idade
def exercicio_1():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = 2026

    idade = ano_atual - ano_nascimento

    print(f"Você tem aproximadamente {idade} anos.")


# 2. Calculadora
def exercicio_2():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    print("\nEscolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        resultado = numero1 + numero2
        print(f"Resultado: {resultado}")

    elif opcao == 2:
        resultado = numero1 - numero2
        print(f"Resultado: {resultado}")

    elif opcao == 3:
        resultado = numero1 * numero2
        print(f"Resultado: {resultado}")

    elif opcao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado: {resultado}")
        else:
            print("Não é possível dividir por zero.")

    else:
        print("Opção inválida.")


# 3. Verificar número par ou ímpar
def exercicio_3():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")


# 4. Calcular média e situação do aluno
def exercicio_4():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Aluno APROVADO.")

    elif media >= 5:
        print("Aluno em RECUPERAÇÃO.")

    else:
        print("Aluno REPROVADO.")


# 5. Tabuada
def exercicio_5():
    numero = int(input("Digite um número: "))

    print(f"\nTabuada do {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# 6. Celsius para Fahrenheit
def exercicio_6():
    celsius = float(input("Digite a temperatura em Celsius: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")


# 7. Juros simples
def exercicio_7():
    valor_principal = float(input("Digite o valor principal: R$ "))
    taxa = float(input("Digite a taxa de juros anual (%): "))
    tempo = float(input("Digite o período em anos: "))

    # Conversão da taxa percentual para decimal
    taxa_decimal = taxa / 100

    juros = valor_principal * taxa_decimal * tempo
    valor_total = valor_principal + juros

    print(f"Juros: R$ {juros:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")


# 8. Calcular IMC
def exercicio_8():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = peso / (altura * altura)

    print(f"Seu IMC é: {imc:.2f}")


# Programa principal
while True:
    print("\n===================================")
    print("   LISTA DE EXERCÍCIOS - PYTHON")
    print("===================================")
    print("1 - Calcular idade")
    print("2 - Calculadora")
    print("3 - Par ou ímpar")
    print("4 - Média do aluno")
    print("5 - Tabuada")
    print("6 - Celsius para Fahrenheit")
    print("7 - Juros simples")
    print("8 - IMC")
    print("0 - Sair")
    print("===================================")
    opcao = int(input("Escolha um exercício: "))
    if opcao == 1:
        exercicio_1()
    elif opcao == 2:
        exercicio_2()
    elif opcao == 3:
        exercicio_3()
    elif opcao == 4:
        exercicio_4()
        
    elif opcao == 5:
        exercicio_5()
    elif opcao == 6:
        exercicio_6()
    elif opcao == 7:
        exercicio_7()
    elif opcao == 8:
        exercicio_8()
    elif opcao == 0:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
    input("\nPressione ENTER para continuar...")