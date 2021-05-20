#odd no within given range
a=int(input("enter beg="))
b=int(input("enter end="))
for i in range(a,b+1):
    if(i%2!=0):
        print(i)