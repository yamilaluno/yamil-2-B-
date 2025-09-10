numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))
operacao = input("Digite a operação matematica: ")

if operacao == "soma" or operacao == "adicao":
    print(numero_um + numero_dois)
elif operacao == "multiplicacao" or operacao == "multiplicar":
    print(numero_um * numero_dois)
elif operacao == "dividir" or operacao == "divisao":
    print(numero_um / numero_dois)
elif operacao == "diminuir" or operacao == "subtracao":
    print(numero_um - numero_dois)

print("Fim da calculadora")
