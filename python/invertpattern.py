n=int(input("enter range="))
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(n-i>=j):
            print(" ",end="")
        else:
            print("*",end="")
    print()