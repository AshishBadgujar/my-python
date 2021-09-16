# import test
# x=test.add(5,10)
# print("x=",x)


import os
files=os.listdir()
files.remove('main.py')
# print(files)

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")


createIfNotExist('images')
createIfNotExist('pythons')
createIfNotExist('docs')
createIfNotExist('others')

imgExts=['.png','.jpg']
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]

pyExts=['.py']
python=[file for file in files if os.path.splitext(file)[1].lower() in pyExts]

docsExts=['.txt','.pdf']
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsExts]

others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if(ext not in imgExts) and (ext not in pyExts) and (ext not in docsExts)and os.path.isfile(file):
        others.append(file)


move("images",images)
move("pythons",python)
move("docs",docs)
move("others",others)