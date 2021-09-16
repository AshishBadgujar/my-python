#enumerate function
a=[1,2,3,4,5,6,7,8,9,0,0,8,6,45,3,2,3]
for i,item in enumerate(a):
    if(i+1)%2==0:
        print(item)