class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo =  titulo
        self.autor = autor
        self.ano = ano 
        
    def descricao(self):
        print(f"o nome do filme é {self.titulo} o autor é  {self.autor} foi lançado em {self.ano}")
    
livro1 = Livro("velosos e furiosos","Rob Cohen","2000")

livro1.descricao()