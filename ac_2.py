"""
1 -
Monte uma função que recebe um salário por hora e o 
número de horas trabalhadas no mês, e retorne o salário a ser recebido.
"""

def exercicio_1(salario, hora):
    print(salario * hora)


"""
2 -
Elabore uma função que receba três números e exiba na tela: 
(1) o produto do dobro do primeiro com metade do segundo; (2) a 
soma do triplo do primeiro com o terceiro; e (3) o terceiro elevado ao cubo.
"""

def exercicio_2(a, b, c):
    eq_1 = (2 * a) * (b / 2)
    eq_2 = (3 * a) + c
    eq_3 = (c ** 3)
    print(eq_1, eq_2, eq_3)


"""
3 -
Elabore uma função com as mesmas regras do exercício anterior, 
porém retornando os três resultados, ao invés de exibi-los na tela.
"""

def exercicio_3(a, b, c):
    eq_1 = (2 * a) * (b / 2)
    eq_2 = (3 * a) + c
    eq_3 = (c ** 3)
    return(eq_1, eq_2, eq_3)


"""
4 -
Elabore uma função que receba uma variável inteira ano. 
Em seguida, retorne o resultado da expressão lógica que indica se 
um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. 
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. 
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
"""

def exercicio_4(ano):
    return(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)


# Testes: 

exercicio_1(16, 8)
exercicio_2(3, 5, 7)
print(exercicio_3(2, 4, 6))
print(exercicio_4(2020))
