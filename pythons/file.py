#open a file
data =open("data.txt","wb")
print("name of the file:",data.name)
print("closed or not:",data.closed)
print("opening mode:",data.mode)
data.close()