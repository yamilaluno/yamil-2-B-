# 1️⃣ Tupla com os dias da semana
dias_semana = ("Segunda", "Terça", "Quarta", "Quinta",
               "Sexta", "Sábado", "Domingo")

# Imprime a tupla completa
print("Tupla completa:", dias_semana)

# Mostra apenas o primeiro e o último dia
print("Primeiro dia da semana:", dias_semana[0])
print("Último dia da semana:", dias_semana[-1])


# 2️⃣ Tupla com 6 números inteiros pares
numeros_pares = (2, 4, 6, 8, 10, 12)

# Mostra o maior, o menor e a soma
print("\nTupla de números pares:", numeros_pares)
print("Maior número:", max(numeros_pares))
print("Menor número:", min(numeros_pares))
print("Soma dos números:", sum(numeros_pares))


# 3️⃣ Tupla com 4 cantores
cantores = ("Luccas Lucco", "Luan Santana", "Mariana Meidonsa", "Ana Catela")

# Converte a tupla em lista
lista_cantores = list(cantores)

# Adiciona um novo cantor
lista_cantores.append("Gustavo Lima")

print("\nLista de cantores atualizada:", lista_cantores)
