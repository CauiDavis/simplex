import sys
class Simplex:
    def __init__(self):
        self.tabela = []
    def add_funcao_objetiva(self,fo:list):
        self.tabela.append(fo)
    def add_restricoes(self,re:list):
        self.tabela.append(re)
    def coluna_entra(self)->list:
        coluna_pivo = min(self.tabela[0])
        indice = self.tabela[0].index(coluna_pivo)
        return indice
    def linha_sai(self,coluna_entra:int)->list:
        resultado = {}
        qtd_de_restricoes=0
        qtd_de_negativos=0
        for linha in range(len(self.tabela)):
            if linha > 0:
                if self.tabela[linha][coluna_entra] > 0:
                    divisao = self.tabela[linha][-1] / self.tabela[linha][coluna_entra]
                    resultado[linha] = divisao
                if self.tabela[linha][coluna_entra] < 0:
                    qtd_de_negativos+=1
                qtd_de_restricoes+=1
        if qtd_de_restricoes == qtd_de_negativos:
            print("ppl ilimitado")
            self.mostrar_tabela()
            exit()
        else:
         indice = min(resultado, key=resultado.get)
         return indice
    def calcular_nova_linha_pivo(self, coluna_entra: int, linha_sair: int) -> list:
        linha = self.tabela[linha_sair]
        pivo = linha[coluna_entra]
        nova_linha_pivo = [valor / pivo for valor in linha]
        return nova_linha_pivo
    def calcular_nova_linha(self, linha: list, coluna_entra: int, linha_pivo: list) -> list:
        pivo = linha[coluna_entra] * -1
        linha_resultado = [valor * pivo for valor in linha_pivo]
        nova_linha = []
        for i in range(len(linha_resultado)):
            somar_valor = linha_resultado[i] + linha[i]
            nova_linha.append(somar_valor)
        return nova_linha
    def calcular(self):
        coluna_entra = self.coluna_entra()
        primeira_linha_sair = self.linha_sai(coluna_entra)
        linha_pivo = self.calcular_nova_linha_pivo(coluna_entra, primeira_linha_sair)
        self.tabela[primeira_linha_sair] = linha_pivo
        tabela_copia = self.tabela.copy()
        indice = 0
        while indice < len(self.tabela):
            if indice != primeira_linha_sair:
                linha = tabela_copia[indice]
                nova_linha = self.calcular_nova_linha(linha, coluna_entra, linha_pivo)
                self.tabela[indice] = nova_linha
            indice += 1

    def is_negativo(self) -> bool:
        negativo = list(filter(lambda x: x < 0, self.tabela[0]))
        return True if len(negativo) > 0 else False
    def multipla_ou_unica_solucao(self)->bool:
        qtd_de_zero=0
        qtd_de_restricoes=0
        for coluna in range(len(self.tabela[0])):
            if self.tabela[0][coluna] ==0:
                qtd_de_zero +=1
        for linha in range(len(self.tabela)):
            if linha >0:
                qtd_de_restricoes+=1
        return True if (qtd_de_zero)>(qtd_de_restricoes) else False
    def resolver(self):
        self.calcular()
        while self.is_negativo():
            print("não é solução ótima")
            for i in range(len(self.tabela)):
                for j in range(len(self.tabela[0])):
                    print(f"{self.tabela[i][j]}\t", end="")
                print()
            self.calcular()
        if self.multipla_ou_unica_solucao():
            print("solução é ótima, porém tem multiplas soluções")
        else:
            print("solução é otima e tem só uma solução")
        self.mostrar_tabela()
    def mostrar_tabela(self):
        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[0])):
                print(f"{self.tabela[i][j]}\t",end="")
            print()
simplex1 = Simplex()
simplex1.add_funcao_objetiva([-300,-500,0,0,0,0])
simplex1.add_restricoes([2,1,1,0,0,16])
simplex1.add_restricoes([1,2,0,1,0,11])
simplex1.add_restricoes([1,3,0,0,1,15])
simplex1.resolver()
print()
simplex2 = Simplex()
simplex2.add_funcao_objetiva([-2,-4,0,0,0])
simplex2.add_restricoes([1,2,1,0,4])
simplex2.add_restricoes([-1,1,0,1,1])
simplex2.resolver()
print()
#OBS:eu resolvi o ppl ilimitado de uma maneira que não pode ser implementado depois -
#dele, por isso eu o coloquei por ultimo, se precisar colocar outro ppl ilimitado -
#mude o ppl ilimitado anterior para o ppl ilimitado que quer implementar,porém -
#se quiser implementar algum outro tipo de ppl que nao seja ilimitado, pode implementar -
#normalmente que vai dar certo.
simplex = Simplex()
simplex.add_funcao_objetiva([-1,-3,0,0,0])
simplex.add_restricoes([1,-2,1,0,4])
simplex.add_restricoes([-1,1,0,1,3])
simplex.resolver()
