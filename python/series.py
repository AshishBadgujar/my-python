n=int(input("enter no="))
a=[]
for i in range(1,n+1):
    print(i,end=" ")
    if(n>i):
        print("+",end=" ")
    a.append(i)
print("=",sum(a))