from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str ):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos= []
        
        # Criar todos os atributos, incluindo as listas
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo 

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora:Editora):
        self.__editora = editora
    @property
    def autores(self):
         return self.__autores
    @property
    def capitulos(self):
         return self.__capitulos
    
    def incluir_autor(self, autor: Autor):
        if (isinstance(autor, Autor)) and (autor not in self.__autores):
            self.__autores.append(autor)

        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!

    def excluir_autor(self, autor: Autor):
        if (isinstance(autor, Autor)) and (autor in self.__autores):
            self.__autores.remove(autor)


    def incluir_capitulo(self, numero: int, titulo: str):
        if self.find_capitulo_by_titulo(titulo) == None:
            self.__capitulos.append(Capitulo(numero,titulo))

        #... Nao permitir insercao de Capitulos duplicados!

    def excluir_capitulo(self, titulo: str):
       cap =  self.find_capitulo_by_titulo(titulo)
       if cap != None:
            self.__capitulos.remove(cap)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
             if capitulo.titulo == titulo:
                return capitulo
        return None
