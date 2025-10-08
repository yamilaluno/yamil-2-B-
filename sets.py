import random

# ===== Exercício 1: União =====
pares = {2, 4, 6, 8, 10}
impares = {1, 3, 5, 7, 9}
uniao = pares.union(impares)
print("União dos conjuntos (pares e ímpares):", uniao)


# ===== Exercício 2: Interseção =====
# Criando duas listas com 5 números aleatórios cada
lista1 = [random.randint(1, 10) for _ in range(5)]
lista2 = [random.randint(1, 10) for _ in range(5)]

print("\nLista 1:", lista1)
print("Lista 2:", lista2)

# Convertendo listas em conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Descobrindo interseção
intersecao = conjunto1.intersection(conjunto2)

if intersecao:
    print("Valores em comum entre os conjuntos:", intersecao)
else:
    print("Não existem valores em comum entre os conjuntos.")
