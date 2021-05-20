#LCM
n1=int(input("enter 1st no="))
n2=int(input("enter 2nd no="))
i=1
if(n1>n2):
    temp=n1
    while temp>0:
        f=temp*i
        if(f%n2==0):
            print("LCM",f)
            break
        i=i+1
else:
    temp=n2
    while temp>0:
        f=temp*i
        if(f%n1==0):
            print("LCM",f)
            break
        i=i+1

    
        
