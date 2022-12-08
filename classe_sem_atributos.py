# Iremos riar uma classe sem atributo apenas para entendermos a semantica de funcionamento 
# Toda classe por convenção declaramos com a primeira letra Maiuscula

class Livro():
    pass


# Instanciar um objeto (Criar um objeto aprtir de uma classe)

livro1 = Livro
print(livro1)

print(type(livro1))