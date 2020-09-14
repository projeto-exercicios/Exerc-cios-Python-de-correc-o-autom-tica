from random import randint
from random import seed

seed(135)

e = 35
class M:
    global e
    e = 36
    def print_v1(self):
        if self == True:
            print("function print_v1")
        else:    
            print(self)
            
    def print_v2():
        print("function print_v2")
        
    def even_nums(self, nums):
        return [x for x in nums if x % 2 == 0]

    def odd_nums(self, nums):
        return [x for x in nums if x % 2 != 0]
    
    def fixed_num(self,nums):
        return [nums[x] for x in range(len(nums)) if x == nums[x]]


def print_v3(self):
    print(self)
    
a = []
even = []
odd = []
fixed_nums_list = []
answer_4_true = ''

for n in range(13):
    a.append(randint(33, 66))

m = M()
even = m.even_nums(a)
odd = m.odd_nums(a)
fixed_nums_list = m.fixed_num(a)

