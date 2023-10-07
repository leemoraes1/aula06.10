class estudante:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
   
    def texto(self):
        print(f"o nome do estudante é {self.nome} e a idade é {self.idade}")

estudante1 = estudante("maria", "98")

print(estudante1.nome)
print(estudante1.idade) 

estudante1.texto()
