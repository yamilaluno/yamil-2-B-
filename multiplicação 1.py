frutas = []

while True:
    texto = input("Digite uma fruta (ou 'sair' para encerrar): ")
    if texto.lower() == "sair":
        break
    frutas.append(texto)

print("Frutas digitadas: ", frutas)
