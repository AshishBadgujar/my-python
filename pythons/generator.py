def gen(n):                          #created generator
    for i in range(n):
        yield i
    
obj=gen(10)

print(next(obj))              
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

print(obj)       #address where object is generated


#iterable
# num=900
# for i in num:    #error int object is not iterable
#     print (i)
    
