class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura= ano_abertura
        self.ano_atual= ano_atual

    def pode_abrir(self):
        if self.ano_atual == self.ano_abertura:
            print("Sua capsula pode ser aberta")
        else:
            print(f"Ainda não pode abrir")
    
    def calcular_espera(self):
        diferenca = self.ano_abertura - self.ano_atual
        if diferenca >0:
            print(f"Faltam {diferenca} ano(s)")
        else:
            print("A cápsula já pode ser aberta")
        
    def classificar_espera(self):
        diferenca = self.ano_abertura - self.ano_atual
        if diferenca ==0:
            print("Pode abrir agora")
        elif diferenca>= 1 and diferenca<=3:
            print("espera curta.")
        else:
            print("espera longa.")
        
    def exibir_resumo(self):
        print(f"Autor: {self.autor} \nAno de abertura: {self.ano_abertura} \nSituação da cápsula:")
        self.pode_abrir()
        self.classificar_espera

pes1= CapsulaDoTempo("Maria", "Amo a Carol", 2027, 2026)
pes1.exibir_resumo()
pes1.calcular_espera()
pes1.pode_abrir()
pes1.classificar_espera()
pes1.exibir_resumo()