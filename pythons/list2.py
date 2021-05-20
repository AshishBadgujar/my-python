a=[]
n=int(input("enter no of elements ="))
for i in range(1,n+1):
    b=int(input("enter element="))
    a.append(b)
k=0
num=int(input("enter no "))
for j in a:
    if(j==num):
        k=k+1
print("your no is ",k,"of times in list ")