class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel
    def pode_abrir(self):
        if self.energia_disponivel >= self.energia_necessaria:
            print("Há energia suficiente!")
        else:
            print("Não há energia suficiente! ")
    def calcular_falta_energia(self):
        if self.energia_necessaria >= self.energia_disponivel:
            print(f"Falta {self.energia_necessaria - self.energia_disponivel}")
        else:
            print(0)    
    def classificar_estabilidade(self):
        if self.energia_disponivel >= self.energia_necessaria:
            print("Energia suficiente!")
        elif self.energia_disponivel >= 20:
            print("Portal estável!")
        elif self.energia_disponivel <= 20:
            print("Portal instável!")    
    def exibir_resumo(self):
        print(f"O nome é {self.nome}, seu destino será {self.destino}, sua energia disponível: {self.energia_disponivel}, energia necessária: {self.energia_necessaria}")
        self.classificar_estabilidade() 


p1 = PortalDimensional("desenho animado", "MLP", 300, 200)
p1.pode_abrir()
p1.calcular_falta_energia()
p1.classificar_estabilidade()
p1.exibir_resumo()
