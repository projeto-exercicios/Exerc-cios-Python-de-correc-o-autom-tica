>>> m1
Matriz(3,3)
1 223 225 
185 74 106 
238 197 179 

>>> m2
Matriz(3,3)
248 167 27 
116 153 131 
127 106 39

>>> m1.row_times_column('linha', 2, m2, 'linha', 1)
77582
>>> m2.matrix_cross_product()
35058
>>> m1.mult_by_itself()
Matriz(3,3)
100355 40537 84444 
40537 50937 77582 
84444 77582 127494 

>>> m2.std()
62.49
