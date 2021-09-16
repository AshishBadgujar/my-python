import bisect
num=5
a=[1,2,3,4,6,7,8,9]
print(bisect.bisect(a,num))
bisect.insort(a,num)
print(a)