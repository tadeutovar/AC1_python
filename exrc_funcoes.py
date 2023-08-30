"""
João Papo-de-Pescador, homem de bem, comprou um computador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma função que leia a 
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
e na variável multa o valor da multa que João deverá pagar. Retorne o valor da multa. Assumir que a quantidade de quilos 
é sempre superior a 50.
"""

def exerc_1(peso_de_peixes):
    valor_extra = (peso_de_peixes - 50) * 4
    return(valor_extra)

"""
Faça um programa que receba dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

def exerc_2(base, expoente):
    count = 1
    result = 1
    while count <= expoente:
        result *= base
        count += 1
    return(result)

"""
Faça uma função media(), que recebe os parâmetros posicionais ap1, ap2 e ac, e 
retorne a média de avaliações, utilizando a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""

def media(ap1, ap2, ac):
    result = ((ap1 + ap2) * 0.4) + (ac * 0.2)
    return(result)

"""
Faça uma função m_para_cm() que receba um comprimento em metros e converta para centímetros.
"""

def m_para_cm(comp):
    result = comp * 100
    return(result)

"""
Faça uma função que receba o raio de um círculo, calcule e retorne sua área. Considere pi como aproximadamente igual a 3.14.
"""

def area_circulo(raio):
    result = 3.14 * (raio ** 2)
    return(result)

"""
Monte um conversor de temperatura, que recebe uma temperatura em graus Fahrenheit e devolva a temperatura em graus Celsius. 
A fórmula para conversão é C / 5 = (F - 32) / 9.
"""

def converter(temp):
    result = ((temp - 32) / 9) * 5
    return(result)

"""
Desenvolva uma função que gera um relatório na tela do usuário. Essa função calcula o contracheque de uma pessoa. 
O salário é calculado como as horas trabalhadas no mês vezes o valor por hora. O salário líquido precisa ter descontado o 
IRPF (11%), INSS (8%, que pode variar entre pessoas) e sindicato (5%). O relatório precisa ter o formato indicado abaixo:
"""

def salario(hora, valor_por_hora):
    total = hora * valor_por_hora
    irpf = total * 0.11
    inss = total * 0.08
    sindicato = total * 0.05
    liquido = total - irpf - inss - sindicato
    print(f"Salário por hora trabalhada: {valor_por_hora}")
    print(f"Número de horas trabalhadas no mês: {hora}")
    print("----------------------------------------")
    print(f"Salário bruto: {total}")
    print(f"(-) Imposto de Renda: {irpf}")
    print(f"(-) INSS: {inss}")
    print(f"(-) Sindicato: {sindicato}")
    print(f"(=) Salário Líquido: {liquido}")

print(exerc_1(57))
print(exerc_2(2, 5))
print(media(5, 7, 9))
print(m_para_cm(7))
print(area_circulo(5))
print(converter(60))
salario(20, 10.5)
