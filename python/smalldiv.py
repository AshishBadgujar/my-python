#smallest divisor
n=int(input("enter no="))
for i in range(2,n):
    if(n%i==0):
        print("smallest divisor=",i)
        break