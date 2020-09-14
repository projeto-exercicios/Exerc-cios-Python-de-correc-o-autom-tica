chosen_nums = []
dist = 0
mst_freq = 0
lst_freq = 0
int_t_r = 0
list_distance = 0
mst_freq = most_frequent(b)
lst_freq = least_frequent(b)
int_t_r = int_to_roman(choice(b))
list_distance = choice((3, 4, 5, 6, 7))
dist = choice(range(len(b) - list_distance))
chosen_nums = b[dist: dist + list_distance]

answer_1_true = b[1]
answer_2_true = mst_freq
answer_3_true = lst_freq
answer_4_true = int_t_r
answer_5_true = rotate_list(chosen_nums, list_distance)

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
