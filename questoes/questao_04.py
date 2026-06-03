class MochilaDeMissao:
    def __init__(self, agente, capacidade_maxima):
        self.agente = agente
        self.equipamentos = []
        self.capacidade_maxima = capacidade_maxima
    def adicionar_equipamento(self, equipamento):
        if len(equipamento) > 0:
            self.equipamentos.append(equipamento)
        elif len(self.equipamentos) > self.capacidade_maxima:
            print("Espaço Indisponível!")
    def listar_equipamentos(self):
        for i in self.equipamentos:
            print(i)
    def contar_equipamentos(self):
        print(len(self.equipamentos))
    def verificar_espaco(self):
        if self.capacidade_maxima > len(self.equipamentos):
            print("Ainda há espaço.") 
        elif self.capacidade_maxima == len(self.equipamentos):
            print("Mochila cheia!")
        elif self.capacidade_maxima < len(self.quipamentos):   
            print("Não espaço!") 
    def exibir_relatorio(self):
       print(f"O nome é {self.agente}, a capacidade máxima é {self.capacidade_maxima}")
       self.contar_equipamentos()
       self.verificar_espaco()

m1 = MochilaDeMissao("Carol", 5)
m1.adicionar_equipamento("Jornal")
m1.adicionar_equipamento("Luvas")
m1.listar_equipamentos()
m1.contar_equipamentos()
m1.verificar_espaco()
m1.exibir_relatorio()
