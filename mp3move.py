import os
import shutil
filepath = []
myfiles = []
for path, _, files in os.walk('C:\\Users\\badgu\\Music'):
    # print("path=", path)
    # print ("_", _)
    # print("files=",files)

    for file in files:
        if str(file).endswith('.mp3'):
            myfiles.append(path.replace("\\", '/')+"/"+file)
    # You might want to exclude some directories or limit search files found to directories:
    # exclude paths that have 'Program Files' folder and only include all paths that have 'Downloads',
    # ie derp/Downloads/a/ or Downloads/durp/ included, anything with 'Program Files' excluded
    # if ('Program Files' not in path) and ('Music' in path):
    #     # in case of windows system replace \ with /
    #     filepath.extend([os.path.join(path, file).replace('\\', '/') for file in files
    #                      if str(file).endswith('.mp3')])

# print("filepath=", filepath)
# for file in filepath:
#     os.rename(filepath, os.path.split(filpath)[1])
print("mt files=", myfiles)
for file in myfiles:
    shutil.move(file, "C:\\Users\\badgu\\Music")
