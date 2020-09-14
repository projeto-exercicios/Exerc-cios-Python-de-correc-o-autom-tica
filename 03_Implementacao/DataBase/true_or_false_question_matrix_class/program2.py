from random import randint
from random import seed

seed(135)

a = []

class M:
    def __init__(self,numero_linhas,numero_colunas):
        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas = []
        for l in range(numero_linhas):
            linha = []
            for c in range(numero_colunas):
                linha.append(randint(0, 255))
            self.linhas.append(linha)

    def __repr__(self):

        resultado = "Matriz(" +str(self.numero_linhas) + "," \
                    + str(self.numero_colunas) + ")\n"
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado += str(self.linhas[l][c])+ " "
            resultado += "\n"
        return resultado

    def row_times_column(self, cl_1, v1, other_matrix, cl_2, v2):
        

    def matrix_cross_product(self):
        

    def std(self):        

    
    def mult_by_itself(self):

   
for n in range(13):
    a.append(M(3,3))


