class Aluno:
    nome = ""
    nota = 0

    def mostrarSituacao(self):
        if self.nota >= 5:
            print(self.nome, "foi aprovado")
        else:
            print(self.nome, "foi reprovado")


a1 = Aluno()
a1.nome = "Diego"
a1.nota = 3
a1.mostrarSituacao()

a2 = Aluno()
a2.nome = "Matheus Morais"
a2.nota = 7
a2.mostrarSituacao()

a3 = Aluno()
a3.nome = "Matheus Pizzo"
a3.nota = 7
a3.mostrarSituacao()

a4 = Aluno()
a4.nome = "Rodrigo Raimundo"
a4.nota = 6
a4.mostrarSituacao()

a5 = Aluno()
a5.nome = "Luan Barbosa"
a5.nota = 4
a5.mostrarSituacao()

a6 = Aluno()
a6.nome = "Gabriel Oliveira"
a6.nota = 5
a6.mostrarSituacao()

a7 = Aluno()
a7.nome = "Phelipe Eduardo"
a7.nota = 8
a7.mostrarSituacao()

a8 = Aluno()
a8.nome = "Jonathan dos Santos"
a8.nota = 6
a8.mostrarSituacao()
