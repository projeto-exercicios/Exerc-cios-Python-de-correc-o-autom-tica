idx_m1 = choice(range(len(a)))
m1 = a[idx_m1]
while True:
    idx_m2 = choice(range(len(a)))
    if idx_m2 != idx_m1:
        break
m2 = a[idx_m2]  
cl_1 = choice(("coluna", "linha"))
cl_2 = choice(("coluna", "linha"))
if cl_1 == "coluna":
    v1 = choice(range(m1.get_tamanho()[1]))
if cl_1 == "linha":
    v1 = choice(range(m1.get_tamanho()[0]))
if cl_2 == "coluna":
    v2 = choice(range(m2.get_tamanho()[1]))
if cl_2 == "linha":
    v2 = choice(range(m2.get_tamanho()[0]))

answer_1_true = m1.row_times_column(cl_1, v1, m2, cl_2, v2)
decisao = choice(("coluna", "linha"))
answer_2_idx = 0
if decisao == "coluna":
    answer_2_idx = choice(range(m1.get_tamanho()[1]))
    answer_2_true = m1.get_coluna(answer_2_idx)
if decisao == "linha":
    answer_2_idx = choice(range(m1.get_tamanho()[0]))
    answer_2_true = m1.get_linha(answer_2_idx)

answer_3_true = m2.matrix_cross_product()
answer_4_true = m1.mult_by_itself()
answer_5_true = m2.std()


print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
