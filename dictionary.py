# ===== Exercício: Dictionary =====

# Criando o dicionário com informações pessoais
pessoa = {
    "nome": "Yamil",
    "idade": 18,
    "altura": 1.75
}

# Mostrando o dicionário completo
print("Dicionário completo:", pessoa)

# Mostrando apenas o nome
print("Nome:", pessoa["nome"])

# Adicionando uma nova chave 'peso'
pessoa["peso"] = 70
print("\nDicionário após adicionar o peso:", pessoa)

# Removendo a chave 'idade'
del pessoa["idade"]
print("Dicionário após remover a idade:", pessoa)

# Percorrendo o dicionário e imprimindo todas as chaves e valores
print("\nChaves e valores do dicionário:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
