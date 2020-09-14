from random import randint
from random import seed

seed(135)

a = []

class P:
    __var = 7

    def __init__(self, num = 0):
        self.num = num

    def __truediv__(self, othernum):
        try:
            print(self.num,"/", othernum.num)
            result = self.num / othernum.num
            print(result)
            assert result % 2 == 0
        except AssertionError:
            print("result odd")
        except ZeroDivisionError:
            print("ZeroDivisionError")
        finally:
            print("Done!")
        

def factorial(num):
    if isinstance(num, P):
        num = num.num
    if num == 1: return 1
    else: return num * factorial(num - 1)

    
def print_cicle(a):
    for i in range(a):
        print(i)
        return 
    return i


for n in range(13):
    a.append(P(randint(3, 33)))

p = P()


answer_1_true = print_cicle(10)
answer_2_true = a[0] / a[3]
answer_3_true = a[4].num
answer_4_true = p.num
answer_5_true = a[3].num
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
