# def cria funções (ou métodos dentro da classe)
class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""

# def buzinar
    def buzinar(self):
        print("Bi-Bi")

# def ligar
    def ligar(self):
        print("PHAM PHAM BRRRRRRRRRRRRRRRRRRRR...")

# def acelerar
    def acelerar(self):
        print("VRUUUUUUUUUUUMMMM ")

# def frear
    def frear(self):
        print("IIIIIIIIIIIIIIIIHHHHHHHHHHH ")

# def desligar
    def desligar(self):
        print("Toc... Toc... O motor foi desligado.")


# Criando o carro
c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "Nissan GT3"
c1.ano = 2006
c1.cor = "verde de Bem10"

# Testando os métodos
print("Carro: ", c1.marca, "-", c1.modelo, "Ano: ", c1.ano, "Cor: ", c1.cor)
c1.ligar()
c1.acelerar()
c1.frear()
c1.desligar()
c1.buzinar()
