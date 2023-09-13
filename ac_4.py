"""
Elabore uma função e_primo(num) que retorna se um número 
num é primo ou não. Caso num não seja primo, liste todos 
os números pelos quais num é divisível.
"""

def e_primo(num):
    divisivel = 0
    for i in range(2,num):
        if num % i == 0:
            print(f"Divisível por: {i}")
            divisivel += 1
    
    if (divisivel == 0):
        print("É primo")
    else:
        print("Não é primo")

e_primo(11)

"""
Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento. 
O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, e o percentual 
de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo. 
O relatório com as opções de pagamento deve conter os seguintes dados: valor dos juros, 
valor total da dívida (incluindo juros), quantidade de parcelas e valor da parcela. 
A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. 
No momento, não é necessário formatar os valores.

 Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
 1                       0
 3                       10
 6                       15
 9                       20
 12                      25

 Valor dos Juros Valor Total     Quantidade de Parcelas  Valor da Parcela
 0               R$ 1.000,00     1                       R$  1.000,00
 R$ 100,00       R$ 1.100,00     3                       R$    366,00
 R$ 150,00       R$ 1.150,00     6          
"""

def divida():
    divida = int(input("Dívida: "))

    for i in range(0, 12 + 1, 3):
        if i == 0:
            juros = 0
        elif i == 3:
            juros = 0.1
        elif i == 6:
            juros = 0.15
        elif i == 9:
            juros = 0.2
        elif i == 12:
            juros = 0.25

        total = divida + (divida * juros)

        if i > 0:
            print(f"Parcelas: {i}; Juros: {juros * 100}%; Total: {total}$; Valor da parcela: {(total / i):.2f}$")
        elif i == 0:
            print(f"Parcelas: {i}; Juros: {juros * 100}%; Total: {total}$; Valor da parcela: {total:.2f}$")

divida()

"""
Faça um programa que leia uma quantidade indeterminada de números positivos e 
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
"""

def exercicio_3():
    grp_1 = 0
    grp_2 = 0
    grp_3 = 0
    grp_4 = 0

    while True:
        num = int(input("Insira um número positivo: "))

        if num < 0:
            print("Número negativo")
            break
        elif num <= 25:
            grp_1 += 1
            print(f" 0-25: {grp_1} \n 26-50: {grp_2} \n 51-75: {grp_3} \n 76-100: {grp_4}")
        elif num <= 50:
            grp_2 += 1
            print(f" 0-25: {grp_1} \n 26-50: {grp_2} \n 51-75: {grp_3} \n 76-100: {grp_4}")
        elif num <= 75:
            grp_3 += 1
            print(f" 0-25: {grp_1} \n 26-50: {grp_2} \n 51-75: {grp_3} \n 76-100: {grp_4}")
        elif num <= 100:
            grp_4 += 1
            print(f" 0-25: {grp_1} \n 26-50: {grp_2} \n 51-75: {grp_3} \n 76-100: {grp_4}")
    
exercicio_3()