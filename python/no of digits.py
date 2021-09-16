#no of digits in no
n=int(input("enter no="))
i=0
while n>0:
    r=n%10
    n=n//10
    i=i+1
print("no of digits=",i)