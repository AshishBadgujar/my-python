#wrinting in file
data=open("data.txt","w")
data.write("welcome to my python tutorial")
print("done")
data.close()



data=open("data.txt","r")
#print(data.read())
print(data.read(8))
print(data.read())
data.close()