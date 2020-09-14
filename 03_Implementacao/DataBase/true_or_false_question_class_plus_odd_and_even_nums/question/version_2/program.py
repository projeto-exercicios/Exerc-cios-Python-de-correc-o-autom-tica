from random import randint
from random import seed

seed(1946738)

c = 35
class o:
    global c
    c = 36
    def print_v1(self):
        if self == True:
            print("function print_v1")
        else:    
            print(self)
            
    def print_v2():
        print("function print_v2")
        
    def even_nums(self, nums):
        return [n for n in nums if n % 2 == 0]

    def odd_nums(self, nums):
        return [n for n in nums if n % 2 != 0]
    
    def fixed_num(self,nums):
        return [nums[n] for n in range(len(nums)) if n == nums[n]]


def print_v3(self):
    print(self)
    
q = []
even = []
odd = []
fixed_nums_list = []
answer_4_true = ''

for b in range(19836):
    q.append(randint(2098, 8086))

h = o()
even = h.even_nums(q)
odd = h.odd_nums(q)
fixed_nums_list = h.fixed_num(q)

