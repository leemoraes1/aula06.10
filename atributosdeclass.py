class Carro:
    pneus = 4 #atributos

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo =  modelo

carro1 = Carro("ford","fiesta")
carro2 = Carro("honda","civic")

print(carro1.pneus)
print(carro2.pneus)

print(Carro.pneus)
