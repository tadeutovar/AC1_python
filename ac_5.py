"""
Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. 
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def exercicio_1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="   ")
        print()

numero = int(input("Número: "))
exercicio_1(numero)

"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def contar_digitos(num):
    if num < 0:
        num_len = len(str(num)) - 1
    else:
        num_len = len(str(num))
    return num_len

num = int(input("Número: "))
print(f"O número possui {contar_digitos(num)} dígitos")

"""
Faça um programa que solicite ao usuário 2 números inteiros. 
A seguir, calcule e mostre a divisão do primeiro pelo segundo. 
Para resolver este problema, utilize a instrução try-except, 
particularmente analizando as exceções do tipo ValueError e 
ZeroDivisionError. Inclua uma instrução finally para exibir o 
resultado da operação.
"""

def exercicio_3():
    try:
        num1 = int(input("Primeiro número: "))
        num2 = int(input("Segundo número: "))
        resultado = num1 / num2

    except ValueError:
        print("Insira valores válidos.")
        return

    except ZeroDivisionError:
        print("Divisão por zero não pode ser realizada.")
        return

    finally:
        print(resultado)

exercicio_3()

