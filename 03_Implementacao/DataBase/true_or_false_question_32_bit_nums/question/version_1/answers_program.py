answer_1_true = d[1]
answer_2_true = g[2]
answer_3_true = sum(np.array(d) != np.array(v) * 1.0)
answer_4_true = sum(np.array(v) == 0 * 1.0)
answer_5_true = q.reverse(binary_sum(to_bits(d[0]),to_bits(g[0])))


print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
