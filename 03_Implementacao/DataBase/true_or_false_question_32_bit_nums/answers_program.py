answer_1_true = a[1]
answer_2_true = b[2]
answer_3_true = sum(np.array(a) != np.array(c) * 1.0)
answer_4_true = sum(np.array(c) == 0 * 1.0)
answer_5_true = r.reverse(binary_sum(to_bits(a[0]),to_bits(b[0])))


print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
