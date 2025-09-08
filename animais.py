# def cria funções (ou métodos dentro da classe)
class Animal:
    nome = ""
    especie = ""
    idade = 0

# def comer
    def comer(self):
        print(self.especie, self.nome, "está comendo ")

# def dormir
    def dormir(self):
        print(self.especie, self.nome, "está dormindo ")

# def andar
    def andar(self):
        print(self.especie, self.nome, "está andando ")


# Criando os animais
a1 = Animal()
a1.nome = "Rex"
a1.especie = "Cachorro"
a1.idade = 3

a2 = Animal()
a2.nome = "Mel"
a2.especie = "Gato"
a2.idade = 2

a3 = Animal()
a3.nome = "Robson"
a3.especie = "Cavalo"
a3.idade = 4

a4 = Animal()
a4.nome = "Simba"
a4.especie = "Leão"
a4.idade = 3

a5 = Animal()
a5.nome = "Dumbo"
a5.especie = "Elefante"
a5.idade = 8


# Testando os métodos
print("Animal:", a1.especie, "-", a1.nome, "Idade:", a1.idade)
a1.comer()
a1.dormir()
a1.andar()

print("Animal:", a2.especie, "-", a2.nome, "Idade:", a2.idade)
a2.comer()
a2.dormir()
a2.andar()

print("Animal:", a3.especie, "-", a3.nome, "Idade:", a3.idade)
a3.comer()
a3.dormir()
a3.andar()

print("Animal:", a4.especie, "-", a4.nome, "Idade:", a4.idade)
a4.comer()
a4.dormir()
a4.andar()

print("Animal:", a5.especie, "-", a5.nome, "Idade:", a5.idade)
a5.comer()
a5.dormir()
a5.andar()
