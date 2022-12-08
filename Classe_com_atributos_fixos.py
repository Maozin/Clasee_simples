# O método contrutor __init__ constroi os atributos para uma instancia.
# O Self ou tambem chamado de namespace são os valores atribuidos e exclusivos para cada atributo de um obj.


# Método é uma ação que podemos configurar dentro de uma classe. Pode atuar com o obj ou não.

class Livro():
    def __init__(self):
        self.titulo = "Curso de Python"
        self.autor = "Guido Van Rossum"

# Uma função dentro de uma class vira uma Função.

    def imprime(self):
        print("Este livro é %s e o autor %s"%(self.titulo,self.autor))


# Instanciar os obj 

livro1 = Livro()
print(livro1)

# Listar os atributos do obj 

print(livro1.titulo)
print(livro1.autor)

livro1.imprime()

livro2 = Livro()
livro2.imprime

