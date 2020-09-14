from random import seed
from random import randint
seed(135)

class Vector3D:

    def __init__(self,x ,y ,z):
        self.x = x
        self.y = y
        self.z = z

    def mult(self, vector):
        return self.x * vector.x, self.y * vector.y, self.z * vector.z

    def add(self, vector):
        return self.x + vector.x, self.y + vector.y, self.z + vector.z

    def div(self, vector):
        return self.x / vector.x, self.y / vector.y, self.z / vector.z

    def sub(self, vector):
        return self.x - vector.x, self.y - vector.y, self.z - vector.z


def act(vector1, vector2, val):
    if val == 1:
        return vector1.mult(vector2)
    elif val == 2:
        return vector1.add(vector2)
    elif val == 3:
        return vector1.div(vector2)
    elif val == 4:
        return vector1.sub(vector2)

a = []
for n in range(20):
    v1 = Vector3D(randint(1,255),randint(1,255),randint(1,255))
    v2 = Vector3D(randint(1,255),randint(1,255),randint(1,255))
    a.append(act(v1, v2, randint(1,4)))
# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = a[1]
answer_2_true = a[2]
answer_3_true = a[3]
answer_4_true = a[4]
answer_5_true = a[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
