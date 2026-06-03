class RoboColetor:
    def __init__(self, nome, capacidade_maxima):
        self.nome= nome
        self.amostras= []
        self.capacidade_maxima= capacidade_maxima

    def adicionar_amostra(self, amostra):
        if amostra != "" and self.capacidade_maxima > len(self.amostras):
            self.amostras.append(amostra)
        else:
            print("Espaço lotado e/ou amostra vazia") 
        
    def listar_amostras(self):
        for i in self.amostras:
            print(i)
    
    def contar_amostras(self):
        quant= len(self.amostras)
        print(quant)
    
    def verificar_armazenamento(self):
        if len(self.amostras)>= self.capacidade_maxima:
            print("Está cheio")
        else:
            print("Ainda passui espaço")

    def exibir_relatorio(self):
        print(f"Nome do robo: {self.nome}\nQuantidade de amostra: ")
        self.contar_amostras()
        print(f"\ncapacidade máxima: {self.capacidade_maxima}\nsituação:")
        self.verificar_armazenamento()

robo1= RoboColetor("Mah", 3)
robo1.adicionar_amostra("Morfis")
robo1.adicionar_amostra("Maria")
robo1.adicionar_amostra("Mosaico")
robo1.adicionar_amostra("macaco")
robo1.adicionar_amostra("carol")
robo1.listar_amostras()
robo1.exibir_relatorio()
