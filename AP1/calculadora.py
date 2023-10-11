resultado = 0.0

while True:
    print(resultado)

    valor_inicio = float(input("Informe um número, ou aperte ENTER para sair:"))
    if valor_inicio == "":
        break
    else:
        resultado = valor_inicio
        print(resultado)

    while True:
        operacao = input("Operação (+, -, *, /), X para zerar ou ENTER para sair:")
        
        if operacao == "":
            break
        elif operacao == "X":
            resultado = 0.0
            print(resultado)
            continue
        elif operacao == "+":
            valor_secundario = float(input("Informe um número, ou aperte ENTER para sair: "))
            resultado += valor_secundario
            print(resultado)
            continue
        elif operacao == "-":
            valor_secundario = float(input("Informe um número, ou aperte ENTER para sair: "))
            resultado -= valor_secundario
            print(resultado)
            continue
        elif operacao == "*":
            valor_secundario = float(input("Informe um número, ou aperte ENTER para sair: "))
            resultado *= valor_secundario
            print(resultado)
            continue
        elif operacao == "/":
            valor_secundario = float(input("Informe um número, ou aperte ENTER para sair: "))
            resultado /= valor_secundario
            print(resultado)
            continue
        