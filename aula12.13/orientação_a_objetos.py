# class Automovel:
#             def __init__ (self, placa='XYZ=4925'):
#                 self.placa = placa
#             def get_placa(self):
#                 print(f'estou dirigindo a {velocidade} Km/h')
# carro = Automovel ()
# print (carro.get_placa())
# carro.dirigir(220)


class Automovel:
    def __init__ (self, placa, cor):
        self.placa = placa
        self.cor = cor
    def get_placa (self):
        return self.placa
    def dirigir (self, velocidade):
        print (f'Estou dirigindo a {velocidade} Km/h')
    def get_cor(self):
        return self.cor
    def set_cor (self, nova_cor):
        self.cor = nova_cor