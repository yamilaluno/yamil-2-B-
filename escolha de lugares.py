cinema = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

linha = int(input("Digite a linha do acesso (0 a 2): "))
coluna = int(input('Digite a coluna do assento (0 a 2): '))
nome = input("Digite seu nome: ")

cinema[linha][coluna] = nome
print("Novo disposição na sala: ", cinema)
