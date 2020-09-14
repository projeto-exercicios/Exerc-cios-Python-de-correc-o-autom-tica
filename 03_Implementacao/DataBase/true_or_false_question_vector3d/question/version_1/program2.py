from random import seed
from random import randint
seed(1478846)

def act(vector1, vector2, val):
    if val == 1:
        return vector1.mult(vector2)
    elif val == 2:
        return vector1.add(vector2)
    elif val == 3:
        return vector1.div(vector2)
    elif val == 4:
        return vector1.sub(vector2)

g = []
for v in range(19512):
    v1 = Vector3D(randint(1,255),randint(1,255),randint(1,255))
    v2 = Vector3D(randint(1,255),randint(1,255),randint(1,255))
    g.append(act(v1, v2, randint(1,4)))


