"""
Elabore uma função e_par, que recebe um número e retorna True ou False conforme o número seja par ou não.
"""

def e_par(num):
    print("é par" if num % 2 == 0 else "é ímpar")

e_par(3)

"""
Implemente um programa que receba dois números e retorne o maior deles.
"""

def bigger_num(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Igual"
    
print(bigger_num(2, 2))

def Positive_or_negative(num):
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    elif num == 0:
        return "Zero"
    else:
        return "NaN"

print(Positive_or_negative(4))