#divisor
n=int(input("enter no ="))
print("divisors=")
for i in range(1,n):
    if(n%i==0):
        print(i)