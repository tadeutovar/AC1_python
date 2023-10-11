"""
O time deve desenvolver um simulador de rolagem de dados. Primeiramente, o programa deve pedir o tamanho do dado que deseja rolar, 
podendo ser qualquer valor inteiro maior que zero (3, 6, 10, etc.). O programa deve fazer os seguintes tratamentos com relação à 
informação coletada:

Se o usuário não passar um valor numérico maior que zero, repita o pedido até passar um valor válido;
Se o usuário passar uma string vazia, encerre o programa.
Em seguida, o programa deve pedir quantos dados o usuário deseja rolar. Faça as mesmas validações do pedido anterior, 
porém considere que caso o valor passado seja uma string vazia, adotar que será rolado apenas um dado.

Por último, o programa deve gerar valores aleatórios para cada dado, e imprimi-los lado a lado na tela.

Se o tamanho do dado for válido, porém o número de dados não for, continue pedindo apenas pelo número de dados.
"""
import random

while True:
    resposta = input("Forneça o tamanho do dado que será rolado (ENTER para sair): ")

    if resposta.isnumeric():
        tamanho_do_dado = int(resposta)
        if tamanho_do_dado > 0:
            break
        else:
            print("O número passado deve ser maior que zero!")
            continue
    elif resposta == "":
        break
    else:
        print("A informação passada não é válida!")
        continue

while tamanho_do_dado > 0:
    dados = input("Forneça o número de dados que serão rolados (em branco == 1): ")

    if dados.isnumeric():
        qtdd_de_dados = int(dados)
        if qtdd_de_dados > 0:
            break
        else:
            print("O número passado deve ser maior que zero!")
            continue
    elif dados == "":
        qtdd_de_dados = 1
        break
    else:
        print("A informação passada não é válida!")
        continue

for i in range(qtdd_de_dados):
    resultado = random.randint(1, tamanho_do_dado)
    print(f"Lançamento n. {i + 1}: {resultado}")

print(f"\n{qtdd_de_dados} dado(s) de {tamanho_do_dado} lados:")

for i in range(qtdd_de_dados):
    resultado = random.randint(1, tamanho_do_dado)
    print(i, end=" ")

