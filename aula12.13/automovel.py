class Automovel ():
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