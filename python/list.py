#list
a=[]
elarge=0
olarge=0
n=int(input("enter the size of list="))
for i in range(1,n+1):
    b=int(input("element :"))
    a.append(b)
    if(b%2==0):
        if(elarge<b):
            elarge=b
            
    else:
        if(olarge<b):
            olarge=b
print("large even no=",elarge)
print("large odd no=",olarge)