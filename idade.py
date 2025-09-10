class Aluno:
    nome = ""
    idade = 0

    def mostrarSituacao(self):
        if self.idade >= 18:
            print(self.nome, "é maior de idade")
        else:
            print(self.nome, "é menor de idade")


# Criando cada aluno com idade fixa
a1 = Aluno()
a1.nome = "Diego Alves"
a1.idade = 18
a1.mostrarSituacao()

a2 = Aluno()
a2.nome = "Matheus Morais"
a2.idade = 17
a2.mostrarSituacao()

a3 = Aluno()
a3.nome = "Matheus Pizzo"
a3.idade = 17
a3.mostrarSituacao()

a4 = Aluno()
a4.nome = "Phelipe Eduardo"
a4.idade = 17
a4.mostrarSituacao()

a5 = Aluno()
a5.nome = "Jonathan dos Santos"
a5.idade = 16
a5.mostrarSituacao()

a6 = Aluno()
a6.nome = "Yamil Josué"
a6.idade = 16
a6.mostrarSituacao()

a7 = Aluno()
a7.nome = "Rodrigo Raimundo"
a7.idade = 17
a7.mostrarSituacao()

a8 = Aluno()
a8.nome = "Gabriel Oliveira"
a8.idade = 17
a8.mostrarSituacao()

a9 = Aluno()
a9.nome = "Luan Barbosa"
a9.idade = 17
a9.mostrarSituacao()

a10 = Aluno()
a10.nome = "Lucca Cruz"
a10.idade = 17
a10.mostrarSituacao()
