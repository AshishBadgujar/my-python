#removed odd index
s1=input("enter string ")
st=''
for i in range(len(s1)):
    if(i%2==0):
        st=st+s1[i]
print(st)

