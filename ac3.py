"""
Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram 
para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário 
de um colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. 
Após o aumento ser realizado, informe na tela:

O salário antes do reajuste;
O percentual de aumento aplicado;
O valor do aumento;
O novo salário, após o aumento.
"""

def exercicio_1(salario):
    if salario <= 280:
        porcentagem = 20
    elif salario <= 700:
        porcentagem = 15
    elif salario <= 1500:
        porcentagem = 10
    else:
        porcentagem = 5

    novo_salario = (salario * porcentagem) / 100

    print(f"{salario}")
    print(f"{porcentagem}%")
    print(f"{novo_salario}")
    print(f"{salario + novo_salario}")

exercicio_1(1000)

"""
Implementa uma função que receba um número e exiba o dia correspondente da semana 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

def exercicio_2(dia):
    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3:
            print("Terça-Feira")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case 6:
            print("Sexta-Feira")
        case 7:
            print("Sábado")
        case _:
            print("Valor inválido")

exercicio_2(9)

"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c. 
O programa deverá receber os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não 
deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.
"""

def exercicio_3(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    result_1 = (-b + (delta ** 0.5)) / (2 * a)
    result_2 = (-b - (delta ** 0.5)) / (2 * a)

    if a == 0:
        print("não é de segundo grau")
    elif delta < 0:
        print("não possui raizes reais")
    elif delta == 0:
        print(f"possui apenas uma raiz: {result_1}")
    else:
        print(f"possui duas raizes: {result_1} ; {result_2}")


exercicio_3(1, -1, 1)