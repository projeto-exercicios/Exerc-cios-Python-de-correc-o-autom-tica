from random import randint
from random import seed

seed(1918616)

o = []

class B:
    __q = 7

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
    if isinstance(num, B):
        num = num.num
    if num == 1: return 1
    else: return num * factorial(num - 1)

    
def print_cicle(o):
    for n in range(o):
        print(n)
        return 
    return n


for e in range(19684):
    o.append(B(randint(-27, 1380)))

g = B()


