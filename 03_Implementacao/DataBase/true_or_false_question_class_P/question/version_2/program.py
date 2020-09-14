from random import randint
from random import seed

seed(1502207)

m = []

class Y:
    __i = 7

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
    if isinstance(num, Y):
        num = num.num
    if num == 1: return 1
    else: return num * factorial(num - 1)

    
def print_cicle(m):
    for g in range(m):
        print(g)
        return 
    return g


for b in range(19446):
    m.append(Y(randint(-33, 41)))

r = Y()


