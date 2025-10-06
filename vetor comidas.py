saldaveis = ["alface", "cebola", "cenoura"]

naosaldavel = ["pizza", "frango frito", "salsicha"]

comidas = input("Digite a comida: ")

if comidas in saldaveis:
    print("Sim, é saldavel")

if comidas in naosaldavel:
    print("Não, é saldavel")
else:
    print("Não existe")