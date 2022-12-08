# Iremos declarar uma variavel nos atributos do construtor da classe 

class Livro():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def imprime(self):
        print("Esse livro é %s e o autor %s"%(self.titulo,self.autor))

# Instanciando os obj

livro1 = Livro("Titulo do livro 1","Autor do livro 1") # Este possui um self 
livro2 = Livro('Titulo do livro 2',"Autor do livro 2") # Este possui outro self de atributos diferente 


print(livro1.titulo)

print(livro2.autor)

livro1.imprime()
livro2.imprime()
