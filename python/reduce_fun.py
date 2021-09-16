#reduce function
from functools import reduce
def sum_num(a,b):
    return a+b

lil=reduce(sum_num,[1,2,3,4,5])
print(lil)