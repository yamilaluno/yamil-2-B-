# Entrada das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Processamento da média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída da média
print("Sua média é", media)

# Verificação de aprovação ou reprovação
if media >= 5:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")
