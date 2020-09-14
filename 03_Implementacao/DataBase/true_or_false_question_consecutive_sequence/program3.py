>>> teste = [100, 4, 200, 1, 1, 3, 2, 10, 11, 12, 13]
>>> print(longest_consecutive_sequence(teste))
[1, 2, 3, 4]
>>> print(consecutive_sequences(teste))
[[1, 2, 3, 4], [1, 2, 3, 4], [3, 4], [2, 3, 4]
 , [10, 11, 12, 13], [11, 12, 13], [12, 13]]
>>> xx = consecutive_sequences(teste)
>>> print(filtered_consecutive_sequences(xx))
[[1, 2, 3, 4], [2, 3, 4], [3, 4], [10, 11, 12, 13]
 , [11, 12, 13], [12, 13]]
>>> yy = filtered_consecutive_sequences(xx)
>>> print(distinct_numbers_in_sequence(yy))
[1, 2, 3, 4, 10, 11, 12, 13]
