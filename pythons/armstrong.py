#armstrong
n=int(input("enter no="))
temp=n
sum=0
while n>0:
    r=n%10
    n=n//10
    sum=sum+(r*r*r)
if(sum==temp):
    print("armstrong")
else:
    print("not armstrong")