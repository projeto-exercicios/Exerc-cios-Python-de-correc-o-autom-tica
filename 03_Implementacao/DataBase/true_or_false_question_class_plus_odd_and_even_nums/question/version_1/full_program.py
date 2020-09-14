from random import randint
from random import seed

seed(1712110)

f = 35
class l:
    global f
    f = 36
    def print_v1(self):
        if self == True:
            print("function print_v1")
        else:    
            print(self)
            
    def print_v2():
        print("function print_v2")
        
    def even_nums(self, nums):
        return [s for s in nums if s % 2 == 0]

    def odd_nums(self, nums):
        return [s for s in nums if s % 2 != 0]
    
    def fixed_num(self,nums):
        return [nums[s] for s in range(len(nums)) if s == nums[s]]


def print_v3(self):
    print(self)
    
n = []
even = []
odd = []
fixed_nums_list = []
answer_4_true = ''

for e in range(19426):
    n.append(randint(4416, 8780))

m = l()
even = m.even_nums(n)
odd = m.odd_nums(n)
fixed_nums_list = m.fixed_num(n)

# to run this program (in linux/mac):
#
# cat program.py answers_program.py | python3

# just to check
#print('list min = ', min(a))
#print('list max = ', max(a))

answer_1_true = n[1]
answer_2_true = len(even)
answer_3_true = fixed_nums_list
answer_4_true = "pares que impares" if even > odd else "impares que pares"
answer_5_true = n[5]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
