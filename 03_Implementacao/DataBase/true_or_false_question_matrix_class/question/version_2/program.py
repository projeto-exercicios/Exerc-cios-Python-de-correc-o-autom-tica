from random import randint
from random import choice
from random import seed
import math

seed(1508048)

g = []

class M:
    def __init__(self,numero_linhas,numero_colunas):
        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas = []
        for l in range(numero_linhas):
            linha = []
            for c in range(numero_colunas):
                linha.append(randint(0, 239))
            self.linhas.append(linha)

    def __repr__(self):

        resultado = "\\newline Matriz(" +str(self.numero_linhas) + ","                    + str(self.numero_colunas) + ")\n \\newline"
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado += str(self.linhas[l][c])+ " "
            if l + 1 < self.numero_linhas:
                resultado += "\n \\newline"
        return resultado

    def get_tamanho(self):
        return len(self.linhas), len(self.linhas[0])
    
    def set_entrada(self,linha,coluna,valor):
        self.linhas[linha -1][coluna -1] = valor

    def get_entrada(self,linha,coluna):
        return self.linhas[linha -1][coluna -1]

    def get_linha(self, linha):
        return self.linhas[linha]
    
    def get_coluna(self, coluna):
        resultado_coluna = []
        for row in self.linhas:
            resultado_coluna.append(row[coluna])
        return resultado_coluna

    def row_times_column(self, cl_1, v1, other_matrix, cl_2, v2):
        m1 = []
        m2 = []
        if cl_1 == "coluna":
            m1 = self.get_coluna(v1)
        if cl_1 == "linha":
            m1 = self.get_linha(v1)
        if cl_2 == "coluna":
            m2 = self.get_coluna(v2)
        if cl_2 == "linha":
            m2 = self.get_linha(v2)   

        result = 0
        for idx in range(len(m1)):
            result += m1[idx] * m2[idx]
        return result

    def matrix_cross_product(self):
        quadr_impar = []
        quadr_par = []
        valor = 0
        for linha in self.linhas:
            quadr_impar.append(linha[valor])
            quadr_par.append(linha[- valor - 1])
            valor += 1
        result = 0
        for idx in range(len(quadr_impar)):
            result += quadr_impar[idx] * quadr_par[idx]
        return result

    def transposta(self):
        resultado = M(self.numero_colunas,self.numero_linhas)
        for l in range(resultado.numero_linhas):
            for c in range(resultado.numero_colunas):
                resultado.linhas[l][c] =  self.linhas[c][l]
        return resultado

    def mean(self, valores):
        return sum(valores) * 1.0 / len(valores)

    def to_1d(self):
        d1_arr = []
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                d1_arr.append(self.linhas[l][c])
        return d1_arr

    def std(self):
        valores = self.to_1d()
        m = self.mean(valores)
        resultado_sum = 0
        for i in range(len(valores)):
            resultado_sum += ((valores[i]) - m)**2

        antes_sqrt = resultado_sum / len(valores)

        return round(math.sqrt(antes_sqrt),2)
        
    
    def mult_by_itself(self):
        m_trans = self.transposta()
        nova_matriz = M(self.numero_linhas,self.numero_colunas)
        for l in range(self.numero_linhas):
            for c in range(m_trans.numero_colunas):
                gl = self.get_linha(l)
                cl = m_trans.get_coluna(c)
                valor = 0
                for i in range(len(gl)):
                    valor += gl[i] * cl[i]
                nova_matriz.linhas[l][c] = valor
        return nova_matriz


   
for i in range(19229):
    g.append(M(3,3))

    
######********######
idx_m1 = 0
idx_m2 = 0
m1 = 0
m2 = 0
decisao = 0
v1 = 0
v2 = 0
cl_1 = 0
cl_2 = 0
answer_1_true = 0
answer_2_true = 0
answer_3_true = 0
answer_4_true = 0
answer_5_true = 0
######********######
