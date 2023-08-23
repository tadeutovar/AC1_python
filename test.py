"""
Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0.
O programa deve pedir os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
Considere que as raízes são reais. Exemplo: a = 1, b = -6, c = 8 dá como raízes 4 e 2.
"""

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

delta = ((b * b) - (4 * a * c)) ** (1/2)
result1 = (- b + delta) / (2 * a)
result2 = (- b - delta) / (2 * a)

print(result1)
print(result2)

"""
Elabore um programa que leia uma variável inteira ano. 
Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. 
Um ano é bissexto se ele é múltiplo de quatro. 
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. 
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
"""

year = int(input("ano: "))

result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(result)