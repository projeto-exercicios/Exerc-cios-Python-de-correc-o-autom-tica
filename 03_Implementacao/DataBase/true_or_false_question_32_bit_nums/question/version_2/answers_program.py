answer_1_true = i[1]
answer_2_true = w[2]
answer_3_true = sum(np.array(i) != np.array(o) * 1.0)
answer_4_true = sum(np.array(o) == 0 * 1.0)
answer_5_true = v.reverse(binary_sum(to_bits(i[0]),to_bits(w[0])))


print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
