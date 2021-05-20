n=int(input("enter no="))
print("factors are=")
for i in range(2,n):
    if(n%i==0):
        temp=0
        for j in range(2,i):
            if(i%j==0):
                temp=1            
        if(temp==0):
            print(i)
        else:
            print("no prime factors")