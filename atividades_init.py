# Crie uma classe com atributos utilizando o metodo construtor __INIT__ e crie atributos para a mesma.
# E instanie os objetos dessa classe printando os atributos (Atributos Fixos)

class Pessoa():
    def __init__(self):
        self.nome = "Mauro Bruschi"
        self.idade = "19"
        self.peso = "80"

    def imprime(self):
        print("O nome do individuo é %s, tem %s anos e pesa %s Kg"%(self.nome, self.idade, self.peso))

Pessoa1 = Pessoa()
print(Pessoa1)

print(Pessoa1.nome)
print(Pessoa1.idade)

Pessoa1.imprime()

