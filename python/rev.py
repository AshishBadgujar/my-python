#reverce
n=int(input("enter no="))
while(n>0):
    r=n%10
    n=n//10
    print(r,end="")