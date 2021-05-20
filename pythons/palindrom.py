n=int(input("enter no="))
temp=n
i=0
while n>0:
    r=n%10
    i=i*10+r
    n=n//10
if(i==temp):
    print("palindrome")
else:
    print("not palindrome") 