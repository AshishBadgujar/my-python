#strong no
#145=1!+4!+5!
n=int(input("enter no="))
temp=n
def factorial(r):
    f=1
    for i in range(1,r+1):
        f=f*i
    return(f)


sum=0
while n>0:
    r=n%10
    n=n//10
    sum=sum+factorial(r)
if(temp==sum):
    print("strong")
else:
    print("not strong")