s1=input("enter string ")
word=input("enter word")
a=[]
count=0
a=s1.split(' ')
for i in range(0,len(s1)):
    if(word==a[i]):
        count=count+1
print(count)