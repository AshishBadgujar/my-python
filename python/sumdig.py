#sum of digits
n=int(input("enter no="))
s=0
while(n>0):
    r=n%10
    n=n//10
    s=r+s
print(s)