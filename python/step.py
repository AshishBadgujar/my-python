a=int(input("enter bigin="))
#b=int(input("enter end="))
step=int(input("enter step ="))
b=0
for i in range(a,10000,step):
    print(i)
    if(b==10):
        break
    b=b+1